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

from PyQt4 import QtGui, QtCore
from PyQt4 import Qsci
from QProgEdit import QColorScheme

class QLexer(Qsci.QsciLexer):

	"""A themeable wrapper around the standard Lexer system"""

	def __init__(self, parent=None, lang=u'text', colorScheme=u'Default'):

		"""
		Constructor

		Keyword arguments:
		parent		--	a QEditor
		lang			--	the language (default='text')
		colorScheme	--	the colorScheme (default='default')
		"""

		self.editor = parent

		# If the language matches an existing Lexer, morph into that
		# pre-existing lexer class
		lexerClass = u'QsciLexer%s' % lang
		if hasattr(Qsci, lexerClass):
			self.__class__ = getattr(Qsci, lexerClass)
			getattr(Qsci, lexerClass).__init__(self, parent)
		else:
			super(QLexer, self).__init__(parent)

		# Set the font based on the configuration
		font = QtGui.QFont(self.editor.qProgEdit.cfg.qProgEditFontFamily,
				self.editor.qProgEdit.cfg.qProgEditFontSize)
		self.setFont(font)

		# Apply the color theme
		colorScheme = getattr(QColorScheme, colorScheme)
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
				self.setColor(QtGui.QColor(colorScheme[styleName]), style)

	def description(self, style):

		"""
		Gives a style description for the generic Lexer

		Arguments:
		style	--	the style number

		Returns:
		The 'Default' QString for style 0 and empty QStrings for all other styles
		"""

		if style == 0:
			return QtCore.QString(u'Default')
		else:
			return QtCore.QString()

