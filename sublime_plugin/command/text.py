#!/usr/bin/env python

from prymatex.gui.codeeditor.modes import CodeEditorComplitionMode

TEXT_COMMANDS = []

class TextCommandMeta(type):
    def __new__(meta, name, bases, dct):
        super_new = super(TextCommandMeta, meta).__new__

        # Also ensure initialization is only performed for subclasses of TextCommandMeta
        # (excluding TextCommandMeta class itself).
        parents = [b for b in bases if isinstance(b, TextCommandMeta)]
        if not parents:
            return super_new(meta, name, bases, dct)
            
        new_class = super_new(meta, name, bases, dct)
        TEXT_COMMANDS.append(new_class)
        return new_class

class TextCommand(metaclass=TextCommandMeta):
    def __init__(self, view):
        self.view = view

    def run(self, edit, *args, **kwargs):
        """None Called when the command is run.
        """
        pass
    
    def is_enabled(self, *args, **kwargs):
        """bool Returns true if the command is able to be run at this time. The default implementation simply always returns True.
        """
        pass
        
    def is_visible(self, *args, **kwargs):
        """bool Returns true if the command should be shown in the menu at this time. The default implementation always returns True.
        """
        pass

    def description(self, *args, **kwargs):
        """String Returns a description of the command with the given arguments. Used in the menu, if no caption is provided. Return None to get the default description.
        """
        pass
        
class InsertSnippetCommand(TextCommand):
    pass

class AutoCompleteCommand(TextCommand):
    def __init__(self, view):
        self.view = view
        self.editor = view.editor()
    
    def run(self, edit, *args, **kwargs):
        alreadyTyped, start, end = self.editor.wordUnderCursor(direction="left", search=True)
        locations = self.view.sel()
        completions = []
        flags = 0
        for listener in self.view.listeners():
            cmpls, flags = listener.on_query_completions(self.view, alreadyTyped, locations)
            print(cmpls, flags)
            completions.extend(cmpls)
        self.editor.showCompletionWidget(completions, completion_prefix=alreadyTyped)

class HideAutoCompleteCommand(TextCommand):
    def __init__(self, view):
        self.view = view
        self.editor = view.editor()
    
    def run(self, edit, *args, **kwargs):
        print("Fuera bicho")