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

import _ast
try:
	from pyflakes.checker import Checker
	# Check whether PyFlakes supports the builtins keyword
	try:
		Checker(compile(u'', u'<string>', u'exec', _ast.PyCF_ONLY_AST), \
			builtins=None)
		pyflakesBuiltins = True
	except TypeError:
		pyflakesBuiltins = False
except:
	Checker = None

_builtins = []

def addPythonBuiltins(builtins):

	"""
	Adds a number of names that should be interpreted as builtins, and not
	trigger a warning.

	Argument:
	builtins	--	A list of names.
	"""

	global _builtins
	_builtins += builtins

def python(script):

	"""
	Validates a Python script using pyflakes.

	Arguments:
	script		--	The script to validate.

	Returns:
	A list of (line number, message) tuples contain all warnings.
	"""

	l = []
	try:
		c = compile(script, u'<string>', u'exec', _ast.PyCF_ONLY_AST)
	except SyntaxError as e:
		return [ (e.lineno-1, e.args[0]) ]
	else:
		if Checker is None:
			return []
		# Older version of PyFlakes don't support the builtins keyword, and
		# we don't want to crash on that.
		if pyflakesBuiltins:
			messages = Checker(c, builtins=_builtins).messages
		else:
			messages = Checker(c).messages
		for msg in messages:
			l.append((msg.lineno-1, msg.message % msg.message_args))
	return l
