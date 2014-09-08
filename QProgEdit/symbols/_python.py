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

import re

def python(script):

	"""
	desc:
		Extracts the symbols from a Python script.

	arguments:
		script:
			desc:	A Python script.
			type:	unicode

	returns:
		desc:		A list of symbols, where each symbol is a (lineNr,
					type, name, argSpec) tuple. Type is always 'class' or 'def'.
		type:		list
	"""

	regexp = \
		r'\s*(?P<type>def|class)\s+(?P<name>\w+)\((?P<argspec>[^\)]*)\){0,1}\s*:{0,1}'
	symbols = []
	for lineNo, line in enumerate(script.split(u'\n')):
		m = re.match(regexp, line)
		if m != None:
			symbols.append( (lineNo+1, m.group(u'type'), m.group(u'name'),
				m.group(u'argspec')) )
	return symbols
