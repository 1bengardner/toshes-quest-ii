"""
File: TUAIgaloCathedral.py
Author: Ben Gardner
Created: November 8, 2022
Revised: November 13, 2022
"""

from random import randint

class IgaloCathedral:

    name = "Cathedral of Valour"
    audio = "Gouda"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"
        
        entr = self.entrance
        erth = self.earthMage
        watr = self.waterMage
        fire = self.fireMage
        
        self.spots = [
            [None, None, None, None, None],
            [None, None, watr, None, None],
            [None, erth, None, fire, None],
            [None, None, entr, None, None],
            [None, None, None, None, None],
        ]
        
        self.encounters = None
        
        self.venomblastOrDerecho = None
    
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
    
    def roll(self, numberOfSides=100):
        return randint(1, numberOfSides)
    
    def hasGainedPowerOf(self, animal):
        return "Animal Powers" in self.c.flags and animal in self.c.flags['Animal Powers']
    
    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        
        if selectionIndex == 0:
            X = 1
            Y = 2
            return self.actions({'area': "Igalo Cathedral",
                                 'coordinates': (X, Y)})
        if selectionIndex == 1:
            X = 2
            Y = 1
            return self.actions({'area': "Igalo Cathedral",
                                 'coordinates': (X, Y)})
        if selectionIndex == 2:
            X = 3
            Y = 2
            return self.actions({'area': "Igalo Cathedral",
                                 'coordinates': (X, Y)})
        if selectionIndex == 3:
            X = 2
            Y = 8
            return self.actions({'area': "Igalo",
                                 'coordinates': (X, Y)})
        
        self.text = "You step into the great hall of the archmages' cathedral."
        self.menu = [
            "Visit the Earth Archmage.",
            "Visit the Water Archmage.",
            "Visit the Fire Archmage.",
            "Leave.",
        ]
        
        return self.actions()
    
    def earthMage(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        
        skills = [
            ("Stone Skin", 5000),
            ("Asteroid", 10000),
        ]
        if self.hasGainedPowerOf("Giant Scarab2"):
            if self.venomblastOrDerecho == "Venomblast" or self.venomblastOrDerecho is None and self.hasGainedPowerOf("Giant Scorpion2") and self.roll() > 50:
                skills.append(("Venomblast", 30000))
                self.venomblastOrDerecho = "Venomblast"
            else:
                skills.append(("Derecho", 50000))
                self.venomblastOrDerecho = "Derecho"
        elif self.hasGainedPowerOf("Giant Scorpion2"):
            skills.append(("Venomblast", 30000))
        
        self.menu = ["Learn %s (%s euros)." % (skill[0], skill[1]) for skill in skills]
        self.menu.append("Leave.")
        
        if selectionIndex == len(skills):
            X = 2
            Y = 3
            return self.actions({'area': "Igalo Cathedral",
                                 'coordinates': (X, Y)})
        elif selectionIndex is not None:
            return self.actions({'skill': skills[selectionIndex][0],
                                 'cost': skills[selectionIndex][1]},)
        
        if "Halvar" not in self.c.flags or self.roll() > 50:
            self.text = "%s strokes his beard tentacles slowly.\nHalvar: The wax within my...rather eloquent beard has a strength that rivals even earth magic. Perhaps my conjured rocks are the only thing in this universe that are as hard. Peculiar." % ("Halvar" if "Halvar" in self.c.flags else "The earth archmage")
            self.c.flags['Halvar'] = True
        elif not self.hasGainedPowerOf("Giant Scarab2") and not self.hasGainedPowerOf("Giant Scorpion2"):
            self.text = "Halvar: There exist two special techniques that I can only teach to those whom wield the power of great earthen critters."
        else:
            self.text = "Halvar: It is scientifically proven that lightning may strike twice. In the case of my Derecho, it is magically proven that it will strike nine times. Intriguing, yes?"
        
        return self.actions()
    
    def waterMage(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        
        skills = [
            ("Torrent Funnel", 15000),
            ("Blizzard", 30000),
        ]
        if self.hasGainedPowerOf("Giant Seal2") or self.hasGainedPowerOf("Giant Shark2"):
            skills.append(("Tsunami", 60000))
        
        self.menu = ["Learn %s (%s euros)." % (skill[0], skill[1]) for skill in skills]
        self.menu.append("Leave.")
        
        if selectionIndex == len(skills):
            X = 2
            Y = 3
            return self.actions({'area': "Igalo Cathedral",
                                 'coordinates': (X, Y)})
        elif selectionIndex is not None:
            return self.actions({'skill': skills[selectionIndex][0],
                                 'cost': skills[selectionIndex][1]},)
        
        if "Niles" not in self.c.flags or self.roll() > 50:
            self.c.flags['Niles'] = True
            self.text = "Niles: I am a wizard. Not Santa Claus."
        elif not self.hasGainedPowerOf("Giant Seal2") and not self.hasGainedPowerOf("Giant Shark2"):
            self.text = "Niles: Once you have slain and absorbed the power of a great water beast, you may learn my final spell."
        else:
            self.text = "Niles: A fresh bath will cleanse the soul. A strong Tsunami will surely kill you."
        
        return self.actions()
    
    def fireMage(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        
        skills = [
            ("Burning Mind", 2500),
            ("Immolation", 25000),
        ]
        if self.hasGainedPowerOf("Giant Salamander2"):
            skills.append(("Eruption", 45000))
        
        self.menu = ["Learn %s (%s euros)." % (skill[0], skill[1]) for skill in skills]
        self.menu.append("Leave.")
        
        if selectionIndex == len(skills):
            X = 2
            Y = 3
            return self.actions({'area': "Igalo Cathedral",
                                 'coordinates': (X, Y)})
        elif selectionIndex is not None:
            return self.actions({'skill': skills[selectionIndex][0],
                                 'cost': skills[selectionIndex][1]},)
        
        if "Aiden" not in self.c.flags or self.roll() > 50:
            self.c.flags['Aiden'] = True
            self.text = "Aiden: Greetings, mage. I hail from the United States. My cosplay group told me to come check this place out."
        elif not self.hasGainedPowerOf("Giant Salamander2"):
            self.text = "Aiden: Return to me after you conquer the amphibious fire beast."
            self.text += "\nToshe: Wait...what fire beast?"
            self.text += "\nAiden: Its name is Meltmaw the Magical. It is located somewhere in Eastern Kosovo."
            self.text += "\nToshe: Are you making this up?"
            self.text += "\nAiden: I am one-hundred percent serious. After you gain its power, I shall bestow mighty knowledge within you."
        else:
            self.text = "Aiden: Why, yes. My armour is one-hundred percent authentic. Its defence value is zero with absolutely no resistances whatsoever. However, it is authentic."
        
        return self.actions()