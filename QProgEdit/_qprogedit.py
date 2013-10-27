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
from PyQt4.Qsci import QsciScintilla, QsciScintillaBase, QsciLexerPython
from QProgEdit import QEditor, QEditorCfg, QEditorPrefs, QEditorFind

class QProgEdit(QtGui.QWidget):
	
	"""
	A single editor window, with preferences widget and search functionality.
	"""

	def __init__(self, parent=None, lang=u'text', cfg=None, dPrint=None,
		title=u'Empty document', handler=None):
				
		"""
		Constructor.
		
		Keyword arguments:
		parent		--	A parent QWidget, typically a QTabManager.
						(default=None)
		lang		--	The language to be used for syntax highlighting.
						(default=u'text')
		cfg			--	The configuration back-end or None to use a
						non-persistent back-end. (default=None)
		dPrint		--	A function to be used for debug printing. Should
						accept a single parameter, which is the debug message.
						If no debug function is specified, the standard output
						is used. (default=None)
		title		--	A title for the document. (default=u'Empty document')
		handler		--	A function that is called when the editor loses focus,
						typically to respond to changes in the content.
						(default=None)
		"""

		super(QProgEdit, self).__init__(parent)

		self.tabManager = parent
		self.title = title
		self.handler = handler
		if dPrint != None:
			self.dPrint = dPrint
		if cfg == None:
			self.cfg = QEditorCfg(self)
		else:
			self.cfg = cfg

		self.editor = QEditor(self, lang=lang)
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
		
		if self.tabManager != None:
			self.editor.cursorPositionChanged.connect( \
				self.tabManager.cornerWidget().statusWidget.updateCursorPos)

	def applyCfg(self):

		"""Applies the configuration."""

		self.editor.applyCfg()
		
	def callHandler(self):
		
		"""Calls the handler."""
		
		if self.handler != None:
			self.handler()

	def dPrint(self, msg):

		print u'debug: %s' % msg
		
	def isModified(self):
		
		"""
		Returns the modified status.
				
		Returns:
		True if the editor is modified, False otherwise.
		"""
		
		return self.editor.isModified()

	def lang(self):

		"""
		Returns the language used for syntax highlighting.
		
		Returns:
		The language.
		"""

		return self.editor.lang()
	
	def setHandler(self, handler=None):
		
		"""
		Sets the handler function, i.e. the function that is called when the
		editor loses focus and changes need to be processed.
		
		Keyword arguments:
		handler		--	A handler function or None to disable the handler.
						(default=None)
		"""
		
		self.handler = handler

	def setLang(self, lang=u'text'):

		"""
		Sets the language.

		Keyword arguments:
		lang		-- 	language, used to select a lexer for syntax highlighting.
					if an appropriate lexer isn't found, no error is
					generated, but syntax highlighting is disabled. For a
					list of available lexers, refer to the QsciScintilla
					documentation. (default=u'text')
		"""

		self.editor.setLang(lang=lang)

	def setText(self, txt):

		"""
		Sets the content of the editor.

		Arguments
		txt		--	The new editor content.
		"""

		# Unicode is preferred, so give a warning if a str is passed.
		if isinstance(txt, str):
			self.dPrint( \
				u'Warning: QProgEdit.setText() received str (utf-8 assumed)')
			txt = txt.decode('utf-8', 'ignore')
		self.editor.setText(txt)

	def text(self):

		"""
		Retrieves the editor contents.
		
		Returns:
		The editor contents.
		"""

		return self.editor.text()

	def toggle(self, widget, visible):

		"""
		Toggles the visibility of a widget with a smooth animation.

		Arguments:
		widget		--	A QWidget.
		visible		--	A boolean indicating the visibility of the widget.
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
		Toggles the visibility of the find widget

		Arguments:
		visible		--	A boolean indicating the visibility of the widget.
		"""

		self.toggle(self.find, visible)

	def togglePrefs(self, visible):

		"""
		Toggles the visibility of the preferences widget

		Arguments:
		visible		--	A boolean indicating the visibility of the widget.
		"""

		if visible:
			self.prefs.refresh()
		self.toggle(self.prefs, visible)
