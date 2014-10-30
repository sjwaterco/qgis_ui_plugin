import urllib2
import json
import socket
import _winreg
from postgis_utils import *
from qgis.core import *
from google import Google
from PyQt4 import QtGui

# The searcher class implements SJWC's search routines.  We segregate our searches by type
# (address, intersection, station, etc.) in order to make our user interface more familiar to
# our users (like systems they have used in the past)  Initializing the SearchFactory without
# the needed reg keys will LIKELY cause the plugin to break at load time.  (I don't know, I haven't done it.)
# In order to make the module work for you, comment out the init section.  Note that (obviously)
# the searches will not work for you since you don't have our database schema, so executing
# searches will also cause the plugin to break/throw an exception.  You'll want to modify
# the UI and/or SearchFactory accordingly.  Send me an email if you have questions.

class Search:
  def __init__(self, database):
    self.name = ""
    self.database = database
    self.minSearchLength = 4
  def autocomplete_execute(self, query):
    return []
  def execute(self, query):
    return []

# Sets up the child searches and produces the correct one for given search type
class SearchFactory:
  def __init__(self):
    #for SJW testing, if in SJ, do postgis.sjwater.com.  If in TX -- do cl-fs2
    if(socket.gethostbyname(socket.gethostname()).startswith('192')):
      regKeyString = r'SOFTWARE\Wow6432Node\Canyon Lake Water Services Company\CLWSC GDI Desktop\Database\CLWSC')
    else:
      regKeyString = r'SOFTWARE\Wow6432Node\Canyon Lake Water Services Company\CLWSC GDI Desktop\Database\SJWC')
    
    regKey = OpenKey(HKEY_LOCAL_MACHINE, regKeyString)
    self.database = getDbConnection(regKey) 

    regKey = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Wow6432Node\Canyon Lake Water Services Company')
    key = QueryValueEx(key, "gmclient")[0]
    self.geocoder = Google(api_key=key,output_format="json")
    self.AddressSearch = AddressSearch(self.database, self.geocoder)
    self.IntersectionSearch = IntersectionSearch(self.database, self.geocoder)
    self.SubdivisionSearch = SubdivisionSearch(self.database)
    self.MAPSCOSearch = MAPSCOSearch(self.database)
    self.StationSearch = StationSearch(self.database)
  
  def getDbConnection(self, key):
    host = QueryValueEx(key, "h")
    passwd = QueryValueEx(key, "p")
    user = QueryValueEx(key, "u")
    port = QueryValueEx(key, "pt")
    db = QueryValueEx(key, "dbn")
    return GeoDB(host=host[0],port=port[0],dbname=db[0], \
        user=user[0],passwd=passwd[0])

  def getSearcher(self, type):
    if(type == "address"):
      return self.AddressSearch
    elif(type == "intersection"):
      return self.IntersectionSearch
    elif(type == "mapsco"):
      return self.MAPSCOSearch
    elif(type == "subdivision"):
      return self.SubdivisionSearch
    elif(type == "station"):
      return self.StationSearch

# Search for an Address 
class AddressSearch(Search):
  def __init__(self, database, geocoder):
    self.geocoder = geocoder
    Search.__init__(self,database)
    
  def autocomplete_execute(self, query):
    print "acquery executing..."
    query = "SELECT DISTINCT address FROM clwsc_gispub.service_meter " + \
      "WHERE lower(address) like lower('{0}%')".format(self.database._quote_str(query))
    print query
    print self.database.execute_query(query)
    return self.database.execute_query(query)
  
  def execute(self, address):
    query = "SELECT address, " +\
      "ST_X(ST_CENTROID(gdo_geometry::geometry)) as longitude, " + \
      "ST_Y(ST_CENTROID(gdo_geometry::geometry)) as latitude " + \
      "FROM clwsc_gispub.service_meter WHERE lower(address) = lower('{0}')" \
      .format(self.database._quote_str(address))
    results = self.database.execute_query(query)
    print results
    
    #If we don't get any results from the database, attempt to geocode the point
    if(len(results) == 0):
      results = []
      result = self.geocoder.geocode(address)

      if(result != None and result[2] >= 8):
        coordinates = result[1]
        transformation = QgsCoordinateTransform( \
          QgsCoordinateReferenceSystem(4326), \
          QgsCoordinateReferenceSystem(2278))
        transformedCoords = transformation.transform( \
          coordinates[1], coordinates[0])
        results.append((result[0], \
          transformedCoords.x(), transformedCoords.y()))
    return results

