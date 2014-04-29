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
from PyQt4 import QtGui, QtCore
from PyQt4 import Qsci
from PyQt4.Qsci import QsciScintilla
from QProgEdit.ui import Ui_widgetFind

class QEditorFind(QtGui.QWidget):

	"""A find/ replace widget"""

	def __init__(self, parent=None):

		"""
		Constructor

		Keyword arguments:
		parent		-- 	the parent QWidget (default=None)
		"""

		super(QEditorFind, self).__init__(parent)
		self.qProgEdit = parent
		self.ui = Ui_widgetFind()
		self.ui.setupUi(self)
		self.ui.pushButtonFind.clicked.connect(self.find)
		self.ui.lineEditFind.returnPressed.connect(self.find)
		self.ui.pushButtonReplace.clicked.connect(self.replace)
		self.ui.pushButtonReplaceAll.clicked.connect(self.replaceAll)
		self.bestHeight = self.height()

	def find(self):

		"""
		Finds in the document

		Returns:
		True if matching text has been found, False otherwise
		"""

		return self.qProgEdit.editor.findFirst(self.ui.lineEditFind.text(), \
			False, self.ui.checkBoxCaseSensitive.isChecked(), \
			self.ui.checkBoxMatchWhole.isChecked(), True)

	def replace(self):

		"""
		Replaces the first occurence in the document

		Returns:
		True if text has been replaces, False otherwise
		"""

		if self.ui.lineEditFind.text().toLower() in \
			self.ui.lineEditReplace.text().toLower():
			return False

		if not self.find():
			return False
		self.qProgEdit.editor.replace(self.ui.lineEditReplace.text())
		return True

	def replaceAll(self):

		"""Replace all occurences in the document"""

		i = 0
		while self.replace():
			i += 1

	def unshow(self):

		"""Toggles the widget's visibility."""

		self.qProgEdit.toggleFind(False)
