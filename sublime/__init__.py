#!/usr/bin/env python
# Sublime qt abstraction layer

import os
import threading

from prymatex.qt import QtCore
from prymatex.qt.helpers import qapplication
from prymatex.utils import json
from prymatex.utils.settings import Settings as PrymatexSettings

from .edit import Edit
from .region import Region
from .selection import Selection
from .settings import Settings
from .view import View
from .window import Window
from sublime_plugin import LISTENERS

CLASS_EMPTY_LINE = 1 << 8  #256
CLASS_LINE_END = 1 << 7 #128
CLASS_LINE_START = 1 << 6 #64
CLASS_PUNCTUATION_END = 1 << 3 #8
CLASS_PUNCTUATION_START = 1 << 2 #4
CLASS_SUB_WORD_END = 1 << 5 #32
CLASS_SUB_WORD_START = 1 << 4 #16
CLASS_WORD_END = 1 << 1 #2
CLASS_WORD_START = 1 << 0 #1
COOPERATE_WITH_AUTO_COMPLETE = 1 << 1 #2
DIALOG_CANCEL = 0 #0
DIALOG_NO = 1 << 1 #2
DIALOG_YES = 1 << 0 #1
DRAW_EMPTY = 1 << 0 #1
DRAW_EMPTY_AS_OVERWRITE = 1 << 2 #4
DRAW_NO_FILL = 1 << 5 #32
DRAW_NO_OUTLINE = 1 << 8 #256
DRAW_OUTLINED = 1 << 5 #32
DRAW_SOLID_UNDERLINE = 1 << 9 #512
DRAW_SQUIGGLY_UNDERLINE = 1 << 11 #2048
DRAW_STIPPLED_UNDERLINE = 1 << 10 #1024
ENCODED_POSITION = 1 << 0 #1
FORCE_GROUP  = 1 << 3 #8
HIDDEN = 1 << 7 #128
HIDE_ON_MINIMAP = 1 << 1 #2
HTML = 1 << 0 #1
IGNORECASE = 1 << 1 #2
INHIBIT_WORD_COMPLETIONS = 1 << 3 #8
INHIBIT_EXPLICIT_COMPLETIONS = 1 << 4 #16
KEEP_OPEN_ON_FOCUS_LOST = 1 << 1 #2
LITERAL = 1 << 0 #1
MONOSPACE_FONT = 1 << 0 #1
OP_EQUAL = 0 #0
OP_NOT_EQUAL = 1 << 0 #1
OP_NOT_REGEX_CONTAINS = - ~(1 << 2) #5
OP_NOT_REGEX_MATCH = - ~(1 << 1) #3
OP_REGEX_CONTAINS = 1 << 2 #4
OP_REGEX_MATCH = 1 << 1 #2
PERSISTENT = 1 << 4 #16
TRANSIENT = 1 << 2 #4

pmx = qapplication()

SETTINGS = {
    "Preferences.sublime-settings": Settings(
        pmx.settingsManager.prymatex_settings
    )
}

WINDOWS = {
    
}

def load_settings(base_name):
    if base_name not in SETTINGS:
        for package in pmx.packageManager.packages.values():
            path = os.path.join(package.directory, base_name)
            if os.path.exists(path):
                settings = pmx.settingsManager.getSettings(path)
                SETTINGS[base_name] = Settings(settings)
    return SETTINGS.get(base_name, None)

def on_windowCreated(window):
    _id = id(window)
    if _id not in WINDOWS:
        WINDOWS[_id] = Window(pmx, window)

pmx.windowCreated.connect(on_windowCreated)

def active_window():
    window = pmx.currentWindow()
    _id = id(window)
    if _id in WINDOWS:
        return WINDOWS[_id]

def set_timeout(callback, delay, *args, **kwargs):
    timer = threading.Timer(delay / 1000, callback, args, kwargs)
    timer.name = "Sublime Timer"
    timer.start()
