#!/usr/bin/env python

WINDOW_COMMANDS = []

class WindowCommandMeta(type):
    def __new__(meta, name, bases, dct):
        super_new = super(WindowCommandMeta, meta).__new__

        # Also ensure initialization is only performed for subclasses of WindowCommandMeta
        # (excluding WindowCommandMeta class itself).
        parents = [b for b in bases if isinstance(b, WindowCommandMeta)]
        if not parents:
            return super_new(meta, name, bases, dct)
            
        new_class = super_new(meta, name, bases, dct)
        WINDOW_COMMANDS.append(new_class)
        return new_class

class WindowCommand(object):
    def run(self, *args, **kwargs):
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
