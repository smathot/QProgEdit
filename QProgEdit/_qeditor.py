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
		self.commentShortcut = QtGui.QShortcut(QtGui.QKeySequence( \
			self.qProgEdit.cfg.qProgEditCommentShortcut), self)
		self.uncommentShortcut = QtGui.QShortcut(QtGui.QKeySequence( \
			self.qProgEdit.cfg.qProgEditUncommentShortcut), self)
		self.commentShortcut.activated.connect(self.commentSelection)
		self.uncommentShortcut.activated.connect(self.uncommentSelection)
		self.applyCfg()
		self.linesChanged.connect(self.updateMarginWidth)
		
	def applyCfg(self):

		"""Apply the configuration"""

		self.commentShortcut.setKey(QtGui.QKeySequence( \
			self.qProgEdit.cfg.qProgEditCommentShortcut))
		self.uncommentShortcut.setKey(QtGui.QKeySequence( \
			self.qProgEdit.cfg.qProgEditUncommentShortcut))
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
		self.cfgVersion = self.qProgEdit.cfg.version()

	def commentSelection(self):
		
		"""Comments out the currently selected text."""

		self.beginUndoAction()
		cl, ci = self.getCursorPosition()
		if not self.hasSelectedText():
			select = False
			# If there is no selection, use the current line
			fl = self.getCursorPosition()[0]
			tl = fl
			fi = 0
			ti = self.lineLength(tl)
		else:
			select = True
			fl, fi, tl, ti = self.getSelection()
			if fi > 0:
				fi += 1
			ti += 1
		for l in range(fl, tl+1):
			self.insertAt(u'#', l, 0)
		ci += 1
		self.setCursorPosition(cl, ci)
		if select:
			self.setSelection(fl, fi, tl, ti)
		self.endUndoAction()
		
	def focusOutEvent(self, e):

		"""Lets the qProgEdit call the handler when we lose focus."""

		if self.qProgEdit.tabManager.callHandlerOnFocusOut:
			self.qProgEdit.callHandler()
		super(QEditor, self).focusOutEvent(e)
			
	def focusInEvent(self, e):
		
		"""Apply the current configuration when we receive focus."""

		if self.qProgEdit.tabManager.cfg.version() != self.cfgVersion:
			self.applyCfg()
		super(QEditor, self).focusInEvent(e)

	def uncommentSelection(self):
		
		"""Uncomments the currently selected text."""

		self.beginUndoAction()
		cl, ci = self.getCursorPosition()
		if not self.hasSelectedText():
			select = False
			# If there is no selection, use the current line
			fl = self.getCursorPosition()[0]
			tl = fl
			fi = 0
			ti = self.lineLength(tl)-1
		else:
			select = True
			fl, fi, tl, ti = self.getSelection()
		stripped = False
		for l in range(fl, tl+1):
			l = self.setSelection(l, 0, l, self.lineLength(l))
			s = self.selectedText()
			_s = s.trimmed()
			if len(_s) == 0 or _s[0] != u'#':
				continue
			stripped = True
			i = s.indexOf(u'#')
			s = s.remove(i, 1)
			self.replaceSelectedText(s)
		# If a comment character has been stripped, we need to jump back one
		# position, but not below 0
		if stripped:
			ci = max(0, ci-1)
			ti = max(0, ti-1)
		self.setCursorPosition(cl, ci)
		if select:
			self.setSelection(fl, fi, tl, ti)
		self.endUndoAction()

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
