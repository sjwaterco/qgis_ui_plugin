# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ClwscDW
                                 A QGIS plugin
Search widght -- Docked on the left side.
                             -------------------
        begin                : 2012-03-30
        copyright            : (C) 2012 by SJWC
        email                : aaron_gundel@sjwater.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from search import *
from gdi_desktop_qgis.ui_clwscdw import Ui_ClwscDW
# create the dialog for zoom to point
class ClwscDW(QDockWidget, Ui_ClwscDW, object):
    def __init__(self, iface):
        QDockWidget.__init__(self, None)
        self.setupUi(self)
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.plugin = iface
        self.mapTool = None
        self.autoCompleter = QStringListModel()
        self.connectDlgSignals()
        self.searchFactory = SearchFactory()
        self.completerListModel = QStringListModel()
        self.autoCompleter = QCompleter()
        self.autoCompleter.setModel(self.completerListModel)
        self.autoCompleter.setCaseSensitivity(0)
        self.autoCompleter.setModelSorting(2)
        self.autoCompleter.connect( \
          self.autoCompleter, \
          SIGNAL("activated(QString)"), \
          self.goToLocation)

        self.textBoxQuery.setCompleter(self.autoCompleter)
 
    def connectDlgSignals(self):
      self.textBoxQuery.textEdited.connect(self.autocompleteSetup)
      #self.textBoxQuery.connect(self.textBoxQuery, SIGNAL("clicked()"), self.search)
      self.buttonSearch.connect( \
        self.buttonSearch, SIGNAL("clicked()"), \
        self.goToLocation)
      for button in self.frame.children():
        button.connect(\
        button, SIGNAL("clicked()"), \
        self.clearCompleter)
    
    # initialize the qcompleter object for our search box
    def autocompleteSetup(self, text):
      # We only update the model of the minimum number of chars have been entered
      buttonName = self.getCheckedButton()
      searcher = self.searchFactory.getSearcher(buttonName)
      if(len(text) == searcher.minSearchLength):
        result = searcher.autocomplete_execute(text)
        resultArray = QStringList()
        self.result = result
        for i in result:
          resultArray.append(str(i[0]))
        
        if(len(result) > 0):
          self.completerListModel.setStringList(resultArray)
          self.completerListModel.sort(0)
    
    # clear the autocomplete menu
    def clearCompleter(self):
      self.completerListModel.setStringList(QStringList())
        
    def goToLocation(self, text = ""):
      #if the search text isn't provided, raid the text box component. 
      if(text == ""):
        text = self.textBoxQuery.text()
      
      buttonName = self.getCheckedButton()
      searcher = self.searchFactory.getSearcher(buttonName)  
      result = searcher.execute(text)

      if(result[0]):
        x = result[0][1]
        y = result[0][2]
      else:
        return

      # Get the map canvas
      mc = self.plugin.iface.mapCanvas()

      coordX = mc.extent().xMinimum()
      coordY = mc.extent().yMaximum()
      height2 = mc.extent().height() * 1 / 2.0
      width2 = mc.extent().width() * 1 / 2.0
     
      rect = QgsRectangle(x-width2,y-height2,x+width2,y+height2)

      mc.setExtent(rect)

      mc.refresh()
      if(buttonName != "mapsco"):
          mc.zoomScale(1200)
      else:
          mc.zoomScale(3200)
      
    def getCheckedButton(self):
      if(self.buttonAddress.isChecked()):
        return "address"
      elif(self.buttonIntersection.isChecked()):
        return "intersection"
      elif(self.buttonMapsco.isChecked()):
        return "mapsco"
      elif(self.buttonStation.isChecked()):
        return "station"
      elif(self.buttonSubdivision.isChecked()):
        return "subdivision"
