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

import sys
from PyQt4 import QtGui, QtCore
from QProgEdit import QTabManager, validate

def focusOut():
	
	"""Is called when an editor widget loses focus."""
	
	print u'focusOut()'
	
def apply():
	
	"""Is called when the apply button is pressed."""
	
	print u'apply()'	

def main():
	
	"""Runs a simple QProgEdit demonstration."""

	validate.addPythonBuiltins(['builtin_var'])
	app = QtGui.QApplication(sys.argv)
	tabManager = QTabManager(defaultLang=u'python', handler=apply, \
		focusOutHandler=focusOut, handlerButtonText=u'apply')
	tabManager.setWindowIcon(QtGui.QIcon.fromTheme(u'accessories-text-editor'))
	tabManager.setWindowTitle(u'QProgEdit')
	tabManager.resize(800, 600)
	tabManager.addTab(u'Tab 1', lang=u'Python')
	tabManager.setText(open(__file__).read())
	tabManager.addTab(u'Tab 2', lang=u'Python')
	tabManager.setText(u'def test():\n\tprint undefined_var\n\tbuiltin_var\n\ntest()\n')
	tabManager.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
