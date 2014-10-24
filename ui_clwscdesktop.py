# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_clwscdesktop.ui'
#
# Created: Mon Apr 23 14:59:15 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CLWSCDesktop(object):
    def setupUi(self, CLWSCDesktop):
        CLWSCDesktop.setObjectName(_fromUtf8("CLWSCDesktop"))
        CLWSCDesktop.resize(297, 298)
        CLWSCDesktop.setWindowTitle(QtGui.QApplication.translate("CLWSCDesktop", "Report a Problem or Suggestion", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(CLWSCDesktop)
        self.buttonBox.setGeometry(QtCore.QRect(100, 260, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.textBoxDescription = QtGui.QTextEdit(CLWSCDesktop)
        self.textBoxDescription.setGeometry(QtCore.QRect(20, 150, 251, 101))
        self.textBoxDescription.setObjectName(_fromUtf8("textBoxDescription"))
        self.label = QtGui.QLabel(CLWSCDesktop)
        self.label.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label.setText(QtGui.QApplication.translate("CLWSCDesktop", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(CLWSCDesktop)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 41, 16))
        self.label_2.setText(QtGui.QApplication.translate("CLWSCDesktop", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(CLWSCDesktop)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 51, 16))
        self.label_3.setText(QtGui.QApplication.translate("CLWSCDesktop", "Subject", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(CLWSCDesktop)
        self.label_4.setGeometry(QtCore.QRect(50, 130, 191, 20))
        self.label_4.setText(QtGui.QApplication.translate("CLWSCDesktop", "Problem Description/Request", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.buttonSubmit = QtGui.QPushButton(CLWSCDesktop)
        self.buttonSubmit.setGeometry(QtCore.QRect(190, 260, 81, 31))
        self.buttonSubmit.setText(QtGui.QApplication.translate("CLWSCDesktop", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSubmit.setObjectName(_fromUtf8("buttonSubmit"))
        self.textBoxName = QtGui.QTextEdit(CLWSCDesktop)
        self.textBoxName.setGeometry(QtCore.QRect(80, 10, 191, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBoxName.sizePolicy().hasHeightForWidth())
        self.textBoxName.setSizePolicy(sizePolicy)
        self.textBoxName.setObjectName(_fromUtf8("textBoxName"))
        self.textBoxEmail = QtGui.QTextEdit(CLWSCDesktop)
        self.textBoxEmail.setGeometry(QtCore.QRect(80, 50, 191, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBoxEmail.sizePolicy().hasHeightForWidth())
        self.textBoxEmail.setSizePolicy(sizePolicy)
        self.textBoxEmail.setObjectName(_fromUtf8("textBoxEmail"))
        self.textBoxSubject = QtGui.QTextEdit(CLWSCDesktop)
        self.textBoxSubject.setGeometry(QtCore.QRect(80, 90, 191, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBoxSubject.sizePolicy().hasHeightForWidth())
        self.textBoxSubject.setSizePolicy(sizePolicy)
        self.textBoxSubject.setObjectName(_fromUtf8("textBoxSubject"))

        self.retranslateUi(CLWSCDesktop)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CLWSCDesktop.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CLWSCDesktop.reject)
        QtCore.QMetaObject.connectSlotsByName(CLWSCDesktop)

    def retranslateUi(self, CLWSCDesktop):
        pass

