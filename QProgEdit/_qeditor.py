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
from QProgEdit import QLexer, QColorScheme, validate, clean, _

class QEditor(QsciScintilla):

	"""A single editor widget."""

	invalidMarker = 8

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
		self.validationErrors = {}
		self.setLang(lang)
		self.commentShortcut = QtGui.QShortcut(QtGui.QKeySequence( \
			self.qProgEdit.cfg.qProgEditCommentShortcut), self)
		self.uncommentShortcut = QtGui.QShortcut(QtGui.QKeySequence( \
			self.qProgEdit.cfg.qProgEditUncommentShortcut), self)
		self.commentShortcut.activated.connect(self.commentSelection)
		self.uncommentShortcut.activated.connect(self.uncommentSelection)
		self.applyCfg()
		self.linesChanged.connect(self.updateMarginWidth)
		self.cursorPositionChanged.connect(self.validate)
		self.marginClicked.connect(self.onMarginClick)
		self.setMarginSensitivity(1, True)

	def applyCfg(self):

		"""Apply the configuration"""

		if hasattr(QColorScheme, self.qProgEdit.cfg.qProgEditColorScheme):
			colorScheme = getattr(QColorScheme, \
				self.qProgEdit.cfg.qProgEditColorScheme)
		else:
			colorScheme = QColorScheme.Default
		self.markerDefine(QsciScintilla.RightArrow, self.invalidMarker)
		self.setMarkerBackgroundColor(QtGui.QColor( \
			colorScheme[u'Invalid']), self.invalidMarker)
		self.setMarkerForegroundColor(QtGui.QColor( \
			colorScheme[u'Invalid']), self.invalidMarker)
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
		self.setMarginLineNumbers(0, self.qProgEdit.cfg.qProgEditLineNumbers)
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

		if self.isModified():
			self.qProgEdit.callFocusOutHandler()
			self.setModified(False)
		super(QEditor, self).focusOutEvent(e)

	def focusInEvent(self, e):

		"""Apply the current configuration when we receive focus."""

		if self.qProgEdit.tabManager.cfg.version() != self.cfgVersion:
			self.applyCfg()
		super(QEditor, self).focusInEvent(e)

	def keyPressEvent(self, event):

		"""
		Intercepts certain keypress events to implement custom copy-pasting and
		zoomin.

		Arguments:
		event	--	A QKeyPressEvent.
		"""

		key = event.key()
		ctrl = event.modifiers() & QtCore.Qt.ControlModifier
		shift = event.modifiers() & QtCore.Qt.ShiftModifier
		# Zoom in/out
		if ((key == QtCore.Qt.Key_Plus) and ctrl) \
			or ((key == QtCore.Qt.Key_Equal) and shift and ctrl):
			self.zoomIn()
			event.accept()
		elif (key == QtCore.Qt.Key_Minus) and ctrl:
			self.zoomOut()
			event.accept()
		elif (key == QtCore.Qt.Key_V) and ctrl:
			self.paste()
			event.accept()
		else:
			QsciScintilla.keyPressEvent(self, event)

	def onMarginClick(self, margin, line, state):

		"""
		Show validation errors when the margin symbol is clicked.

		Arguments:
		margin		--	The margin number.
		line		--	The line number.
		state		--	The keyboard state.
		"""

		if margin != 1:
			return
		if line in self.validationErrors:
			err = self.validationErrors[line]
			QtGui.QToolTip.showText(QtGui.QCursor().pos(), err)

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

	def paste(self):

		"""
		Re-implements the paste method to allow modification of paste content.
		"""

		text = unicode(QtGui.QApplication.clipboard().text())
		if hasattr(clean, self.lang().lower()):
			msg, cleanText = getattr(clean, self.lang().lower())(text)
			if msg != None:
				resp = QtGui.QMessageBox.question(self, _(u'Pasting content'), \
					msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if resp == QtGui.QMessageBox.Yes:
					text = cleanText
		self.removeSelectedText()
		self.insert(text)

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
		self.validate()

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
		self.setModified(False)

	def text(self):

		"""
		Retrieves the editor contents.

		Returns:
		A unicode object.
		"""

		return unicode(super(QEditor, self).text())

	def updateMarginWidth(self):

		"""Updates the width of the margin containing the line numbers"""

		self.setMarginWidth(0, u' %s' % self.lines())

	def validate(self):

		"""Validates the text."""

		cl = self.getCursorPosition()[0]
		validateCurrentLine = cl in self.validationErrors
		self.validationErrors = {}
		self.markerDeleteAll()
		if not self.qProgEdit.cfg.qProgEditValidate or not hasattr(validate, \
			self.lang().lower()):
			return
		validator = getattr(validate, self.lang().lower())
		for l, s in validator(self.text()):
			# Do not validate negative positions or the current line, unless the
			# current line already had a negative validation before.
			if l < 0 or (not validateCurrentLine and l == cl):
				continue
			self.validationErrors[l] = s
			self.markerAdd(l, self.invalidMarker)

	def wheelEvent(self, event):

		"""
		Implements scroll-to-zoom functionality.

		Arguments:
		event	--	A QWheelEvent.
		"""

		if QtCore.Qt.ControlModifier == event.modifiers():
			event.ignore()
			if event.delta() > 0:
				self.zoomIn()
			else:
				self.zoomOut()
		else:
			super(QEditor, self).wheelEvent(event)

