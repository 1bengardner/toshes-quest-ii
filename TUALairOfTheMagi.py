"""
File: TUALairOfTheMagi.py
Author: Ben Gardner
Created: October 27, 2022
Revised: October 29, 2022
"""


import random


class LairOfTheMagi:

    name = "Lair of the Magi"
    audio = "Perilous Hour"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        plch = self.placeholder

        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, plch, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, plch, None, None, None, None, None],
            [None, None, None, None, plch, plch, plch, None, None, None, None],
            [None, plch, None, plch, plch, None, plch, plch, None, plch, None],
            [None, None, None, None, plch, plch, plch, None, None, None, None],
            [None, None, None, None, None, plch, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, plch, None, None, None, None, None],
            [None, None, None, None, plch, plch, plch, None, None, None, None],
            [None, None, None, plch, plch, None, plch, plch, None, None, None],
            [None, None, plch, plch, None, None, None, plch, plch, None, None],
            [None, plch, plch, None, None, plch, None, None, plch, plch, None],
            [None, None, plch, plch, None, None, None, plch, plch, None, None],
            [None, None, None, plch, plch, None, plch, plch, None, None, None],
            [None, None, None, None, plch, plch, plch, None, None, None, None],
            [None, None, None, None, None, plch, None, None, None, None, None],
            [None, None, None, None, None, plch, None, None, None, None, None],
            [None, None, None, None, None, plch, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None]]

        self.encounters = {plch: {},
        }

    def movementActions(self):
        pass

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def placeholder(self, selectionIndex=None):
        self.view = "travel"
        self.menu = []
        
        return self.actions()