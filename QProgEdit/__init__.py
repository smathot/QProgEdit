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

---
desc: |
	# QProgEdit

	v%--python: from QProgEdit import __version__; print(__version__)--%

	QProgEdit is a PyQt4 widget that implements a full-featured text editor
	component. It's primary target at the moment is
	[OpenSesame](http://osdoc.cogsci.nl), a graphical experiment builder.

	Copyright (2013-2015) Sebastiaan Mathôt

	<http://www.cogsci.nl/smathot>

	## Overview

	%--
	toc:
		mindepth: 2
		maxdepth: 3
		exclude: [Overview]
	--%

	## Dependencies

	- `PyQt4`
	- `Qscintilla2`

	## Example

	~~~ python
	%--include: example.py--%
	~~~

license: |
	`QProgEdit` is released under the terms of the
	[General Public License v3](http://www.gnu.org/licenses/gpl-3.0.txt).
---
"""

version = __version__ = u'3.0.1a1'

from QProgEdit.py3compat import *

# A simple wrapper around the translate function
from QProgEdit.qt.QtCore import QCoreApplication
_ = lambda s: QCoreApplication.translate(u'qprogedit', s)

import QProgEdit._qeditorconst as QEditorConst
import QProgEdit._qcolorscheme as QColorScheme
from QProgEdit._quiloader import QUiLoader
from QProgEdit._qsymboltreewidgetitem import QSymbolTreeWidgetItem
from QProgEdit._qeditorcfg import QEditorCfg
from QProgEdit._qeditorshortcut import QEditorShortcut
from QProgEdit._qlexer import QLexer
from QProgEdit._qlangmenu import QLangMenu
from QProgEdit._qeditor import QEditor
from QProgEdit._qeditorprefs import QEditorPrefs
from QProgEdit._qeditorfind import QEditorFind
from QProgEdit._qeditorstatus import QEditorStatus
from QProgEdit._qprogedit import QProgEdit
from QProgEdit._qtabcornerwidget import QTabCornerWidget
from QProgEdit._qtabmanager import QTabManager
