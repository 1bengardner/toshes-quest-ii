"""
File: TUALairOfTheMagi.py
Author: Ben Gardner
Created: October 27, 2022
Revised: October 30, 2022
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
        entr = self.entrance
        spid = self.spiderStairs
        arch = self.archway
        splt = self.split
        dnLt = self.downLeft
        dnRt = self.downRight
        upLt = self.upLeft
        upRt = self.upRight
        noRt = self.noRight
        noLt = self.noLeft
        strU = self.stairsUp
        strD = self.stairsDown
        encL = self.enclaveLeft
        encR = self.enclaveRight
        encU = self.enclaveUp
        noR2 = self.noRight2
        noL2 = self.noLeft2

        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, plch, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, encU, None, None, None, None, None],
            [None, None, None, None, dnRt, plch, dnLt, None, None, None, None],
            [None, plch, None, encL, noR2, None, noL2, encR, None, plch, None],
            [None, None, None, None, upRt, splt, upLt, None, None, None, None],
            [None, None, None, None, None, strD, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, strU, None, None, None, None, None],
            [None, None, None, None, dnRt, plch, dnLt, None, None, None, None],
            [None, None, None, dnRt, upLt, None, upRt, dnLt, None, None, None],
            [None, None, dnRt, upLt, None, None, None, upRt, dnLt, None, None],
            [None, plch, noRt, None, None, plch, None, None, noLt, plch, None],
            [None, None, upRt, dnLt, None, None, None, dnRt, upLt, None, None],
            [None, None, None, upRt, dnLt, None, dnRt, upLt, None, None, None],
            [None, None, None, None, upRt, splt, upLt, None, None, None, None],
            [None, None, None, None, None, arch, None, None, None, None, None],
            [None, None, None, None, None, spid, None, None, None, None, None],
            [None, None, None, None, None, entr, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None]]

        self.encounters = {
            plch: {},
            entr: {},
            spid: {},
            arch: {},
            splt: {},
            dnLt: {},
            dnRt: {},
            upLt: {},
            upRt: {},
            noRt: {},
            noLt: {},
            strU: {},
            strD: {},
            encL: {},
            encR: {},
            encU: {},
            noR2: {},
            noL2: {},
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

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def spiderStairs(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def archway(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def split(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def downLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def downRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def upLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def upRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def noRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def noLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def stairsUp(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def stairsDown(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def enclaveLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def enclaveRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def enclaveUp(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def noRight2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def noLeft2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()