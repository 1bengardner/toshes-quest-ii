"""
File: TUAPreferences.py
Author: Ben Gardner
Created: November 5, 2022
Revised: November 13, 2022
"""

from collections import OrderedDict

class LastUpdatedOrderedDictWithLimit(OrderedDict):
    '''Store items up to LIMIT in the order the keys were last added.
    Items are evicted in FIFO sequence.'''

    LIMIT = 6

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)
        while len(self) > self.LIMIT:
            del self[self.items()[0][0]]

class Preferences:

    def __init__(self):
        self.musicOn = True
        self.sfxOn = True
        self.recentCharacters = LastUpdatedOrderedDictWithLimit()
