# -*- coding: cp1252 -*-
"""
File: TUAGalijula.py
Author: Ben Gardner
Created: April 22, 2016
Revised: October 25, 2022
"""


import random


class Galijula:
    
    name = "Galijula"
    audio = "On Thin Ice"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.adriaticSea
        wrp2 = self.fartooqHold
        entr = self.entrance
        ltRt = self.leftRight
        arcL = self.arcLeft
        arcR = self.arcRight
        upRt = self.upRight
        upLt = self.upLeft
        notL = self.notLeft
        notR = self.notRight
        upD1 = self.upDown1
        upD2 = self.upDown2
        dnRt = self.downRight
        dnLt = self.downLeft
        path = self.path
        aval = self.avalanche
        icC1 = self.iceCorridor1
        icW1 = self.iceWall1
        cra1 = self.crack1
        icW2 = self.iceWall2
        gla1 = self.glacier1
        gla2 = self.glacier2
        icC2 = self.iceCorridor2
        icW3 = self.iceWall3
        cra2 = self.crack2
        cavE = self.caveEntrance
        atak = self.avalancheAttack
        hol1 = self.hole1
        hol2 = self.hole2
        
        
        self.spots = [
            [None, None, None, None, None, None, None, None],
            [None, atak, None, None, wrp2, None, None, None],
            [None, None, None, None, cavE, None, None, None],
            [None, None, icC2, icW3, cra2, hol2, None, None],
            [None, None, gla2, None, None, None, None, None],
            [None, None, gla1, icW2, icW1, cra1, hol1, None],
            [None, None, None, None, icC1, None, None, None],
            [None, None, None, None, aval, None, None, None],
            [None, None, dnRt, ltRt, path, ltRt, dnLt, None],
            [None, None, upD1, None, None, None, upD2, None],
            [None, None, notL, ltRt, None, ltRt, notR, None],
            [None, None, upRt, arcL, ltRt, arcR, upLt, None],
            [None, None, None, None, entr, None, None, None],
            [None, None, None, None, wrp1, None, None, None],
            [None, None, None, None, None, None, None, None]
            ]
        
        e = {'Horn Dog': 20,
             'Horn Beast': 10,
             'Eyeless Yeti': 10}
        e2 = {'Horn Beast': 20,
              'Eyeless Yeti': 10,
              'Frost Dragon': 10}
             
        self.encounters = {wrp1: {},
                           wrp2: {},
                           entr: {},
                           ltRt: e,
                           arcL: e,
                           arcR: e,
                           upRt: e,
                           upLt: e,
                           notL: e,
                           notR: e,
                           upD1: e,
                           upD2: e,
                           dnRt: e,
                           dnLt: e,
                           path: e,
                           aval: {},
                           icC1: e2,
                           icW1: e2,
                           cra1: e2,
                           icW2: e2,
                           gla1: e2,
                           gla2: e2,
                           icC2: e2,
                           icW3: e2,
                           cra2: e2,
                           cavE: e2,
                           atak: {},
                           hol1: e2,
                           hol2: e2,
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
    
    def adriaticSea(self, selectionIndex=None):
        X = 8
        Y = 15
        return self.actions({'area': "Adriatic Sea",
                             'coordinates': (X, Y)})
    
    def fartooqHold(self, selectionIndex=None):
        X = 4
        Y = 9
        return self.actions({'area': "Fartooq Hold",
                             'coordinates': (X, Y)})
    
    def hole1(self, selectionIndex=None):
        self.c.flags['Fell in a Hole'] = True
        X = 10
        Y = 7
        return self.actions({'area': "Adriatic Sea",
                             'coordinates': (X, Y)})
    
    def hole2(self, selectionIndex=None):
        self.c.flags['Fell in a Hole'] = True
        X = 9
        Y = 5
        return self.actions({'area': "Adriatic Sea",
                             'coordinates': (X, Y)})
    
    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Galijula" not in self.c.flags:
            self.c.flags['Galijula'] = True
            self.text = ("Toshe: Where am Ï now?")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Eh, s-some s-sort of" +
                              " f-f-frozen island?" +
                              "\nToshe: I didn't think we swam that far north.")
            else:
                self.text += (" I didn't think I swam that far north.")
        return self.actions()
    
    def leftRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def arcLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def arcRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def upRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def upLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def notLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if ( "Galijula Left Ambush" not in self.c.flags):
            self.c.flags['Galijula Left Ambush'] = True
            self.view = "battle"
            self.text = "You are ambushed by a yeti!"
            return self.actions({'enemy': "Angry Eyeless Yeti",
                                 'mercenaries': self.c.mercenaries})
        return self.actions()
    
    def notRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if ( "Galijula Right Ambush" not in self.c.flags):
            self.c.flags['Galijula Right Ambush'] = True
            self.view = "battle"
            self.text = "You are ambushed by a yeti!"
            return self.actions({'enemy': "Angry Eyeless Yeti",
                                 'mercenaries': self.c.mercenaries})
        return self.actions()
    
    def upDown1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def upDown2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def downRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def downLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def path(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def avalanche(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        if "Avalanche Attack" not in self.c.flags:
            X = 1
            Y = 1
            return self.actions({'area': "Galijula",
                                 'coordinates': (X, Y)})
        elif ("Avalanche Wait" not in self.c.flags and
              "Avalanche Aftermath" not in self.c.flags):
            hpLoss = random.randint(200, 300)
            self.text = ("You trudge through heavy snow for" +
                         " a few minutes until a loud noise is heard" +
                         " up ahead. Snow crashes down on you, dealing" +
                         " %s damage." % hpLoss +
                         "\nToshe: Damn it!")
            self.c.hp -= hpLoss
            self.c.flags['Avalanche Aftermath'] = True
        elif "Avalanche Aftermath" not in self.c.flags:
            self.text = ("The avalanche stops and the path is clear.")
            self.c.flags['Avalanche Aftermath'] = True
            
        return self.actions()
    
    def iceCorridor1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def iceWall1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def crack1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def iceWall2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def glacier1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def glacier2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def iceCorridor2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def iceWall3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 21
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def crack2(self, selectionIndex=None):
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
        if ( "Galijula Cave Ambush" not in self.c.flags):
            self.c.flags['Galijula Cave Ambush'] = True
            self.view = "battle"
            self.text = "You are ambushed by a yeti!"
            return self.actions({'enemy': "Angry Eyeless Yeti",
                                 'mercenaries': self.c.mercenaries})
        if (self.c.hasItem("Oracular Orb")):
            self.text = ("The oracular orb escapes your grasp and returns" +
                         " to the cave.")
            self.c.removeItem(self.c.indexOfItem("Oracular Orb"))
        
        return self.actions()

    def avalancheAttack(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 24
        self.text = None
        self.helpText = None
        self.menu = []
        if "Avalanche Attack" in self.c.flags:
            X = 4
            Y = 7
            return self.actions({'area': "Galijula",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0 and "Avalanche Wait" not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            self.text = ("You wait and watch as the snow rushes down the" +
                         " slope." +
                         "\nYou hear a war cry echo throughout the sky." +
                         " Suddenly, a dragon swoops down to attack!")
            self.tempFlag = "Avalanche Wait"
            self.menu = ["Brace yourself."]
            return self.actions()
        elif "Avalanche Wait" in self.c.flags:
            self.view = "battle"
            self.c.flags["Avalanche Attack"] = True
            return self.actions({'enemy': "Frost Dragon"})
        elif selectionIndex == 1:
            self.c.flags['Avalanche Attack'] = True
            X = 4
            Y = 7
            return self.actions({'area': "Galijula",
                                 'coordinates': (X, Y)})

        elif self.c.hasMercenary("Qendresa"):
            self.text = ("Qendresa: Halt. I can see an abundance of snow on" +
                         " the hill ahead. We can stay back and let the snow" +
                         " fall or continue and risk being caught in it.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Whaddya think, Toshe?")
        else:
            self.text = ("There is an impending avalanche ahead.")
        self.menu = ["Wait.",
                     "Proceed."]
        return self.actions()
