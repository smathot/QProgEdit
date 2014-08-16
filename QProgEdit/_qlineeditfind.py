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

class QLineEditFind(QtGui.QLineEdit):

	"""
	desc:
		Implements a line-edit widget that closes the find box on Escape presses
		and selects the highlighted text when receiving focus.
	"""

	def focusInEvent(self, e):

		"""
		desc:
			Selects the contents on focus.

		arguments:
			e:
				type:	QFocusEvent
		"""

		self.selectAll()
		e.accept()

	def keyPressEvent(self, e):

		"""
		desc:
			Handles key presses to deal with Escape.

		arguments:
			e:
				type:	QKeyEvent
		"""

		if e.key() == QtCore.Qt.Key_Escape:
			e.accept()
			self.parent().unshow()
		else:
			e.ignore()
			QtGui.QLineEdit.keyPressEvent(self, e)
