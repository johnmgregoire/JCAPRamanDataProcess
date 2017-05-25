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
        self.textBrowser_xy.setGeometry(QtCore.QRect(490, 10, 491, 301))
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
        self.textBrowser_xy2.setGeometry(QtCore.QRect(490, 320, 491, 301))
        self.textBrowser_xy2.setObjectName(_fromUtf8("textBrowser_xy2"))
        self.avePushButton = QtGui.QPushButton(DataParseDialog)
        self.avePushButton.setGeometry(QtCore.QRect(280, 140, 111, 31))
        self.avePushButton.setObjectName(_fromUtf8("avePushButton"))
        self.ramaninfoTextBrowser = QtGui.QTextBrowser(DataParseDialog)
        self.ramaninfoTextBrowser.setGeometry(QtCore.QRect(300, 290, 151, 211))
        self.ramaninfoTextBrowser.setObjectName(_fromUtf8("ramaninfoTextBrowser"))
        self.OutlierAveDoubleSpinBox = QtGui.QDoubleSpinBox(DataParseDialog)
        self.OutlierAveDoubleSpinBox.setGeometry(QtCore.QRect(420, 170, 41, 22))
        self.OutlierAveDoubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.OutlierAveDoubleSpinBox.setProperty("value", 0.05)
        self.OutlierAveDoubleSpinBox.setObjectName(_fromUtf8("OutlierAveDoubleSpinBox"))
        self.label_8 = QtGui.QLabel(DataParseDialog)
        self.label_8.setGeometry(QtCore.QRect(400, 130, 91, 41))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(DataParseDialog)
        QtCore.QMetaObject.connectSlotsByName(DataParseDialog)

    def retranslateUi(self, DataParseDialog):
        DataParseDialog.setWindowTitle(_translate("DataParseDialog", "Dialog", None))
        self.rawpathLineEdit.setToolTip(_translate("DataParseDialog", "Paste the path to the Renishaw file here or use \"select\" to choose it.\n"
"This is required beofre \"Get Raman File Info\" or \"Extract Raman Spectra\"", None))
        self.label.setText(_translate("DataParseDialog", "Renishaw txt file", None))
        self.rawpathPushButton.setText(_translate("DataParseDialog", "select", None))
        self.label_2.setText(_translate("DataParseDialog", "Renishaw info pck file", None))
        self.infopathLineEdit.setToolTip(_translate("DataParseDialog", "Creating this *__info.pck takes time so select it if you have already created it. \n"
"Required before \"Match Raman File\" or \"Extract Raman Spectra\"", None))
        self.infopathPushButton.setToolTip(_translate("DataParseDialog", "Select existing *__info.pck file, and then \"Get Raman Info\" will run.", None))
        self.infopathPushButton.setText(_translate("DataParseDialog", "select", None))
        self.savepathLineEdit.setToolTip(_translate("DataParseDialog", "Where the .map file and the select spectra will be saved. Required before\n"
"\"Match Raman File\" or \"copy map\" or \"Extract\", etc.", None))
        self.savepathPushButton.setText(_translate("DataParseDialog", "Browse", None))
        self.label_3.setText(_translate("DataParseDialog", "save spectra folder", None))
        self.sampleinfoTextBrowser.setToolTip(_translate("DataParseDialog", "Table with 5 required columns needed to generate .map file.\n"
"This can have extra columns and the column headings can be anything as long as\n"
"the 5 required columns are present with headings listed below.", None))
        self.label_4.setText(_translate("DataParseDialog", "Select Sample Table (tab-deliminated)", None))
        self.label_5.setText(_translate("DataParseDialog", "column names for\n"
"sample_no,xrng_0,xrng_1,yrng_0,yrng_1", None))
        self.infokeysLineEdit.setToolTip(_translate("DataParseDialog", "The names of the 5 column headings must be entered here.", None))
        self.infokeysLineEdit.setText(_translate("DataParseDialog", "sample_no,xrng_0,xrng_1,yrng_0,yrng_1", None))
        self.getinfoPushButton.setToolTip(_translate("DataParseDialog", "Either creates the *__info.pck from the *.txt or read the .pck if it already exists. \n"
"This is general info on the file and independent of choosing samples", None))
        self.getinfoPushButton.setText(_translate("DataParseDialog", "Get Raman File Info\n"
"(read pck if exists)", None))
        self.matchPushButton.setToolTip(_translate("DataParseDialog", "Creates raman_sample_index_map.map in the save spectra folder\n"
"which contains the list of sample_no and the spectrum indeces that belong to it.", None))
        self.matchPushButton.setText(_translate("DataParseDialog", "Match Raman File to\n"
"Select Sample Table", None))
        self.extractPushButton.setToolTip(_translate("DataParseDialog", "Saves the selected spectra in Sample*_selectspectra.rmn files in save folder. \n"
"The table and column names must be entered first.", None))
        self.extractPushButton.setText(_translate("DataParseDialog", "Extract Raman\n"
"Spectra to File", None))
        self.sampleComboBox.setToolTip(_translate("DataParseDialog", "For each line in the Select Sample Table shows the sampl_no (# of Raman spectra found).\n"
"Selecting a menu option will cause the plots to update.", None))
        self.plotComboBox.setToolTip(_translate("DataParseDialog", "Select the algorithm for generating plots  based on teh set of spectra for the sample_no selected above", None))
        self.label_6.setText(_translate("DataParseDialog", "sample (# spectra)", None))
        self.label_7.setText(_translate("DataParseDialog", "plot style", None))
        self.infopathnewPushButton.setToolTip(_translate("DataParseDialog", "If creating *__info.pck file for the first time select the \"new\" path here.", None))
        self.infopathnewPushButton.setText(_translate("DataParseDialog", "new", None))
        self.copymatchPushButton.setToolTip(_translate("DataParseDialog", "Choose a previosuly-generated raman_sample_index_map.map or one that you made custom.", None))
        self.copymatchPushButton.setText(_translate("DataParseDialog", "OR copy\n"
"map file", None))
        self.readfolderPushButton.setToolTip(_translate("DataParseDialog", "Read .rmn files from \"save spectra folder\" for plotting only", None))
        self.readfolderPushButton.setText(_translate("DataParseDialog", "Read Save\n"
"Spectra Folder", None))
        self.avePushButton.setToolTip(_translate("DataParseDialog", "create Sample*_ave.rmn files", None))
        self.avePushButton.setText(_translate("DataParseDialog", "Save Ave Spectrum\n"
" for each sample", None))
        self.ramaninfoTextBrowser.setToolTip(_translate("DataParseDialog", "General info on the Raman file. If text appears here then the \"Get Raman File Info\" successfully completed.", None))
        self.OutlierAveDoubleSpinBox.setToolTip(_translate("DataParseDialog", "Take this fraction of the number of \n"
"spectra about to be averaged and remove the highest difference from mean\n"
"using sum-of-squares to compare spectra.\n"
"This happens in saving and plotting to set to 0 for quick calculation.", None))
        self.label_8.setText(_translate("DataParseDialog", "Frac spectra to\n"
"remove as outliers", None))

