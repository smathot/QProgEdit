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
from QProgEdit.qt import Qsci
from QProgEdit import QColorScheme

class QBaseLexer(object):

	"""
	desc:
		A base object for custom lexers.
	"""

	def setTheme(self, editor, colorScheme):

		"""
		desc:
			Applies the colorscheme to the lexer.

		arguments:
			editor:
				desc:	An editor object.
				type:	QsciScintilla
			colorScheme:
				desc:	A colorscheme.
				type:	dict
		"""

		self.editor = editor
		# Set the font based on the configuration
		font = QtGui.QFont(self.editor.cfg.qProgEditFontFamily,
			self.editor.cfg.qProgEditFontSize)
		self.setFont(font)
		# Apply the color theme
		if hasattr(QColorScheme, colorScheme):
			colorScheme = getattr(QColorScheme, colorScheme)
		else:
			colorScheme = QColorScheme.Default
		if u'Background' in colorScheme:
			self.setPaper(QtGui.QColor(colorScheme[u'Background']))
			self.setDefaultPaper(QtGui.QColor(colorScheme[u'Background']))
		if u'Default' in colorScheme:
			self.editor.setCaretForegroundColor(QtGui.QColor(
				colorScheme[u'Default']))
			self.setDefaultColor(QtGui.QColor(colorScheme[u'Default']))
		if u'Selection background' in colorScheme:
			self.editor.setSelectionBackgroundColor(QtGui.QColor(
				colorScheme[u'Selection background']))
		if u'Selection foreground' in colorScheme:
			self.editor.setSelectionForegroundColor(QtGui.QColor(
				colorScheme[u'Selection foreground']))
		if u'Caret-line background' in colorScheme:
			self.editor.setCaretLineBackgroundColor(QtGui.QColor(
				colorScheme[u'Caret-line background']))
		for style in range(50):
			styleName = str(self.description(style))
			if styleName != u'' and styleName in colorScheme:
				if isinstance(colorScheme[styleName], tuple):
					color, bold, italic = colorScheme[styleName]
					self.setColor(QtGui.QColor(colorScheme[styleName]), style)
					_font = QtGui.QFont(font)
					_font.setBold(bold)
					_font.setItalic(italic)
					self.setFont(_font, style)
				else:
					color = colorScheme[styleName]
				self.setColor(QtGui.QColor(color), style)

class QPythonLexer(QBaseLexer, Qsci.QsciLexerPython):

	"""
	desc:
		A custom Python lexer.
	"""

	def keywords(self, keyset):

		"""
		desc:
			Specifies keywords.

		arguments:
			keyset:
				desc:	The keyword set.
				type:	int

		returns:
			desc:	A space-separated list of keywords.
			type:	str
		"""

		if keyset == 1:
			return Qsci.QsciLexerPython.keywords(self, keyset).replace(
				' None', '') + ' exp win self set widget'
		elif keyset == 2:
			return 'None True False'
		return Qsci.QsciLexerPython.keywords(self, keyset)

class QOpenSesameLexer(QBaseLexer, Qsci.QsciLexerPython):

	"""
	desc:
		A lexer for OpenSesame script.
	"""

	def keywords(self, keyset):

		"""
		desc:
			Specifies keywords.

		arguments:
			keyset:
				desc:	The keyword set.
				type:	int

		returns:
			desc:	A space-separated list of keywords.
			type:	str
		"""

		if keyset == 1:
			return (b'set define draw setcycle log run widget ellipse circle '
				b'line arrow textline image gabore noise fixdot label checkbox '
				b'button image image_button rating_scale text_input')
		return Qsci.QsciLexerPython.keywords(self, keyset)

class QFallbackLexer(QBaseLexer, Qsci.QsciLexer):

	"""
	desc:
		A fallback lexer for plain text.
	"""

	def description(self, style):

		"""
		desc:
			Gives a style description for the generic Lexer.

		arguments:
			style:
				desc:	The style number.
				type:	int

		returns:
			desc:	The 'Default' str for style 0 and empty str for all
					other styles.
			type:	str
		"""

		if style == 0:
			return u'Default'
		else:
			return u''

def QLexer(editor, lang=u'text', colorScheme=u'Default'):

	"""
	desc:
		A factory for a lexer.

	arguments:
		editor:
			desc:	The parent QEditor.
			type:	QEditor

	keywords:
		lang:
			desc:	The language.
			type:	unicode
		colorScheme:
			desc:	The color scheme.
			type:	unicode
	"""

	if lang.lower() == u'opensesame':
		lexer = QOpenSesameLexer(editor)
	elif lang.lower() == u'python':
		lexer = QPythonLexer(editor)
	else:
		lexer = QFallbackLexer(editor)
	lexer.setTheme(editor, colorScheme)
	return lexer
