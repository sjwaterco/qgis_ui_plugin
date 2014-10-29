# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CLWSCDesktop
                                 A QGIS plugin
 Changes the User Interface to Help
                             -------------------
        begin                : 2012-03-30
        copyright            : (C) 2012 by SJWC
        email                : aaron.gundel@sjwater.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "GDI Desktop"
def description():
    return "GDI Desktop in QGIS"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load CLWSCDesktop class from file CLWSCDesktop
    from clwscdesktop import CLWSCDesktop
    return CLWSCDesktop(iface)
