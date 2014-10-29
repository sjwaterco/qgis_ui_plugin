# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CLWSCDesktopDialog
                                 A QGIS plugin
 Creates an additional dialog for the user to provide feedback
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
"""
import struct
import urllib2
import _winreg

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from xml.sax.saxutils import escape

import gdi_desktop_qgis.resources_rc

from gdi_desktop_qgis.ui_clwscdesktop import Ui_CLWSCDesktop
# create the dialog for zoom to point
class CLWSCDesktopDialog(QDialog):
    def __init__(self, iface):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_CLWSCDesktop()
        self.ui.setupUi(self)
        self.iface = iface
        
        #connect all signals to slots
        self.connectDlgSignals()
    
    def connectDlgSignals(self):
        self.iface.connect(self.ui.buttonSubmit, SIGNAL("clicked()"), self.saveTicket)
      

    # Save the ticket to Pivotal Tracker
    # NOTE: this info is specific to SJW.  If you were to customize this 
    # section of code, you would modify this save ticket function to either use
    # your own Pivotal Tracker project/key or insert the feedback into your own
    # ticketing/tracking system.  All of this is completely optional.  This code
    # will only fire when attempting to submit feedback.
    def saveTicket(self):
        storyXml = "<story><story_type>bug</story_type><name>{0}</name><description>" + \
                   "{1}</description><requested_by>Portal User</requested_by></story>"
        url = "https://www.pivotaltracker.com/services/v3/projects/874265/stories"
        regKey = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Wow6432Node\Canyon Lake Water Services Company\CLWSC GDI Desktop')
        # This token should be your Pivotal Tracker API Key
        token = QueryValueEx(key, "pttoken")[0]
        description = escape(self.ui.textBoxName.toPlainText()) + " &lt;" + escape(self.ui.textBoxEmail.toPlainText()) + "&gt;\n"
        description += escape(self.ui.textBoxDescription.toPlainText())
        storyXml = storyXml.format(escape(self.ui.textBoxSubject.toPlainText()), description)
        contentType = "application/xml"
        headers = {
          'X-TrackerToken': token,
          'Content-Type': contentType
        }
        request = urllib2.Request(url=url, data=storyXml, headers=headers)
        response = urllib2.urlopen(request)
        if(response.getcode() == 200):
            QMessageBox.about(self, "Success", "Suggestion successfully submitted.")
            self.ui.textBoxDescription.setText("")
            self.ui.textBoxName.setText("")
            self.ui.textBoxEmail.setText("")
            self.ui.textBoxSubject.setText("")
            self.close()
        else:
            QMessageBox.about(self, "Error", "Message was not submitted successfully.  Try again later.")