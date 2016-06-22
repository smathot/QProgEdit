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

from QProgEdit.py3compat import *
from qtpy import QtGui, QtCore
from QProgEdit.pyqt5compat import Qsci
from QProgEdit import QColorScheme

python_builtins = (' abs dict help min setattr all dir hex next slice any '
'id object sorted ascii enumerate input oct staticmethod bin eval int open str '
'bool exec isinstance ord sum bytearray filter issubclass pow super bytes '
'float iter print tuple callable format len property type chr frozenset list '
'range vars classmethod getattr locals repr zip compile globals map reversed '
'__import__ complex hasattr max round delattr hash memoryview set divmod')

opensesame_builtins = ' exp win self var pool items items clock log'

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
				type:Qsci.QsciScintilla
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
			styleName = safe_decode(self.description(style), errors=u'ignore')
			if styleName != u'' and styleName in colorScheme:
				if isinstance(colorScheme[styleName], tuple):
					color, bold, italic = colorScheme[styleName]
					self.setColor(QtGui.QColor(color), style)
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
				' None', '') + python_builtins + opensesame_builtins
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
			return (b'set define draw setcycle log run widget shuffle '
				b'shuffle_horiz fullfactorial slice sort sortby reverse roll '
				b'weight constrain maxrep mindist')
		if keyset == 2:
			return (b'ellipse circle line arrow textline image gabore noise '
				b'fixdot label checkbox button image image_button rating_scale '
				b'text_input rect')
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
