"""
File: TUAHiddenPassage.py
Author: Ben Gardner
Created: July 27, 2015
Revised: November 11, 2022
"""


import random


class HiddenPassage:

    name = "Hidden Passage"
    audio = "Buscagardzia"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.albanianDesert
        ent1 = self.entrance1
        tun1 = self.tunnel1
        bend = self.bend
        gann = self.gan
        splt = self.split
        toys = self.toys
        glow = self.glow
        tun2 = self.tunnel2
        ent2 = self.entrance2
        wrp2 = self.greece
        wrp3 = self.toMerchant
        mrch = self.merchant
        
        
        self.spots = [
            [None, None, None, None, None, None, None],
            [None, wrp1, None, mrch, None, None, None],
            [None, ent1, None, None, None, None, None],
            [None, tun1, None, None, None, None, None],
            [None, bend, gann, splt, toys, None, None],
            [None, None, None, glow, None, None, None],
            [None, None, None, tun2, wrp3, None, None],
            [None, None, None, ent2, None, None, None],
            [None, None, None, wrp2, None, None, None],
            [None, None, None, None, None, None, None]]
        
        e = {'Turbid Adurbid': 5,
             'Dark Asp': 6,
             'Skeleton Arcanist': 6,
             'Ninja': 2}
             
        self.encounters = {wrp1: {},
                           wrp2: {},
                           wrp3: {},
                           ent1: {},
                           tun1: e,
                           bend: e,
                           gann: {},
                           splt: e,
                           toys: e,
                           glow: e,
                           tun2: e,
                           mrch: {},
                           ent2: {}
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

    def albanianDesert(self, selectionIndex=None):
        X = 7
        Y = 35
        return self.actions({'area': "Albanian Desert",
                             'coordinates': (X, Y)})

    def greece(self, selectionIndex=None):
        X = 1
        Y = 7
        return self.actions({'area': "Greece",
                             'coordinates': (X, Y)})

    def toMerchant(self, selectionIndex=None):
        X = 3
        Y = 1
        return self.actions({'area': "Hidden Passage",
                             'coordinates': (X, Y)})

    def entrance1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        merc1 = "Qendresa"
        merc2 = "Barrie"
        if "Hidden Passage" not in self.c.flags:
            self.text = ("Toshe: I need to get to Greece and find out who" +
                         " really has the Key to Macedonia.")
            if self.c.hasMercenary(merc1):
                self.text += ("\n%s: Yes. We must also stop Silvio." % merc1 +
                              " It is likely that he escaped through this" +
                              " wall.")
            elif self.c.hasMercenary(merc2):
                self.text += ("\n%s: Everything's comin' together now." % merc2)
            self.c.flags['Hidden Passage'] = True
        return self.actions()

    def tunnel1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def bend(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def gan(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and "Gan Passage" not in self.c.flags:
            self.text = ("You shine your flashlight on the man." +
                         "\nGan: Hello." +
                         "\nToshe: Hey! It's you again!" +
                         "\nGan: Yes. I meditate in this cave." +
                         "\nToshe: Well, it's actually a wall, but--" +
                         "\nGan: Come closer." +
                         "\nGan pulls you toward him and covers your mouth." +
                         "\nThings go black for a moment." +
                         "\nGan: You are learning well, pupil.")
            self.c.flags['Gan Passage'] = True
            return self.actions({'skill': "Inner Zen",
                                 'cost': 0})
        elif selectionIndex == 0:
            kills = self.c.flags['Kills']
            animalPowers = self.c.flags['Animal Powers']
            random.seed(self.c.xp)
            suffix = random.choice(["Stab", "Slice", "Smash", "Sever"])
            if (("Giant Seal2" in kills and
                 "Giant Seal2" not in animalPowers) or
                ("Giant Shark2" in kills and
                 "Giant Shark2" not in animalPowers) or
                ("Giant Salamander2" in kills and
                 "Giant Salamander2" not in animalPowers) or
                ("Giant Scorpion2" in kills and
                 "Giant Scorpion2" not in animalPowers) or
                ("Giant Scarab2" in kills and
                 "Giant Scarab2" not in animalPowers)):
                self.text = ("Gan: Toshe, you are ready now." +
                             " Go right when you are prepared to ascend.")
                self.c.flags['Animal Ascension'] = True
            elif len(self.c.flags['Animal Powers']) == 5:
                self.text = ("Gan: True power is a lifelong quest.")
            else:
                self.text = ("Gan: If you seek true power, you must become" +
                             " one with nature and all its beasts, small and" +
                             " large. Giant too. Specifically giant. Speak to" +
                             " me when you have done this.")
        elif "Gan Passage" not in self.c.flags:
            self.imageIndex = 9
            self.text = ("You see someone holding their chest, who" +
                         " looks like they may be in pain.")
            self.menu = ["Talk to the person."]
        elif ("Gan Passage" in self.c.flags and
              "Animal Powers" not in self.c.flags):
            self.text = ("Gan: If you seek true power, you must become" +
                         " one with nature and all its beasts, small and" +
                         " large. Giant too. Specifically giant. Speak to" +
                         " me when you have done this.")
            self.c.flags['Animal Powers'] = dict()
        # Check for any killed rare giants whose power has not been claimed
        elif ("Gan Passage" in self.c.flags):
            self.text = random.choice([
                "Gan: If I can sleep tonight and wake tomorrow, I am" +
                " grateful, for the road ahead may be daunting, but" +
                " it is many times worth the journey.",
                "Gan: What lies beyond is of no concern to me. What" +
                " matters is the present. Make use of today.",
                "Gan: I find the cave to be quite peaceful.",
                "Gan: The things I found useful once before are now" +
                " dated and inadequate. It is a constant struggle to" +
                " survive in this evolving world.",
                "Gan: Are you still here, Toshe?"])
            self.menu = ["Talk to Gan."]
            
        return self.actions()

    def split(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def toys(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        suffix = None
        animal = None
        if "Animal Ascension" in self.c.flags:
            del self.c.flags['Animal Ascension']
            kills = self.c.flags['Kills']
            animalPowers = self.c.flags['Animal Powers']
            suffix = random.choice(["Stab", "Slice", "Smash", "Sever"])
            if ( "Giant Seal2" in kills and
                 "Giant Seal2" not in animalPowers):
                self.text = ("You bask in the light as otarine" +
                             " energy flows into you.")
                self.c.flags['Animal Powers']['Giant Seal2'] = 1
                animal = "Seal"
            elif ("Giant Shark2" in kills and
                  "Giant Shark2" not in animalPowers):
                self.text = ("You bask in the light as piscine" +
                             " energy flows into you.")
                self.c.flags['Animal Powers']['Giant Shark2'] = 1
                animal = "Shark"
            elif ("Giant Salamander2" in kills and
                  "Giant Salamander2" not in animalPowers):
                self.text = ("You bask in the light as salamandrine" +
                             " energy flows into you.")
                self.c.flags['Animal Powers']['Giant Salamander2'] = 1
                animal = "Salamander"
            elif ("Giant Scorpion2" in kills and
                  "Giant Scorpion2" not in animalPowers):
                self.text = ("You bask in the light as venomous" +
                             " energy flows into you.")
                self.c.flags['Animal Powers']['Giant Scorpion2'] = 1
                animal = "Scorpion"
            elif ("Giant Scarab2" in kills and
                  "Giant Scarab2" not in animalPowers):
                self.text = ("You bask in the light as insectine" +
                             " energy flows into you.")
                self.c.flags['Animal Powers']['Giant Scarab2'] = 1
                animal = "Scarab"
            return self.actions({'skill': "%s %s" % (animal, suffix),
                                 'cost': 0,
                                 'save': True})
        else:
            self.text = ("Light shines in through the cracks in the wall upon" +
                         " ancient oriental artifacts scattered about.")
        return self.actions()

    def glow(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tunnel2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if "Passage Merchant" not in self.c.flags:
            self.text = ("You spot a man to the right with a contraption for"+
                         " holding sacks on his back.")
        else:
            self.text = ("You see the merchant in the corner.")
        return self.actions()

    def entrance2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def merchant(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 6
            return self.actions({'area': "Hidden Passage",
                                 'coordinates': (X, Y)})
        npc = "Merchant"
        if "Buyback Items" not in self.c.flags:
            self.c.flags['Buyback Items'] = [None]*9
        self.c.flags['Passage Merchant'] = True
        self.text = npc+": " + random.choice(
            ["I'm a collector.",
             "Macedonia? Exit the tunnel, then go east and slightly north" +
             " until you reach the highlands.",
             "I'll buy and sell most anything."])
        self.menu = ["Return to the tunnel."]
        return self.actions({'items for sale': self.c.flags['Buyback Items'],
                             'buyback': True})
