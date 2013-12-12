# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/prefsWidget.ui'
#
# Created: Thu Dec 12 14:48:46 2013
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
        widgetPrefs.resize(853, 224)
        widgetPrefs.setAutoFillBackground(True)
        self.gridLayout = QtGui.QGridLayout(widgetPrefs)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBoxWordWrap = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxWordWrap.setObjectName(_fromUtf8("checkBoxWordWrap"))
        self.gridLayout.addWidget(self.checkBoxWordWrap, 4, 1, 1, 1)
        self.comboBoxColorScheme = QtGui.QComboBox(widgetPrefs)
        self.comboBoxColorScheme.setObjectName(_fromUtf8("comboBoxColorScheme"))
        self.gridLayout.addWidget(self.comboBoxColorScheme, 2, 3, 1, 1)
        self.spinBoxTabWidth = QtGui.QSpinBox(widgetPrefs)
        self.spinBoxTabWidth.setObjectName(_fromUtf8("spinBoxTabWidth"))
        self.gridLayout.addWidget(self.spinBoxTabWidth, 2, 1, 1, 1)
        self.labelFontFamily = QtGui.QLabel(widgetPrefs)
        self.labelFontFamily.setObjectName(_fromUtf8("labelFontFamily"))
        self.gridLayout.addWidget(self.labelFontFamily, 0, 0, 1, 1)
        self.checkBoxShowIndent = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowIndent.setObjectName(_fromUtf8("checkBoxShowIndent"))
        self.gridLayout.addWidget(self.checkBoxShowIndent, 4, 3, 1, 1)
        self.spinBoxFontSize = QtGui.QSpinBox(widgetPrefs)
        self.spinBoxFontSize.setObjectName(_fromUtf8("spinBoxFontSize"))
        self.gridLayout.addWidget(self.spinBoxFontSize, 1, 1, 1, 1)
        self.checkBoxShowEol = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowEol.setObjectName(_fromUtf8("checkBoxShowEol"))
        self.gridLayout.addWidget(self.checkBoxShowEol, 5, 2, 1, 1)
        self.labelTabWidth = QtGui.QLabel(widgetPrefs)
        self.labelTabWidth.setObjectName(_fromUtf8("labelTabWidth"))
        self.gridLayout.addWidget(self.labelTabWidth, 2, 0, 1, 1)
        self.checkBoxAutoIndent = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxAutoIndent.setObjectName(_fromUtf8("checkBoxAutoIndent"))
        self.gridLayout.addWidget(self.checkBoxAutoIndent, 6, 0, 1, 1)
        self.checkBoxLineNumbers = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxLineNumbers.setObjectName(_fromUtf8("checkBoxLineNumbers"))
        self.gridLayout.addWidget(self.checkBoxLineNumbers, 4, 2, 1, 1)
        self.fontComboBoxFontFamily = QtGui.QFontComboBox(widgetPrefs)
        self.fontComboBoxFontFamily.setObjectName(_fromUtf8("fontComboBoxFontFamily"))
        self.gridLayout.addWidget(self.fontComboBoxFontFamily, 0, 1, 1, 1)
        self.labelFontSize = QtGui.QLabel(widgetPrefs)
        self.labelFontSize.setObjectName(_fromUtf8("labelFontSize"))
        self.gridLayout.addWidget(self.labelFontSize, 1, 0, 1, 1)
        self.checkBoxHighlightCurrentLine = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxHighlightCurrentLine.setObjectName(_fromUtf8("checkBoxHighlightCurrentLine"))
        self.gridLayout.addWidget(self.checkBoxHighlightCurrentLine, 4, 0, 1, 1)
        self.checkBoxHighlightMatchingBrackets = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxHighlightMatchingBrackets.setObjectName(_fromUtf8("checkBoxHighlightMatchingBrackets"))
        self.gridLayout.addWidget(self.checkBoxHighlightMatchingBrackets, 5, 0, 1, 1)
        self.labelCommentShortcut = QtGui.QLabel(widgetPrefs)
        self.labelCommentShortcut.setObjectName(_fromUtf8("labelCommentShortcut"))
        self.gridLayout.addWidget(self.labelCommentShortcut, 0, 2, 1, 1)
        self.lineEditUncommentShortcut = QtGui.QLineEdit(widgetPrefs)
        self.lineEditUncommentShortcut.setObjectName(_fromUtf8("lineEditUncommentShortcut"))
        self.gridLayout.addWidget(self.lineEditUncommentShortcut, 1, 3, 1, 1)
        self.checkBoxShowWhitespace = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowWhitespace.setObjectName(_fromUtf8("checkBoxShowWhitespace"))
        self.gridLayout.addWidget(self.checkBoxShowWhitespace, 5, 3, 1, 1)
        self.checkBoxShowFolding = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxShowFolding.setObjectName(_fromUtf8("checkBoxShowFolding"))
        self.gridLayout.addWidget(self.checkBoxShowFolding, 5, 1, 1, 1)
        self.lineEditCommentShortcut = QtGui.QLineEdit(widgetPrefs)
        self.lineEditCommentShortcut.setObjectName(_fromUtf8("lineEditCommentShortcut"))
        self.gridLayout.addWidget(self.lineEditCommentShortcut, 0, 3, 1, 1)
        self.labelColorScheme = QtGui.QLabel(widgetPrefs)
        self.labelColorScheme.setObjectName(_fromUtf8("labelColorScheme"))
        self.gridLayout.addWidget(self.labelColorScheme, 2, 2, 1, 1)
        self.checkBoxAutoComplete = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxAutoComplete.setObjectName(_fromUtf8("checkBoxAutoComplete"))
        self.gridLayout.addWidget(self.checkBoxAutoComplete, 6, 1, 1, 1)
        self.labelUncommentShortcut = QtGui.QLabel(widgetPrefs)
        self.labelUncommentShortcut.setObjectName(_fromUtf8("labelUncommentShortcut"))
        self.gridLayout.addWidget(self.labelUncommentShortcut, 1, 2, 1, 1)
        self.checkBoxWordWrapMarker = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxWordWrapMarker.setObjectName(_fromUtf8("checkBoxWordWrapMarker"))
        self.gridLayout.addWidget(self.checkBoxWordWrapMarker, 6, 3, 1, 1)
        self.checkBoxValidate = QtGui.QCheckBox(widgetPrefs)
        self.checkBoxValidate.setObjectName(_fromUtf8("checkBoxValidate"))
        self.gridLayout.addWidget(self.checkBoxValidate, 6, 2, 1, 1)

        self.retranslateUi(widgetPrefs)
        QtCore.QMetaObject.connectSlotsByName(widgetPrefs)

    def retranslateUi(self, widgetPrefs):
        widgetPrefs.setWindowTitle(_translate("widgetPrefs", "Form", None))
        self.checkBoxWordWrap.setText(_translate("widgetPrefs", "Enable word wrapping", None))
        self.comboBoxColorScheme.setToolTip(_translate("widgetPrefs", "A color scheme for the editor component", None))
        self.spinBoxTabWidth.setToolTip(_translate("widgetPrefs", "The tab width for the editor component", None))
        self.spinBoxTabWidth.setSuffix(_translate("widgetPrefs", " characters", None))
        self.labelFontFamily.setText(_translate("widgetPrefs", "Font family", None))
        self.checkBoxShowIndent.setText(_translate("widgetPrefs", "Show indentation", None))
        self.spinBoxFontSize.setToolTip(_translate("widgetPrefs", "The font size for the editor component", None))
        self.spinBoxFontSize.setSuffix(_translate("widgetPrefs", " pt", None))
        self.checkBoxShowEol.setText(_translate("widgetPrefs", "Show end-of-lines", None))
        self.labelTabWidth.setText(_translate("widgetPrefs", "Tab width", None))
        self.checkBoxAutoIndent.setText(_translate("widgetPrefs", "Enable automatic indentation", None))
        self.checkBoxLineNumbers.setText(_translate("widgetPrefs", "Show line numbers", None))
        self.fontComboBoxFontFamily.setToolTip(_translate("widgetPrefs", "The font font the editor component", None))
        self.labelFontSize.setText(_translate("widgetPrefs", "Font size", None))
        self.checkBoxHighlightCurrentLine.setText(_translate("widgetPrefs", "Highlight current line", None))
        self.checkBoxHighlightMatchingBrackets.setText(_translate("widgetPrefs", "Highlight matching brackets", None))
        self.labelCommentShortcut.setText(_translate("widgetPrefs", "Comment shortcut", None))
        self.lineEditUncommentShortcut.setToolTip(_translate("widgetPrefs", "A keyboard shortcut, such as Ctrl+Shift+M", None))
        self.checkBoxShowWhitespace.setText(_translate("widgetPrefs", "Show whitespace", None))
        self.checkBoxShowFolding.setText(_translate("widgetPrefs", "Enable block folding", None))
        self.lineEditCommentShortcut.setToolTip(_translate("widgetPrefs", "A keyboard shortcut, such as Ctrl+M", None))
        self.labelColorScheme.setText(_translate("widgetPrefs", "Color scheme", None))
        self.checkBoxAutoComplete.setText(_translate("widgetPrefs", "Enable automatic completion", None))
        self.labelUncommentShortcut.setText(_translate("widgetPrefs", "Uncomment shortcut", None))
        self.checkBoxWordWrapMarker.setText(_translate("widgetPrefs", "Show 80 character word-wrap marker", None))
        self.checkBoxValidate.setText(_translate("widgetPrefs", "Validate content", None))

