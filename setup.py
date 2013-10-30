#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is part of zoteromarkdown.

zoteromarkdown is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

zoteromarkdown is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with zoteromarkdown.  If not, see <http://www.gnu.org/licenses/>.
"""

from QProgEdit import version
from distutils.core import setup

setup(
    name=u'python-qprogedit',
    version=version,
    description= \
		u'A QScintilla-based text-editor component',
    author=u'Sebastiaan Mathôt',
    author_email=u's.mathot@cogsci.nl',
    license=u'GNU GPL Version 3',
    url=u'https://github.com/smathot/QProgEdit',
    packages=['QProgEdit', 'QProgEdit.ui']
)
