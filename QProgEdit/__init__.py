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

version = u'1.2.4'

# A simple wrapper around the translate function
from PyQt4.QtCore import QCoreApplication
_ = lambda s: unicode(QCoreApplication.translate(u'qprogedit', s))

import _qeditorconst as QEditorConst
import _qcolorscheme as QColorScheme
from _qeditorcfg import QEditorCfg
from _qlexer import QLexer
from _qlangmenu import QLangMenu
from _qeditor import QEditor
from _qeditorprefs import QEditorPrefs
from _qeditorfind import QEditorFind
from _qeditorstatus import QEditorStatus
from _qprogedit import QProgEdit
from _qtabcornerwidget import QTabCornerWidget
from _qtabmanager import QTabManager
