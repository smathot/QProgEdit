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

from QProgEdit import __version__
from setuptools import setup, find_packages

setup(
	name=u'python-qprogedit',
	version=__version__,
	description= u'A QScintilla-based text-editor component',
	author=u'Sebastiaan Mathôt',
	author_email=u's.mathot@cogsci.nl',
	license=u'GNU GPL Version 3',
	url=u'https://github.com/smathot/QProgEdit',
	install_requires='qtpy',
	packages=find_packages('.'),
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: End Users/Desktop',
		'Topic :: Text Editors',
		'Environment :: MacOS X',
		'Environment :: Win32 (MS Windows)',
		'Environment :: X11 Applications',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
	],
)
