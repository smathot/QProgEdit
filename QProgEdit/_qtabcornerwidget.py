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
from QProgEdit import QLangMenu, QEditorStatus

class QTabCornerWidget(QtGui.QWidget):

	"""
	desc:
		Contains a number of buttons that are displayed in the tab bar.
	"""

	def __init__(self, tabManager, msg=None, handlerButtonText=None):

		"""
		desc:
			Constructor.

		arguments:
			tabManager:
				desc:	A tab manager.
				type:	QTabManager

		keywords:
			msg:
				desc:	An informative text message.
				type:	[str, unicode, NoneType]
			handlerButtonText:
				desc:	Text for a top-right button, which can be clicked to
						call the handler, or None for no button.
				type:	[str, unicode, NoneType]
		"""

		super(QTabCornerWidget, self).__init__(tabManager)
		self.tabManager = tabManager
		# Preferences button
		self.prefsButton = QtGui.QPushButton(QtGui.QIcon.fromTheme(
			u'preferences-desktop'), u'', self)
		self.prefsButton.setCheckable(True)
		self.prefsButton.toggled.connect(self.tabManager.togglePrefs)
		self.prefsShortcut = QtGui.QShortcut(
			QtGui.QKeySequence(u'Ctrl+Shift+P'), self.tabManager,
			context=QtCore.Qt.WidgetWithChildrenShortcut)
		self.prefsShortcut.activated.connect(self.prefsButton.toggle)
		# Find button
		self.findButton = QtGui.QPushButton(QtGui.QIcon.fromTheme(
			u'edit-find'), u'', self)
		self.findButton.setCheckable(True)
		self.findButton.toggled.connect(self.tabManager.toggleFind)
		# Keyboard shortcuts for find widget
		self.findShortcut = QtGui.QShortcut(QtGui.QKeySequence(u'Ctrl+F'),
			self.tabManager, context=QtCore.Qt.WidgetWithChildrenShortcut)
		self.findShortcut.activated.connect(self.findButton.toggle)
		self.replaceShortcut = QtGui.QShortcut(
			QtGui.QKeySequence(u'Ctrl+Shift+R'), self.tabManager,
			context=QtCore.Qt.WidgetWithChildrenShortcut)
		self.replaceShortcut.activated.connect(self.findButton.toggle)
		# Language button (filled by update())
		self.langButton = QtGui.QPushButton(self)
		self.langButton.setMenu(QLangMenu(self))
		self.langShortcut = QtGui.QShortcut(QtGui.QKeySequence(u'Ctrl+Shift+L'),
			self.tabManager, context=QtCore.Qt.WidgetWithChildrenShortcut)
		self.langShortcut.activated.connect(self.langButton.click)
		# Handler button
		if handlerButtonText is not None:
			self.handlerButton = QtGui.QPushButton(QtGui.QIcon.fromTheme(
				u'document-save'), handlerButtonText, self)
			self.handlerButton.clicked.connect(self.handlerButtonClicked)
		else:
			self.handlerButton = None
		# Editor status
		self.statusWidget = QEditorStatus(self)
		# Message
		if msg is not None:
			self.msgLabel = QtGui.QLabel(u'<small>%s</small>' % msg, parent= \
				self)
		self.hBox = QtGui.QHBoxLayout(self)
		self.hBox.setSpacing(2)
		self.hBox.setContentsMargins(2,2,2,2)
		if msg is not None:
			self.hBox.addWidget(self.msgLabel)
		self.hBox.addWidget(self.statusWidget)
		self.hBox.addWidget(self.prefsButton)
		self.hBox.addWidget(self.findButton)
		self.hBox.addWidget(self.langButton)
		if self.handlerButton is not None:
			self.hBox.addWidget(self.handlerButton)
		self.setLayout(self.hBox)
		# Set the tab order for keyboard navigation
		self.setTabOrder(self.prefsButton, self.findButton)
		self.setTabOrder(self.findButton, self.langButton)
		self.setTabOrder(self.langButton, self.handlerButton)

	def handlerButtonClicked(self):

		"""
		desc:
			Is called when the handler button is clicked and emits the relevant
			signals.
		"""

		self.tabManager.handlerButtonClicked.emit(
			self.tabManager.currentIndex())
		self.tabManager.tab().handlerButtonClicked.emit()

	def update(self):

		"""
		desc:
			Updates widget to reflect document contents.
		"""

		self.langButton.setIcon(QtGui.QIcon.fromTheme(
			u'text-x-%s' % self.tabManager.tab().lang().lower(),
			QtGui.QIcon.fromTheme(u'text-plain')))
		self.findButton.setChecked(False)
		self.prefsButton.setChecked(False)
