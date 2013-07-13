# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/prefsWidget.ui'
#
# Created: Wed Dec 26 14:36:43 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_widgetPrefs(object):
    def setupUi(self, widgetPrefs):
        widgetPrefs.setObjectName(_fromUtf8("widgetPrefs"))
        widgetPrefs.resize(572, 238)
        widgetPrefs.setAutoFillBackground(True)
        self.gridLayout = QtGui.QGridLayout(widgetPrefs)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fontComboBoxFontFamily = QtGui.QFontComboBox(widgetPrefs)
        self.fontComboBoxFontFamily.setObjectName(_fromUtf8("fontComboBoxFontFamily"))
        self.gridLayout.addWidget(self.fontComboBoxFontFamily, 0, 1, 1, 1)
        self.checkBoxShowEol = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowEol.setObjectName(_fromUtf8("checkBoxShowEol"))
        self.gridLayout.addWidget(self.checkBoxShowEol, 4, 1, 1, 1)
        self.labelTabWidth = QtGui.QLabel(widgetPrefs)
        self.labelTabWidth.setObjectName(_fromUtf8("labelTabWidth"))
        self.gridLayout.addWidget(self.labelTabWidth, 2, 0, 1, 1)
        self.spinBoxTabWidth = QtGui.QSpinBox(widgetPrefs)
        self.spinBoxTabWidth.setObjectName(_fromUtf8("spinBoxTabWidth"))
        self.gridLayout.addWidget(self.spinBoxTabWidth, 2, 1, 1, 1)
        self.checkBoxShowIndent = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowIndent.setObjectName(_fromUtf8("checkBoxShowIndent"))
        self.gridLayout.addWidget(self.checkBoxShowIndent, 6, 1, 1, 1)
        self.labelFontSize = QtGui.QLabel(widgetPrefs)
        self.labelFontSize.setObjectName(_fromUtf8("labelFontSize"))
        self.gridLayout.addWidget(self.labelFontSize, 1, 0, 1, 1)
        self.spinBoxFontSize = QtGui.QSpinBox(widgetPrefs)
        self.spinBoxFontSize.setObjectName(_fromUtf8("spinBoxFontSize"))
        self.gridLayout.addWidget(self.spinBoxFontSize, 1, 1, 1, 1)
        self.labelFontFamily = QtGui.QLabel(widgetPrefs)
        self.labelFontFamily.setObjectName(_fromUtf8("labelFontFamily"))
        self.gridLayout.addWidget(self.labelFontFamily, 0, 0, 1, 1)
        self.checkBoxShowWhitespace = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowWhitespace.setObjectName(_fromUtf8("checkBoxShowWhitespace"))
        self.gridLayout.addWidget(self.checkBoxShowWhitespace, 5, 1, 1, 1)
        self.checkBoxLineNumbers = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxLineNumbers.setObjectName(_fromUtf8("checkBoxLineNumbers"))
        self.gridLayout.addWidget(self.checkBoxLineNumbers, 3, 1, 1, 1)
        self.checkBoxHighlightCurrentLine = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxHighlightCurrentLine.setObjectName(_fromUtf8("checkBoxHighlightCurrentLine"))
        self.gridLayout.addWidget(self.checkBoxHighlightCurrentLine, 3, 0, 1, 1)
        self.checkBoxHighlightMatchingBrackets = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxHighlightMatchingBrackets.setObjectName(_fromUtf8("checkBoxHighlightMatchingBrackets"))
        self.gridLayout.addWidget(self.checkBoxHighlightMatchingBrackets, 4, 0, 1, 1)
        self.checkBoxAutoIndent = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxAutoIndent.setObjectName(_fromUtf8("checkBoxAutoIndent"))
        self.gridLayout.addWidget(self.checkBoxAutoIndent, 5, 0, 1, 1)
        self.checkBoxWordWrap = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxWordWrap.setObjectName(_fromUtf8("checkBoxWordWrap"))
        self.gridLayout.addWidget(self.checkBoxWordWrap, 6, 0, 1, 1)
        self.checkBoxShowFolding = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowFolding.setObjectName(_fromUtf8("checkBoxShowFolding"))
        self.gridLayout.addWidget(self.checkBoxShowFolding, 12, 0, 1, 1)
        self.checkBoxAutoComplete = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxAutoComplete.setObjectName(_fromUtf8("checkBoxAutoComplete"))
        self.gridLayout.addWidget(self.checkBoxAutoComplete, 13, 0, 1, 1)
        self.checkBoxWordWrapMarker = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxWordWrapMarker.setObjectName(_fromUtf8("checkBoxWordWrapMarker"))
        self.gridLayout.addWidget(self.checkBoxWordWrapMarker, 12, 1, 1, 1)

        self.retranslateUi(widgetPrefs)
        QtCore.QMetaObject.connectSlotsByName(widgetPrefs)

    def retranslateUi(self, widgetPrefs):
        widgetPrefs.setWindowTitle(QtGui.QApplication.translate("widgetPrefs", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowEol.setText(QtGui.QApplication.translate("widgetPrefs", "Show end-of-lines", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTabWidth.setText(QtGui.QApplication.translate("widgetPrefs", "Tab width", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxTabWidth.setSuffix(QtGui.QApplication.translate("widgetPrefs", " characters", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowIndent.setText(QtGui.QApplication.translate("widgetPrefs", "Show indentation", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFontSize.setText(QtGui.QApplication.translate("widgetPrefs", "Font size", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxFontSize.setSuffix(QtGui.QApplication.translate("widgetPrefs", " pt", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFontFamily.setText(QtGui.QApplication.translate("widgetPrefs", "Font family", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowWhitespace.setText(QtGui.QApplication.translate("widgetPrefs", "Show whitespace", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxLineNumbers.setText(QtGui.QApplication.translate("widgetPrefs", "Show line numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxHighlightCurrentLine.setText(QtGui.QApplication.translate("widgetPrefs", "Highlight current line", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxHighlightMatchingBrackets.setText(QtGui.QApplication.translate("widgetPrefs", "Highlight matching brackets", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxAutoIndent.setText(QtGui.QApplication.translate("widgetPrefs", "Enable automatic indentation", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxWordWrap.setText(QtGui.QApplication.translate("widgetPrefs", "Enable word wrapping", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowFolding.setText(QtGui.QApplication.translate("widgetPrefs", "Enable block folding", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxAutoComplete.setText(QtGui.QApplication.translate("widgetPrefs", "Enable automatic completion", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxWordWrapMarker.setText(QtGui.QApplication.translate("widgetPrefs", "Show 80 character word-wrap marker", None, QtGui.QApplication.UnicodeUTF8))

