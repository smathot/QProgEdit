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
import sys
from QProgEdit.qt import QtCore, uic

class QUiLoader(QtCore.QObject):

	"""
	desc:
		A simple base class that implements dynamic UI loading for widgets.
	"""

	def loadUi(self, name):

		"""
		desc:
			Load a UI.

		arguments:
			name:
				desc:	The name of the UI file, without the .ui extension.
				type:	unicode
		"""

		dirPath = os.path.dirname(__file__)
		try:
			dirPath = dirPath.decode(sys.getfilesystemencoding())
		except:
			# This fails on Python 3
			pass
		# We pass an open file object, because loadUi otherwise tries to str()
		# the filename, which causes encoding trouble.
		path = os.path.join(dirPath, u'ui', u'%s.ui' % name)
		with open(path) as fd:
			self.ui = uic.loadUi(fd, self)
