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
from .window import Window

INHIBIT_WORD_COMPLETIONS = False
INHIBIT_EXPLICIT_COMPLETIONS = False

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
        WINDOWS[_id] = Window(window)

pmx.windowCreated.connect(on_windowCreated)

def active_window():
    window = pmx.currentWindow()
    _id = id(window)
    if _id in WINDOWS:
        return WINDOWS[_id]

def set_timeout(callback, delay):
    pmx.setTimeout(delay / 1000, callback)

