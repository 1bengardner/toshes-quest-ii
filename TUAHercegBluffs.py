"""
File: TUAHercegBluffs.py
Author: Ben Gardner
Created: May 20, 2013
Revised: November 14, 2022
"""


class HercegBluffs:

    name = "Billowing Bluffs"
    audio = "Hummingbird"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp2 = self.hercegNovi
        entr = self.entrance
        main = self.mainPoint
        side = self.hillside
        rigt = self.right
        tip1 = self.tip1
        crtr = self.crater
        fork = self.fork
        tip2 = self.tip2
        slp1 = self.slope1
        wall = self.wall
        path = self.path
        bowl = self.bowl
        crve = self.curve
        tip3 = self.tip3
        grvl = self.gravel
        slp2 = self.slope2
        stns = self.stones
        grs1 = self.grass1
        rbbl = self.rubble
        hkrs = self.hikers
        flat = self.flat
        grs2 = self.grass2
        slp3 = self.slope3
        cave = self.caveEntrance
        lft1 = self.left1
        lft2 = self.left2
        grs3 = self.grass3
        grs4 = self.grass4
        rock = self.rock
        bend = self.bend
        mtns = self.mountains
        twst = self.twist
        fogy = self.foggy
        wrp1 = self.igalo
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, tip2, None, None, tip1, None, None],
            [None, None, None, None, tip3, fork, crtr, side, main, rigt, None],
            [None, None, None, None, crve, slp1, None, None, entr, None, None],
            [None, None, None, None, wall, path, None, None, wrp2, None, None],
            [None, None, None, None, grvl, bowl, None, None, None, None, None],
            [None, None, None, slp3, slp2, None, tip2, None, None, None, None],
            [None, lft1, grs2, grs1, stns, rbbl, flat, cave, None, None, None],
            [None, None, lft2, grs3, hkrs, rock, bend, None, None, None, None],
            [None, None, None, grs4, bowl, None, None, None, None, None, None],
            [None, None, None, mtns, None, None, None, None, None, None, None],
            [None, None, None, twst, None, None, None, None, None, None, None],
            [None, None, None, fogy, None, None, None, None, None, None, None],
            [None, None, None, wrp1, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None]]

        e1 = {'Mountain Goblin': 6,
              'Moghi': 6,
              'Divelk': 6,
              'Golem': 2}
        e2 = {'Mountain Goblin': 4,
              'Moghi': 4,
              'Divelk': 4,
              'Golem': 8}
        self.encounters = {wrp2: {},
                           entr: {},
                           main: e1,
                           rigt: e1,
                           tip1: e1,
                           side: e1,
                           crtr: e1,
                           fork: e1,
                           tip2: e1,
                           slp1: e1,
                           tip3: e1,
                           crve: e1,
                           wall: e1,
                           path: e1,
                           grvl: e1,
                           bowl: e1,
                           slp3: e1,
                           slp2: e1,
                           lft1: e1,
                           grs2: e1,
                           grs1: e1,
                           stns: e1,
                           rbbl: e2,
                           flat: e2,
                           cave: e2,
                           lft2: e1,
                           grs3: e1,
                           hkrs: e1,
                           rock: e2,
                           bend: e2,
                           grs4: e1,
                           mtns: e1,
                           twst: e1,
                           fogy: {},
                           wrp1: {}}
    
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

    def igalo(self, selectionIndex=None):
        X = 1
        Y = 5
        return self.actions({'area': "Igalo",
                             'coordinates': (X, Y)})

    def hercegNovi(self, selectionIndex=None):
        X = 1
        Y = 2
        return self.actions({'area': "Herceg Novi",
                             'coordinates': (X, Y)})

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def mainPoint(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def hillside(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def right(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tip1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def crater(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def fork(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tip2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def slope1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def wall(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def path(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def bowl(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def curve(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tip3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def gravel(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def slope2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def stones(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def grass1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        if ( "Barrie Bluffs Remark" not in self.c.flags and
             self.c.hasMercenary("Barrie")):
            self.c.flags['Barrie Bluffs Remark'] = True
            self.text = ("Barrie sniffs the air." +
                         "\nBarrie: I smell something very dank nearby.")
        return self.actions()

    def rubble(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def hikers(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("Hiker: Don't get lost up here! Igalo is south from "+
                     "here and Herceg Novi is northeast.")
        return self.actions()

    def flat(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def grass2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 21
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def slope3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 22
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def caveEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 23
        self.text = None
        self.helpText = None
        self.menu = []
        if ( selectionIndex == 0 and
             "Moved Boulders" not in self.c.flags):
            self.c.flags['Moved Boulders'] = True
        elif selectionIndex == 0:
            X = 3
            Y = 2
            return self.actions({'area': "Golem Cavern: Floor 1",
                                 'coordinates': (X, Y)})            
            
        if "Moved Boulders" not in self.c.flags:
            self.c.flags['Vismurg Entrance Found'] = True
            self.text = ("There is a large cave in the mountainside. The "+
                         "opening is closed in, and it doesn't look like just "+
                         "human strength could move the rocks away.")
        elif "Moved Boulders Aftermath" not in self.c.flags:
            self.imageIndex = 34
            self.text = ("The pile of rocks comes crashing down with" +
                         " the power of your magical energy.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Time to explore.")
            self.c.flags['Moved Boulders Aftermath'] = True
        elif "Climbing Up" in self.c.flags:
            self.c.flags['Golem Cavern Complete'] = True
            del self.c.flags['Climbing Up']
            self.imageIndex = 33
            self.text = ("You climb up the vines to find yourself back at the" +
                         " cave entrance.")
        elif "Golem Cavern Complete" not in self.c.flags:
            self.imageIndex = 34
            self.text = ("There is a magical force deep inside the cave.")
        else:
            self.imageIndex = 33
            self.text = ("There is a secluded cave in the mountainside.")

        if ( "Avalanche" in [skill.NAME for skill in self.c.skills] and
             "Moved Boulders" not in self.c.flags):
            self.menu = ["Cast Avalanche."]
        elif "Moved Boulders" in self.c.flags:
            self.menu = ["Enter the cave."]

        return self.actions()

    def left1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 24
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def left2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 25
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def grass3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 26
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def grass4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 27
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def rock(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 28
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def bend(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 29
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def mountains(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 30
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def twist(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 31
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def foggy(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 32
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
