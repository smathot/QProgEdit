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
from PyQt4.Qsci import QsciScintilla, QsciScintillaBase
from QProgEdit import QLexer

class QEditor(QsciScintilla):

	"""A single editor widget."""

	def __init__(self, parent=None, lang=u'text'):

		"""
		Constructor.

		Keyword arguments:
		parent		-- 	The parent QWidget (default=None)
		lang		-- 	Language used to select a lexer for syntax highlighting.
						If an appropriate lexer isn't found, no error is
						generated, but syntax highlighting is disabled. For a
						list of available lexers, refer to the QsciScintilla
						documentation. (default='text')
		"""

		super(QEditor, self).__init__(parent)
		self.setUtf8(True)
		self.qProgEdit = parent
		self.setLang(lang)
		self.applyCfg()
		self.linesChanged.connect(self.updateMarginWidth)
		QtGui.QShortcut(QtGui.QKeySequence(u'Ctrl+M'),
			self).activated.connect(self.commentSelection)
		QtGui.QShortcut(QtGui.QKeySequence(u'Ctrl+Shift+M'),
			self).activated.connect(self.uncommentSelection)

	def applyCfg(self):

		"""Apply the configuration"""

		font = QtGui.QFont(self.qProgEdit.cfg.qProgEditFontFamily,
			self.qProgEdit.cfg.qProgEditFontSize)
		self.setFont(font)
		self.setTabWidth(self.qProgEdit.cfg.qProgEditTabWidth)
		self.setAutoIndent(self.qProgEdit.cfg.qProgEditAutoIndent)
		self.setEolVisibility(self.qProgEdit.cfg.qProgEditShowEol)
		self.setIndentationGuides(self.qProgEdit.cfg.qProgEditShowIndent)
		self.setCaretLineVisible(
			self.qProgEdit.cfg.qProgEditHighlightCurrentLine)
		if self.qProgEdit.cfg.qProgEditShowFolding:
			self.setFolding(QsciScintilla.PlainFoldStyle)
		else:
			self.setFolding(QsciScintilla.NoFoldStyle)
		self.setMarginLineNumbers(1, self.qProgEdit.cfg.qProgEditLineNumbers)
		if self.qProgEdit.cfg.qProgEditShowWhitespace:
			self.setWhitespaceVisibility(QsciScintilla.WsVisible)
		else:
			self.setWhitespaceVisibility(QsciScintilla.WsInvisible)
		if self.qProgEdit.cfg.qProgEditWordWrap:
			self.setWrapMode(QsciScintilla.WrapWord)
		else:
			self.setWrapMode(QsciScintilla.WrapNone)
		if self.qProgEdit.cfg.qProgEditWordWrapMarker != None:			
			self.setEdgeColumn(self.qProgEdit.cfg.qProgEditWordWrapMarker)
			self.setEdgeMode(QsciScintilla.EdgeLine)
		else:
			self.setEdgeMode(QsciScintilla.EdgeNone)
		if self.qProgEdit.cfg.qProgEditAutoComplete:
			self.setAutoCompletionSource(QsciScintilla.AcsAll)
		else:
			self.setAutoCompletionSource(QsciScintilla.AcsNone)
		if self.qProgEdit.cfg.qProgEditHighlightMatchingBrackets:
			self.setBraceMatching(QsciScintilla.StrictBraceMatch)
		else:
			self.setBraceMatching(QsciScintilla.NoBraceMatch)
		self.setLang(self.lang())

	def doWithSelection(self, func):

		"""
		Calls a function on each line of the selected text. If no text has been
		selected, the current line is used. After the operation, if there was a
		selection before, the new selection is the full lines (even if previously
		some lines were only partly selected.

		Arguments:
		func	--	a function, which accepts the old QString and returns a new
					QString for each line.
		"""

		if not self.hasSelectedText():
			# If there is no selection, use the current line
			fl = self.getCursorPosition()[0]
			tl = fl
			fi = 0
			ti = self.lineLength(tl)
			selectAfter = False
		else:
			# Generally when the cursor is on the first position of a line, you
			# do not want to comment that line
			fl, fi, tl, ti = self.getSelection()
			if ti == 0:
				tl -= 1
		for l in range(fl, tl+1):
			self.insertAt(u'#', l, 0)
		self.setSelection(fl, fi, tl, ti)

	def commentSelection(self):

		if not self.hasSelectedText():
			# If there is no selection, use the current line
			fl = self.getCursorPosition()[0]
			tl = fl
			fi = 0
			ti = self.lineLength(tl)
		else:
			# Generally when the cursor is on the first position of a line, you
			# do not want to comment that line
			fl, fi, tl, ti = self.getSelection()
			if ti == 0:
				tl -= 1
		for l in range(fl, tl+1):
			self.insertAt(u'#', l, 0)
		self.setSelection(fl, fi, tl, ti)
		
	def focusOutEvent(self, e):

		"""Let the qProgEdit call the handler when we lose focus."""

		self.qProgEdit.callHandler()

	def uncommentSelection(self):

		if not self.hasSelectedText():
			# If there is no selection, use the current line
			fl = self.getCursorPosition()[0]
			tl = fl
			fi = 0
			ti = self.lineLength(tl)-1
		else:
			# Generally when the cursor is on the first position of a line, you
			# do not want to comment that line
			fl, fi, tl, ti = self.getSelection()
			if ti == 0:
				tl -= 1
		for l in range(fl, tl+1):
			l = self.setSelection(l, 0, l, self.lineLength(l)-1)
			s = self.selectedText()
			_s = s.trimmed()
			if len(_s) == 0 or _s[0] != u'#':
				continue
			i = s.indexOf(u'#')
			s = s.remove(i, 1)
			self.replaceSelectedText(s)
		self.setSelection(fl, fi, tl, ti)

	def lang(self):

		"""
		Returns:
		The language of the editor
		"""

		return self._lang

	def setLang(self, lang=u'text'):

		"""
		Sets the language

		Keyword arguments:
		lang	-- 	language, used to select a lexer for syntax highlighting.
					if an appropriate lexer isn't found, no error is
					generated, but syntax highlighting is disabled. For a
					list of available lexers, refer to the QsciScintilla
					documentation. (default=u'text')
		"""


		print u'lang = %s' % lang
		self._lexer = QLexer(self, lang=lang, colorScheme= \
			self.qProgEdit.cfg.qProgEditColorScheme)
		self._lang = lang
		self.SendScintilla(QsciScintillaBase.SCI_CLEARDOCUMENTSTYLE)
		self.setLexer(self._lexer)
		
	def setText(self, text):
		
		"""
		Sets the editor contents.
		
		Arguments:
		text	--	A text string. This can be a str object, which is assumed
					to be in utf-8 encoding, a Unicode object, or a QString.
		"""
		
		if isinstance(text, str):
			text = text.decode(u'utf-8')
		elif not isinstance(text, unicode) and not isinstance(text, \
			QtCore.QString):
			raise Exception(u'Expecting a str, unicode, or QString object')
		super(QEditor, self).setText(text)
		
	def text(self):
		
		"""
		Retrieves the editor contents.
		
		Returns:
		A unicode object.
		"""

		return unicode(super(QEditor, self).text())

	def updateMarginWidth(self):

		"""Updates the width of the margin containing the line numbers"""

		self.setMarginWidth(1, u' %s' % self.lines())
