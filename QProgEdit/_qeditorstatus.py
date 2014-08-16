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

class QEditorStatus(QtGui.QLabel):

	"""
	desc:
		A simple widget that indicates the editor status, which currently
		corresponds only to the cursor position.
	"""

	def __init__(self, qProgEdit):

		"""
		desc:
			Constructor.

		arguments:
			qProgEdit:
				desc:	The parent QProgEdit.
				type:	QProgEdit
		"""

		super(QEditorStatus, self).__init__(qProgEdit)
		self.qProgEdit = qProgEdit
		if os.name == u'nt':
			self.setFont(QtGui.QFont(u'courier new', pointSize=8))
		else:
			self.setFont(QtGui.QFont(u'monospace', pointSize=8))

	def updateCursorPos(self, line=0, index=0):

		"""
		desc:
			Updates the cursor position.

		keywords:
			line:
				desc:	The line number.
				type:	int
			index:
				desc:	The column number.
				type:	int
		"""

		self.setText(u'(%.3d, %.3d)' % (index+1, line+1))
