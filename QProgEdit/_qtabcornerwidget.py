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
from QProgEdit import QLangMenu, QEditorStatus

class QTabCornerWidget(QtGui.QWidget):

	"""Contains a number of buttons that are displayed in the tab bar"""

	def __init__(self, parent=None, msg=None, handlerButtonText=None):

		"""
		Constructor

		Keyword arguments:
		parent				-- 	The parent QWidget. (default=None)
		msg					--	An informative text message. (default=None)
		handlerButtonText	--	Text for a top-right button, which can be
								clicked to call the handler, or None for no
								button. (default=None)
		"""

		super(QTabCornerWidget, self).__init__()

		self.tabManager = parent

		# Preferences button
		self.prefsButton = QtGui.QPushButton(QtGui.QIcon.fromTheme(
			u'preferences-desktop'), u'', self)
		self.prefsButton.setCheckable(True)
		self.prefsButton.toggled.connect(self.tabManager.togglePrefs)
		QtGui.QShortcut(QtGui.QKeySequence(u'Ctrl+Shift+P'),
			self).activated.connect(self.prefsButton.toggle)

		# Find button
		self.findButton = QtGui.QPushButton(QtGui.QIcon.fromTheme(
			u'edit-find'), u'', self)
		self.findButton.setCheckable(True)
		self.findButton.toggled.connect(self.tabManager.toggleFind)
		QtGui.QShortcut(QtGui.QKeySequence(u'Ctrl+F'), self).activated.connect(
			self.findButton.toggle)

		# Language button (filled by update())
		self.langButton = QtGui.QPushButton(self)
		self.langButton.setMenu(QLangMenu(self))
		QtGui.QShortcut(QtGui.QKeySequence(u'Ctrl+Shift+L'),
			self).activated.connect(self.langButton.click)
		
		# Handler button
		if handlerButtonText != None:
			self.handlerButton = QtGui.QPushButton(QtGui.QIcon.fromTheme(
				u'document-save'), handlerButtonText, self)
			self.handlerButton.clicked.connect(self.tabManager.handler)
		else:
			self.handlerButton = None
		
		# Editor status
		self.statusWidget = QEditorStatus(self)		
		
		# Message
		if msg != None:
			self.msgLabel = QtGui.QLabel(u'<small>%s</small>' % msg, parent= \
				self)

		self.hBox = QtGui.QHBoxLayout(self)
		self.hBox.setSpacing(2)
		self.hBox.setContentsMargins(2,2,2,2)
		if msg != None:
			self.hBox.addWidget(self.msgLabel)
		self.hBox.addWidget(self.statusWidget)
		self.hBox.addWidget(self.prefsButton)
		self.hBox.addWidget(self.findButton)
		self.hBox.addWidget(self.langButton)
		if self.handlerButton != None:
			self.hBox.addWidget(self.handlerButton)
		self.setLayout(self.hBox)		
		
	def update(self):

		"""Update to reflect document contents"""

		self.langButton.setIcon(QtGui.QIcon.fromTheme(u'text-x-%s' % \
			self.tabManager.lang().lower(), \
			QtGui.QIcon.fromTheme(u'text-plain')))
		self.findButton.setChecked(False)
		self.prefsButton.setChecked(False)