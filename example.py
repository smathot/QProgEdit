#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
This file is part of QProgEdit.

QProgEdit is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

QProgEdit is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with QProgEdit.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
from QProgEdit.qt import QtGui, QtCore
from QProgEdit import QTabManager, validate

def cursorRowChanged(index, rowFrom, rowTo):

	print(u'curorRowChanged(): %d, %d, %d' % (index, rowFrom, rowTo))

def focusLost(index):

	print(u'focusOut(): %s' % index)

def focusReceived(index):

	print(u'focusReceived(): %s' % index)

def handlerButtonClicked(index):

	print(u'handlerButtonClicked(): %s' % index)

def activateSymbolTree(treeWidgetItem):

	if hasattr(treeWidgetItem, u'activate'):
		treeWidgetItem.activate()

def runSelectedText(s):

	print('run:\n%s' % s)

def main():

	"""Runs a simple QProgEdit demonstration."""

	validate.addPythonBuiltins(['builtin_var'])
	app = QtGui.QApplication(sys.argv)

	treeWidgetItem1 = QtGui.QTreeWidgetItem([u'Tab 1'])
	treeWidgetItem3 = QtGui.QTreeWidgetItem([u'Tab 3'])
	symbolTree = QtGui.QTreeWidget()
	symbolTree.addTopLevelItem(treeWidgetItem1)
	symbolTree.addTopLevelItem(treeWidgetItem3)
	symbolTree.itemActivated.connect(activateSymbolTree)

	tabManager = QTabManager(handlerButtonText=u'apply', runButton=True)
	tabManager.setWindowIcon(QtGui.QIcon.fromTheme(u'accessories-text-editor'))
	tabManager.setWindowTitle(u'QProgEdit')
	tabManager.resize(800, 600)

	tabManager.cursorRowChanged.connect(cursorRowChanged)
	tabManager.focusLost.connect(focusLost)
	tabManager.focusReceived.connect(focusReceived)
	tabManager.handlerButtonClicked.connect(handlerButtonClicked)
	tabManager.execute.connect(runSelectedText)

	tab = tabManager.addTab(u'Tab 1')
	tab.setLang(u'Python')
	tab.setSymbolTree(treeWidgetItem1)
	tab.setText(open(__file__).read())

	tab = tabManager.addTab(u'Tab 2')
	tab.setText(u'Some plain text')

	tab = tabManager.addTab(u'Tab 3')
	tab.setLang(u'Python')
	tab.setSymbolTree(treeWidgetItem3)
	if os.path.exists(u'content.txt'):
		tab.setText(open(u'content.txt').read())

	layout = QtGui.QHBoxLayout()
	layout.addWidget(symbolTree)
	layout.addWidget(tabManager)
	container = QtGui.QWidget()
	container.setLayout(layout)
	container.show()

	res = app.exec_()
	open(u'content.txt', u'w').write(tab.text())
	sys.exit(res)

if __name__ == '__main__':
	main()
