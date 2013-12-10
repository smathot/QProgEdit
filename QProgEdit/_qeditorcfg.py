
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

class QEditorCfg(QtCore.QObject):

	"""A non-persistent configuration object."""

	def __init__(self, parent=None):

		"""
		Constructor

		Keyword arguments:
		parent	--	a QWidget
		"""

		super(QEditorCfg, self).__init__(parent)
		self.qProgEditFontFamily = u'Monospace'
		self.qProgEditFontSize = 10
		self.qProgEditLineNumbers = True
		self.qProgEditHighlightCurrentLine = False
		self.qProgEditHighlightMatchingBrackets = True
		self.qProgEditWordWrapMarker = 80
		self.qProgEditWordWrap = True
		self.qProgEditTabWidth = 4
		self.qProgEditAutoIndent = True
		self.qProgEditShowEol = False
		self.qProgEditShowWhitespace = False
		self.qProgEditShowIndent = False
		self.qProgEditShowFolding = True
		self.qProgEditAutoComplete = True
		self.qProgEditColorScheme = u'SolarizedDark'
		self.qProgEditCommentShortcut = u'Ctrl+M'
		self.qProgEditUncommentShortcut = u'Ctrl+Shift+M'
		
	def version(self):
		
		return 0

