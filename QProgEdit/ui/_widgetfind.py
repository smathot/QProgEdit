# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/findWidget.ui'
#
# Created: Wed Dec 26 14:36:42 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_widgetFind(object):
    def setupUi(self, widgetFind):
        widgetFind.setObjectName(_fromUtf8("widgetFind"))
        widgetFind.resize(625, 128)
        widgetFind.setAutoFillBackground(True)
        self.gridLayout = QtGui.QGridLayout(widgetFind)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelReplace = QtGui.QLabel(widgetFind)
        self.labelReplace.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelReplace.setObjectName(_fromUtf8("labelReplace"))
        self.gridLayout.addWidget(self.labelReplace, 1, 0, 1, 1)
        self.labelFind = QtGui.QLabel(widgetFind)
        self.labelFind.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelFind.setObjectName(_fromUtf8("labelFind"))
        self.gridLayout.addWidget(self.labelFind, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(widgetFind)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonFind = QtGui.QPushButton(self.widget)
        self.pushButtonFind.setObjectName(_fromUtf8("pushButtonFind"))
        self.horizontalLayout.addWidget(self.pushButtonFind)
        self.pushButtonReplace = QtGui.QPushButton(self.widget)
        self.pushButtonReplace.setObjectName(_fromUtf8("pushButtonReplace"))
        self.horizontalLayout.addWidget(self.pushButtonReplace)
        self.pushButtonReplaceAll = QtGui.QPushButton(self.widget)
        self.pushButtonReplaceAll.setObjectName(_fromUtf8("pushButtonReplaceAll"))
        self.horizontalLayout.addWidget(self.pushButtonReplaceAll)
        self.gridLayout.addWidget(self.widget, 6, 0, 1, 3)
        self.widget_2 = QtGui.QWidget(widgetFind)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBoxCaseSensitive = QtGui.QCheckBox(self.widget_2)
        self.checkBoxCaseSensitive.setObjectName(_fromUtf8("checkBoxCaseSensitive"))
        self.horizontalLayout_2.addWidget(self.checkBoxCaseSensitive)
        self.checkBoxMatchWhole = QtGui.QCheckBox(self.widget_2)
        self.checkBoxMatchWhole.setObjectName(_fromUtf8("checkBoxMatchWhole"))
        self.horizontalLayout_2.addWidget(self.checkBoxMatchWhole)
        self.gridLayout.addWidget(self.widget_2, 3, 0, 1, 2)
        self.lineEditReplace = QtGui.QLineEdit(widgetFind)
        self.lineEditReplace.setObjectName(_fromUtf8("lineEditReplace"))
        self.gridLayout.addWidget(self.lineEditReplace, 1, 1, 1, 1)
        self.lineEditFind = QtGui.QLineEdit(widgetFind)
        self.lineEditFind.setObjectName(_fromUtf8("lineEditFind"))
        self.gridLayout.addWidget(self.lineEditFind, 0, 1, 1, 1)

        self.retranslateUi(widgetFind)
        QtCore.QMetaObject.connectSlotsByName(widgetFind)

    def retranslateUi(self, widgetFind):
        widgetFind.setWindowTitle(QtGui.QApplication.translate("widgetFind", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.labelReplace.setText(QtGui.QApplication.translate("widgetFind", "Replace:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFind.setText(QtGui.QApplication.translate("widgetFind", "Find:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFind.setText(QtGui.QApplication.translate("widgetFind", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonReplace.setText(QtGui.QApplication.translate("widgetFind", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonReplaceAll.setText(QtGui.QApplication.translate("widgetFind", "Replace all", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCaseSensitive.setText(QtGui.QApplication.translate("widgetFind", "Case sensitive", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxMatchWhole.setText(QtGui.QApplication.translate("widgetFind", "Match whole words", None, QtGui.QApplication.UnicodeUTF8))

