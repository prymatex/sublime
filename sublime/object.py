#!/usr/bin/env python

from prymatex.qt import QtCore
from prymatex.utils import text as textutils

class SublimeObject(QtCore.QObject):
    runCommand = QtCore.Signal(str, dict)
    def __init__(self, component):
        super().__init__(parent=component)
        self._component = component
        self._commands = {}
        self._listeners = []
        
    def id(self):
        """id() int Returns a number that uniquely identifies this component."""
        return id(self._component)
    
    def add_command(self, command):
        names = textutils.camelcase_to_text(command.__class__.__name__).split()
        name = "_".join(names[:-1])
        self._commands[name] = command

    def run_command(self, name, args=None):
        """ return None    
        Runs the named Command with the (optional) given arguments. run_command is able to run both any sort of command, dispatching the command via input focus.
        """
        print("run", name, args)
        self.runCommand.emit(name, args or {})
