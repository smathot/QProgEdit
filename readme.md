# QProgEdit

QProgEdit is a PyQt4 widget that implements a full-featured text editor component. It's primary target at the moment is [OpenSesame](http://osdoc.cogsci.nl), a graphical experiment builder.

Copyright (2013) Sebastiaan Mathôt  
<http://www.cogsci.nl/smathot>

## Example

To see a standalone example, run `qprogedit`.

## Structure

- `QTabManger` implements a multiple-tab editor, including  a menu in the top-right. Embeds:
	- `QTabCornerWidget` implements the menu in the top-right of the tab window. Embeds:
		- `QLangMenu` implements a language-selection menu.
		- `QEditorStatus` implements a cursor position indicator.
	- `QProgEdit` which corresponds to a single programming editor. Embeds:
		- A `QEditorPrefs` widget, which implements the preferences menu.
		- A `QEditorFind` widget, which implements the search/ replace dialog.
		- A `QEditor` widget, which is the actual editor widget, based on `Qsci.QsciScintilla`.
		
The following are non-widget classes:
	
- `QLexer` is used by `QEditor` to implement syntax highlighting and theming. This class morphs into an extension of a `Qsci.QsciLexer[Language]` class.
- `QEditorCfg` is a non-persistent configuration back-end.

The following are modules:
	
- `QEditorConst` contains a number of constants.
- `QColorScheme` contains color-scheme definitions.

## License

`QProgEdit` is released under the terms of the [General Public License v3](http://www.gnu.org/licenses/gpl-3.0.txt). For license details, please visit <http://www.gnu.org/licenses/gpl-3.0.txt> or see the included file `COPYING`.