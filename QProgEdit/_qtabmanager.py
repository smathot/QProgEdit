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
from QProgEdit import QEditorCfg, QProgEdit, QTabCornerWidget, _

class QTabManager(QtGui.QTabWidget):

	"""A widget that contains multiple document tabs"""

	def __init__(self, parent=None, defaultLang=u'text', cfg=QEditorCfg(),
		createTab=False, tabsClosable=False, tabsMovable=False, handler=None,
		msg=None, handlerButtonText=None, callHandlerOnFocusOut=True):

		"""
		Constructor

		Keyword arguments:
		parent			-- 	the parent QWidget (default=None)
		defaultlang		-- 	default language, used to select a lexer for syntax
							highlighting. If an appropriate lexer isn't found, no
							error is generated, but syntax highlighting is
							disabled. For a list of available lexers, refer to
							the QsciScintilla documentation. (default=u'text')
		cfg				--	a configuration backend. By default QEditorCfg is
							used. Custom backends must have the same API for
							getting and setting options (default=QEditorCfg())
		createTab		--	Indicates whether an empty tab should be created upon
							initialization. (default=False)
		tabsClosable	--	Indicates whether a close button should be shown on
							each tab. (default=False)
		tabsMovable		--	Indicates whether tabs can be re-ordered.
							(default=False)
		handler			--	The handler function. (default=None)
		msg				--	An informative message for the corner widget, or
							None for auto-detect. (default=None)
		handlerButtonText	--	Text for a top-right button, which can be
								clicked to call the handler, or None for no
								button. (default=None)
		callHandlerOnFocusOut	--	Indicates whether the handler should be
									called when the editor loses focus.
									(default=True)
		"""

		super(QTabManager, self).__init__(parent)		
		self.defaultLang = defaultLang
		if defaultLang == u'Python' and msg == None:
			msg = u'Python %d.%d.%d' % (sys.version_info[0], \
				sys.version_info[1], sys.version_info[2])
		self.cfg = cfg
		self.callHandlerOnFocusOut = callHandlerOnFocusOut
		self.setDocumentMode(True)
		self.setTabsClosable(tabsClosable)
		self.setMovable(tabsMovable)		
		self.currentChanged.connect(self.tabChanged)
		self.tabCloseRequested.connect(self.closeTab)
		self.setHandler(handler)
		self.setCornerWidget(QTabCornerWidget(self, msg=msg, \
			handlerButtonText=handlerButtonText))
		if createTab:
			self.addTab(_(u'Empty document'))
		# Under Windows, the tab bar is too small for the icons. Forcing the
		# tab-bar height looks funny on Linux. Mac OS not tested.
		if os.name == u'nt':
			self.setStyleSheet(u'QTabBar::tab { min-height: 32px; }')

	def addTab(self, title, lang=None, select=True):

		"""
		Adds an empty document tab

		Arguments:
		title	--	the title of the tabs

		Keyword arguments:
		lang		--	a language, if different from the default language
					(default=None)
		select	-- 	indicates whether the newly created tab should be selected
					(default=True)
		"""

		if lang == None:
			lang = self.defaultLang
		progEdit = QProgEdit(self, lang=lang, cfg=self.cfg, title=title, \
			handler=self.handler)
		index = super(QTabManager, self).addTab(progEdit, progEdit.title)
		if select:
			self.setCurrentIndex(index)
			self.cornerWidget().update()

	def applyCfg(self):

		"""Apply the configuration"""

		for index in range(self.count()):
			progEdit = self.widget(index)
			progEdit.applyCfg()

	def closeTab(self, index=None):

		"""
		Closes a tab

		Arguments:
		index	--	the index of the tab to be closed, or None to close the
					current tab (default=None)
		"""

		if index == None:
			index = self.currentIndex()
		self.removeTab(index)
		if self.count() == 0:
			self.addTab(_(u'Empty document'))

	def isModified(self, index=None):
		
		"""
		Returns the modified status for one or all tabs.
		
		Keyword arguments:
		index	--	The index for a tab, or None to check all tabs.
					(default=None)
		
		Returns:
		True if (one of) the tab(s) is modified, False otherwise.
		"""
		
		if index == None:
			for i in range(self.count()):
				if self.widget(i).isModified():
					return True
			return False
		return self.widget(i).isModified()

	def lang(self, index=None):

		"""
		Gets the language of a tab

		Keyword arguments:
		index	--	the index of the tab, or None for current tab (default=None)

		Returns:
		A string with the language (e.g., 'text', or 'python'). If an invalid tab
		has been specified, None is returned.
		"""

		if self.count() == 0:
			return None
		if index == None:
			return self.currentWidget().lang()
		elif index >= 0 and index < self.count():
			return self.widget(index).lang()
		return None
	
	def setHandler(self, handler=None):
		
		"""
		Set the handler function, i.e. the function that is called when the
		editor loses focus and changes need to be processed.
		
		Keyword arguments:
		handler		--	A handler function or None to disable the handler.
						(default=None)
		"""
		
		self.handler = handler
		for i in range(self.count()):
			self.widget(i).setHandler(handler)

	def setLang(self, lang=u'text', index=None):

		"""
		Sets the language

		Keyword arguments:
		lang	-- 	language, used to select a lexer for syntax highlighting.
					If an appropriate lexer isn't found, no error is
					generated, but syntax highlighting is disabled. For a
					list of available lexers, refer to the QsciScintilla
					documentation. (default='text')
		index	--	the index of the tab, or None for all tabs (default=None)
		"""

		if self.count() == 0:
			return
		elif index == None:
			for i in range(self.count()):
				self.widget(i).setLang(lang)
		elif index >= 0 and index < self.count():
			self.widget(index).setLang(lang)

	def setText(self, txt, index=None):

		"""
		Sets the document text for a given tab. If the tab is not available, the
		function will fail silently.

		Arguments:
		txt		--	the text to set

		Keyword arguments:
		index	--	the index of the tab, or None for current tab (default=None)
		"""

		if self.count() == 0:
			return
		elif index == None:
			self.currentWidget().setText(txt)
		elif index >= 0 and index < self.count():
			self.widget(index).setText(txt)

	def text(self, index=None):

		"""
		Returns the text for a given tab

		Arguments:
		index	--	the index of the tab, or None for current tab (default=None)

		Returns:
		A unicode string with the tab contents or None if the specified tab does
		not exist.
		"""

		if self.count() == 0:
			return None
		if index == None:
			return unicode(self.currentWidget().text())
		if index >= 0 and index < self.count():
			return unicode(self.widget(index).text())
		return None

	def toggleFind(self, visible):

		"""
		Toggle the visibility of the find widget

		Arguments:
		visible		--	a boolean
		"""

		self.currentWidget().toggleFind(visible)

	def togglePrefs(self, visible):

		"""
		Toggle the visibility of the preferences widget

		Arguments:
		visible		--	a boolean
		"""

		self.currentWidget().togglePrefs(visible)

	def tabChanged(self, index):

		"""
		Is called when the current tab must be updated, for example because a
		new tab is selected.

		Arguments:
		index	--	the index of the newly selected tabs
		"""

		if self.count() == 0:
			return
		self.cornerWidget().update()
		self.currentWidget().find.hide()
		self.currentWidget().prefs.hide()
		self.setWindowTitle(self.currentWidget().title)