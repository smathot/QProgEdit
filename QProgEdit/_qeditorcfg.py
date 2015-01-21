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
from QProgEdit.qt import QtGui, QtCore

class QEditorCfg(QtCore.QObject):

	"""
	desc:
		A non-persistent configuration object.
	"""

	def __init__(self, parent=None):

		"""
		desc:
			Constructor.

		keywords:
			parent:
				desc:	The parent widget.
				type:	[QWidget, NoneType]
		"""

		super(QEditorCfg, self).__init__(parent)
		if os.name == u'nt':
			self.qProgEditFontFamily = u'Courier New'
		else:
			self.qProgEditFontFamily = u'Ubuntu Mono'
		self.qProgEditFontSize = 13
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
		self.qProgEditValidate = True
		self.qProgEditColorScheme = u'CogsciBright'
		self.qProgEditCommentShortcut = u'Ctrl+M'
		self.qProgEditUncommentShortcut = u'Ctrl+Shift+M'
		self.qProgEditSwitchLeftShortcut = u'Alt+Left'
		self.qProgEditSwitchRightShortcut = u'Alt+Right'
		self.qProgEditSymbolTreeWidgetItemIcon = u'text-x-script'

	def version(self):

		"""
		desc:
			Returns the config version.
		"""

		return 0
