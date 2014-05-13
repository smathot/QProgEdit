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
		self.matchNr = None
		
	def caseSensitive(self):
		
		"""
		Returns:
		True or False, depending on whether we should search case sensitive.
		"""
		
		return self.ui.checkBoxCaseSensitive.isChecked()
		
	def editor(self):
		
		"""
		Returns:
		The QsciScintilla object.
		"""
		
		return self.qProgEdit.editor
	
	def findText(self):
		
		"""
		Returns:
		The find text.
		"""
		
		return self.ui.lineEditFind.text()
	
	def find(self):

		"""
		Finds the current text in the document.

		Returns:
		True if matching text has been found, False otherwise.
		"""
		
		return self.editor().findFirst(self.findText(), False,
			self.caseSensitive(), self.matchWhole(), True)
	
	def matchWhole(self):
		
		"""
		Returns:
		True or False, depending on whether we should match whole words only.
		"""
		
		return self.ui.checkBoxMatchWhole.isChecked()	

	def replace(self):

		"""
		Replaces the first occurence in the document.

		Returns:
		True if text has been replaced, False otherwise.
		"""

		selection = self.editor().selectedText()
		findText = self.findText()
		if not self.caseSensitive():
			selection = selection.toLower()
			findText = findText.toLower()
		if selection != findText and not self.find():
			return False
		self.editor().replace(self.replaceText())
		return True

	def replaceAll(self):

		"""Replace all occurences in the document."""
		
		self.editor().beginUndoAction()
		text = QtCore.QString(self.editor().text())
		if self.caseSensitive():
			cs = QtCore.Qt.CaseSensitive
		else:
			cs = QtCore.Qt.CaseInsensitive
		n = text.count(self.findText(), cs)
		for i in range(n):
			self.replace()
		self.editor().endUndoAction()
		
	def replaceText(self):
		
		"""
		Returns:
		The replace text.
		"""
		
		return self.ui.lineEditReplace.text()

	def unshow(self):

		"""Toggles the widget's visibility."""

		self.qProgEdit.toggleFind(False)
