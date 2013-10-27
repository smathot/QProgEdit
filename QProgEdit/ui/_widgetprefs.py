# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/prefsWidget.ui'
#
# Created: Sun Oct 27 10:48:20 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_widgetPrefs(object):
    def setupUi(self, widgetPrefs):
        widgetPrefs.setObjectName(_fromUtf8("widgetPrefs"))
        widgetPrefs.resize(573, 267)
        widgetPrefs.setAutoFillBackground(True)
        self.gridLayout = QtGui.QGridLayout(widgetPrefs)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBoxWordWrapMarker = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxWordWrapMarker.setObjectName(_fromUtf8("checkBoxWordWrapMarker"))
        self.gridLayout.addWidget(self.checkBoxWordWrapMarker, 13, 1, 1, 1)
        self.labelTabWidth = QtGui.QLabel(widgetPrefs)
        self.labelTabWidth.setObjectName(_fromUtf8("labelTabWidth"))
        self.gridLayout.addWidget(self.labelTabWidth, 2, 0, 1, 1)
        self.spinBoxTabWidth = QtGui.QSpinBox(widgetPrefs)
        self.spinBoxTabWidth.setObjectName(_fromUtf8("spinBoxTabWidth"))
        self.gridLayout.addWidget(self.spinBoxTabWidth, 2, 1, 1, 1)
        self.labelFontFamily = QtGui.QLabel(widgetPrefs)
        self.labelFontFamily.setObjectName(_fromUtf8("labelFontFamily"))
        self.gridLayout.addWidget(self.labelFontFamily, 0, 0, 1, 1)
        self.checkBoxShowWhitespace = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowWhitespace.setObjectName(_fromUtf8("checkBoxShowWhitespace"))
        self.gridLayout.addWidget(self.checkBoxShowWhitespace, 6, 1, 1, 1)
        self.checkBoxLineNumbers = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxLineNumbers.setObjectName(_fromUtf8("checkBoxLineNumbers"))
        self.gridLayout.addWidget(self.checkBoxLineNumbers, 4, 1, 1, 1)
        self.checkBoxWordWrap = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxWordWrap.setObjectName(_fromUtf8("checkBoxWordWrap"))
        self.gridLayout.addWidget(self.checkBoxWordWrap, 7, 0, 1, 1)
        self.checkBoxShowFolding = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowFolding.setObjectName(_fromUtf8("checkBoxShowFolding"))
        self.gridLayout.addWidget(self.checkBoxShowFolding, 13, 0, 1, 1)
        self.checkBoxAutoComplete = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxAutoComplete.setObjectName(_fromUtf8("checkBoxAutoComplete"))
        self.gridLayout.addWidget(self.checkBoxAutoComplete, 14, 0, 1, 1)
        self.fontComboBoxFontFamily = QtGui.QFontComboBox(widgetPrefs)
        self.fontComboBoxFontFamily.setObjectName(_fromUtf8("fontComboBoxFontFamily"))
        self.gridLayout.addWidget(self.fontComboBoxFontFamily, 0, 1, 1, 1)
        self.checkBoxShowEol = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowEol.setObjectName(_fromUtf8("checkBoxShowEol"))
        self.gridLayout.addWidget(self.checkBoxShowEol, 5, 1, 1, 1)
        self.checkBoxShowIndent = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowIndent.setObjectName(_fromUtf8("checkBoxShowIndent"))
        self.gridLayout.addWidget(self.checkBoxShowIndent, 7, 1, 1, 1)
        self.labelFontSize = QtGui.QLabel(widgetPrefs)
        self.labelFontSize.setObjectName(_fromUtf8("labelFontSize"))
        self.gridLayout.addWidget(self.labelFontSize, 1, 0, 1, 1)
        self.spinBoxFontSize = QtGui.QSpinBox(widgetPrefs)
        self.spinBoxFontSize.setObjectName(_fromUtf8("spinBoxFontSize"))
        self.gridLayout.addWidget(self.spinBoxFontSize, 1, 1, 1, 1)
        self.checkBoxHighlightCurrentLine = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxHighlightCurrentLine.setObjectName(_fromUtf8("checkBoxHighlightCurrentLine"))
        self.gridLayout.addWidget(self.checkBoxHighlightCurrentLine, 4, 0, 1, 1)
        self.checkBoxHighlightMatchingBrackets = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxHighlightMatchingBrackets.setObjectName(_fromUtf8("checkBoxHighlightMatchingBrackets"))
        self.gridLayout.addWidget(self.checkBoxHighlightMatchingBrackets, 5, 0, 1, 1)
        self.checkBoxAutoIndent = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxAutoIndent.setObjectName(_fromUtf8("checkBoxAutoIndent"))
        self.gridLayout.addWidget(self.checkBoxAutoIndent, 6, 0, 1, 1)
        self.comboBoxColorScheme = QtGui.QComboBox(widgetPrefs)
        self.comboBoxColorScheme.setObjectName(_fromUtf8("comboBoxColorScheme"))
        self.gridLayout.addWidget(self.comboBoxColorScheme, 3, 1, 1, 1)
        self.labelColorScheme = QtGui.QLabel(widgetPrefs)
        self.labelColorScheme.setObjectName(_fromUtf8("labelColorScheme"))
        self.gridLayout.addWidget(self.labelColorScheme, 3, 0, 1, 1)

        self.retranslateUi(widgetPrefs)
        QtCore.QMetaObject.connectSlotsByName(widgetPrefs)

    def retranslateUi(self, widgetPrefs):
        widgetPrefs.setWindowTitle(_translate("widgetPrefs", "Form", None))
        self.checkBoxWordWrapMarker.setText(_translate("widgetPrefs", "Show 80 character word-wrap marker", None))
        self.labelTabWidth.setText(_translate("widgetPrefs", "Tab width", None))
        self.spinBoxTabWidth.setSuffix(_translate("widgetPrefs", " characters", None))
        self.labelFontFamily.setText(_translate("widgetPrefs", "Font family", None))
        self.checkBoxShowWhitespace.setText(_translate("widgetPrefs", "Show whitespace", None))
        self.checkBoxLineNumbers.setText(_translate("widgetPrefs", "Show line numbers", None))
        self.checkBoxWordWrap.setText(_translate("widgetPrefs", "Enable word wrapping", None))
        self.checkBoxShowFolding.setText(_translate("widgetPrefs", "Enable block folding", None))
        self.checkBoxAutoComplete.setText(_translate("widgetPrefs", "Enable automatic completion", None))
        self.checkBoxShowEol.setText(_translate("widgetPrefs", "Show end-of-lines", None))
        self.checkBoxShowIndent.setText(_translate("widgetPrefs", "Show indentation", None))
        self.labelFontSize.setText(_translate("widgetPrefs", "Font size", None))
        self.spinBoxFontSize.setSuffix(_translate("widgetPrefs", " pt", None))
        self.checkBoxHighlightCurrentLine.setText(_translate("widgetPrefs", "Highlight current line", None))
        self.checkBoxHighlightMatchingBrackets.setText(_translate("widgetPrefs", "Highlight matching brackets", None))
        self.checkBoxAutoIndent.setText(_translate("widgetPrefs", "Enable automatic indentation", None))
        self.labelColorScheme.setText(_translate("widgetPrefs", "Color scheme", None))

