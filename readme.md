<span class="ModuleDoc YAMLDoc" id="QProgEdit" markdown="1">

# *module* QProgEdit

# QProgEdit

v3.0.0~pre2


QProgEdit is a PyQt4 widget that implements a full-featured text editor
component. It's primary target at the moment is
[OpenSesame](http://osdoc.cogsci.nl), a graphical experiment builder.

Copyright (2013-2015) Sebastiaan Mathôt

<http://www.cogsci.nl/smathot>

## Overview


- [Dependencies](#dependencies)
- [Example](#example)
- [class __QProgEdit.QEditor__](#class-__qprogeditqeditor__)
	- [function __QProgEdit\.QEditor\.\_\_init\_\___\(qProgEdit\)](#function-__qprogeditqeditor__init____qprogedit)
	- [function __QProgEdit\.QEditor\.applyCfg__\(\)](#function-__qprogeditqeditorapplycfg__)
	- [function __QProgEdit\.QEditor\.commentSelection__\(\)](#function-__qprogeditqeditorcommentselection__)
	- [function __QProgEdit\.QEditor\.cursorMoved__\(\)](#function-__qprogeditqeditorcursormoved__)
	- [function __QProgEdit\.QEditor\.focusInEvent__\(e\)](#function-__qprogeditqeditorfocusinevent__e)
	- [function __QProgEdit\.QEditor\.focusOutEvent__\(e\)](#function-__qprogeditqeditorfocusoutevent__e)
	- [function __QProgEdit\.QEditor\.highlightSelection__\(\)](#function-__qprogeditqeditorhighlightselection__)
	- [function __QProgEdit\.QEditor\.keyPressEvent__\(event\)](#function-__qprogeditqeditorkeypressevent__event)
	- [function __QProgEdit\.QEditor\.lang__\(\)](#function-__qprogeditqeditorlang__)
	- [function __QProgEdit\.QEditor\.onMarginClick__\(margin, line, state\)](#function-__qprogeditqeditoronmarginclick__margin-line-state)
	- [function __QProgEdit\.QEditor\.paste__\(\)](#function-__qprogeditqeditorpaste__)
	- [function __QProgEdit\.QEditor\.selectedText__\(currentLineFallback=False\)](#function-__qprogeditqeditorselectedtext__currentlinefallbackfalse)
	- [function __QProgEdit\.QEditor\.setKeyBindings__\(\)](#function-__qprogeditqeditorsetkeybindings__)
	- [function __QProgEdit\.QEditor\.setLang__\(lang=u'text'\)](#function-__qprogeditqeditorsetlang__langutext)
	- [function __QProgEdit\.QEditor\.setSymbolTree__\(symbolTree, symbolTreeWidgetItemClass=<class 'QProgEdit\.\_qsymboltreewidgetitem\.QSymbolTreeWidgetItem'>\)](#function-__qprogeditqeditorsetsymboltree__symboltree-symboltreewidgetitemclassclass-qprogedit_qsymboltreewidgetitemqsymboltreewidgetitem)
	- [function __QProgEdit\.QEditor\.setText__\(text\)](#function-__qprogeditqeditorsettext__text)
	- [function __QProgEdit\.QEditor\.symbols__\(\)](#function-__qprogeditqeditorsymbols__)
	- [function __QProgEdit\.QEditor\.text__\(\)](#function-__qprogeditqeditortext__)
	- [function __QProgEdit\.QEditor\.uncommentSelection__\(\)](#function-__qprogeditqeditoruncommentselection__)
	- [function __QProgEdit\.QEditor\.updateMarginWidth__\(\)](#function-__qprogeditqeditorupdatemarginwidth__)
	- [function __QProgEdit\.QEditor\.updateSymbolTree__\(\)](#function-__qprogeditqeditorupdatesymboltree__)
	- [function __QProgEdit\.QEditor\.validate__\(\)](#function-__qprogeditqeditorvalidate__)
	- [function __QProgEdit\.QEditor\.wheelEvent__\(event\)](#function-__qprogeditqeditorwheelevent__event)
- [class __QProgEdit.QEditorCfg__](#class-__qprogeditqeditorcfg__)
	- [function __QProgEdit\.QEditorCfg\.\_\_init\_\___\(parent=None\)](#function-__qprogeditqeditorcfg__init____parentnone)
	- [function __QProgEdit\.QEditorCfg\.version__\(\)](#function-__qprogeditqeditorcfgversion__)
- [class __QProgEdit.QEditorFind__](#class-__qprogeditqeditorfind__)
	- [function __QProgEdit\.QEditorFind\.\_\_init\_\___\(qProgEdit\)](#function-__qprogeditqeditorfind__init____qprogedit)
	- [function __QProgEdit\.QEditorFind\.caseSensitive__\(\)](#function-__qprogeditqeditorfindcasesensitive__)
	- [function __QProgEdit\.QEditorFind\.find__\(\)](#function-__qprogeditqeditorfindfind__)
	- [function __QProgEdit\.QEditorFind\.findText__\(\)](#function-__qprogeditqeditorfindfindtext__)
	- [function __QProgEdit\.QEditorFind\.loadUi__\(name\)](#function-__qprogeditqeditorfindloadui__name)
	- [function __QProgEdit\.QEditorFind\.lock__\(\)](#function-__qprogeditqeditorfindlock__)
	- [function __QProgEdit\.QEditorFind\.matchWhole__\(\)](#function-__qprogeditqeditorfindmatchwhole__)
	- [function __QProgEdit\.QEditorFind\.replace__\(\)](#function-__qprogeditqeditorfindreplace__)
	- [function __QProgEdit\.QEditorFind\.replaceAll__\(\)](#function-__qprogeditqeditorfindreplaceall__)
	- [function __QProgEdit\.QEditorFind\.replaceText__\(\)](#function-__qprogeditqeditorfindreplacetext__)
	- [function __QProgEdit\.QEditorFind\.setFindText__\(txt=u''\)](#function-__qprogeditqeditorfindsetfindtext__txtu)
	- [function __QProgEdit\.QEditorFind\.unlock__\(\)](#function-__qprogeditqeditorfindunlock__)
	- [function __QProgEdit\.QEditorFind\.unshow__\(\)](#function-__qprogeditqeditorfindunshow__)
- [class __QProgEdit.QEditorPrefs__](#class-__qprogeditqeditorprefs__)
	- [function __QProgEdit\.QEditorPrefs\.\_\_init\_\___\(qProgEdit\)](#function-__qprogeditqeditorprefs__init____qprogedit)
	- [function __QProgEdit\.QEditorPrefs\.apply__\(dummy=None\)](#function-__qprogeditqeditorprefsapply__dummynone)
	- [function __QProgEdit\.QEditorPrefs\.loadUi__\(name\)](#function-__qprogeditqeditorprefsloadui__name)
	- [function __QProgEdit\.QEditorPrefs\.refresh__\(\)](#function-__qprogeditqeditorprefsrefresh__)
- [class __QProgEdit.QEditorStatus__](#class-__qprogeditqeditorstatus__)
	- [function __QProgEdit\.QEditorStatus\.\_\_init\_\___\(qProgEdit\)](#function-__qprogeditqeditorstatus__init____qprogedit)
	- [function __QProgEdit\.QEditorStatus\.updateCursorPos__\(line=0, index=0\)](#function-__qprogeditqeditorstatusupdatecursorpos__line0-index0)
- [class __QProgEdit.QLangMenu__](#class-__qprogeditqlangmenu__)
	- [function __QProgEdit\.QLangMenu\.\_\_init\_\___\(tabCornerWidget\)](#function-__qprogeditqlangmenu__init____tabcornerwidget)
	- [function __QProgEdit\.QLangMenu\.setLang__\(action\)](#function-__qprogeditqlangmenusetlang__action)
- [function __QProgEdit\.QLexer__\(editor, lang=u'text', colorScheme=u'Default'\)](#function-__qprogeditqlexer__editor-langutext-colorschemeudefault)
- [class __QProgEdit.QProgEdit__](#class-__qprogeditqprogedit__)
	- [function __QProgEdit\.QProgEdit\.\_\_init\_\___\(tabManager, dPrint=None, title=u'Empty document', \*\*editorParams\)](#function-__qprogeditqprogedit__init____tabmanager-dprintnone-titleuempty-document-editorparams)
	- [function __QProgEdit\.QProgEdit\.dPrint__\(msg\)](#function-__qprogeditqprogeditdprint__msg)
	- [function __QProgEdit\.QProgEdit\.focusTab__\(\)](#function-__qprogeditqprogeditfocustab__)
	- [function __QProgEdit\.QProgEdit\.tabIndex__\(\)](#function-__qprogeditqprogedittabindex__)
	- [function __QProgEdit\.QProgEdit\.toggle__\(widget, visible\)](#function-__qprogeditqprogedittoggle__widget-visible)
	- [function __QProgEdit\.QProgEdit\.toggleFind__\(visible\)](#function-__qprogeditqprogedittogglefind__visible)
	- [function __QProgEdit\.QProgEdit\.togglePrefs__\(visible\)](#function-__qprogeditqprogedittoggleprefs__visible)
- [class __QProgEdit.QSymbolTreeWidgetItem__](#class-__qprogeditqsymboltreewidgetitem__)
	- [function __QProgEdit\.QSymbolTreeWidgetItem\.\_\_init\_\___\(editor, lineNo, \_type, name, argSpec\)](#function-__qprogeditqsymboltreewidgetitem__init____editor-lineno-_type-name-argspec)
	- [function __QProgEdit\.QSymbolTreeWidgetItem\.activate__\(\)](#function-__qprogeditqsymboltreewidgetitemactivate__)
- [class __QProgEdit.QTabCornerWidget__](#class-__qprogeditqtabcornerwidget__)
	- [function __QProgEdit\.QTabCornerWidget\.\_\_init\_\___\(tabManager, msg=None, handlerButtonText=None, runButton=False\)](#function-__qprogeditqtabcornerwidget__init____tabmanager-msgnone-handlerbuttontextnone-runbuttonfalse)
	- [function __QProgEdit\.QTabCornerWidget\.handlerButtonClicked__\(\)](#function-__qprogeditqtabcornerwidgethandlerbuttonclicked__)
	- [function __QProgEdit\.QTabCornerWidget\.update__\(\)](#function-__qprogeditqtabcornerwidgetupdate__)
- [class __QProgEdit.QTabManager__](#class-__qprogeditqtabmanager__)
	- [function __QProgEdit\.QTabManager\.\_\_init\_\___\(parent=None, cfg=<QProgEdit\.\_qeditorcfg\.QEditorCfg object at 0x7f73885d59d0>, tabsClosable=False, tabsMovable=False, msg=None, handlerButtonText=None, runButton=False\)](#function-__qprogeditqtabmanager__init____parentnone-cfgqprogedit_qeditorcfgqeditorcfg-object-at-0x7f73885d59d0-tabsclosablefalse-tabsmovablefalse-msgnone-handlerbuttontextnone-runbuttonfalse)
	- [function __QProgEdit\.QTabManager\.addTab__\(title=u'Empty document', select=True\)](#function-__qprogeditqtabmanageraddtab__titleuempty-document-selecttrue)
	- [function __QProgEdit\.QTabManager\.applyCfg__\(\)](#function-__qprogeditqtabmanagerapplycfg__)
	- [function __QProgEdit\.QTabManager\.closeTab__\(index=None\)](#function-__qprogeditqtabmanagerclosetab__indexnone)
	- [function __QProgEdit\.QTabManager\.isAnyModified__\(\)](#function-__qprogeditqtabmanagerisanymodified__)
	- [function __QProgEdit\.QTabManager\.runSelectedText__\(\)](#function-__qprogeditqtabmanagerrunselectedtext__)
	- [function __QProgEdit\.QTabManager\.runText__\(\)](#function-__qprogeditqtabmanagerruntext__)
	- [function __QProgEdit\.QTabManager\.selectTab__\(index\)](#function-__qprogeditqtabmanagerselecttab__index)
	- [function __QProgEdit\.QTabManager\.selectedText__\(index=None, currentLineFallback=False\)](#function-__qprogeditqtabmanagerselectedtext__indexnone-currentlinefallbackfalse)
	- [function __QProgEdit\.QTabManager\.setFocus__\(index=None\)](#function-__qprogeditqtabmanagersetfocus__indexnone)
	- [function __QProgEdit\.QTabManager\.setText__\(text, index=None\)](#function-__qprogeditqtabmanagersettext__text-indexnone)
	- [function __QProgEdit\.QTabManager\.switchTabLeft__\(\)](#function-__qprogeditqtabmanagerswitchtableft__)
	- [function __QProgEdit\.QTabManager\.switchTabRight__\(\)](#function-__qprogeditqtabmanagerswitchtabright__)
	- [function __QProgEdit\.QTabManager\.tab__\(index=None\)](#function-__qprogeditqtabmanagertab__indexnone)
	- [function __QProgEdit\.QTabManager\.tabChanged__\(index\)](#function-__qprogeditqtabmanagertabchanged__index)
	- [function __QProgEdit\.QTabManager\.tabIndex__\(index=None\)](#function-__qprogeditqtabmanagertabindex__indexnone)
	- [function __QProgEdit\.QTabManager\.tabs__\(\)](#function-__qprogeditqtabmanagertabs__)
	- [function __QProgEdit\.QTabManager\.text__\(index=None\)](#function-__qprogeditqtabmanagertext__indexnone)
	- [function __QProgEdit\.QTabManager\.toggleFind__\(visible\)](#function-__qprogeditqtabmanagertogglefind__visible)
	- [function __QProgEdit\.QTabManager\.togglePrefs__\(visible\)](#function-__qprogeditqtabmanagertoggleprefs__visible)
- [class __QProgEdit.QUiLoader__](#class-__qprogeditquiloader__)
	- [function __QProgEdit\.QUiLoader\.loadUi__\(name\)](#function-__qprogeditquiloaderloadui__name)



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

import os
import sys
from QProgEdit.qt import QtGui, QtCore
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

	if hasattr(treeWidgetItem, u'activate'):
		treeWidgetItem.activate()

def runSelectedText(s):

	print('run:\n%s' % s)

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

	tabManager = QTabManager(handlerButtonText=u'apply', runButton=True)
	tabManager.setWindowIcon(QtGui.QIcon.fromTheme(u'accessories-text-editor'))
	tabManager.setWindowTitle(u'QProgEdit')
	tabManager.resize(800, 600)

	tabManager.cursorRowChanged.connect(cursorRowChanged)
	tabManager.focusLost.connect(focusLost)
	tabManager.focusReceived.connect(focusReceived)
	tabManager.handlerButtonClicked.connect(handlerButtonClicked)
	tabManager.execute.connect(runSelectedText)

	tab = tabManager.addTab(u'Tab 1')
	tab.setLang(u'Python')
	tab.setSymbolTree(treeWidgetItem1)
	tab.setText(open(__file__).read())

	tab = tabManager.addTab(u'Tab 2')
	tab.setText(u'Some plain text')

	tab = tabManager.addTab(u'Tab 3')
	tab.setLang(u'Python')
	tab.setSymbolTree(treeWidgetItem3)
	if os.path.exists(u'content.txt'):
		tab.setText(open(u'content.txt').read())

	layout = QtGui.QHBoxLayout()
	layout.addWidget(symbolTree)
	layout.addWidget(tabManager)
	container = QtGui.QWidget()
	container.setLayout(layout)
	container.show()

	res = app.exec_()
	open(u'content.txt', u'w').write(tab.text())
	sys.exit(res)

if __name__ == '__main__':
	main()

~~~

<span class="ClassDoc YAMLDoc" id="QProgEdit-QEditor" markdown="1">

## class __QProgEdit.QEditor__

A single editor widget, which is embedded in a QProgEdit widget.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-__init__" markdown="1">

### function __QProgEdit\.QEditor\.\_\_init\_\___\(qProgEdit\)

Constructor.

__Arguments:__

- `qProgEdit` -- The parent QProgEdit.
	- Type: QProgEdit

</span>

[QProgEdit.QEditor.__init__]: #QProgEdit-QEditor-__init__
[QEditor.__init__]: #QProgEdit-QEditor-__init__
[__init__]: #QProgEdit-QEditor-__init__

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-applyCfg" markdown="1">

### function __QProgEdit\.QEditor\.applyCfg__\(\)

Applies the configuration.

</span>

[QProgEdit.QEditor.applyCfg]: #QProgEdit-QEditor-applyCfg
[QEditor.applyCfg]: #QProgEdit-QEditor-applyCfg
[applyCfg]: #QProgEdit-QEditor-applyCfg

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-commentSelection" markdown="1">

### function __QProgEdit\.QEditor\.commentSelection__\(\)

Comments out the currently selected text.

</span>

[QProgEdit.QEditor.commentSelection]: #QProgEdit-QEditor-commentSelection
[QEditor.commentSelection]: #QProgEdit-QEditor-commentSelection
[commentSelection]: #QProgEdit-QEditor-commentSelection

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-cursorMoved" markdown="1">

### function __QProgEdit\.QEditor\.cursorMoved__\(\)

Is called whenever the cursor moves, checks whether the cursor has jumped from one line to the next, and, if so, calls the relevant functions.

</span>

[QProgEdit.QEditor.cursorMoved]: #QProgEdit-QEditor-cursorMoved
[QEditor.cursorMoved]: #QProgEdit-QEditor-cursorMoved
[cursorMoved]: #QProgEdit-QEditor-cursorMoved

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-focusInEvent" markdown="1">

### function __QProgEdit\.QEditor\.focusInEvent__\(e\)

Called when the editor receives focus.

__Arguments:__

- `e` -- No description

</span>

[QProgEdit.QEditor.focusInEvent]: #QProgEdit-QEditor-focusInEvent
[QEditor.focusInEvent]: #QProgEdit-QEditor-focusInEvent
[focusInEvent]: #QProgEdit-QEditor-focusInEvent

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-focusOutEvent" markdown="1">

### function __QProgEdit\.QEditor\.focusOutEvent__\(e\)

Called when the editor loses focus.

__Arguments:__

- `e` -- No description

</span>

[QProgEdit.QEditor.focusOutEvent]: #QProgEdit-QEditor-focusOutEvent
[QEditor.focusOutEvent]: #QProgEdit-QEditor-focusOutEvent
[focusOutEvent]: #QProgEdit-QEditor-focusOutEvent

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-highlightSelection" markdown="1">

### function __QProgEdit\.QEditor\.highlightSelection__\(\)

Highlights all parts of the text that match the current selection.

</span>

[QProgEdit.QEditor.highlightSelection]: #QProgEdit-QEditor-highlightSelection
[QEditor.highlightSelection]: #QProgEdit-QEditor-highlightSelection
[highlightSelection]: #QProgEdit-QEditor-highlightSelection

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-keyPressEvent" markdown="1">

### function __QProgEdit\.QEditor\.keyPressEvent__\(event\)

Intercepts certain keypress events to implement custom copy-pasting and zooming.

__Arguments:__

- `event` -- No description
	- Type: QKeyPressEvent

</span>

[QProgEdit.QEditor.keyPressEvent]: #QProgEdit-QEditor-keyPressEvent
[QEditor.keyPressEvent]: #QProgEdit-QEditor-keyPressEvent
[keyPressEvent]: #QProgEdit-QEditor-keyPressEvent

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-lang" markdown="1">

### function __QProgEdit\.QEditor\.lang__\(\)

No description specified.

__Returns:__

The language of the editor.

- Type: unicode

</span>

[QProgEdit.QEditor.lang]: #QProgEdit-QEditor-lang
[QEditor.lang]: #QProgEdit-QEditor-lang
[lang]: #QProgEdit-QEditor-lang

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-onMarginClick" markdown="1">

### function __QProgEdit\.QEditor\.onMarginClick__\(margin, line, state\)

Shows validation errors when the margin symbol is clicked.

__Arguments:__

- `margin` -- The margin number.
	- Type: int
- `line` -- The line number.
	- Type: int
- `state` -- The keyboard state.
	- Type: int

</span>

[QProgEdit.QEditor.onMarginClick]: #QProgEdit-QEditor-onMarginClick
[QEditor.onMarginClick]: #QProgEdit-QEditor-onMarginClick
[onMarginClick]: #QProgEdit-QEditor-onMarginClick

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-paste" markdown="1">

### function __QProgEdit\.QEditor\.paste__\(\)

Re-implements the paste method to allow modification of paste content.

</span>

[QProgEdit.QEditor.paste]: #QProgEdit-QEditor-paste
[QEditor.paste]: #QProgEdit-QEditor-paste
[paste]: #QProgEdit-QEditor-paste

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-selectedText" markdown="1">

### function __QProgEdit\.QEditor\.selectedText__\(currentLineFallback=False\)

Returns the selected text.

__Keywords:__

- `currentLineFallback` -- Indicates whether the current line should be returned if no text has been selected. Otherwise, an empty string is returned.
	- Type: bool
	- Default: False

__Returns:__

The selected text.

- Type: str

</span>

[QProgEdit.QEditor.selectedText]: #QProgEdit-QEditor-selectedText
[QEditor.selectedText]: #QProgEdit-QEditor-selectedText
[selectedText]: #QProgEdit-QEditor-selectedText

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-setKeyBindings" markdown="1">

### function __QProgEdit\.QEditor\.setKeyBindings__\(\)

Sets keybindings so that they don't interfere with the default keybindings of OpenSesame, and are more atom-like.

</span>

[QProgEdit.QEditor.setKeyBindings]: #QProgEdit-QEditor-setKeyBindings
[QEditor.setKeyBindings]: #QProgEdit-QEditor-setKeyBindings
[setKeyBindings]: #QProgEdit-QEditor-setKeyBindings

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-setLang" markdown="1">

### function __QProgEdit\.QEditor\.setLang__\(lang=u'text'\)

Sets the editor language.

__Keywords:__

- `lang` -- A language, used to select a lexer for syntax highlighting, validation, cleaning, etc. if an appropriate lexer isn't found, no error is generated, but syntax highlighting is disabled. For a list of available lexers, refer to the QsciScintilla documentation.
	- Default: u'text'

</span>

[QProgEdit.QEditor.setLang]: #QProgEdit-QEditor-setLang
[QEditor.setLang]: #QProgEdit-QEditor-setLang
[setLang]: #QProgEdit-QEditor-setLang

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-setSymbolTree" markdown="1">

### function __QProgEdit\.QEditor\.setSymbolTree__\(symbolTree, symbolTreeWidgetItemClass=<class 'QProgEdit\.\_qsymboltreewidgetitem\.QSymbolTreeWidgetItem'>\)

Sets the symbol-tree widget.

__Arguments:__

- `symbolTree` -- A symbol-tree widget.
	- Type: QTreeWidgetItem

__Keywords:__

- `symbolTreeWidgetItemClass` -- The class to use for symbol-tree widgets. This should derive from QSymbolTreeWidgetItem.
	- Type: type
	- Default: <class 'QProgEdit._qsymboltreewidgetitem.QSymbolTreeWidgetItem'>

</span>

[QProgEdit.QEditor.setSymbolTree]: #QProgEdit-QEditor-setSymbolTree
[QEditor.setSymbolTree]: #QProgEdit-QEditor-setSymbolTree
[setSymbolTree]: #QProgEdit-QEditor-setSymbolTree

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-setText" markdown="1">

### function __QProgEdit\.QEditor\.setText__\(text\)

Sets the editor contents.

__Arguments:__

- `text` -- A text string. This can be a str object or unicode object.
	- Type: str, unicode

</span>

[QProgEdit.QEditor.setText]: #QProgEdit-QEditor-setText
[QEditor.setText]: #QProgEdit-QEditor-setText
[setText]: #QProgEdit-QEditor-setText

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-symbols" markdown="1">

### function __QProgEdit\.QEditor\.symbols__\(\)

Returns an up-to-date list of symbols.

__Returns:__

A list of symbols.

- Type: list

</span>

[QProgEdit.QEditor.symbols]: #QProgEdit-QEditor-symbols
[QEditor.symbols]: #QProgEdit-QEditor-symbols
[symbols]: #QProgEdit-QEditor-symbols

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-text" markdown="1">

### function __QProgEdit\.QEditor\.text__\(\)

Retrieves the editor contents.

__Returns:__

The editor contents.

- Type: unicode

</span>

[QProgEdit.QEditor.text]: #QProgEdit-QEditor-text
[QEditor.text]: #QProgEdit-QEditor-text
[text]: #QProgEdit-QEditor-text

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-uncommentSelection" markdown="1">

### function __QProgEdit\.QEditor\.uncommentSelection__\(\)

Uncomments the currently selected text.

</span>

[QProgEdit.QEditor.uncommentSelection]: #QProgEdit-QEditor-uncommentSelection
[QEditor.uncommentSelection]: #QProgEdit-QEditor-uncommentSelection
[uncommentSelection]: #QProgEdit-QEditor-uncommentSelection

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-updateMarginWidth" markdown="1">

### function __QProgEdit\.QEditor\.updateMarginWidth__\(\)

Updates the width of the margin containing the line numbers.

</span>

[QProgEdit.QEditor.updateMarginWidth]: #QProgEdit-QEditor-updateMarginWidth
[QEditor.updateMarginWidth]: #QProgEdit-QEditor-updateMarginWidth
[updateMarginWidth]: #QProgEdit-QEditor-updateMarginWidth

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-updateSymbolTree" markdown="1">

### function __QProgEdit\.QEditor\.updateSymbolTree__\(\)

Updates the symbol tree, if any has been specified and a symbol parser is available for the langauage.

</span>

[QProgEdit.QEditor.updateSymbolTree]: #QProgEdit-QEditor-updateSymbolTree
[QEditor.updateSymbolTree]: #QProgEdit-QEditor-updateSymbolTree
[updateSymbolTree]: #QProgEdit-QEditor-updateSymbolTree

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-validate" markdown="1">

### function __QProgEdit\.QEditor\.validate__\(\)

Validates the content.

</span>

[QProgEdit.QEditor.validate]: #QProgEdit-QEditor-validate
[QEditor.validate]: #QProgEdit-QEditor-validate
[validate]: #QProgEdit-QEditor-validate

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditor-wheelEvent" markdown="1">

### function __QProgEdit\.QEditor\.wheelEvent__\(event\)

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

## class __QProgEdit.QEditorCfg__

A non-persistent configuration object.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorCfg-__init__" markdown="1">

### function __QProgEdit\.QEditorCfg\.\_\_init\_\___\(parent=None\)

Constructor.

__Keywords:__

- `parent` -- The parent widget.
	- Type: QWidget, NoneType
	- Default: None

</span>

[QProgEdit.QEditorCfg.__init__]: #QProgEdit-QEditorCfg-__init__
[QEditorCfg.__init__]: #QProgEdit-QEditorCfg-__init__
[__init__]: #QProgEdit-QEditorCfg-__init__

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorCfg-version" markdown="1">

### function __QProgEdit\.QEditorCfg\.version__\(\)

Returns the config version.

</span>

[QProgEdit.QEditorCfg.version]: #QProgEdit-QEditorCfg-version
[QEditorCfg.version]: #QProgEdit-QEditorCfg-version
[version]: #QProgEdit-QEditorCfg-version

</span>

[QProgEdit.QEditorCfg]: #QProgEdit-QEditorCfg
[QEditorCfg]: #QProgEdit-QEditorCfg

<span class="ClassDoc YAMLDoc" id="QProgEdit-QEditorFind" markdown="1">

## class __QProgEdit.QEditorFind__

A find/ replace widget.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-__init__" markdown="1">

### function __QProgEdit\.QEditorFind\.\_\_init\_\___\(qProgEdit\)

Constructor.

__Arguments:__

- `qProgEdit` -- The parent QProgEdit.
	- Type: QProgEdit

</span>

[QProgEdit.QEditorFind.__init__]: #QProgEdit-QEditorFind-__init__
[QEditorFind.__init__]: #QProgEdit-QEditorFind-__init__
[__init__]: #QProgEdit-QEditorFind-__init__

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-caseSensitive" markdown="1">

### function __QProgEdit\.QEditorFind\.caseSensitive__\(\)

No description specified.

__Returns:__

True or False, depending on whether we should search case sensitive.

- Type: bool

</span>

[QProgEdit.QEditorFind.caseSensitive]: #QProgEdit-QEditorFind-caseSensitive
[QEditorFind.caseSensitive]: #QProgEdit-QEditorFind-caseSensitive
[caseSensitive]: #QProgEdit-QEditorFind-caseSensitive

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-find" markdown="1">

### function __QProgEdit\.QEditorFind\.find__\(\)

Finds the current text in the document.

__Returns:__

True if matching text has been found, False otherwise.

- Type: bool

</span>

[QProgEdit.QEditorFind.find]: #QProgEdit-QEditorFind-find
[QEditorFind.find]: #QProgEdit-QEditorFind-find
[find]: #QProgEdit-QEditorFind-find

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-findText" markdown="1">

### function __QProgEdit\.QEditorFind\.findText__\(\)

No description specified.

__Returns:__

The find text.

- Type: unicode

</span>

[QProgEdit.QEditorFind.findText]: #QProgEdit-QEditorFind-findText
[QEditorFind.findText]: #QProgEdit-QEditorFind-findText
[findText]: #QProgEdit-QEditorFind-findText

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-loadUi" markdown="1">

### function __QProgEdit\.QEditorFind\.loadUi__\(name\)

Load a UI.

__Arguments:__

- `name` -- The name of the UI file, without the .ui extension.
	- Type: unicode

</span>

[QProgEdit.QEditorFind.loadUi]: #QProgEdit-QEditorFind-loadUi
[QEditorFind.loadUi]: #QProgEdit-QEditorFind-loadUi
[loadUi]: #QProgEdit-QEditorFind-loadUi

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-lock" markdown="1">

### function __QProgEdit\.QEditorFind\.lock__\(\)

Locks the editor and find widget, so that we don't get into recursion problems during replace actions.

</span>

[QProgEdit.QEditorFind.lock]: #QProgEdit-QEditorFind-lock
[QEditorFind.lock]: #QProgEdit-QEditorFind-lock
[lock]: #QProgEdit-QEditorFind-lock

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-matchWhole" markdown="1">

### function __QProgEdit\.QEditorFind\.matchWhole__\(\)

No description specified.

__Returns:__

True or False, depending on whether we should match whole words only.

- Type: bool

</span>

[QProgEdit.QEditorFind.matchWhole]: #QProgEdit-QEditorFind-matchWhole
[QEditorFind.matchWhole]: #QProgEdit-QEditorFind-matchWhole
[matchWhole]: #QProgEdit-QEditorFind-matchWhole

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-replace" markdown="1">

### function __QProgEdit\.QEditorFind\.replace__\(\)

Replaces the first occurence in the document.

__Returns:__

True if text has been replaced, False otherwise.

- Type: bool

</span>

[QProgEdit.QEditorFind.replace]: #QProgEdit-QEditorFind-replace
[QEditorFind.replace]: #QProgEdit-QEditorFind-replace
[replace]: #QProgEdit-QEditorFind-replace

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-replaceAll" markdown="1">

### function __QProgEdit\.QEditorFind\.replaceAll__\(\)

Replaces all occurences in the document.

</span>

[QProgEdit.QEditorFind.replaceAll]: #QProgEdit-QEditorFind-replaceAll
[QEditorFind.replaceAll]: #QProgEdit-QEditorFind-replaceAll
[replaceAll]: #QProgEdit-QEditorFind-replaceAll

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-replaceText" markdown="1">

### function __QProgEdit\.QEditorFind\.replaceText__\(\)

No description specified.

__Returns:__

The replace text.

- Type: unicode

</span>

[QProgEdit.QEditorFind.replaceText]: #QProgEdit-QEditorFind-replaceText
[QEditorFind.replaceText]: #QProgEdit-QEditorFind-replaceText
[replaceText]: #QProgEdit-QEditorFind-replaceText

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-setFindText" markdown="1">

### function __QProgEdit\.QEditorFind\.setFindText__\(txt=u''\)

Sets the text of the find widget.

__Keywords:__

- `txt` -- The text to set.
	- Type: unicode
	- Default: u''

</span>

[QProgEdit.QEditorFind.setFindText]: #QProgEdit-QEditorFind-setFindText
[QEditorFind.setFindText]: #QProgEdit-QEditorFind-setFindText
[setFindText]: #QProgEdit-QEditorFind-setFindText

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-unlock" markdown="1">

### function __QProgEdit\.QEditorFind\.unlock__\(\)

Unlocks the editor and find widget, to resume normal operations after replacing.

</span>

[QProgEdit.QEditorFind.unlock]: #QProgEdit-QEditorFind-unlock
[QEditorFind.unlock]: #QProgEdit-QEditorFind-unlock
[unlock]: #QProgEdit-QEditorFind-unlock

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorFind-unshow" markdown="1">

### function __QProgEdit\.QEditorFind\.unshow__\(\)

Hides the widget.

</span>

[QProgEdit.QEditorFind.unshow]: #QProgEdit-QEditorFind-unshow
[QEditorFind.unshow]: #QProgEdit-QEditorFind-unshow
[unshow]: #QProgEdit-QEditorFind-unshow

</span>

[QProgEdit.QEditorFind]: #QProgEdit-QEditorFind
[QEditorFind]: #QProgEdit-QEditorFind

<span class="ClassDoc YAMLDoc" id="QProgEdit-QEditorPrefs" markdown="1">

## class __QProgEdit.QEditorPrefs__

An editor preferences widget.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorPrefs-__init__" markdown="1">

### function __QProgEdit\.QEditorPrefs\.\_\_init\_\___\(qProgEdit\)

Constructor.

__Arguments:__

- `qProgEdit` -- The parent QProgEdit.
	- Type: QProgEdit

</span>

[QProgEdit.QEditorPrefs.__init__]: #QProgEdit-QEditorPrefs-__init__
[QEditorPrefs.__init__]: #QProgEdit-QEditorPrefs-__init__
[__init__]: #QProgEdit-QEditorPrefs-__init__

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorPrefs-apply" markdown="1">

### function __QProgEdit\.QEditorPrefs\.apply__\(dummy=None\)

Applies the controls.

__Keywords:__

- `dummy` -- No description
	- Default: None

</span>

[QProgEdit.QEditorPrefs.apply]: #QProgEdit-QEditorPrefs-apply
[QEditorPrefs.apply]: #QProgEdit-QEditorPrefs-apply
[apply]: #QProgEdit-QEditorPrefs-apply

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorPrefs-loadUi" markdown="1">

### function __QProgEdit\.QEditorPrefs\.loadUi__\(name\)

Load a UI.

__Arguments:__

- `name` -- The name of the UI file, without the .ui extension.
	- Type: unicode

</span>

[QProgEdit.QEditorPrefs.loadUi]: #QProgEdit-QEditorPrefs-loadUi
[QEditorPrefs.loadUi]: #QProgEdit-QEditorPrefs-loadUi
[loadUi]: #QProgEdit-QEditorPrefs-loadUi

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorPrefs-refresh" markdown="1">

### function __QProgEdit\.QEditorPrefs\.refresh__\(\)

Refreshes the controls.

</span>

[QProgEdit.QEditorPrefs.refresh]: #QProgEdit-QEditorPrefs-refresh
[QEditorPrefs.refresh]: #QProgEdit-QEditorPrefs-refresh
[refresh]: #QProgEdit-QEditorPrefs-refresh

</span>

[QProgEdit.QEditorPrefs]: #QProgEdit-QEditorPrefs
[QEditorPrefs]: #QProgEdit-QEditorPrefs

<span class="ClassDoc YAMLDoc" id="QProgEdit-QEditorStatus" markdown="1">

## class __QProgEdit.QEditorStatus__

A simple widget that indicates the editor status, which currently corresponds only to the cursor position.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorStatus-__init__" markdown="1">

### function __QProgEdit\.QEditorStatus\.\_\_init\_\___\(qProgEdit\)

Constructor.

__Arguments:__

- `qProgEdit` -- The parent QProgEdit.
	- Type: QProgEdit

</span>

[QProgEdit.QEditorStatus.__init__]: #QProgEdit-QEditorStatus-__init__
[QEditorStatus.__init__]: #QProgEdit-QEditorStatus-__init__
[__init__]: #QProgEdit-QEditorStatus-__init__

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QEditorStatus-updateCursorPos" markdown="1">

### function __QProgEdit\.QEditorStatus\.updateCursorPos__\(line=0, index=0\)

Updates the cursor position.

__Keywords:__

- `line` -- The line number.
	- Type: int
	- Default: 0
- `index` -- The column number.
	- Type: int
	- Default: 0

</span>

[QProgEdit.QEditorStatus.updateCursorPos]: #QProgEdit-QEditorStatus-updateCursorPos
[QEditorStatus.updateCursorPos]: #QProgEdit-QEditorStatus-updateCursorPos
[updateCursorPos]: #QProgEdit-QEditorStatus-updateCursorPos

</span>

[QProgEdit.QEditorStatus]: #QProgEdit-QEditorStatus
[QEditorStatus]: #QProgEdit-QEditorStatus

<span class="ClassDoc YAMLDoc" id="QProgEdit-QLangMenu" markdown="1">

## class __QProgEdit.QLangMenu__

The language selection menu.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QLangMenu-__init__" markdown="1">

### function __QProgEdit\.QLangMenu\.\_\_init\_\___\(tabCornerWidget\)

Constructor.

__Arguments:__

- `tabCornerWidget` -- The parent QTabCornerWidget.
	- Type: QTabCornerWidget

</span>

[QProgEdit.QLangMenu.__init__]: #QProgEdit-QLangMenu-__init__
[QLangMenu.__init__]: #QProgEdit-QLangMenu-__init__
[__init__]: #QProgEdit-QLangMenu-__init__

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QLangMenu-setLang" markdown="1">

### function __QProgEdit\.QLangMenu\.setLang__\(action\)

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

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QLexer" markdown="1">

## function __QProgEdit\.QLexer__\(editor, lang=u'text', colorScheme=u'Default'\)

A factory for a lexer.

__Arguments:__

- `editor` -- The parent QEditor.
	- Type: QEditor

__Keywords:__

- `lang` -- The language.
	- Type: unicode
	- Default: u'text'
- `colorScheme` -- The color scheme.
	- Type: unicode
	- Default: u'Default'

</span>

[QProgEdit.QLexer]: #QProgEdit-QLexer
[QLexer]: #QProgEdit-QLexer

<span class="ClassDoc YAMLDoc" id="QProgEdit-QProgEdit" markdown="1">

## class __QProgEdit.QProgEdit__

A single editor window, with preferences widget and search functionality.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-__init__" markdown="1">

### function __QProgEdit\.QProgEdit\.\_\_init\_\___\(tabManager, dPrint=None, title=u'Empty document', \*\*editorParams\)

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

### function __QProgEdit\.QProgEdit\.dPrint__\(msg\)

Prints a debug message.

__Arguments:__

- `msg` -- A debug message.
	- Type: unicode, str

</span>

[QProgEdit.QProgEdit.dPrint]: #QProgEdit-QProgEdit-dPrint
[QProgEdit.dPrint]: #QProgEdit-QProgEdit-dPrint
[dPrint]: #QProgEdit-QProgEdit-dPrint

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-focusTab" markdown="1">

### function __QProgEdit\.QProgEdit\.focusTab__\(\)

Focuses the current tab.

</span>

[QProgEdit.QProgEdit.focusTab]: #QProgEdit-QProgEdit-focusTab
[QProgEdit.focusTab]: #QProgEdit-QProgEdit-focusTab
[focusTab]: #QProgEdit-QProgEdit-focusTab

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-tabIndex" markdown="1">

### function __QProgEdit\.QProgEdit\.tabIndex__\(\)

Gets the index of the current tab.

__Returns:__

The tab index.

- Type: int

</span>

[QProgEdit.QProgEdit.tabIndex]: #QProgEdit-QProgEdit-tabIndex
[QProgEdit.tabIndex]: #QProgEdit-QProgEdit-tabIndex
[tabIndex]: #QProgEdit-QProgEdit-tabIndex

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-toggle" markdown="1">

### function __QProgEdit\.QProgEdit\.toggle__\(widget, visible\)

Toggles the visibility of a widget with a smooth animation.

__Arguments:__

- `widget` -- A QWidget.
- `visible` -- A boolean indicating the visibility of the widget.

</span>

[QProgEdit.QProgEdit.toggle]: #QProgEdit-QProgEdit-toggle
[QProgEdit.toggle]: #QProgEdit-QProgEdit-toggle
[toggle]: #QProgEdit-QProgEdit-toggle

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-toggleFind" markdown="1">

### function __QProgEdit\.QProgEdit\.toggleFind__\(visible\)

Toggles the visibility of the find widget.

__Arguments:__

- `visible` -- A boolean indicating the visibility of the widget.

</span>

[QProgEdit.QProgEdit.toggleFind]: #QProgEdit-QProgEdit-toggleFind
[QProgEdit.toggleFind]: #QProgEdit-QProgEdit-toggleFind
[toggleFind]: #QProgEdit-QProgEdit-toggleFind

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QProgEdit-togglePrefs" markdown="1">

### function __QProgEdit\.QProgEdit\.togglePrefs__\(visible\)

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

## class __QProgEdit.QSymbolTreeWidgetItem__

A symbol-tree widget item to use for symbol overviews.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QSymbolTreeWidgetItem-__init__" markdown="1">

### function __QProgEdit\.QSymbolTreeWidgetItem\.\_\_init\_\___\(editor, lineNo, \_type, name, argSpec\)

Constructor.

__Arguments:__

- `editor` -- The editor widget.
	- Type: QEditor
- `lineNo` -- A line number.
	- Type: int
- `_type` -- The symbol type, such as 'class' or 'def'
	- Type: unicode
- `name` -- The symbol name
	- Type: unicode
- `argSpec` -- The symbol's argument specification.
	- Type: unicode

</span>

[QProgEdit.QSymbolTreeWidgetItem.__init__]: #QProgEdit-QSymbolTreeWidgetItem-__init__
[QSymbolTreeWidgetItem.__init__]: #QProgEdit-QSymbolTreeWidgetItem-__init__
[__init__]: #QProgEdit-QSymbolTreeWidgetItem-__init__

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QSymbolTreeWidgetItem-activate" markdown="1">

### function __QProgEdit\.QSymbolTreeWidgetItem\.activate__\(\)

Is called when the symbol is activated, to focus the symbol in the editor.

</span>

[QProgEdit.QSymbolTreeWidgetItem.activate]: #QProgEdit-QSymbolTreeWidgetItem-activate
[QSymbolTreeWidgetItem.activate]: #QProgEdit-QSymbolTreeWidgetItem-activate
[activate]: #QProgEdit-QSymbolTreeWidgetItem-activate

</span>

[QProgEdit.QSymbolTreeWidgetItem]: #QProgEdit-QSymbolTreeWidgetItem
[QSymbolTreeWidgetItem]: #QProgEdit-QSymbolTreeWidgetItem

<span class="ClassDoc YAMLDoc" id="QProgEdit-QTabCornerWidget" markdown="1">

## class __QProgEdit.QTabCornerWidget__

Contains a number of buttons that are displayed in the tab bar.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabCornerWidget-__init__" markdown="1">

### function __QProgEdit\.QTabCornerWidget\.\_\_init\_\___\(tabManager, msg=None, handlerButtonText=None, runButton=False\)

Constructor.

__Arguments:__

- `tabManager` -- A tab manager.
	- Type: QTabManager

__Keywords:__

- `msg` -- An informative text message.
	- Type: str, unicode, NoneType
	- Default: None
- `handlerButtonText` -- Text for a top-right button, which can be clicked to call the handler, or None for no button.
	- Type: str, unicode, NoneType
	- Default: None
- `runButton` -- Indicates whether a run-selected-text button should be shown.
	- Type: bool
	- Default: False

</span>

[QProgEdit.QTabCornerWidget.__init__]: #QProgEdit-QTabCornerWidget-__init__
[QTabCornerWidget.__init__]: #QProgEdit-QTabCornerWidget-__init__
[__init__]: #QProgEdit-QTabCornerWidget-__init__

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabCornerWidget-handlerButtonClicked" markdown="1">

### function __QProgEdit\.QTabCornerWidget\.handlerButtonClicked__\(\)

Is called when the handler button is clicked and emits the relevant signals.

</span>

[QProgEdit.QTabCornerWidget.handlerButtonClicked]: #QProgEdit-QTabCornerWidget-handlerButtonClicked
[QTabCornerWidget.handlerButtonClicked]: #QProgEdit-QTabCornerWidget-handlerButtonClicked
[handlerButtonClicked]: #QProgEdit-QTabCornerWidget-handlerButtonClicked

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabCornerWidget-update" markdown="1">

### function __QProgEdit\.QTabCornerWidget\.update__\(\)

Updates widget to reflect document contents.

</span>

[QProgEdit.QTabCornerWidget.update]: #QProgEdit-QTabCornerWidget-update
[QTabCornerWidget.update]: #QProgEdit-QTabCornerWidget-update
[update]: #QProgEdit-QTabCornerWidget-update

</span>

[QProgEdit.QTabCornerWidget]: #QProgEdit-QTabCornerWidget
[QTabCornerWidget]: #QProgEdit-QTabCornerWidget

<span class="ClassDoc YAMLDoc" id="QProgEdit-QTabManager" markdown="1">

## class __QProgEdit.QTabManager__

A tab manager that contains multiple QProgEdit tabs.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-__init__" markdown="1">

### function __QProgEdit\.QTabManager\.\_\_init\_\___\(parent=None, cfg=<QProgEdit\.\_qeditorcfg\.QEditorCfg object at 0x7f73885d59d0>, tabsClosable=False, tabsMovable=False, msg=None, handlerButtonText=None, runButton=False\)

Constructor.

__Keywords:__

- `parent` -- The parent widget.
	- Type: QWidget
	- Default: None
- `cfg` -- A configuration backend. By default QEditorCfg is used. Custom backends must have the same API for getting and setting options.
	- Default: <QProgEdit._qeditorcfg.QEditorCfg object at 0x7f73885d59d0>
- `tabsClosable` -- Indicates whether a close button should be shown on tabs.
	- Type: bool
	- Default: False
- `tabsMovable` -- Indicates whether tabs can be re-ordered.
	- Type: bool
	- Default: False
- `msg` -- An informative message for the corner widget.
	- Type: str, unicode, NoneType
	- Default: None
- `handlerButtonText` -- Text for a top-right button, which can be clicked to call the handler, or None for no button.
	- Type: str, unicode, NoneType
	- Default: None
- `runButton` -- Indicates whether a run-selected-text button should be shown.
	- Type: bool
	- Default: False

</span>

[QProgEdit.QTabManager.__init__]: #QProgEdit-QTabManager-__init__
[QTabManager.__init__]: #QProgEdit-QTabManager-__init__
[__init__]: #QProgEdit-QTabManager-__init__

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-addTab" markdown="1">

### function __QProgEdit\.QTabManager\.addTab__\(title=u'Empty document', select=True\)

Adds an empty document tab.

__Keywords:__

- `title` -- A tab title.
	- Type: unicode, str
	- Default: u'Empty document'
- `select` -- Indicates whether the newly created tab should be selected.
	- Type: bool
	- Default: True

__Returns:__

The newly added tab widget.

- Type: QProgEdit

</span>

[QProgEdit.QTabManager.addTab]: #QProgEdit-QTabManager-addTab
[QTabManager.addTab]: #QProgEdit-QTabManager-addTab
[addTab]: #QProgEdit-QTabManager-addTab

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-applyCfg" markdown="1">

### function __QProgEdit\.QTabManager\.applyCfg__\(\)

Applies the configuration.

</span>

[QProgEdit.QTabManager.applyCfg]: #QProgEdit-QTabManager-applyCfg
[QTabManager.applyCfg]: #QProgEdit-QTabManager-applyCfg
[applyCfg]: #QProgEdit-QTabManager-applyCfg

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-closeTab" markdown="1">

### function __QProgEdit\.QTabManager\.closeTab__\(index=None\)

Closes a tab.

__Keywords:__

- `index` -- A tab index (see [tabIndex]).
	- Default: None

</span>

[QProgEdit.QTabManager.closeTab]: #QProgEdit-QTabManager-closeTab
[QTabManager.closeTab]: #QProgEdit-QTabManager-closeTab
[closeTab]: #QProgEdit-QTabManager-closeTab

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-isAnyModified" markdown="1">

### function __QProgEdit\.QTabManager\.isAnyModified__\(\)

Checks if one or more of the tabs have been modified.

__Returns:__

True if (one of) the tab(s) is modified, False otherwise.

- Type: bool

</span>

[QProgEdit.QTabManager.isAnyModified]: #QProgEdit-QTabManager-isAnyModified
[QTabManager.isAnyModified]: #QProgEdit-QTabManager-isAnyModified
[isAnyModified]: #QProgEdit-QTabManager-isAnyModified

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-runSelectedText" markdown="1">

### function __QProgEdit\.QTabManager\.runSelectedText__\(\)

Emits the execute signal with the selected text.

</span>

[QProgEdit.QTabManager.runSelectedText]: #QProgEdit-QTabManager-runSelectedText
[QTabManager.runSelectedText]: #QProgEdit-QTabManager-runSelectedText
[runSelectedText]: #QProgEdit-QTabManager-runSelectedText

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-runText" markdown="1">

### function __QProgEdit\.QTabManager\.runText__\(\)

Emits the execute signal with the current text.

</span>

[QProgEdit.QTabManager.runText]: #QProgEdit-QTabManager-runText
[QTabManager.runText]: #QProgEdit-QTabManager-runText
[runText]: #QProgEdit-QTabManager-runText

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-selectTab" markdown="1">

### function __QProgEdit\.QTabManager\.selectTab__\(index\)

Switches to a specific tab.

__Arguments:__

- `index` -- A tab index, as understood by [tabIndex].

</span>

[QProgEdit.QTabManager.selectTab]: #QProgEdit-QTabManager-selectTab
[QTabManager.selectTab]: #QProgEdit-QTabManager-selectTab
[selectTab]: #QProgEdit-QTabManager-selectTab

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-selectedText" markdown="1">

### function __QProgEdit\.QTabManager\.selectedText__\(index=None, currentLineFallback=False\)

Returns the selected text for a specific tab.
For details, see `QProgEdit.QEditor`.

__Keywords:__

- `index` -- A tab index, as understood by [tabIndex].
	- Default: None
- `currentLineFallback` -- No description
	- Default: False

__Returns:__

The selected text.

</span>

[QProgEdit.QTabManager.selectedText]: #QProgEdit-QTabManager-selectedText
[QTabManager.selectedText]: #QProgEdit-QTabManager-selectedText
[selectedText]: #QProgEdit-QTabManager-selectedText

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-setFocus" markdown="1">

### function __QProgEdit\.QTabManager\.setFocus__\(index=None\)

Focuses a specific tab.

__Keywords:__

- `index` -- A tab index, as understood by [tabIndex].
	- Default: None

</span>

[QProgEdit.QTabManager.setFocus]: #QProgEdit-QTabManager-setFocus
[QTabManager.setFocus]: #QProgEdit-QTabManager-setFocus
[setFocus]: #QProgEdit-QTabManager-setFocus

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-setText" markdown="1">

### function __QProgEdit\.QTabManager\.setText__\(text, index=None\)

Sets the text on a specific tab.

__Arguments:__

- `text` -- The new text.

__Keywords:__

- `index` -- A tab index, as understood by [tabIndex].
	- Default: None

</span>

[QProgEdit.QTabManager.setText]: #QProgEdit-QTabManager-setText
[QTabManager.setText]: #QProgEdit-QTabManager-setText
[setText]: #QProgEdit-QTabManager-setText

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-switchTabLeft" markdown="1">

### function __QProgEdit\.QTabManager\.switchTabLeft__\(\)

Switches to the tab on the left.

</span>

[QProgEdit.QTabManager.switchTabLeft]: #QProgEdit-QTabManager-switchTabLeft
[QTabManager.switchTabLeft]: #QProgEdit-QTabManager-switchTabLeft
[switchTabLeft]: #QProgEdit-QTabManager-switchTabLeft

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-switchTabRight" markdown="1">

### function __QProgEdit\.QTabManager\.switchTabRight__\(\)

Switches to the tab on the left.

</span>

[QProgEdit.QTabManager.switchTabRight]: #QProgEdit-QTabManager-switchTabRight
[QTabManager.switchTabRight]: #QProgEdit-QTabManager-switchTabRight
[switchTabRight]: #QProgEdit-QTabManager-switchTabRight

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-tab" markdown="1">

### function __QProgEdit\.QTabManager\.tab__\(index=None\)

Returns the QProgEdit instance for a given tab.

__Keywords:__

- `index` -- Specifies the tab, either by a name (i.e. the name on a tab), an index, or None to get the current tab.
	- Type: int, str, unicode, NoneType
	- Default: None

__Returns:__

A tab, or None if no matching tab was found.

- Type: QProgEdit, NoneType

</span>

[QProgEdit.QTabManager.tab]: #QProgEdit-QTabManager-tab
[QTabManager.tab]: #QProgEdit-QTabManager-tab
[tab]: #QProgEdit-QTabManager-tab

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-tabChanged" markdown="1">

### function __QProgEdit\.QTabManager\.tabChanged__\(index\)

Is called when the current tab must be updated, for example because a new tab is selected.

__Arguments:__

- `index` -- The index of the newly selected tab.
	- Type: int

</span>

[QProgEdit.QTabManager.tabChanged]: #QProgEdit-QTabManager-tabChanged
[QTabManager.tabChanged]: #QProgEdit-QTabManager-tabChanged
[tabChanged]: #QProgEdit-QTabManager-tabChanged

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-tabIndex" markdown="1">

### function __QProgEdit\.QTabManager\.tabIndex__\(index=None\)

Returns the index for a given tab.

__Keywords:__

- `index` -- Specifies the tab, either by a name (i.e. the name on a tab), an index, or None to get the current tab.
	- Type: int, str, unicode, NoneType
	- Default: None

__Returns:__

A tab index, or None if no matching tab was found.

- Type: int, NoneType

</span>

[QProgEdit.QTabManager.tabIndex]: #QProgEdit-QTabManager-tabIndex
[QTabManager.tabIndex]: #QProgEdit-QTabManager-tabIndex
[tabIndex]: #QProgEdit-QTabManager-tabIndex

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-tabs" markdown="1">

### function __QProgEdit\.QTabManager\.tabs__\(\)

Gets all tabs.

__Returns:__

A list of all tab widgets.

- Type: list

</span>

[QProgEdit.QTabManager.tabs]: #QProgEdit-QTabManager-tabs
[QTabManager.tabs]: #QProgEdit-QTabManager-tabs
[tabs]: #QProgEdit-QTabManager-tabs

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-text" markdown="1">

### function __QProgEdit\.QTabManager\.text__\(index=None\)

Gets the text on a specific tab.

__Keywords:__

- `index` -- A tab index, as understood by [tabIndex].
	- Default: None

__Returns:__

The text or None if the tab does not exist.

</span>

[QProgEdit.QTabManager.text]: #QProgEdit-QTabManager-text
[QTabManager.text]: #QProgEdit-QTabManager-text
[text]: #QProgEdit-QTabManager-text

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-toggleFind" markdown="1">

### function __QProgEdit\.QTabManager\.toggleFind__\(visible\)

Toggle the visibility of the find widget.

__Arguments:__

- `visible` -- Visibility status.
	- Type: bool

</span>

[QProgEdit.QTabManager.toggleFind]: #QProgEdit-QTabManager-toggleFind
[QTabManager.toggleFind]: #QProgEdit-QTabManager-toggleFind
[toggleFind]: #QProgEdit-QTabManager-toggleFind

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QTabManager-togglePrefs" markdown="1">

### function __QProgEdit\.QTabManager\.togglePrefs__\(visible\)

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

<span class="ClassDoc YAMLDoc" id="QProgEdit-QUiLoader" markdown="1">

## class __QProgEdit.QUiLoader__

A simple base class that implements dynamic UI loading for widgets.

<span class="FunctionDoc YAMLDoc" id="QProgEdit-QUiLoader-loadUi" markdown="1">

### function __QProgEdit\.QUiLoader\.loadUi__\(name\)

Load a UI.

__Arguments:__

- `name` -- The name of the UI file, without the .ui extension.
	- Type: unicode

</span>

[QProgEdit.QUiLoader.loadUi]: #QProgEdit-QUiLoader-loadUi
[QUiLoader.loadUi]: #QProgEdit-QUiLoader-loadUi
[loadUi]: #QProgEdit-QUiLoader-loadUi

</span>

[QProgEdit.QUiLoader]: #QProgEdit-QUiLoader
[QUiLoader]: #QProgEdit-QUiLoader

</span>

[QProgEdit]: #QProgEdit


[Overview]: #overview
[Dependencies]: #dependencies
[Example]: #example
[class __QProgEdit.QEditor__]: #class-__qprogeditqeditor__
[function __QProgEdit\.QEditor\.\_\_init\_\___\(qProgEdit\)]: #function-__qprogeditqeditor__init____qprogedit
[function __QProgEdit\.QEditor\.applyCfg__\(\)]: #function-__qprogeditqeditorapplycfg__
[function __QProgEdit\.QEditor\.commentSelection__\(\)]: #function-__qprogeditqeditorcommentselection__
[function __QProgEdit\.QEditor\.cursorMoved__\(\)]: #function-__qprogeditqeditorcursormoved__
[function __QProgEdit\.QEditor\.focusInEvent__\(e\)]: #function-__qprogeditqeditorfocusinevent__e
[function __QProgEdit\.QEditor\.focusOutEvent__\(e\)]: #function-__qprogeditqeditorfocusoutevent__e
[function __QProgEdit\.QEditor\.highlightSelection__\(\)]: #function-__qprogeditqeditorhighlightselection__
[function __QProgEdit\.QEditor\.keyPressEvent__\(event\)]: #function-__qprogeditqeditorkeypressevent__event
[function __QProgEdit\.QEditor\.lang__\(\)]: #function-__qprogeditqeditorlang__
[function __QProgEdit\.QEditor\.onMarginClick__\(margin, line, state\)]: #function-__qprogeditqeditoronmarginclick__margin-line-state
[function __QProgEdit\.QEditor\.paste__\(\)]: #function-__qprogeditqeditorpaste__
[function __QProgEdit\.QEditor\.selectedText__\(currentLineFallback=False\)]: #function-__qprogeditqeditorselectedtext__currentlinefallbackfalse
[function __QProgEdit\.QEditor\.setKeyBindings__\(\)]: #function-__qprogeditqeditorsetkeybindings__
[function __QProgEdit\.QEditor\.setLang__\(lang=u'text'\)]: #function-__qprogeditqeditorsetlang__langutext
[function __QProgEdit\.QEditor\.setSymbolTree__\(symbolTree, symbolTreeWidgetItemClass=<class 'QProgEdit\.\_qsymboltreewidgetitem\.QSymbolTreeWidgetItem'>\)]: #function-__qprogeditqeditorsetsymboltree__symboltree-symboltreewidgetitemclassclass-qprogedit_qsymboltreewidgetitemqsymboltreewidgetitem
[function __QProgEdit\.QEditor\.setText__\(text\)]: #function-__qprogeditqeditorsettext__text
[function __QProgEdit\.QEditor\.symbols__\(\)]: #function-__qprogeditqeditorsymbols__
[function __QProgEdit\.QEditor\.text__\(\)]: #function-__qprogeditqeditortext__
[function __QProgEdit\.QEditor\.uncommentSelection__\(\)]: #function-__qprogeditqeditoruncommentselection__
[function __QProgEdit\.QEditor\.updateMarginWidth__\(\)]: #function-__qprogeditqeditorupdatemarginwidth__
[function __QProgEdit\.QEditor\.updateSymbolTree__\(\)]: #function-__qprogeditqeditorupdatesymboltree__
[function __QProgEdit\.QEditor\.validate__\(\)]: #function-__qprogeditqeditorvalidate__
[function __QProgEdit\.QEditor\.wheelEvent__\(event\)]: #function-__qprogeditqeditorwheelevent__event
[class __QProgEdit.QEditorCfg__]: #class-__qprogeditqeditorcfg__
[function __QProgEdit\.QEditorCfg\.\_\_init\_\___\(parent=None\)]: #function-__qprogeditqeditorcfg__init____parentnone
[function __QProgEdit\.QEditorCfg\.version__\(\)]: #function-__qprogeditqeditorcfgversion__
[class __QProgEdit.QEditorFind__]: #class-__qprogeditqeditorfind__
[function __QProgEdit\.QEditorFind\.\_\_init\_\___\(qProgEdit\)]: #function-__qprogeditqeditorfind__init____qprogedit
[function __QProgEdit\.QEditorFind\.caseSensitive__\(\)]: #function-__qprogeditqeditorfindcasesensitive__
[function __QProgEdit\.QEditorFind\.find__\(\)]: #function-__qprogeditqeditorfindfind__
[function __QProgEdit\.QEditorFind\.findText__\(\)]: #function-__qprogeditqeditorfindfindtext__
[function __QProgEdit\.QEditorFind\.loadUi__\(name\)]: #function-__qprogeditqeditorfindloadui__name
[function __QProgEdit\.QEditorFind\.lock__\(\)]: #function-__qprogeditqeditorfindlock__
[function __QProgEdit\.QEditorFind\.matchWhole__\(\)]: #function-__qprogeditqeditorfindmatchwhole__
[function __QProgEdit\.QEditorFind\.replace__\(\)]: #function-__qprogeditqeditorfindreplace__
[function __QProgEdit\.QEditorFind\.replaceAll__\(\)]: #function-__qprogeditqeditorfindreplaceall__
[function __QProgEdit\.QEditorFind\.replaceText__\(\)]: #function-__qprogeditqeditorfindreplacetext__
[function __QProgEdit\.QEditorFind\.setFindText__\(txt=u''\)]: #function-__qprogeditqeditorfindsetfindtext__txtu
[function __QProgEdit\.QEditorFind\.unlock__\(\)]: #function-__qprogeditqeditorfindunlock__
[function __QProgEdit\.QEditorFind\.unshow__\(\)]: #function-__qprogeditqeditorfindunshow__
[class __QProgEdit.QEditorPrefs__]: #class-__qprogeditqeditorprefs__
[function __QProgEdit\.QEditorPrefs\.\_\_init\_\___\(qProgEdit\)]: #function-__qprogeditqeditorprefs__init____qprogedit
[function __QProgEdit\.QEditorPrefs\.apply__\(dummy=None\)]: #function-__qprogeditqeditorprefsapply__dummynone
[function __QProgEdit\.QEditorPrefs\.loadUi__\(name\)]: #function-__qprogeditqeditorprefsloadui__name
[function __QProgEdit\.QEditorPrefs\.refresh__\(\)]: #function-__qprogeditqeditorprefsrefresh__
[class __QProgEdit.QEditorStatus__]: #class-__qprogeditqeditorstatus__
[function __QProgEdit\.QEditorStatus\.\_\_init\_\___\(qProgEdit\)]: #function-__qprogeditqeditorstatus__init____qprogedit
[function __QProgEdit\.QEditorStatus\.updateCursorPos__\(line=0, index=0\)]: #function-__qprogeditqeditorstatusupdatecursorpos__line0-index0
[class __QProgEdit.QLangMenu__]: #class-__qprogeditqlangmenu__
[function __QProgEdit\.QLangMenu\.\_\_init\_\___\(tabCornerWidget\)]: #function-__qprogeditqlangmenu__init____tabcornerwidget
[function __QProgEdit\.QLangMenu\.setLang__\(action\)]: #function-__qprogeditqlangmenusetlang__action
[function __QProgEdit\.QLexer__\(editor, lang=u'text', colorScheme=u'Default'\)]: #function-__qprogeditqlexer__editor-langutext-colorschemeudefault
[class __QProgEdit.QProgEdit__]: #class-__qprogeditqprogedit__
[function __QProgEdit\.QProgEdit\.\_\_init\_\___\(tabManager, dPrint=None, title=u'Empty document', \*\*editorParams\)]: #function-__qprogeditqprogedit__init____tabmanager-dprintnone-titleuempty-document-editorparams
[function __QProgEdit\.QProgEdit\.dPrint__\(msg\)]: #function-__qprogeditqprogeditdprint__msg
[function __QProgEdit\.QProgEdit\.focusTab__\(\)]: #function-__qprogeditqprogeditfocustab__
[function __QProgEdit\.QProgEdit\.tabIndex__\(\)]: #function-__qprogeditqprogedittabindex__
[function __QProgEdit\.QProgEdit\.toggle__\(widget, visible\)]: #function-__qprogeditqprogedittoggle__widget-visible
[function __QProgEdit\.QProgEdit\.toggleFind__\(visible\)]: #function-__qprogeditqprogedittogglefind__visible
[function __QProgEdit\.QProgEdit\.togglePrefs__\(visible\)]: #function-__qprogeditqprogedittoggleprefs__visible
[class __QProgEdit.QSymbolTreeWidgetItem__]: #class-__qprogeditqsymboltreewidgetitem__
[function __QProgEdit\.QSymbolTreeWidgetItem\.\_\_init\_\___\(editor, lineNo, \_type, name, argSpec\)]: #function-__qprogeditqsymboltreewidgetitem__init____editor-lineno-_type-name-argspec
[function __QProgEdit\.QSymbolTreeWidgetItem\.activate__\(\)]: #function-__qprogeditqsymboltreewidgetitemactivate__
[class __QProgEdit.QTabCornerWidget__]: #class-__qprogeditqtabcornerwidget__
[function __QProgEdit\.QTabCornerWidget\.\_\_init\_\___\(tabManager, msg=None, handlerButtonText=None, runButton=False\)]: #function-__qprogeditqtabcornerwidget__init____tabmanager-msgnone-handlerbuttontextnone-runbuttonfalse
[function __QProgEdit\.QTabCornerWidget\.handlerButtonClicked__\(\)]: #function-__qprogeditqtabcornerwidgethandlerbuttonclicked__
[function __QProgEdit\.QTabCornerWidget\.update__\(\)]: #function-__qprogeditqtabcornerwidgetupdate__
[class __QProgEdit.QTabManager__]: #class-__qprogeditqtabmanager__
[function __QProgEdit\.QTabManager\.\_\_init\_\___\(parent=None, cfg=<QProgEdit\.\_qeditorcfg\.QEditorCfg object at 0x7f73885d59d0>, tabsClosable=False, tabsMovable=False, msg=None, handlerButtonText=None, runButton=False\)]: #function-__qprogeditqtabmanager__init____parentnone-cfgqprogedit_qeditorcfgqeditorcfg-object-at-0x7f73885d59d0-tabsclosablefalse-tabsmovablefalse-msgnone-handlerbuttontextnone-runbuttonfalse
[function __QProgEdit\.QTabManager\.addTab__\(title=u'Empty document', select=True\)]: #function-__qprogeditqtabmanageraddtab__titleuempty-document-selecttrue
[function __QProgEdit\.QTabManager\.applyCfg__\(\)]: #function-__qprogeditqtabmanagerapplycfg__
[function __QProgEdit\.QTabManager\.closeTab__\(index=None\)]: #function-__qprogeditqtabmanagerclosetab__indexnone
[function __QProgEdit\.QTabManager\.isAnyModified__\(\)]: #function-__qprogeditqtabmanagerisanymodified__
[function __QProgEdit\.QTabManager\.runSelectedText__\(\)]: #function-__qprogeditqtabmanagerrunselectedtext__
[function __QProgEdit\.QTabManager\.runText__\(\)]: #function-__qprogeditqtabmanagerruntext__
[function __QProgEdit\.QTabManager\.selectTab__\(index\)]: #function-__qprogeditqtabmanagerselecttab__index
[function __QProgEdit\.QTabManager\.selectedText__\(index=None, currentLineFallback=False\)]: #function-__qprogeditqtabmanagerselectedtext__indexnone-currentlinefallbackfalse
[function __QProgEdit\.QTabManager\.setFocus__\(index=None\)]: #function-__qprogeditqtabmanagersetfocus__indexnone
[function __QProgEdit\.QTabManager\.setText__\(text, index=None\)]: #function-__qprogeditqtabmanagersettext__text-indexnone
[function __QProgEdit\.QTabManager\.switchTabLeft__\(\)]: #function-__qprogeditqtabmanagerswitchtableft__
[function __QProgEdit\.QTabManager\.switchTabRight__\(\)]: #function-__qprogeditqtabmanagerswitchtabright__
[function __QProgEdit\.QTabManager\.tab__\(index=None\)]: #function-__qprogeditqtabmanagertab__indexnone
[function __QProgEdit\.QTabManager\.tabChanged__\(index\)]: #function-__qprogeditqtabmanagertabchanged__index
[function __QProgEdit\.QTabManager\.tabIndex__\(index=None\)]: #function-__qprogeditqtabmanagertabindex__indexnone
[function __QProgEdit\.QTabManager\.tabs__\(\)]: #function-__qprogeditqtabmanagertabs__
[function __QProgEdit\.QTabManager\.text__\(index=None\)]: #function-__qprogeditqtabmanagertext__indexnone
[function __QProgEdit\.QTabManager\.toggleFind__\(visible\)]: #function-__qprogeditqtabmanagertogglefind__visible
[function __QProgEdit\.QTabManager\.togglePrefs__\(visible\)]: #function-__qprogeditqtabmanagertoggleprefs__visible
[class __QProgEdit.QUiLoader__]: #class-__qprogeditquiloader__
[function __QProgEdit\.QUiLoader\.loadUi__\(name\)]: #function-__qprogeditquiloaderloadui__name