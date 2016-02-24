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

from qtpy import QtCore, QtWidgets, QtGui

class QSymbolTreeWidgetItem(QtWidgets.QTreeWidgetItem):

	"""
	desc:
		A symbol-tree widget item to use for symbol overviews.
	"""

	def __init__(self, editor, lineNo, _type, name, argSpec):

		"""
		desc:
			Constructor.

		arguments:
			editor:
				desc:	The editor widget.
				type:	QEditor
			lineNo:
				desc:	A line number.
				type:	int
			_type:
				desc:	The symbol type, such as 'class' or 'def'
				type:	unicode
			name:
				desc:	The symbol name
				type:	unicode
			argSpec:
				desc:	The symbol's argument specification.
				type:	unicode
		"""

		super(QSymbolTreeWidgetItem, self).__init__([name])
		self.editor = editor
		self.setIcon(0, QtGui.QIcon.fromTheme(
			self.cfg.qProgEditSymbolTreeWidgetItemIcon))
		self.lineNo = lineNo
		self._type = _type
		self.name = name
		self.argSpec = argSpec
		self.setToolTip(0,
			u'Type: <b>%s</b><br/>Line: <b>%d</b><br />Extra: <b>%s</b>' \
			% (_type, lineNo, argSpec))

	@property
	def cfg(self):
		return self.editor.cfg

	def activate(self):

		"""
		desc:
			Is called when the symbol is activated, to focus the symbol in the
			editor.
		"""

		self.editor.setCursorPosition(self.lineNo-1, 0)
		self.editor.focusTab()
