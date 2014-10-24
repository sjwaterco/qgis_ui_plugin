# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CLWSCDesktop
                                 A QGIS plugin
 Changes the User Interface to Help
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
import struct
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from app.clwscdesktopdialog import CLWSCDesktopDialog
from app.clwscdw import ClwscDW

class CLWSCDesktop:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # Create the dialog and keep reference
        self.dlg = CLWSCDesktopDialog(iface)
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/clwscdesktop"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]
       
        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/clwscdesktop_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        
        # Set up the CLWSC Toolbar Actions
        self.actionPan = QAction(QIcon(":/plugins/clwscdesktop/images/tb_pan.png"), 
          "Pan the Map", self.iface.mainWindow())
        self.actionPan.setCheckable(True)
        
        self.actionZoomIn = QAction(QIcon(":/plugins/clwscdesktop/images/tb_zoomIn.png"), 
          "Zoom In",  self.iface.mainWindow())  
        self.actionZoomIn.setCheckable(True)
        
        self.actionZoomOut = QAction(QIcon(":/plugins/clwscdesktop/images/tb_zoomOut.png"), 
          "Zoom Out",  self.iface.mainWindow())  
        self.actionZoomOut.setCheckable(True)
        
        self.actionExtent = QAction(QIcon(":/plugins/clwscdesktop/images/tb_extent.png"), 
          "Zoom to Extent",  self.iface.mainWindow())       
          
        self.actionSuggest = QAction(QIcon(":/plugins/clwscdesktop/images/tb_suggestions.png"), 
          "Suggestions or Problem",  self.iface.mainWindow())      
        
        # Add buttons to the CLWSC Toolbar
        self.toolbar = self.iface.addToolBar("GDI Desktop")
        self.toolbar.setObjectName("GDI Desktop")
        self.toolbar.addAction(self.actionPan)
        self.toolbar.addAction(self.actionZoomIn)
        self.toolbar.addAction(self.actionZoomOut)
        self.toolbar.addAction(self.actionExtent)
        self.actionMeasure = self.iface.actionMeasure()
        self.actionMeasure.setIcon(QIcon(":/plugins/clwscdesktop/images/tb_measureLength.png"))
        self.toolbar.addAction(self.actionMeasure)
        self.actionMeasureArea = self.iface.actionMeasureArea()
        self.actionMeasureArea.setIcon(QIcon(":/plugins/clwscdesktop/images/tb_measureArea.png"))
        self.toolbar.addAction(self.actionMeasureArea)
        self.actionIdentify = self.iface.actionIdentify()
        self.actionIdentify.setIcon(QIcon(":/plugins/clwscdesktop/images/tb_select.png"))
        self.toolbar.addAction(self.actionIdentify)
        self.toolbar.addAction(self.actionSuggest)

        
        #Get the existing tools for map navigation
        self.toolPan = QgsMapToolPan(self.iface.mapCanvas())
        self.toolPan.setAction(self.actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.iface.mapCanvas(), False)
        self.toolZoomIn.setAction(self.actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.iface.mapCanvas(), True)
        self.toolZoomOut.setAction(self.actionZoomOut)
        
        #Handle the events for clicking the CLWSC toolbar buttons
        self.iface.connect(self.actionPan, SIGNAL("triggered()"), self.pan)
        self.iface.connect(self.actionZoomIn, SIGNAL("triggered()"), self.zoomIn)
        self.iface.connect(self.actionZoomOut, SIGNAL("triggered()"), self.zoomOut)
        self.iface.connect(self.actionExtent, SIGNAL("triggered()"), self.zoomExtent)
        self.iface.connect(self.actionSuggest, SIGNAL("triggered()"), self.showSuggest)
        self.actionPan.activate(QAction.Trigger)
        
        self.originalTitle = self.iface.mainWindow().windowTitle()
        self.originalIcon = self.iface.mainWindow().windowIcon()
        self.iface.mainWindow().setWindowTitle("GDI Desktop")
        self.iface.mainWindow().setWindowIcon(QIcon(":/plugins/clwscdesktop/images/icon_128.png"))
        
        # We cannot run this plugin without psycopg2, our postgis driver.
        try:
          import psycopg2
          import psycopg2.extensions
          loaded_psycopg2 = True
        except ImportError:
          loaded_psycopg2 = False
          
        if loaded_psycopg2 == False:
          msgBox = QMessageBox(self.iface.mainWindow())
          msgBox.setText("Psycopg2 is not loaded and is required.")
          msgBox._exec()
          self.iface.SearchDisabled = True
        else:
          self.iface.SearchDisabled = False
          
        
    def pan(self):
      self.iface.mapCanvas().setMapTool(self.toolPan)
    
    def zoomIn(self):
      self.iface.mapCanvas().setMapTool(self.toolZoomIn)
    
    def zoomOut(self):
      self.iface.mapCanvas().setMapTool(self.toolZoomOut)
    
    def zoomExtent(self):
      self.iface.mapCanvas().zoomToFullExtent()
        

    def initGui(self):
        
        # Deactivate all toolbars in the QGIS Interface
        toolbars = self.iface.mainWindow().findChildren(QToolBar)
        
        for toolbar in toolbars:
          if(toolbar.objectName() != "GDI Desktop"):
            toolbar.setVisible(False)
          else:
            toolbar.setVisible(True)
        
        # Add the CLWSC Search bar as a new tab in the layers area.
        layers = self.iface.mainWindow().findChild(QDockWidget, "Legend")
        self.dockWidget = ClwscDW(self)
        self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)
        
        self.iface.mainWindow().tabifyDockWidget(layers, self.dockWidget)
        
        # Activate the Overview Pane
        overview = self.iface.mainWindow().findChild(QDockWidget, "Overview")
        
        if overview:
          overview.show()
          overview.update()
        

        settings = QSettings(QSettings.NativeFormat, QSettings.UserScope, 'QuantumGIS', 'QGis')
        settings.setValue('/Projections/projectDefaultCrs', 'EPSG:2278')
        settings.setValue('/Projections/otfTransformEnabled', True)
        settings.setValue('/Qgis/askToSaveProjectChanges', False)
        settings.setValue('/Qgis/warnOldProjectVersion', False)
        settings.setValue('/Qgis/legendDoubleClickAction', 1)
        settings.setValue('/Qgis/capitaliseLayerName', True)
        settings.setValue('/Qgis/showLegendClassifiers', True)
        settings.setValue('/Qgis/hideSplash', True)
        settings.setValue('/Qgis/wheel_action', 1)
        settings.setValue('/Qgis/enable_render_caching', True)
        settings.setValue('/Qgis/attributeTableBehaviour', 2)
        settings.setValue('/Qgis/measure/decimalplaces', 1)
        settings.setValue('/Qgis/measure/keepbaseunit', True)
        settings.setValue('/Qgis/measure/displayunits', 'feet')
        settings.setValue('/svg/searchPathsForSVG', 'C:\\gdi_desktop_qgis\\svg')
        settings.setValue('/fontPointSize', 10)

        #f = open('/home/aaron/Documents/qgis.log', 'w')
        #for item in dir(layers):
        #  f.write(item + '\n')
        #f.close
              

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removeDockWidget(self.dockWidget)
        del self.dockWidget
        self.iface.mainWindow().setWindowTitle(self.originalTitle)
        self.iface.mainWindow().setWindowIcon(self.originalIcon)
    
    def showSuggest(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass

