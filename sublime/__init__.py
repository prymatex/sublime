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
SETTINGS = {
    "Preferences.sublime-settings": Settings(
        pmx.settingsManager.prymatex_settings
    )
}

def load_settings(base_name):
    if base_name not in SETTINGS:
        for package in pmx.packageManager.packages.values():
            path = os.path.join(package.directory, base_name)
            print(package, path)
            if os.path.exists(path):
                settings = pmx.settingsManager.getSettings(path)
                SETTINGS[base_name] = Settings(settings)
    return SETTINGS.get(base_name, None)

def active_window():
    return Window(pmx.currentWindow())

def set_timeout(callback, delay):
    pmx.setTimeout(delay / 1000, callback)
