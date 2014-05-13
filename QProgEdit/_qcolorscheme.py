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

TangoDark = {
	u'Background'					: u'#2e3436',
	u'Default'						: u'#d3d7cf',
	u'Selection background'			: u'#204a87',
	u'Selection foreground'			: u'#d3d7cf',
	u'Caret-line background'		: u'#555753',
	u'Identifier'					: u'#eeeeec',
	u'Comment'						: u'#ef2929',
	u'Comment block'				: u'#ef2929',
	u'Number'						: u'#8ae234',
	u'Double-quoted string'			: u'#729fcf',
	u'Single-quoted string'			: u'#729fcf',
	u'Triple-quoted string'			: u'#729fcf',
	u'Triple single-quoted string'	: u'#729fcf',
	u'Triple double-quoted string'	: u'#729fcf',
	u'Keyword'						: u'#ad7fa8',
	u'Operator'						: u'#ad7fa8',
	u'Class name'					: u'#e9b96e',
	u'Function or method name'		: u'#e9b96e',
	u'Unclosed string'				: u'#ef2929',
	u'Highlighted identifier'		: u'#ef2929',
	u'Decorator'					: u'#ef2929',
	u'Invalid'						: u'#cc0000',
	u'Highlight'					: u'#fce94f',
	}

SolarizedPalette = {
	u'Base03'	: u'#002b36',
	u'Base02'	: u'#073642',
	u'Base01'	: u'#586e75',
	u'Base00'	: u'#657b83',
	u'Base0'	: u'#839496',
	u'Base1'	: u'#93a1a1',
	u'Base2'	: u'#eee8d5',
	u'Base3'	: u'#fdf6e3',
	u'Yellow'	: u'#b58900',
	u'Orange'	: u'#cb4b16',
	u'Red'		: u'#dc322f',
	u'Magenta'	: u'#d33682',
	u'Violet'	: u'#6c71c4',
	u'Blue'		: u'#268bd2',
	u'Cyan'		: u'#2aa198',
	u'Green'	: u'#859900'
	}

SolarizedDark = {
	u'Background'					: SolarizedPalette[u'Base02'],
	u'Default'						: SolarizedPalette[u'Base1'],
	u'Selection background'			: SolarizedPalette[u'Base2'],
	u'Selection foreground'			: SolarizedPalette[u'Base01'],
	u'Caret-line background'		: SolarizedPalette[u'Base03'],
	u'Identifier'					: SolarizedPalette[u'Base1'],
	u'Comment'						: SolarizedPalette[u'Base00'],
	u'Comment block'				: SolarizedPalette[u'Base00'],
	u'Number'						: SolarizedPalette[u'Blue'],
	u'Double-quoted string'			: SolarizedPalette[u'Cyan'],
	u'Single-quoted string'			: SolarizedPalette[u'Cyan'],
	u'Triple-quoted string'			: SolarizedPalette[u'Cyan'],
	u'Triple single-quoted string'	: SolarizedPalette[u'Cyan'],
	u'Triple double-quoted string'	: SolarizedPalette[u'Cyan'],
	u'Keyword'						: SolarizedPalette[u'Yellow'],
	u'Operator'						: SolarizedPalette[u'Base1'],
	u'Class name'					: SolarizedPalette[u'Magenta'],
	u'Function or method name'		: SolarizedPalette[u'Magenta'],
	u'Unclosed string'				: SolarizedPalette[u'Red'],
	u'Highlighted identifier'		: SolarizedPalette[u'Cyan'],
	u'Decorator'					: SolarizedPalette[u'Orange'],
	u'Invalid'						: SolarizedPalette[u'Orange'],
	u'Highlight'					: SolarizedPalette[u'Orange'],
	}

Default = {u'Invalid' : u'red', u'Highlight' : u'yellow'}

# A list of available themes
schemes = ['Default', 'TangoDark', 'SolarizedDark']
