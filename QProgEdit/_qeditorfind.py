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
from PyQt4 import QtGui, QtCore, Qsci, uic
from PyQt4.Qsci import QsciScintilla
from QProgEdit.py3 import *
from QProgEdit import QUiLoader

class QEditorFind(QtGui.QWidget, QUiLoader):

	"""
	desc:
		A find/ replace widget.
	"""

	def __init__(self, qProgEdit):

		"""
		desc:
			Constructor.

		arguments:
			qProgEdit:
				desc:	The parent QProgEdit.
				type:	QProgEdit
		"""

		super(QEditorFind, self).__init__(qProgEdit)
		self.qProgEdit = qProgEdit
		self.loadUi(u'findWidget')
		self.ui.pushButtonFind.clicked.connect(self.find)
		self.ui.lineEditFind.returnPressed.connect(self.find)
		self.ui.pushButtonReplace.clicked.connect(self.replace)
		self.ui.pushButtonReplaceAll.clicked.connect(self.replaceAll)
		self.bestHeight = self.height()
		self.matchNr = None
		self._locked = False

	@property
	def editor(self):
		return self.qProgEdit.editor

	def caseSensitive(self):

		"""
		returns:
			desc:	True or False, depending on whether we should search case
					sensitive.
			type:	bool
		"""

		return self.ui.checkBoxCaseSensitive.isChecked()

	def findText(self):

		"""
		returns:
			desc:	The find text.
			type:	unicode
		"""

		return unicode(self.ui.lineEditFind.text())

	def find(self):

		"""
		desc:
			Finds the current text in the document.

		returns:
			desc:	True if matching text has been found, False otherwise.
			type:	bool
		"""

		return self.editor.findFirst(self.findText(), False,
			self.caseSensitive(), self.matchWhole(), True)

	def lock(self):

		"""
		desc:
			Locks the editor and find widget, so that we don't get into
			recursion problems during replace actions.
		"""

		self._locked = True
		self.editor.selectionChanged.disconnect()

	def matchWhole(self):

		"""
		returns:
			desc:	True or False, depending on whether we should match whole
					words only.
			type:	bool
		"""

		return self.ui.checkBoxMatchWhole.isChecked()

	def replace(self):

		"""
		desc:
			Replaces the first occurence in the document.

		returns:
			desc:	True if text has been replaced, False otherwise.
			type:	bool
		"""

		self.lock()
		if self.editor.hasSelectedText():
			row1, line1, row2, line2 = self.editor.getSelection()
			self.editor.setCursorPosition(row1, line1)
		self.find()
		self.editor.replace(self.replaceText())
		self.unlock()
		return True

	def replaceAll(self):

		"""
		desc:
			Replaces all occurences in the document.
		"""

		self.lock()
		self.editor.beginUndoAction()
		text = QtCore.QString(self.editor.text())
		if self.caseSensitive():
			cs = QtCore.Qt.CaseSensitive
		else:
			cs = QtCore.Qt.CaseInsensitive
		n = text.count(self.findText(), cs)
		for i in range(n):
			self.find()
			self.editor.replace(self.replaceText())
		self.editor.endUndoAction()
		self.unlock()

	def replaceText(self):

		"""
		returns:
			desc:	The replace text.
			type:	unicode
		"""

		return unicode(self.ui.lineEditReplace.text())

	def setFindText(self, txt=u''):

		"""
		desc:
			Sets the text of the find widget.

		keywords:
			txt:
				desc:	The text to set.
				type:	unicode
		"""

		if self._locked:
			return
		self.ui.lineEditFind.setText(txt)

	def unlock(self):

		"""
		desc:
			Unlocks the editor and find widget, to resume normal operations
			after replacing.
		"""

		self._locked = False
		self.editor.selectionChanged.connect(self.editor.highlightSelection)

	def unshow(self):

		"""
		desc:
			Hides the widget.
		"""

		self.qProgEdit.toggleFind(False)
