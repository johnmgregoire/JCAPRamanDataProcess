# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Google Drive\Documents\PythonCode\JCAP\JCAPRamanDataProcess\ui\DataParseDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DataParseDialog(object):
    def setupUi(self, DataParseDialog):
        DataParseDialog.setObjectName(_fromUtf8("DataParseDialog"))
        DataParseDialog.resize(1074, 630)
        self.rawpathLineEdit = QtGui.QLineEdit(DataParseDialog)
        self.rawpathLineEdit.setGeometry(QtCore.QRect(10, 30, 261, 20))
        self.rawpathLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rawpathLineEdit.setObjectName(_fromUtf8("rawpathLineEdit"))
        self.label = QtGui.QLabel(DataParseDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.rawpathPushButton = QtGui.QPushButton(DataParseDialog)
        self.rawpathPushButton.setGeometry(QtCore.QRect(220, 10, 51, 23))
        self.rawpathPushButton.setObjectName(_fromUtf8("rawpathPushButton"))
        self.label_2 = QtGui.QLabel(DataParseDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 131, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.infopathLineEdit = QtGui.QLineEdit(DataParseDialog)
        self.infopathLineEdit.setGeometry(QtCore.QRect(10, 80, 261, 20))
        self.infopathLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.infopathLineEdit.setObjectName(_fromUtf8("infopathLineEdit"))
        self.infopathPushButton = QtGui.QPushButton(DataParseDialog)
        self.infopathPushButton.setGeometry(QtCore.QRect(170, 60, 51, 23))
        self.infopathPushButton.setObjectName(_fromUtf8("infopathPushButton"))
        self.savepathLineEdit = QtGui.QLineEdit(DataParseDialog)
        self.savepathLineEdit.setGeometry(QtCore.QRect(10, 130, 261, 20))
        self.savepathLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.savepathLineEdit.setObjectName(_fromUtf8("savepathLineEdit"))
        self.savepathPushButton = QtGui.QPushButton(DataParseDialog)
        self.savepathPushButton.setGeometry(QtCore.QRect(220, 110, 51, 23))
        self.savepathPushButton.setObjectName(_fromUtf8("savepathPushButton"))
        self.label_3 = QtGui.QLabel(DataParseDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.sampleinfoTextBrowser = QtGui.QTextBrowser(DataParseDialog)
        self.sampleinfoTextBrowser.setGeometry(QtCore.QRect(10, 180, 281, 321))
        self.sampleinfoTextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sampleinfoTextBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sampleinfoTextBrowser.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.sampleinfoTextBrowser.setReadOnly(False)
        self.sampleinfoTextBrowser.setObjectName(_fromUtf8("sampleinfoTextBrowser"))
        self.label_4 = QtGui.QLabel(DataParseDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 271, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(DataParseDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 510, 271, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.infokeysLineEdit = QtGui.QLineEdit(DataParseDialog)
        self.infokeysLineEdit.setGeometry(QtCore.QRect(10, 540, 261, 20))
        self.infokeysLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.infokeysLineEdit.setObjectName(_fromUtf8("infokeysLineEdit"))
        self.getinfoPushButton = QtGui.QPushButton(DataParseDialog)
        self.getinfoPushButton.setGeometry(QtCore.QRect(280, 0, 151, 41))
        self.getinfoPushButton.setObjectName(_fromUtf8("getinfoPushButton"))
        self.matchPushButton = QtGui.QPushButton(DataParseDialog)
        self.matchPushButton.setGeometry(QtCore.QRect(280, 50, 111, 41))
        self.matchPushButton.setObjectName(_fromUtf8("matchPushButton"))
        self.extractPushButton = QtGui.QPushButton(DataParseDialog)
        self.extractPushButton.setGeometry(QtCore.QRect(280, 100, 91, 31))
        self.extractPushButton.setObjectName(_fromUtf8("extractPushButton"))
        self.sampleComboBox = QtGui.QComboBox(DataParseDialog)
        self.sampleComboBox.setGeometry(QtCore.QRect(300, 210, 141, 22))
        self.sampleComboBox.setObjectName(_fromUtf8("sampleComboBox"))
        self.plotComboBox = QtGui.QComboBox(DataParseDialog)
        self.plotComboBox.setGeometry(QtCore.QRect(300, 260, 141, 22))
        self.plotComboBox.setObjectName(_fromUtf8("plotComboBox"))
        self.label_6 = QtGui.QLabel(DataParseDialog)
        self.label_6.setGeometry(QtCore.QRect(300, 190, 141, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(DataParseDialog)
        self.label_7.setGeometry(QtCore.QRect(300, 240, 141, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.textBrowser_xy = QtGui.QTextBrowser(DataParseDialog)
        self.textBrowser_xy.setGeometry(QtCore.QRect(460, 10, 491, 301))
        self.textBrowser_xy.setObjectName(_fromUtf8("textBrowser_xy"))
        self.infopathnewPushButton = QtGui.QPushButton(DataParseDialog)
        self.infopathnewPushButton.setGeometry(QtCore.QRect(220, 60, 51, 23))
        self.infopathnewPushButton.setObjectName(_fromUtf8("infopathnewPushButton"))
        self.copymatchPushButton = QtGui.QPushButton(DataParseDialog)
        self.copymatchPushButton.setGeometry(QtCore.QRect(390, 50, 51, 41))
        self.copymatchPushButton.setObjectName(_fromUtf8("copymatchPushButton"))
        self.readfolderPushButton = QtGui.QPushButton(DataParseDialog)
        self.readfolderPushButton.setGeometry(QtCore.QRect(370, 100, 81, 31))
        self.readfolderPushButton.setObjectName(_fromUtf8("readfolderPushButton"))
        self.textBrowser_xy2 = QtGui.QTextBrowser(DataParseDialog)
        self.textBrowser_xy2.setGeometry(QtCore.QRect(460, 320, 491, 301))
        self.textBrowser_xy2.setObjectName(_fromUtf8("textBrowser_xy2"))
        self.avePushButton = QtGui.QPushButton(DataParseDialog)
        self.avePushButton.setGeometry(QtCore.QRect(290, 140, 141, 31))
        self.avePushButton.setObjectName(_fromUtf8("avePushButton"))
        self.ramaninfoTextBrowser = QtGui.QTextBrowser(DataParseDialog)
        self.ramaninfoTextBrowser.setGeometry(QtCore.QRect(300, 290, 151, 211))
        self.ramaninfoTextBrowser.setObjectName(_fromUtf8("ramaninfoTextBrowser"))

        self.retranslateUi(DataParseDialog)
        QtCore.QMetaObject.connectSlotsByName(DataParseDialog)

    def retranslateUi(self, DataParseDialog):
        DataParseDialog.setWindowTitle(_translate("DataParseDialog", "Dialog", None))
        self.label.setText(_translate("DataParseDialog", "Renishaw txt file", None))
        self.rawpathPushButton.setText(_translate("DataParseDialog", "select", None))
        self.label_2.setText(_translate("DataParseDialog", "Renishaw info pck file", None))
        self.infopathPushButton.setText(_translate("DataParseDialog", "select", None))
        self.savepathPushButton.setText(_translate("DataParseDialog", "Browse", None))
        self.label_3.setText(_translate("DataParseDialog", "save spectra folder", None))
        self.label_4.setText(_translate("DataParseDialog", "Select Sample Table (tab-deliminated)", None))
        self.label_5.setText(_translate("DataParseDialog", "column names for\n"
"sample_no,xrng_0,xrng_1,yrng_0,yrng_1", None))
        self.infokeysLineEdit.setText(_translate("DataParseDialog", "sample_no,xrng_0,xrng_1,yrng_0,yrng_1", None))
        self.getinfoPushButton.setText(_translate("DataParseDialog", "Get Raman File Info\n"
"(read pck if exists)", None))
        self.matchPushButton.setText(_translate("DataParseDialog", "Match Raman File to\n"
"Select Sample Table", None))
        self.extractPushButton.setText(_translate("DataParseDialog", "Extract Raman\n"
"Spectra to File", None))
        self.label_6.setText(_translate("DataParseDialog", "sample (# spectra)", None))
        self.label_7.setText(_translate("DataParseDialog", "plot style", None))
        self.infopathnewPushButton.setText(_translate("DataParseDialog", "new", None))
        self.copymatchPushButton.setText(_translate("DataParseDialog", "OR copy\n"
"map file", None))
        self.readfolderPushButton.setText(_translate("DataParseDialog", "Read Save\n"
"Spectra Folder", None))
        self.avePushButton.setText(_translate("DataParseDialog", "Save Ave Spectrum\n"
" for each sample", None))

