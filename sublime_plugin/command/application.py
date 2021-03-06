#!/usr/bin/env python

APPLICATION_COMMANDS = []

class ApplicationCommandMeta(type):
    def __new__(meta, name, bases, dct):
        super_new = super(ApplicationCommandMeta, meta).__new__

        # Also ensure initialization is only performed for subclasses of ApplicationCommandMeta
        # (excluding ApplicationCommandMeta class itself).
        parents = [b for b in bases if isinstance(b, ApplicationCommandMeta)]
        if not parents:
            return super_new(meta, name, bases, dct)
            
        new_class = super_new(meta, name, bases, dct)
        APPLICATION_COMMANDS.append(new_class)
        return new_class

class ApplicationCommand(metaclass=ApplicationCommandMeta):
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

    def is_checked(self, *args, **kwargs):
        """bool Returns true if a checkbox should be shown next to the menu item. The .sublime-menu file must have the checkbox attribute set to true for this to be used.
        """
        pass
    
    def description(self, *args, **kwargs):
        """String Returns a description of the command with the given arguments. Used in the menu, if no caption is provided. Return None to get the default description.
        """
        pass
