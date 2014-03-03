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

from QProgEdit import _

def python(script):

	"""
	Cleans a Python script. Essentially, this means changing leading spaces
	into tabs, to avoid indentation issues.

	Arguments:
	script		--	A piece of Python script.

	Returns:
	A (msg, script) tuple, where the msg describes the changes to the text and
	script is the cleaned script. If no changes have been performed, msg is
	None.
	"""

	cleanLines = []
	for l in script.split(u'\n'):
		indent = 0
		while l.startswith(u'    '):
			indent += 1
			l = l[4:]
		cleanLines.append(u'\t'*indent + l)
	cleanScript = u'\n'.join(cleanLines)
	if cleanScript != script:
		msg = \
			_(u'Convert space-based indentation to tab-based indentation?')
	else:
		msg = None
	return msg, cleanScript
