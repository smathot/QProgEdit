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

black = u'#000000'
white = u'#FFFFFF'

# Tango colors
butter = ['#fce94f', '#edd400', '#c4a000']
orange = ['#fcaf3e', '#f57900', '#ce5c00']
chocolate = ['#e9b96e', '#c17d11', '#8f5902']
chameleon = ['#8ae234', '#73d216', '#4e9a06']
skyBlue = ['#729fcf', '#3465a4', '#204a87']
plum = ['#ad7fa8', '#75507b', '#5c3566']
scarletRed = ['#ef2929', '#cc0000', '#a40000']
aluminium = ['#eeeeec', '#d3d7cf', '#babdb6', '#888a85', '#555753', '#2e3436']

CogsciBright = {
	u'Background'					: white,
	u'Default'						: black,
	u'Selection background'			: skyBlue[0],
	u'Selection foreground'			: white,
	u'Caret-line background'		: aluminium[0],
	u'Identifier'					: black,
	u'Number'						: chameleon[2],
	u'Double-quoted string'			: skyBlue[2],
	u'Single-quoted string'			: skyBlue[2],
	u'Triple-quoted string'			: skyBlue[2],
	u'Triple single-quoted string'	: (chocolate[1], False, True),
	u'Triple double-quoted string'	: (chocolate[1], False, True),
	u'Comment'						: (chocolate[1], False, True),
	u'Comment block'				: (chocolate[1], False, True),
	u'Keyword'						: (black, True, False),
	u'Operator'						: aluminium[5],
	u'Class name'					: (plum[2], True, False),
	u'Function or method name'		: (orange[2], True, False),
	u'Unclosed string'				: scarletRed[0],
	u'Highlighted identifier'		: (chameleon[2], True, False),
	u'Decorator'					: butter[2],
	u'Invalid'						: scarletRed[0],
	u'Highlight'					: butter[2],
	u'Fold margin'					: aluminium[0],
	}

CogsciDark = {
	u'Background'					: black,
	u'Default'						: white,
	u'Selection background'			: skyBlue[2],
	u'Selection foreground'			: white,
	u'Caret-line background'		: aluminium[5],
	u'Identifier'					: white,
	u'Number'						: chameleon[0],
	u'Double-quoted string'			: skyBlue[0],
	u'Single-quoted string'			: skyBlue[0],
	u'Triple-quoted string'			: skyBlue[0],
	u'Triple single-quoted string'	: (chocolate[1], False, True),
	u'Triple double-quoted string'	: (chocolate[1], False, True),
	u'Comment'						: (chocolate[1], False, True),
	u'Comment block'				: (chocolate[1], False, True),
	u'Keyword'						: (white, True, False),
	u'Operator'						: aluminium[0],
	u'Class name'					: (plum[0], True, False),
	u'Function or method name'		: (orange[0], True, False),
	u'Unclosed string'				: scarletRed[2],
	u'Highlighted identifier'		: scarletRed[1],
	u'Decorator'					: butter[0],
	u'Invalid'						: scarletRed[2],
	u'Highlight'					: butter[0],
	u'Fold margin'					: aluminium[2],
	}



TangoDark = {
	u'Background'					: aluminium[5],
	u'Default'						: aluminium[1],
	u'Selection background'			: skyBlue[2],
	u'Selection foreground'			: aluminium[1],
	u'Caret-line background'		: aluminium[4],
	u'Identifier'					: aluminium[0],
	u'Comment'						: scarletRed[0],
	u'Comment block'				: scarletRed[0],
	u'Number'						: chameleon[0],
	u'Double-quoted string'			: skyBlue[0],
	u'Single-quoted string'			: skyBlue[0],
	u'Triple-quoted string'			: skyBlue[0],
	u'Triple single-quoted string'	: skyBlue[0],
	u'Triple double-quoted string'	: skyBlue[0],
	u'Keyword'						: plum[0],
	u'Operator'						: plum[0],
	u'Class name'					: chocolate[0],
	u'Function or method name'		: chocolate[0],
	u'Unclosed string'				: scarletRed[0],
	u'Highlighted identifier'		: scarletRed[0],
	u'Decorator'					: scarletRed[0],
	u'Invalid'						: scarletRed[1],
	u'Highlight'					: butter[0],
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
schemes = ['Default', 'CogsciBright', 'CogsciDark', 'TangoDark', 'SolarizedDark']
