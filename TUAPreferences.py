"""
File: TUAPreferences.py
Author: Ben Gardner
Created: November 5, 2022
Revised: November 12, 2022
"""

from collections import OrderedDict

class Max6LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)
        while len(self) > 6:
            del self[self.items()[0][0]]

class Preferences:

    def __init__(self):
        self.musicOn = True
        self.sfxOn = True
        self.recentCharacters = Max6LastUpdatedOrderedDict()
