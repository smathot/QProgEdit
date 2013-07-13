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
from PyQt4 import Qsci
from PyQt4.Qsci import QsciScintilla
from QProgEdit.ui import Ui_widgetPrefs

class QEditorPrefs(QtGui.QWidget):

	"""A single editor widget"""

	# These options correspond to the names of checkboxes in the prefsWidget
	# UI definition.
	checkBoxCfgOptions = [u'AutoComplete', u'AutoIndent',
		u'HighlightCurrentLine', u'HighlightMatchingBrackets', u'LineNumbers',
		u'ShowEol', u'ShowFolding', u'ShowIndent', u'ShowWhitespace',
		u'WordWrap']

	def __init__(self, parent=None):

		"""
		Constructor

		Keyword arguments:
		parent		-- 	the parent QWidget (default=None)
		"""

		super(QEditorPrefs, self).__init__(parent)
		self.qProgEdit = parent
		self.ui = Ui_widgetPrefs()
		self.ui.setupUi(self)
		self.bestHeight = self.height()
		self.lock = False

		# Make connections
		self.ui.fontComboBoxFontFamily.currentIndexChanged.connect(self.apply)
		self.ui.spinBoxFontSize.valueChanged.connect(self.apply)
		self.ui.spinBoxTabWidth.valueChanged.connect(self.apply)
		self.ui.checkBoxWordWrapMarker.toggled.connect(self.apply)
		for cfg in self.checkBoxCfgOptions:
			checkBox = getattr(self.ui, 'checkBox%s' % cfg)
			checkBox.stateChanged.connect(self.apply)

	def refresh(self):

		"""Refresh the controls"""

		self.lock = True
		index = self.ui.fontComboBoxFontFamily.findText(
			self.qProgEdit.cfg.qProgEditFontFamily)
		self.ui.fontComboBoxFontFamily.setCurrentIndex(index)
		self.ui.spinBoxFontSize.setValue(self.qProgEdit.cfg.qProgEditFontSize)
		self.ui.spinBoxTabWidth.setValue(self.qProgEdit.cfg.qProgEditTabWidth)
		self.ui.checkBoxWordWrapMarker.setChecked(
			self.qProgEdit.cfg.qProgEditWordWrapMarker != None)
		for cfg in self.checkBoxCfgOptions:
			checked = getattr(self.qProgEdit.cfg, u'qProgEdit%s' % cfg)
			checkBox = getattr(self.ui, u'checkBox%s' % cfg)
			checkBox.setChecked(checked)
		self.lock = False

	def apply(self):

		"""Apply the controls"""

		if self.lock:
			return
		self.qProgEdit.cfg.qProgEditFontFamily = unicode(
			self.ui.fontComboBoxFontFamily.currentText())
		self.qProgEdit.cfg.qProgEditFontSize = self.ui.spinBoxFontSize.value()
		self.qProgEdit.cfg.qProgEditTabWidth = self.ui.spinBoxTabWidth.value()
		if self.ui.checkBoxWordWrapMarker.isChecked():
			self.qProgEdit.cfg.qProgEditWordWrapMarker = 80
		else:
			self.qProgEdit.cfg.qProgEditWordWrapMarker = None
		for cfg in self.checkBoxCfgOptions:
			checkBox = getattr(self.ui, u'checkBox%s' % cfg)
			checked = checkBox.isChecked()
			setattr(self.qProgEdit.cfg, u'qProgEdit%s' % cfg, checked)
		if self.qProgEdit.tabManager != None:
			self.qProgEdit.tabManager.applyCfg()
		else:
			self.qProgEdit.applyCfg()

