<span class="ModuleDoc YAMLDoc" id="QProgEdit" markdown="1">

# *module* QProgEdit

# QProgEdit

v2.0.0


QProgEdit is a PyQt4 widget that implements a full-featured text editor
component. It's primary target at the moment is
[OpenSesame](http://osdoc.cogsci.nl), a graphical experiment builder.

Copyright (2013) Sebastiaan Mathôt
<http://www.cogsci.nl/smathot>

## Overview


- [Dependencies](#dependencies)
- [Example](#example)
- [*class* QProgEdit.QEditor](#class-qprogeditqeditor)
- [*class* QProgEdit.QEditorCfg](#class-qprogeditqeditorcfg)
- [*class* QProgEdit.QEditorFind](#class-qprogeditqeditorfind)
- [*class* QProgEdit.QEditorPrefs](#class-qprogeditqeditorprefs)
- [*class* QProgEdit.QEditorStatus](#class-qprogeditqeditorstatus)
- [*class* QProgEdit.QLangMenu](#class-qprogeditqlangmenu)
- [*class* QProgEdit.QLexer](#class-qprogeditqlexer)
- [*class* QProgEdit.QProgEdit](#class-qprogeditqprogedit)
- [*class* QProgEdit.QSymbolTreeWidgetItem](#class-qprogeditqsymboltreewidgetitem)
- [*class* QProgEdit.QTabCornerWidget](#class-qprogeditqtabcornerwidget)
- [*class* QProgEdit.QTabManager](#class-qprogeditqtabmanager)
- [*module* QProgEdit.py3](#module-qprogeditpy3)



## Dependencies

- `PyQt4`
- `Qscintilla2`

## Example

~~~ python
#!/usr/bin/env python
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

import sip
sip.setapi('QString', 1)

import sys
from PyQt4 import QtGui, QtCore
from QProgEdit import QTabManager, validate

def cursorRowChanged(index, rowFrom, rowTo):

	print(u'curorRowChanged(): %d, %d, %d' % (index, rowFrom, rowTo))

def focusLost(index):
	
	print(u'focusOut(): %s' % index)
	
def focusReceived(index):

	print(u'focusReceived(): %s' % index)

def handlerButtonClicked(index):

	print(u'handlerButtonClicked(): %s' % index)

def activateSymbolTree(treeWidgetItem):

	treeWidgetItem.activated()

def main():
	
	"""Runs a simple QProgEdit demonstration."""

	validate.addPythonBuiltins(['builtin_var'])
	app = QtGui.QApplication(sys.argv)

	treeWidgetItem1 = QtGui.QTreeWidgetItem([u'Tab 1'])
	treeWidgetItem3 = QtGui.QTreeWidgetItem([u'Tab 3'])
	symbolTree = QtGui.QTreeWidget()
	symbolTree.addTopLevelItem(treeWidgetItem1)
	symbolTree.addTopLevelItem(treeWidgetItem3)
	symbolTree.itemActivated.connect(activateSymbolTree)

	tabManager = QTabManager(handlerButtonText=u'apply')
	tabManager.setWindowIcon(QtGui.QIcon.fromTheme(u'accessories-text-editor'))
	tabManager.setWindowTitle(u'QProgEdit')
	tabManager.resize(800, 600)

	tabManager.cursorRowChanged.connect(cursorRowChanged)
	tabManager.focusLost.connect(focusLost)
	tabManager.focusReceived.connect(focusReceived)
	tabManager.handlerButtonClicked.connect(handlerButtonClicked)

	tabManager.addTab(u'Tab 1')
	tabManager.tab().setLang(u'Python')
	tabManager.tab().setSymbolTree(treeWidgetItem1)
	tabManager.tab().setText(open(__file__).read())

	tabManager.addTab(u'Tab 2')
	tabManager.tab(1).setText(u'Some plain text')

	tabManager.addTab(u'Tab 3')
	tabManager.tab(u'Tab 3').setLang(u'Python')
	tabManager.tab(u'Tab 3').setSymbolTree(treeWidgetItem3)
	tabManager.tab(u'Tab 3').setText(
		u'def test():\n\tprint undefined_var\n\tbuiltin_var\n\ntest()\n')

	layout = QtGui.QHBoxLayout()
	layout.addWidget(symbolTree)
	layout.addWidget(tabManager)
	container = QtGui.QWidget()
	container.setLayout(layout)
	container.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

~~~



<span class="ClassDoc YAMLDoc" id="QProgEdit-QEditor" markdown="1">

## *class* QProgEdit.QEditor

A single editor widget, which is embedded in a QProgEdit widget.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-__init__" markdown="1">

### *function* QProgEdit.QEditor.\_\_init\_\_(qProgEdit)

Constructor.

__Arguments:__

- `qProgEdit` -- The parent QProgEdit.
	- Type: QProgEdit




</span>


[QProgEdit.QEditor.__init__]: #QProgEdit-QEditor-__init__
[QEditor.__init__]: #QProgEdit-QEditor-__init__
[__init__]: #QProgEdit-QEditor-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-applyCfg" markdown="1">

### *function* QProgEdit.QEditor.applyCfg()

Applies the configuration.




</span>


[QProgEdit.QEditor.applyCfg]: #QProgEdit-QEditor-applyCfg
[QEditor.applyCfg]: #QProgEdit-QEditor-applyCfg
[applyCfg]: #QProgEdit-QEditor-applyCfg
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-commentSelection" markdown="1">

### *function* QProgEdit.QEditor.commentSelection()

Comments out the currently selected text.




</span>


[QProgEdit.QEditor.commentSelection]: #QProgEdit-QEditor-commentSelection
[QEditor.commentSelection]: #QProgEdit-QEditor-commentSelection
[commentSelection]: #QProgEdit-QEditor-commentSelection
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-cursorMoved" markdown="1">

### *function* QProgEdit.QEditor.cursorMoved()

Is called whenever the cursor moves, checks whether the cursor has jumped from one line to the next, and, if so, calls the relevant functions.




</span>


[QProgEdit.QEditor.cursorMoved]: #QProgEdit-QEditor-cursorMoved
[QEditor.cursorMoved]: #QProgEdit-QEditor-cursorMoved
[cursorMoved]: #QProgEdit-QEditor-cursorMoved
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-focusInEvent" markdown="1">

### *function* QProgEdit.QEditor.focusInEvent(e)

Called when the editor receives focus.

__Arguments:__

- `e` -- No description




</span>


[QProgEdit.QEditor.focusInEvent]: #QProgEdit-QEditor-focusInEvent
[QEditor.focusInEvent]: #QProgEdit-QEditor-focusInEvent
[focusInEvent]: #QProgEdit-QEditor-focusInEvent
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-focusOutEvent" markdown="1">

### *function* QProgEdit.QEditor.focusOutEvent(e)

Called when the editor loses focus.

__Arguments:__

- `e` -- No description




</span>


[QProgEdit.QEditor.focusOutEvent]: #QProgEdit-QEditor-focusOutEvent
[QEditor.focusOutEvent]: #QProgEdit-QEditor-focusOutEvent
[focusOutEvent]: #QProgEdit-QEditor-focusOutEvent
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-highlightSelection" markdown="1">

### *function* QProgEdit.QEditor.highlightSelection()

Highlights all parts of the text that match the current selection.




</span>


[QProgEdit.QEditor.highlightSelection]: #QProgEdit-QEditor-highlightSelection
[QEditor.highlightSelection]: #QProgEdit-QEditor-highlightSelection
[highlightSelection]: #QProgEdit-QEditor-highlightSelection
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-keyPressEvent" markdown="1">

### *function* QProgEdit.QEditor.keyPressEvent(event)

Intercepts certain keypress events to implement custom copy-pasting and zooming.

__Arguments:__

- `event` -- No description
	- Type: QKeyPressEvent




</span>


[QProgEdit.QEditor.keyPressEvent]: #QProgEdit-QEditor-keyPressEvent
[QEditor.keyPressEvent]: #QProgEdit-QEditor-keyPressEvent
[keyPressEvent]: #QProgEdit-QEditor-keyPressEvent
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-lang" markdown="1">

### *function* QProgEdit.QEditor.lang()

No description specified.

__Returns:__

The language of the editor.

- Type: unicode




</span>


[QProgEdit.QEditor.lang]: #QProgEdit-QEditor-lang
[QEditor.lang]: #QProgEdit-QEditor-lang
[lang]: #QProgEdit-QEditor-lang
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-onMarginClick" markdown="1">

### *function* QProgEdit.QEditor.onMarginClick(margin, line, state)

Shows validation errors when the margin symbol is clicked.

__Arguments:__

- `line` -- The line number.
	- Type: int
- `margin` -- The margin number.
	- Type: int
- `state` -- The keyboard state.
	- Type: int




</span>


[QProgEdit.QEditor.onMarginClick]: #QProgEdit-QEditor-onMarginClick
[QEditor.onMarginClick]: #QProgEdit-QEditor-onMarginClick
[onMarginClick]: #QProgEdit-QEditor-onMarginClick
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-paste" markdown="1">

### *function* QProgEdit.QEditor.paste()

Re-implements the paste method to allow modification of paste content.




</span>


[QProgEdit.QEditor.paste]: #QProgEdit-QEditor-paste
[QEditor.paste]: #QProgEdit-QEditor-paste
[paste]: #QProgEdit-QEditor-paste
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-setLang" markdown="1">

### *function* QProgEdit.QEditor.setLang(lang=u'text')

Sets the editor language.

__Keywords:__

- `lang` -- A language, used to select a lexer for syntax highlighting, validation, cleaning, etc. if an appropriate lexer isn't found, no error is generated, but syntax highlighting is disabled. For a list of available lexers, refer to the QsciScintilla documentation.
	- Default: u'text'




</span>


[QProgEdit.QEditor.setLang]: #QProgEdit-QEditor-setLang
[QEditor.setLang]: #QProgEdit-QEditor-setLang
[setLang]: #QProgEdit-QEditor-setLang
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-setSymbolTree" markdown="1">

### *function* QProgEdit.QEditor.setSymbolTree(symbolTree, symbolTreeWidgetItemClass=<class 'QProgEdit._qsymboltreewidgetitem.QSymbolTreeWidgetItem'>)

Sets the symbol-tree widget.

__Arguments:__

- `symbolTree` -- A symbol-tree widget.
	- Type: QTreeWidgetItem

__Keywords:__

- `symbolTreeWidgetItemClass` -- The class to use for symbol-tree widgets. This should derive from QSymbolTreeWidgetItem.
	- Default: <class 'QProgEdit._qsymboltreewidgetitem.QSymbolTreeWidgetItem'>
	- Type: type




</span>


[QProgEdit.QEditor.setSymbolTree]: #QProgEdit-QEditor-setSymbolTree
[QEditor.setSymbolTree]: #QProgEdit-QEditor-setSymbolTree
[setSymbolTree]: #QProgEdit-QEditor-setSymbolTree
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-setText" markdown="1">

### *function* QProgEdit.QEditor.setText(text)

Sets the editor contents.

__Arguments:__

- `text` -- A text string. This can be a str object, which is assumed to be in utf-8 encoding, a Unicode object, or a QString.
	- Type: str, unicode, QString




</span>


[QProgEdit.QEditor.setText]: #QProgEdit-QEditor-setText
[QEditor.setText]: #QProgEdit-QEditor-setText
[setText]: #QProgEdit-QEditor-setText
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-text" markdown="1">

### *function* QProgEdit.QEditor.text()

Retrieves the editor contents.

__Returns:__

The editor contents.

- Type: unicode




</span>


[QProgEdit.QEditor.text]: #QProgEdit-QEditor-text
[QEditor.text]: #QProgEdit-QEditor-text
[text]: #QProgEdit-QEditor-text
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-uncommentSelection" markdown="1">

### *function* QProgEdit.QEditor.uncommentSelection()

Uncomments the currently selected text.




</span>


[QProgEdit.QEditor.uncommentSelection]: #QProgEdit-QEditor-uncommentSelection
[QEditor.uncommentSelection]: #QProgEdit-QEditor-uncommentSelection
[uncommentSelection]: #QProgEdit-QEditor-uncommentSelection
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-updateMarginWidth" markdown="1">

### *function* QProgEdit.QEditor.updateMarginWidth()

Updates the width of the margin containing the line numbers.




</span>


[QProgEdit.QEditor.updateMarginWidth]: #QProgEdit-QEditor-updateMarginWidth
[QEditor.updateMarginWidth]: #QProgEdit-QEditor-updateMarginWidth
[updateMarginWidth]: #QProgEdit-QEditor-updateMarginWidth
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-updateSymbolTree" markdown="1">

### *function* QProgEdit.QEditor.updateSymbolTree()

Updates the symbol tree, if any has been specified and a symbol parser is available for the langauage.




</span>


[QProgEdit.QEditor.updateSymbolTree]: #QProgEdit-QEditor-updateSymbolTree
[QEditor.updateSymbolTree]: #QProgEdit-QEditor-updateSymbolTree
[updateSymbolTree]: #QProgEdit-QEditor-updateSymbolTree
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-validate" markdown="1">

### *function* QProgEdit.QEditor.validate()

Validates the content.




</span>


[QProgEdit.QEditor.validate]: #QProgEdit-QEditor-validate
[QEditor.validate]: #QProgEdit-QEditor-validate
[validate]: #QProgEdit-QEditor-validate
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-wheelEvent" markdown="1">

### *function* QProgEdit.QEditor.wheelEvent(event)

Implements scroll-to-zoom functionality.

__Arguments:__

- `event` -- No description
	- Type: QWheelEvent




</span>


[QProgEdit.QEditor.wheelEvent]: #QProgEdit-QEditor-wheelEvent
[QEditor.wheelEvent]: #QProgEdit-QEditor-wheelEvent
[wheelEvent]: #QProgEdit-QEditor-wheelEvent


</span>


[QProgEdit.QEditor]: #QProgEdit-QEditor
[QEditor]: #QProgEdit-QEditor
<span class="ClassDoc YAMLDoc" id="QProgEdit-QEditorCfg" markdown="1">

## *class* QProgEdit.QEditorCfg

A non-persistent configuration object.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorCfg-__init__" markdown="1">

### *function* QProgEdit.QEditorCfg.\_\_init\_\_(parent=None)

Constructor.

__Keywords:__

- `parent` -- The parent widget.
	- Default: None
	- Type: QWidget, NoneType




</span>


[QProgEdit.QEditorCfg.__init__]: #QProgEdit-QEditorCfg-__init__
[QEditorCfg.__init__]: #QProgEdit-QEditorCfg-__init__
[__init__]: #QProgEdit-QEditorCfg-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorCfg-version" markdown="1">

### *function* QProgEdit.QEditorCfg.version()

Returns the config version.




</span>


[QProgEdit.QEditorCfg.version]: #QProgEdit-QEditorCfg-version
[QEditorCfg.version]: #QProgEdit-QEditorCfg-version
[version]: #QProgEdit-QEditorCfg-version


</span>


[QProgEdit.QEditorCfg]: #QProgEdit-QEditorCfg
[QEditorCfg]: #QProgEdit-QEditorCfg
<span class="ClassDoc YAMLDoc" id="QProgEdit-QEditorFind" markdown="1">

## *class* QProgEdit.QEditorFind

A find/ replace widget.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-__init__" markdown="1">

### *function* QProgEdit.QEditorFind.\_\_init\_\_(qProgEdit)

Constructor.

__Arguments:__

- `qProgEdit` -- The parent QProgEdit.
	- Type: QProgEdit




</span>


[QProgEdit.QEditorFind.__init__]: #QProgEdit-QEditorFind-__init__
[QEditorFind.__init__]: #QProgEdit-QEditorFind-__init__
[__init__]: #QProgEdit-QEditorFind-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-caseSensitive" markdown="1">

### *function* QProgEdit.QEditorFind.caseSensitive()

No description specified.

__Returns:__

True or False, depending on whether we should search case sensitive.

- Type: bool




</span>


[QProgEdit.QEditorFind.caseSensitive]: #QProgEdit-QEditorFind-caseSensitive
[QEditorFind.caseSensitive]: #QProgEdit-QEditorFind-caseSensitive
[caseSensitive]: #QProgEdit-QEditorFind-caseSensitive
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-find" markdown="1">

### *function* QProgEdit.QEditorFind.find()

Finds the current text in the document.

__Returns:__

True if matching text has been found, False otherwise.

- Type: bool




</span>


[QProgEdit.QEditorFind.find]: #QProgEdit-QEditorFind-find
[QEditorFind.find]: #QProgEdit-QEditorFind-find
[find]: #QProgEdit-QEditorFind-find
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-findText" markdown="1">

### *function* QProgEdit.QEditorFind.findText()

No description specified.

__Returns:__

The find text.

- Type: unicode




</span>


[QProgEdit.QEditorFind.findText]: #QProgEdit-QEditorFind-findText
[QEditorFind.findText]: #QProgEdit-QEditorFind-findText
[findText]: #QProgEdit-QEditorFind-findText
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-lock" markdown="1">

### *function* QProgEdit.QEditorFind.lock()

Locks the editor and find widget, so that we don't get into recursion problems during replace actions.




</span>


[QProgEdit.QEditorFind.lock]: #QProgEdit-QEditorFind-lock
[QEditorFind.lock]: #QProgEdit-QEditorFind-lock
[lock]: #QProgEdit-QEditorFind-lock
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-matchWhole" markdown="1">

### *function* QProgEdit.QEditorFind.matchWhole()

No description specified.

__Returns:__

True or False, depending on whether we should match whole words only.

- Type: bool




</span>


[QProgEdit.QEditorFind.matchWhole]: #QProgEdit-QEditorFind-matchWhole
[QEditorFind.matchWhole]: #QProgEdit-QEditorFind-matchWhole
[matchWhole]: #QProgEdit-QEditorFind-matchWhole
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-replace" markdown="1">

### *function* QProgEdit.QEditorFind.replace()

Replaces the first occurence in the document.

__Returns:__

True if text has been replaced, False otherwise.

- Type: bool




</span>


[QProgEdit.QEditorFind.replace]: #QProgEdit-QEditorFind-replace
[QEditorFind.replace]: #QProgEdit-QEditorFind-replace
[replace]: #QProgEdit-QEditorFind-replace
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-replaceAll" markdown="1">

### *function* QProgEdit.QEditorFind.replaceAll()

Replaces all occurences in the document.




</span>


[QProgEdit.QEditorFind.replaceAll]: #QProgEdit-QEditorFind-replaceAll
[QEditorFind.replaceAll]: #QProgEdit-QEditorFind-replaceAll
[replaceAll]: #QProgEdit-QEditorFind-replaceAll
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-replaceText" markdown="1">

### *function* QProgEdit.QEditorFind.replaceText()

No description specified.

__Returns:__

The replace text.

- Type: unicode




</span>


[QProgEdit.QEditorFind.replaceText]: #QProgEdit-QEditorFind-replaceText
[QEditorFind.replaceText]: #QProgEdit-QEditorFind-replaceText
[replaceText]: #QProgEdit-QEditorFind-replaceText
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-setFindText" markdown="1">

### *function* QProgEdit.QEditorFind.setFindText(txt=u'')

Sets the text of the find widget.

__Keywords:__

- `txt` -- The text to set.
	- Default: u''
	- Type: unicode




</span>


[QProgEdit.QEditorFind.setFindText]: #QProgEdit-QEditorFind-setFindText
[QEditorFind.setFindText]: #QProgEdit-QEditorFind-setFindText
[setFindText]: #QProgEdit-QEditorFind-setFindText
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-unlock" markdown="1">

### *function* QProgEdit.QEditorFind.unlock()

Unlocks the editor and find widget, to resume normal operations after replacing.




</span>


[QProgEdit.QEditorFind.unlock]: #QProgEdit-QEditorFind-unlock
[QEditorFind.unlock]: #QProgEdit-QEditorFind-unlock
[unlock]: #QProgEdit-QEditorFind-unlock
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-unshow" markdown="1">

### *function* QProgEdit.QEditorFind.unshow()

Hides the widget.




</span>


[QProgEdit.QEditorFind.unshow]: #QProgEdit-QEditorFind-unshow
[QEditorFind.unshow]: #QProgEdit-QEditorFind-unshow
[unshow]: #QProgEdit-QEditorFind-unshow


</span>


[QProgEdit.QEditorFind]: #QProgEdit-QEditorFind
[QEditorFind]: #QProgEdit-QEditorFind
<span class="ClassDoc YAMLDoc" id="QProgEdit-QEditorPrefs" markdown="1">

## *class* QProgEdit.QEditorPrefs

An editor preferences widget.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorPrefs-__init__" markdown="1">

### *function* QProgEdit.QEditorPrefs.\_\_init\_\_(qProgEdit)

Constructor.

__Arguments:__

- `qProgEdit` -- The parent QProgEdit.
	- Type: QProgEdit




</span>


[QProgEdit.QEditorPrefs.__init__]: #QProgEdit-QEditorPrefs-__init__
[QEditorPrefs.__init__]: #QProgEdit-QEditorPrefs-__init__
[__init__]: #QProgEdit-QEditorPrefs-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorPrefs-apply" markdown="1">

### *function* QProgEdit.QEditorPrefs.apply(dummy=None)

Applies the controls.

__Keywords:__

- `dummy` -- No description
	- Default: None




</span>


[QProgEdit.QEditorPrefs.apply]: #QProgEdit-QEditorPrefs-apply
[QEditorPrefs.apply]: #QProgEdit-QEditorPrefs-apply
[apply]: #QProgEdit-QEditorPrefs-apply
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorPrefs-refresh" markdown="1">

### *function* QProgEdit.QEditorPrefs.refresh()

Refreshes the controls.




</span>


[QProgEdit.QEditorPrefs.refresh]: #QProgEdit-QEditorPrefs-refresh
[QEditorPrefs.refresh]: #QProgEdit-QEditorPrefs-refresh
[refresh]: #QProgEdit-QEditorPrefs-refresh


</span>


[QProgEdit.QEditorPrefs]: #QProgEdit-QEditorPrefs
[QEditorPrefs]: #QProgEdit-QEditorPrefs
<span class="ClassDoc YAMLDoc" id="QProgEdit-QEditorStatus" markdown="1">

## *class* QProgEdit.QEditorStatus

A simple widget that indicates the editor status, which currently corresponds only to the cursor position.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorStatus-__init__" markdown="1">

### *function* QProgEdit.QEditorStatus.\_\_init\_\_(qProgEdit)

Constructor.

__Arguments:__

- `qProgEdit` -- The parent QProgEdit.
	- Type: QProgEdit




</span>


[QProgEdit.QEditorStatus.__init__]: #QProgEdit-QEditorStatus-__init__
[QEditorStatus.__init__]: #QProgEdit-QEditorStatus-__init__
[__init__]: #QProgEdit-QEditorStatus-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorStatus-updateCursorPos" markdown="1">

### *function* QProgEdit.QEditorStatus.updateCursorPos(index=0, line=0)

Updates the cursor position.

__Keywords:__

- `index` -- The column number.
	- Default: 0
	- Type: int
- `line` -- The line number.
	- Default: 0
	- Type: int




</span>


[QProgEdit.QEditorStatus.updateCursorPos]: #QProgEdit-QEditorStatus-updateCursorPos
[QEditorStatus.updateCursorPos]: #QProgEdit-QEditorStatus-updateCursorPos
[updateCursorPos]: #QProgEdit-QEditorStatus-updateCursorPos


</span>


[QProgEdit.QEditorStatus]: #QProgEdit-QEditorStatus
[QEditorStatus]: #QProgEdit-QEditorStatus
<span class="ClassDoc YAMLDoc" id="QProgEdit-QLangMenu" markdown="1">

## *class* QProgEdit.QLangMenu

The language selection menu.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QLangMenu-__init__" markdown="1">

### *function* QProgEdit.QLangMenu.\_\_init\_\_(tabCornerWidget)

Constructor.

__Arguments:__

- `tabCornerWidget` -- The parent QTabCornerWidget.
	- Type: QTabCornerWidget




</span>


[QProgEdit.QLangMenu.__init__]: #QProgEdit-QLangMenu-__init__
[QLangMenu.__init__]: #QProgEdit-QLangMenu-__init__
[__init__]: #QProgEdit-QLangMenu-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QLangMenu-setLang" markdown="1">

### *function* QProgEdit.QLangMenu.setLang(action)

Select a new language for the selected tab.

__Arguments:__

- `action` -- No description
	- Type: QAction




</span>


[QProgEdit.QLangMenu.setLang]: #QProgEdit-QLangMenu-setLang
[QLangMenu.setLang]: #QProgEdit-QLangMenu-setLang
[setLang]: #QProgEdit-QLangMenu-setLang


</span>


[QProgEdit.QLangMenu]: #QProgEdit-QLangMenu
[QLangMenu]: #QProgEdit-QLangMenu
<span class="ClassDoc YAMLDoc" id="QProgEdit-QLexer" markdown="1">

## *class* QProgEdit.QLexer

A themeable wrapper around the standard Lexer system.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QLexer-__init__" markdown="1">

### *function* QProgEdit.QLexer.\_\_init\_\_(editor, lang=u'text', colorScheme=u'Default')

Constructor.

__Arguments:__

- `editor` -- The parent QEditor.
	- Type: QEditor

__Keywords:__

- `lang` -- The language.
	- Default: u'text'
	- Type: unicode
- `colorScheme` -- The color scheme.
	- Default: u'Default'
	- Type: unicode




</span>


[QProgEdit.QLexer.__init__]: #QProgEdit-QLexer-__init__
[QLexer.__init__]: #QProgEdit-QLexer-__init__
[__init__]: #QProgEdit-QLexer-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QLexer-description" markdown="1">

### *function* QProgEdit.QLexer.description(style)

Gives a style description for the generic Lexer.

__Arguments:__

- `style` -- The style number.
	- Type: int

__Returns:__

The 'Default' QString for style 0 and empty QStrings for all other styles.

- Type: QString




</span>


[QProgEdit.QLexer.description]: #QProgEdit-QLexer-description
[QLexer.description]: #QProgEdit-QLexer-description
[description]: #QProgEdit-QLexer-description


</span>


[QProgEdit.QLexer]: #QProgEdit-QLexer
[QLexer]: #QProgEdit-QLexer
<span class="ClassDoc YAMLDoc" id="QProgEdit-QProgEdit" markdown="1">

## *class* QProgEdit.QProgEdit

A single editor window, with preferences widget and search functionality.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-__init__" markdown="1">

### *function* QProgEdit.QProgEdit.\_\_init\_\_(tabManager, title=u'Empty document', dPrint=None, \*\*editorParams)

Constructor.

__Arguments:__

- `tabManager` -- A tab manager.
	- Type: QTabManager

__Keywords:__

- `dPrint` -- A function to be used for debug printing. Should accept a single parameter, which is the debug message. If no debug function is specified, the standard output is used.
	- Default: None
- `title` -- A title for the document.
	- Default: u'Empty document'

__Keyword dict:__

- `**editorParams`: A dictionary with keywords to be passed to QEditor.




</span>


[QProgEdit.QProgEdit.__init__]: #QProgEdit-QProgEdit-__init__
[QProgEdit.__init__]: #QProgEdit-QProgEdit-__init__
[__init__]: #QProgEdit-QProgEdit-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-dPrint" markdown="1">

### *function* QProgEdit.QProgEdit.dPrint(msg)

Prints a debug message.

__Arguments:__

- `msg` -- A debug message.
	- Type: unicode, str




</span>


[QProgEdit.QProgEdit.dPrint]: #QProgEdit-QProgEdit-dPrint
[QProgEdit.dPrint]: #QProgEdit-QProgEdit-dPrint
[dPrint]: #QProgEdit-QProgEdit-dPrint
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-focusTab" markdown="1">

### *function* QProgEdit.QProgEdit.focusTab()

Focuses the current tab.




</span>


[QProgEdit.QProgEdit.focusTab]: #QProgEdit-QProgEdit-focusTab
[QProgEdit.focusTab]: #QProgEdit-QProgEdit-focusTab
[focusTab]: #QProgEdit-QProgEdit-focusTab
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-tabIndex" markdown="1">

### *function* QProgEdit.QProgEdit.tabIndex()

Gets the index of the current tab.

__Returns:__

The tab index.

- Type: int




</span>


[QProgEdit.QProgEdit.tabIndex]: #QProgEdit-QProgEdit-tabIndex
[QProgEdit.tabIndex]: #QProgEdit-QProgEdit-tabIndex
[tabIndex]: #QProgEdit-QProgEdit-tabIndex
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-toggle" markdown="1">

### *function* QProgEdit.QProgEdit.toggle(widget, visible)

Toggles the visibility of a widget with a smooth animation.

__Arguments:__

- `visible` -- A boolean indicating the visibility of the widget.
- `widget` -- A QWidget.




</span>


[QProgEdit.QProgEdit.toggle]: #QProgEdit-QProgEdit-toggle
[QProgEdit.toggle]: #QProgEdit-QProgEdit-toggle
[toggle]: #QProgEdit-QProgEdit-toggle
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-toggleFind" markdown="1">

### *function* QProgEdit.QProgEdit.toggleFind(visible)

Toggles the visibility of the find widget.

__Arguments:__

- `visible` -- A boolean indicating the visibility of the widget.




</span>


[QProgEdit.QProgEdit.toggleFind]: #QProgEdit-QProgEdit-toggleFind
[QProgEdit.toggleFind]: #QProgEdit-QProgEdit-toggleFind
[toggleFind]: #QProgEdit-QProgEdit-toggleFind
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-togglePrefs" markdown="1">

### *function* QProgEdit.QProgEdit.togglePrefs(visible)

Toggles the visibility of the preferences widget

__Arguments:__

- `visible` -- A boolean indicating the visibility of the widget.




</span>


[QProgEdit.QProgEdit.togglePrefs]: #QProgEdit-QProgEdit-togglePrefs
[QProgEdit.togglePrefs]: #QProgEdit-QProgEdit-togglePrefs
[togglePrefs]: #QProgEdit-QProgEdit-togglePrefs


</span>


[QProgEdit.QProgEdit]: #QProgEdit-QProgEdit
[QProgEdit]: #QProgEdit-QProgEdit
<span class="ClassDoc YAMLDoc" id="QProgEdit-QSymbolTreeWidgetItem" markdown="1">

## *class* QProgEdit.QSymbolTreeWidgetItem

A symbol-tree widget item to use for symbol overviews.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QSymbolTreeWidgetItem-__init__" markdown="1">

### *function* QProgEdit.QSymbolTreeWidgetItem.\_\_init\_\_(editor, lineNo, _type, name, argSpec)

Constructor.

__Arguments:__

- `argSpec` -- The symbol's argument specification.
	- Type: unicode
- `lineNo` -- A line number.
	- Type: int
- `_type` -- The symbol type, such as 'class' or 'def'
	- Type: unicode
- `name` -- The symbol name
	- Type: unicode
- `editor` -- The editor widget.
	- Type: QEditor




</span>


[QProgEdit.QSymbolTreeWidgetItem.__init__]: #QProgEdit-QSymbolTreeWidgetItem-__init__
[QSymbolTreeWidgetItem.__init__]: #QProgEdit-QSymbolTreeWidgetItem-__init__
[__init__]: #QProgEdit-QSymbolTreeWidgetItem-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QSymbolTreeWidgetItem-activated" markdown="1">

### *function* QProgEdit.QSymbolTreeWidgetItem.activated()

Is called when the symbol is activated, to focus the symbol in the editor.




</span>


[QProgEdit.QSymbolTreeWidgetItem.activated]: #QProgEdit-QSymbolTreeWidgetItem-activated
[QSymbolTreeWidgetItem.activated]: #QProgEdit-QSymbolTreeWidgetItem-activated
[activated]: #QProgEdit-QSymbolTreeWidgetItem-activated


</span>


[QProgEdit.QSymbolTreeWidgetItem]: #QProgEdit-QSymbolTreeWidgetItem
[QSymbolTreeWidgetItem]: #QProgEdit-QSymbolTreeWidgetItem
<span class="ClassDoc YAMLDoc" id="QProgEdit-QTabCornerWidget" markdown="1">

## *class* QProgEdit.QTabCornerWidget

Contains a number of buttons that are displayed in the tab bar.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabCornerWidget-__init__" markdown="1">

### *function* QProgEdit.QTabCornerWidget.\_\_init\_\_(tabManager, msg=None, handlerButtonText=None)

Constructor.

__Arguments:__

- `tabManager` -- A tab manager.
	- Type: QTabManager

__Keywords:__

- `msg` -- An informative text message.
	- Default: None
	- Type: str, unicode, NoneType
- `handlerButtonText` -- Text for a top-right button, which can be clicked to call the handler, or None for no button.
	- Default: None
	- Type: str, unicode, NoneType




</span>


[QProgEdit.QTabCornerWidget.__init__]: #QProgEdit-QTabCornerWidget-__init__
[QTabCornerWidget.__init__]: #QProgEdit-QTabCornerWidget-__init__
[__init__]: #QProgEdit-QTabCornerWidget-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabCornerWidget-handlerButtonClicked" markdown="1">

### *function* QProgEdit.QTabCornerWidget.handlerButtonClicked()

Is called when the handler button is clicked and emits the relevant signals.




</span>


[QProgEdit.QTabCornerWidget.handlerButtonClicked]: #QProgEdit-QTabCornerWidget-handlerButtonClicked
[QTabCornerWidget.handlerButtonClicked]: #QProgEdit-QTabCornerWidget-handlerButtonClicked
[handlerButtonClicked]: #QProgEdit-QTabCornerWidget-handlerButtonClicked
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabCornerWidget-update" markdown="1">

### *function* QProgEdit.QTabCornerWidget.update()

Updates widget to reflect document contents.




</span>


[QProgEdit.QTabCornerWidget.update]: #QProgEdit-QTabCornerWidget-update
[QTabCornerWidget.update]: #QProgEdit-QTabCornerWidget-update
[update]: #QProgEdit-QTabCornerWidget-update


</span>


[QProgEdit.QTabCornerWidget]: #QProgEdit-QTabCornerWidget
[QTabCornerWidget]: #QProgEdit-QTabCornerWidget
<span class="ClassDoc YAMLDoc" id="QProgEdit-QTabManager" markdown="1">

## *class* QProgEdit.QTabManager

A tab manager that contains multiple QProgEdit tabs.


<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-__init__" markdown="1">

### *function* QProgEdit.QTabManager.\_\_init\_\_(tabsClosable=False, handlerButtonText=None, parent=None, cfg=<QProgEdit._qeditorcfg.QEditorCfg object at 0x7ff383e0ac30>, msg=None, tabsMovable=False)

Constructor.

__Keywords:__

- `tabsClosable` -- Indicates whether a close button should be shown on tabs.
	- Default: False
	- Type: bool
- `handlerButtonText` -- Text for a top-right button, which can be clicked to call the handler, or None for no button.
	- Default: None
	- Type: str, unicode, NoneType
- `parent` -- The parent widget.
	- Default: None
	- Type: QWidget
- `msg` -- An informative message for the corner widget.
	- Default: None
	- Type: str, unicode, NoneType
- `cfg` -- A configuration backend. By default QEditorCfg is used. Custom backends must have the same API for getting and setting options.
	- Default: <QProgEdit._qeditorcfg.QEditorCfg object at 0x7ff383e0ac30>
- `tabsMovable` -- Indicates whether tabs can be re-ordered.
	- Default: False
	- Type: bool




</span>


[QProgEdit.QTabManager.__init__]: #QProgEdit-QTabManager-__init__
[QTabManager.__init__]: #QProgEdit-QTabManager-__init__
[__init__]: #QProgEdit-QTabManager-__init__
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-addTab" markdown="1">

### *function* QProgEdit.QTabManager.addTab(select=True, title=u'Empty document')

Adds an empty document tab.

__Keywords:__

- `select` -- Indicates whether the newly created tab should be selected.
	- Default: True
	- Type: bool
- `title` -- A tab title.
	- Default: u'Empty document'
	- Type: unicode, str




</span>


[QProgEdit.QTabManager.addTab]: #QProgEdit-QTabManager-addTab
[QTabManager.addTab]: #QProgEdit-QTabManager-addTab
[addTab]: #QProgEdit-QTabManager-addTab
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-applyCfg" markdown="1">

### *function* QProgEdit.QTabManager.applyCfg()

Applies the configuration.




</span>


[QProgEdit.QTabManager.applyCfg]: #QProgEdit-QTabManager-applyCfg
[QTabManager.applyCfg]: #QProgEdit-QTabManager-applyCfg
[applyCfg]: #QProgEdit-QTabManager-applyCfg
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-closeTab" markdown="1">

### *function* QProgEdit.QTabManager.closeTab(index=None)

Closes a tab.

__Keywords:__

- `index` -- A tab index (see [tabIndex]).
	- Default: None




</span>


[QProgEdit.QTabManager.closeTab]: #QProgEdit-QTabManager-closeTab
[QTabManager.closeTab]: #QProgEdit-QTabManager-closeTab
[closeTab]: #QProgEdit-QTabManager-closeTab
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-isAnyModified" markdown="1">

### *function* QProgEdit.QTabManager.isAnyModified()

Checks if one or more of the tabs have been modified.

__Returns:__

True if (one of) the tab(s) is modified, False otherwise.

- Type: bool




</span>


[QProgEdit.QTabManager.isAnyModified]: #QProgEdit-QTabManager-isAnyModified
[QTabManager.isAnyModified]: #QProgEdit-QTabManager-isAnyModified
[isAnyModified]: #QProgEdit-QTabManager-isAnyModified
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-switchTabLeft" markdown="1">

### *function* QProgEdit.QTabManager.switchTabLeft()

Switches to the tab on the left.




</span>


[QProgEdit.QTabManager.switchTabLeft]: #QProgEdit-QTabManager-switchTabLeft
[QTabManager.switchTabLeft]: #QProgEdit-QTabManager-switchTabLeft
[switchTabLeft]: #QProgEdit-QTabManager-switchTabLeft
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-switchTabRight" markdown="1">

### *function* QProgEdit.QTabManager.switchTabRight()

Switches to the tab on the left.




</span>


[QProgEdit.QTabManager.switchTabRight]: #QProgEdit-QTabManager-switchTabRight
[QTabManager.switchTabRight]: #QProgEdit-QTabManager-switchTabRight
[switchTabRight]: #QProgEdit-QTabManager-switchTabRight
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-tab" markdown="1">

### *function* QProgEdit.QTabManager.tab(index=None)

Returns the QProgEdit instance for a given tab.

__Keywords:__

- `index` -- Specifies the tab, either by a name (i.e. the name on a tab), an index, or None to get the current tab.
	- Default: None
	- Type: int, str, unicode, NoneType

__Returns:__

A tab, or None if no matching tab was found.

- Type: QProgEdit, NoneType




</span>


[QProgEdit.QTabManager.tab]: #QProgEdit-QTabManager-tab
[QTabManager.tab]: #QProgEdit-QTabManager-tab
[tab]: #QProgEdit-QTabManager-tab
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-tabChanged" markdown="1">

### *function* QProgEdit.QTabManager.tabChanged(index)

Is called when the current tab must be updated, for example because a new tab is selected.

__Arguments:__

- `index` -- The index of the newly selected tab.
	- Type: int




</span>


[QProgEdit.QTabManager.tabChanged]: #QProgEdit-QTabManager-tabChanged
[QTabManager.tabChanged]: #QProgEdit-QTabManager-tabChanged
[tabChanged]: #QProgEdit-QTabManager-tabChanged
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-tabIndex" markdown="1">

### *function* QProgEdit.QTabManager.tabIndex(index=None)

Returns the index for a given tab.

__Keywords:__

- `index` -- Specifies the tab, either by a name (i.e. the name on a tab), an index, or None to get the current tab.
	- Default: None
	- Type: int, str, unicode, NoneType

__Returns:__

A tab index, or None if no matching tab was found.

- Type: int, NoneType




</span>


[QProgEdit.QTabManager.tabIndex]: #QProgEdit-QTabManager-tabIndex
[QTabManager.tabIndex]: #QProgEdit-QTabManager-tabIndex
[tabIndex]: #QProgEdit-QTabManager-tabIndex
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-tabs" markdown="1">

### *function* QProgEdit.QTabManager.tabs()

Gets all tabs.

__Returns:__

A list of all tab widgets.

- Type: list




</span>


[QProgEdit.QTabManager.tabs]: #QProgEdit-QTabManager-tabs
[QTabManager.tabs]: #QProgEdit-QTabManager-tabs
[tabs]: #QProgEdit-QTabManager-tabs
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-toggleFind" markdown="1">

### *function* QProgEdit.QTabManager.toggleFind(visible)

Toggle the visibility of the find widget.

__Arguments:__

- `visible` -- Visibility status.
	- Type: bool




</span>


[QProgEdit.QTabManager.toggleFind]: #QProgEdit-QTabManager-toggleFind
[QTabManager.toggleFind]: #QProgEdit-QTabManager-toggleFind
[toggleFind]: #QProgEdit-QTabManager-toggleFind
<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-togglePrefs" markdown="1">

### *function* QProgEdit.QTabManager.togglePrefs(visible)

Toggle the visibility of the preferences widget.

__Arguments:__

- `visible` -- Visibility status.
	- Type: bool




</span>


[QProgEdit.QTabManager.togglePrefs]: #QProgEdit-QTabManager-togglePrefs
[QTabManager.togglePrefs]: #QProgEdit-QTabManager-togglePrefs
[togglePrefs]: #QProgEdit-QTabManager-togglePrefs


</span>


[QProgEdit.QTabManager]: #QProgEdit-QTabManager
[QTabManager]: #QProgEdit-QTabManager
<span class="ModuleDoc YAMLDoc" id="QProgEdit-py3" markdown="1">

## *module* QProgEdit.py3

This modules defines some built-ins that are not available in Python 3, but are assumed to exist by QProgEdit.




</span>


[QProgEdit.py3]: #QProgEdit-py3
[py3]: #QProgEdit-py3


</span>


[QProgEdit]: #QProgEdit

[Overview]: #overview
[Dependencies]: #dependencies
[Example]: #example
[*class* QProgEdit.QEditor]: #class-qprogeditqeditor
[*class* QProgEdit.QEditorCfg]: #class-qprogeditqeditorcfg
[*class* QProgEdit.QEditorFind]: #class-qprogeditqeditorfind
[*class* QProgEdit.QEditorPrefs]: #class-qprogeditqeditorprefs
[*class* QProgEdit.QEditorStatus]: #class-qprogeditqeditorstatus
[*class* QProgEdit.QLangMenu]: #class-qprogeditqlangmenu
[*class* QProgEdit.QLexer]: #class-qprogeditqlexer
[*class* QProgEdit.QProgEdit]: #class-qprogeditqprogedit
[*class* QProgEdit.QSymbolTreeWidgetItem]: #class-qprogeditqsymboltreewidgetitem
[*class* QProgEdit.QTabCornerWidget]: #class-qprogeditqtabcornerwidget
[*class* QProgEdit.QTabManager]: #class-qprogeditqtabmanager
[*module* QProgEdit.py3]: #module-qprogeditpy3