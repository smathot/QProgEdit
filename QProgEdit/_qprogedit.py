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

from QProgEdit.qt import QtGui, QtCore
from QProgEdit import QEditor, QEditorPrefs, QEditorFind

class QProgEdit(QtGui.QWidget):

	"""
	desc:
		A single editor window, with preferences widget and search
		functionality.
	"""

	cursorRowChanged = QtCore.pyqtSignal()
	focusLost = QtCore.pyqtSignal()
	focusReceived = QtCore.pyqtSignal()
	handlerButtonClicked = QtCore.pyqtSignal()

	def __init__(self, tabManager, dPrint=None, title=u'Empty document',
		**editorParams):

		"""
		desc:
			Constructor.

		arguments:
			tabManager:
				desc:	A tab manager.
				type:	QTabManager

		keywords:
			dPrint:		A function to be used for debug printing. Should
						accept a single parameter, which is the debug message.
						If no debug function is specified, the standard output
						is used.
			title:		A title for the document.

		keyword-dict:
			editorParams:
						A dictionary with keywords to be passed to QEditor.
		"""

		super(QProgEdit, self).__init__(tabManager)
		self.tabManager = tabManager
		self.title = title
		if dPrint is not None:
			self.dPrint = dPrint
		self.editor = QEditor(self, **editorParams)
		self.prefs = QEditorPrefs(self)
		self.prefs.hide()
		self.find = QEditorFind(self)
		self.find.hide()
		self.mainBox = QtGui.QVBoxLayout(self)
		self.mainBox.setContentsMargins(4,4,4,4)
		self.mainBox.setSpacing(4)
		self.mainBox.addWidget(self.prefs)
		self.mainBox.addWidget(self.find)
		self.mainBox.addWidget(self.editor)
		self.setLayout(self.mainBox)
		if self.tabManager is not None:
			self.editor.cursorPositionChanged.connect(
				self.tabManager.cornerWidget().statusWidget.updateCursorPos)

	# Properties provide direct access to the relevant editor functions.

	@property
	def cfg(self):
		return self.tabManager.cfg

	@property
	def applyCfg(self):
		return self.editor.applyCfg

	@property
	def isModified(self):
		return self.editor.isModified

	@property
	def lang(self):
		return self.editor.lang

	@property
	def text(self):
		return self.editor.text

	@property
	def setLang(self):
		return self.editor.setLang

	@property
	def setSymbolTree(self):
		return self.editor.setSymbolTree

	@property
	def setFocus(self):
		return self.editor.setFocus

	@property
	def setText(self):
		return self.editor.setText

	@property
	def setCursorPosition(self):
		return self.editor.setCursorPosition

	@property
	def symbols(self):
		return self.editor.symbols

	@property
	def updateSymbolTree(self):
		return self.editor.updateSymbolTree

	@property
	def cursorPositionChanged(self):
		return self.editor.cursorPositionChanged

	@property
	def focusLost(self):
		return self.editor.focusLost

	@property
	def focusReceived(self):
		return self.editor.focusReceived

	@property
	def handlerButtonClicked(self):
		return self.editor.handlerButtonClicked

	def dPrint(self, msg):

		"""
		desc:
			Prints a debug message.

		arguments:
			msg:
				desc:	A debug message.
				type:	[unicode, str]
		"""

		print(u'debug: %s' % msg)

	def focusTab(self):

		"""
		desc:
			Focuses the current tab.
		"""

		self.tabManager.setCurrentWidget(self)
		self.editor.setFocus()

	def tabIndex(self):

		"""
		desc:
			Gets the index of the current tab.

		returns:
			desc:	The tab index.
			type:	int
		"""

		return self.tabManager.indexOf(self)

	def toggle(self, widget, visible):

		"""
		desc:
			Toggles the visibility of a widget with a smooth animation.

		arguments:
			widget:		A QWidget.
			visible:	A boolean indicating the visibility of the widget.
		"""

		if not visible:
			widget.setMaximumHeight(0)
		else:
			widget.setMaximumHeight(widget.bestHeight)
		widget.show()
		a = QtCore.QPropertyAnimation(widget, u'maximumHeight', widget)
		if not visible:
			a.setStartValue(widget.bestHeight)
			a.setEndValue(0)
		else:
			a.setStartValue(0)
			a.setEndValue(widget.bestHeight)
		a.setDuration(100)
		a.start()

	def toggleFind(self, visible):

		"""
		desc:
			Toggles the visibility of the find widget.

		arguments:
			visible:	A boolean indicating the visibility of the widget.
		"""

		self.toggle(self.find, visible)
		self.tabManager.cornerWidget().findButton.setChecked(visible)
		if visible:
			self.find.ui.lineEditFind.setFocus()
		else:
			self.editor.setFocus()

	def togglePrefs(self, visible):

		"""
		desc:
			Toggles the visibility of the preferences widget

		arguments:
			visible:	A boolean indicating the visibility of the widget.
		"""

		if visible:
			self.prefs.ui.fontComboBoxFontFamily.setFocus()
			self.prefs.refresh()
		self.toggle(self.prefs, visible)
