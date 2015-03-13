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

INHIBIT_WORD_COMPLETIONS = False
INHIBIT_EXPLICIT_COMPLETIONS = False

pmx = qapplication()
SETTINGS = {}

def load_settings(base_name):
    if base_name not in SETTINGS:
        if base_name == "Preferences.sublime-settings":
            SETTINGS[base_name] = Settings(pmx.profile().settings)
        else:
            path = os.path.join(DESCRIPTOR.path, base_name)
            settings = json.read_file(path)
            if settings:
                SETTINGS[base_name] = Settings(PrymatexSettings(base_name, settings))
    return SETTINGS[base_name]

def active_window():
    return Window(pmx.currentWindow())

def set_timeout(callback, delay):
    pmx.setTimeout(delay / 1000, callback)
