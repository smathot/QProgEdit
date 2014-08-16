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
from PyQt4 import QtGui, QtCore
from PyQt4.Qsci import QsciScintilla, QsciScintillaBase, QsciLexerPython
from QProgEdit.py3 import *
from QProgEdit import QEditorCfg, QProgEdit, QTabCornerWidget, _

class QTabManager(QtGui.QTabWidget):

	"""
	desc:
		A tab manager that contains multiple QProgEdit tabs.
	"""

	cursorRowChanged = QtCore.pyqtSignal(int, int, int)
	focusLost = QtCore.pyqtSignal(int)
	focusReceived = QtCore.pyqtSignal(int)
	handlerButtonClicked = QtCore.pyqtSignal(int)

	def __init__(self, parent=None, cfg=QEditorCfg(), tabsClosable=False,
		tabsMovable=False, msg=None, handlerButtonText=None):

		"""
		desc:
			Constructor.

		keywords:
			parent:
				desc:	The parent widget.
				type:	QWidget
			cfg:
				desc:	A configuration backend. By default QEditorCfg is used.
						Custom backends must have the same API for getting and
						setting options.
			tabsClosable:
				desc:	Indicates whether a close button should be shown on
						tabs.
				type:	bool
			tabsMovable:
				desc:	Indicates whether tabs can be re-ordered.
				type:	bool
			msg:
				desc:	An informative message for the corner widget.
				type:	[str, unicode, NoneType]
			handlerButtonText:
				desc:	Text for a top-right button, which can be clicked to
						call the handler, or None for no button.
				type:	[str, unicode, NoneType]
		"""

		super(QTabManager, self).__init__(parent)		
		self.cfg = cfg
		self.setDocumentMode(True)
		self.setTabsClosable(tabsClosable)
		self.setMovable(tabsMovable)		
		self.currentChanged.connect(self.tabChanged)
		self.tabCloseRequested.connect(self.closeTab)
		QtGui.QShortcut(QtGui.QKeySequence(
			self.cfg.qProgEditSwitchLeftShortcut), self).activated \
			.connect(self.switchTabLeft)
		QtGui.QShortcut(QtGui.QKeySequence(
			self.cfg.qProgEditSwitchRightShortcut), self).activated \
			.connect(self.switchTabRight)
		self.setCornerWidget(QTabCornerWidget(self, msg=msg,
			handlerButtonText=handlerButtonText))
		# Under Windows, the tab bar is too small for the icons. Forcing the
		# tab-bar height looks funny on Linux. Mac OS not tested.
		if os.name == u'nt':
			self.setStyleSheet(u'QTabBar::tab { min-height: 32px; }')

	def addTab(self, title=u'Empty document', select=True):

		"""
		desc:
			Adds an empty document tab.

		keywords:
			title:
				desc:	A tab title.
				type:	[unicode, str]
			select:
				desc:	Indicates whether the newly created tab should be
						selected.
				type:	bool

		returns:
			desc:	The newly added tab widget.
			type:	QProgEdit
		"""

		progEdit = QProgEdit(self, title=title)
		index = super(QTabManager, self).addTab(progEdit, progEdit.title)
		if select:
			self.setCurrentIndex(index)
			self.cornerWidget().update()
		return progEdit

	def applyCfg(self):

		"""
		desc:
			Applies the configuration.
		"""

		for index in range(self.count()):
			progEdit = self.widget(index)
			progEdit.applyCfg()

	def closeTab(self, index=None):

		"""
		desc:
			Closes a tab.

		keywords:
			index:	A tab index (see [tabIndex]).
		"""

		index = self.tabIndex(index)
		if index == None:
			return
		self.removeTab(index)
		if self.count() == 0:
			self.addTab(_(u'Empty document'))

	def isAnyModified(self):
		
		"""
		desc:
			Checks if one or more of the tabs have been modified.
		
		returns:
			desc:	True if (one of) the tab(s) is modified, False otherwise.
			type:	bool
		"""

		for tab in self.tabs():
			if tab.isModified():
				return True
		return False

	def selectTab(self, index):

		"""
		desc:
			Switches to a specific tab.

		arguments:
			index:	A tab index, as understood by [tabIndex].
		"""

		index = self.tabIndex(index)
		if index != None:
			self.setCurrentIndex(index)

	def setText(self, text, index=None):

		"""
		desc:
			Sets the text on a specific tab.

		arguments:
			text:	The new text.

		keywords:
			index:	A tab index, as understood by [tabIndex].
		"""

		tab = self.tab(index)
		if tab != None:
			tab.setText(text)

	def switchTabLeft(self):
		
		"""
		desc:
			Switches to the tab on the left.
		"""
		
		newIndex = (self.currentIndex() - 1) % self.count()
		self.setCurrentIndex(newIndex)

	def switchTabRight(self):
		
		"""
		desc:
			Switches to the tab on the left.
		"""
		
		newIndex = (self.currentIndex() + 1) % self.count()
		self.setCurrentIndex(newIndex)

	def tab(self, index=None):

		"""
		desc:
			Returns the QProgEdit instance for a given tab.

		keywords:
			index:
				desc:	Specifies the tab, either by a name (i.e. the name on a
						tab), an index, or None to get the current tab.
				type:	[int, str, unicode, NoneType]

		returns:
			desc:		A tab, or None if no matching tab was found.
			type:		[QProgEdit, NoneType]
		"""

		index = self.tabIndex(index)
		if index == None:
			return None
		return self.widget(index)

	def tabIndex(self, index=None):

		"""
		desc:
			Returns the index for a given tab.

		keywords:
			index:
				desc:	Specifies the tab, either by a name (i.e. the name on a
						tab), an index, or None to get the current tab.
				type:	[int, str, unicode, NoneType]

		returns:
			desc:		A tab index, or None if no matching tab was found.
			type:		[int, NoneType]
		"""

		if isinstance(index, int):
			if index >= 0 and index < self.count():
				return index
		elif isinstance(index, basestring):
			for i in range(self.count()):
				if self.tabText(i) == index:
					return i
		elif index == None:
			if self.count() > 0:
				return self.currentIndex()
		else:
			raise Exception(u'index should be int, str, unicode, or None')
		return None

	def tabs(self):

		"""
		desc:
			Gets all tabs.

		returns:
			desc:	A list of all tab widgets.
			type:	list
		"""

		return [self.widget(i) for i in range(self.count())]

	def text(self, index=None):

		"""
		desc:
			Gets the text on a specific tab.

		keywords:
			index:	A tab index, as understood by [tabIndex].

		returns:
			The text or None if the tab does not exist.
		"""

		tab = self.tab(index)
		if tab == None:
			return None
		return tab.text()

	def toggleFind(self, visible):

		"""
		desc:
			Toggle the visibility of the find widget.

		arguments:
			visible:
				desc:	Visibility status.
				type:	bool
		"""

		self.currentWidget().toggleFind(visible)

	def togglePrefs(self, visible):

		"""
		desc:
			Toggle the visibility of the preferences widget.

		arguments:
			visible:
				desc:	Visibility status.
				type:	bool
		"""

		self.currentWidget().togglePrefs(visible)

	def tabChanged(self, index):

		"""
		desc:
			Is called when the current tab must be updated, for example because
			a new tab is selected.

		arguments:
			index:
				desc:	The index of the newly selected tab.
				type:	int
		"""

		if self.count() == 0:
			return
		self.cornerWidget().update()
		self.currentWidget().find.hide()
		self.currentWidget().prefs.hide()
		self.setWindowTitle(self.currentWidget().title)
