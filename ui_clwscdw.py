# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_clwscdw.ui'
#
# Created: Fri Aug 23 10:52:13 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ClwscDW(object):
    def setupUi(self, ClwscDW):
        ClwscDW.setObjectName(_fromUtf8("ClwscDW"))
        ClwscDW.resize(265, 440)
        ClwscDW.setMinimumSize(QtCore.QSize(265, 440))
        ClwscDW.setWindowTitle(QtGui.QApplication.translate("ClwscDW", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setMinimumSize(QtCore.QSize(265, 415))
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.buttonSearch = QtGui.QPushButton(self.dockWidgetContents)
        self.buttonSearch.setGeometry(QtCore.QRect(220, 60, 31, 31))
        self.buttonSearch.setText(QtGui.QApplication.translate("ClwscDW", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearch.setObjectName(_fromUtf8("buttonSearch"))
        self.textBoxQuery = QtGui.QLineEdit(self.dockWidgetContents)
        self.textBoxQuery.setGeometry(QtCore.QRect(10, 60, 201, 31))
        self.textBoxQuery.setObjectName(_fromUtf8("textBoxQuery"))
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setGeometry(QtCore.QRect(0, 0, 271, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.buttonAddress = QtGui.QPushButton(self.frame)
        self.buttonAddress.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.buttonAddress.setToolTip(QtGui.QApplication.translate("ClwscDW", "Address Search", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAddress.setAccessibleName(QtGui.QApplication.translate("ClwscDW", "address", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAddress.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/clwscdesktop/images/search_address.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAddress.setIcon(icon)
        self.buttonAddress.setIconSize(QtCore.QSize(32, 32))
        self.buttonAddress.setCheckable(True)
        self.buttonAddress.setChecked(True)
        self.buttonAddress.setAutoExclusive(True)
        self.buttonAddress.setObjectName(_fromUtf8("buttonAddress"))
        self.buttonIntersection = QtGui.QPushButton(self.frame)
        self.buttonIntersection.setGeometry(QtCore.QRect(60, 10, 41, 41))
        self.buttonIntersection.setToolTip(QtGui.QApplication.translate("ClwscDW", "Intersection Search", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonIntersection.setAccessibleName(QtGui.QApplication.translate("ClwscDW", "intersection", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonIntersection.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/clwscdesktop/images/search_intersection.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonIntersection.setIcon(icon1)
        self.buttonIntersection.setIconSize(QtCore.QSize(32, 32))
        self.buttonIntersection.setCheckable(True)
        self.buttonIntersection.setAutoExclusive(True)
        self.buttonIntersection.setObjectName(_fromUtf8("buttonIntersection"))
        self.buttonStation = QtGui.QPushButton(self.frame)
        self.buttonStation.setGeometry(QtCore.QRect(160, 10, 41, 41))
        self.buttonStation.setToolTip(QtGui.QApplication.translate("ClwscDW", "Station Search", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonStation.setAccessibleName(QtGui.QApplication.translate("ClwscDW", "station", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonStation.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/clwscdesktop/images/search_station.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonStation.setIcon(icon2)
        self.buttonStation.setIconSize(QtCore.QSize(32, 32))
        self.buttonStation.setCheckable(True)
        self.buttonStation.setAutoExclusive(True)
        self.buttonStation.setObjectName(_fromUtf8("buttonStation"))
        self.buttonSubdivision = QtGui.QPushButton(self.frame)
        self.buttonSubdivision.setGeometry(QtCore.QRect(110, 10, 41, 41))
        self.buttonSubdivision.setToolTip(QtGui.QApplication.translate("ClwscDW", "Subdivision Search", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSubdivision.setAccessibleName(QtGui.QApplication.translate("ClwscDW", "subdivision", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSubdivision.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/clwscdesktop/images/search_subdivision.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSubdivision.setIcon(icon3)
        self.buttonSubdivision.setIconSize(QtCore.QSize(32, 32))
        self.buttonSubdivision.setCheckable(True)
        self.buttonSubdivision.setAutoExclusive(True)
        self.buttonSubdivision.setObjectName(_fromUtf8("buttonSubdivision"))
        self.buttonMapsco = QtGui.QPushButton(self.frame)
        self.buttonMapsco.setGeometry(QtCore.QRect(210, 10, 41, 41))
        self.buttonMapsco.setToolTip(QtGui.QApplication.translate("ClwscDW", "MAPSCO Search", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonMapsco.setAccessibleName(QtGui.QApplication.translate("ClwscDW", "station", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonMapsco.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/clwscdesktop/images/search_mapsco.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonMapsco.setIcon(icon4)
        self.buttonMapsco.setIconSize(QtCore.QSize(32, 32))
        self.buttonMapsco.setCheckable(True)
        self.buttonMapsco.setAutoExclusive(True)
        self.buttonMapsco.setObjectName(_fromUtf8("buttonMapsco"))
        ClwscDW.setWidget(self.dockWidgetContents)

        self.retranslateUi(ClwscDW)
        QtCore.QMetaObject.connectSlotsByName(ClwscDW)

    def retranslateUi(self, ClwscDW):
        pass

import resources_rc