#Search for an Intersection
class IntersectionSearch(Search):
  def __init__(self, database, geocoder):
    self.geocoder = geocoder
    Search.__init__(self,database)
    
  def autocomplete_execute(self, query):
    query = "SELECT DISTINCT autosuggest_value FROM comal_cty.intersection_autosuggest " + \
      "WHERE  autosuggest_value like upper('{0}%')".format(self.database._quote_str(query))
    return self.database.execute_query(query)
    
  def execute(self, intersection):
    results = []
    #If we don't get any results from the database, attempt to geocode the point
    query = "SELECT DISTINCT autosuggest_value, ST_X(ST_CENTROID(gdo_geometry::geometry)) as longitude, ST_Y(ST_CENTROID(gdo_geometry::geometry)) as latitude  FROM comal_cty.intersection_autosuggest " + \
      "WHERE  autosuggest_value = upper('{0}')".format(self.database._quote_str(intersection))
    
    dbresults = self.database.execute_query(query)

    results = []
    if(len(dbresults) > 0):
      results.append((dbresults[0][0], dbresults[0][1], dbresults[0][2]))
    else:
      result = self.geocoder.geocode(query + "; Comal County, Texas")      

      if(result != None and result[2] >= 6):
        coordinates = result[1]
        transformation = QgsCoordinateTransform( \
          QgsCoordinateReferenceSystem(4326), \
          QgsCoordinateReferenceSystem(2278))
        transformedCoords = transformation.transform( \
          coordinates[1], coordinates[0])
        results.append((result[0], \
          transformedCoords.x(), transformedCoords.y()))

    return results

    
#Search for a Page
class MAPSCOSearch(Search):
  def __init__(self,database):
    Search.__init__(self,database)
    self.minSearchLength = 1
    
  def autocomplete_execute(self, query):
    query = "SELECT DISTINCT page_number FROM comal_cty.mapsco_grid " + \
      "WHERE page_number like '{0}%'".format(self.database._quote_str(query))
    return self.database.execute_query(query)
    
  def execute(self, grid):
    query = "SELECT DISTINCT page_number, " +\
      "ST_X(ST_CENTROID(gdo_geometry::geometry)) as longitude, " + \
      "ST_Y(ST_CENTROID(gdo_geometry::geometry)) as latitude " + \
      "FROM comal_cty.mapsco_grid " + \
      "WHERE page_number = '{0}'".format(self.database._quote_str(grid))
    results = self.database.execute_query(query)
    return results

#Search for a Station    
class StationSearch(Search):
  def __init__(self,database):
    Search.__init__(self,database)
    self.minSearchLength = 1
    
  def autocomplete_execute(self, query):
    query = "SELECT DISTINCT name FROM clwsc_gispub.station " + \
      "WHERE lower(name) like lower('{0}%')".format(self.database._quote_str(query))
    return self.database.execute_query(query)
    
  def execute(self, station):
    query = "SELECT station_number, " +\
      "ST_X(ST_CENTROID(gdo_geometry::geometry)) as longitude, " + \
      "ST_Y(ST_CENTROID(gdo_geometry::geometry)) as latitude " + \
      "FROM clwsc_gispub.station WHERE name = '{0}'" \
      .format(self.database._quote_str(station))
    results = self.database.execute_query(query)
    return results

#Search for a Subdivision    
class SubdivisionSearch(Search):
  def __init__(self,database):
    Search.__init__(self,database)
    self.minSearchLength = 3
  
  def autocomplete_execute(self, query):
    query = "SELECT DISTINCT name FROM clwsc_gispub.subdivision " + \
      "WHERE lower(name) like lower('{0}%')".format(self.database._quote_str(query))
    return self.database.execute_query(query)
    
  def execute(self,subdivision):
    query = "SELECT name, " +\
      "ST_X(ST_CENTROID(gdo_geometry::geometry)) as longitude, " + \
      "ST_Y(ST_CENTROID(gdo_geometry::geometry)) as latitude " + \
      "FROM clwsc_gispub.subdivision WHERE lower(name) = lower('{0}')" \
      .format(self.database._quote_str(subdivision))
    results = self.database.execute_query(query)
    return results;
  
