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
from QProgEdit.py3 import *
from QProgEdit import QEditorConst

class QLangMenu(QtGui.QMenu):

	"""
	desc:
		The language selection menu.
	"""

	def __init__(self, tabCornerWidget):

		"""
		desc:
			Constructor.

		arguments:
			tabCornerWidget:
				desc:	The parent QTabCornerWidget.
				type:	QTabCornerWidget
		"""

		super(QLangMenu, self).__init__(tabCornerWidget)
		self.tabCornerWidget = tabCornerWidget
		for lang in QEditorConst.languages:
			self.addAction(QtGui.QIcon.fromTheme(u'text-x-%s' % lang.lower(),
				QtGui.QIcon.fromTheme(u'text-plain')), lang)
		self.triggered.connect(self.setLang)

	@property
	def tabManager(self):
		return self.tabCornerWidget.tabManager

	def setLang(self, action):

		"""
		desc:
			Select a new language for the selected tab.

		arguments:
			action:
				type:	QAction
		"""

		self.tabManager.tab().setLang(unicode(action.text()))
		self.tabCornerWidget.update()
