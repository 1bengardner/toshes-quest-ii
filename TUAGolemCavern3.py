"""
File: TUAGolemCavern3.py
Author: Ben Gardner
Created: May 28, 2020
Revised: December 6, 2022
"""


class GolemCavern3:
    
    name = "Golem Cavern"
    audio = "Suken"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        cran = self.cranny
        pitt = self.pit
        walk = self.walkway
        wlk2 = self.walkway2
        corr = self.corridor
        cor2 = self.corridor2
        pill = self.pillars
        rok1 = self.rock1
        rok2 = self.rock2
        rok3 = self.rock3
        rok4 = self.rock4
        
        self.rocksHit = set()
        
        self.spots = [
            [None, None, None, None, None, None, None],
            [None, rok3, wlk2, None, walk, rok1, None],
            [None, None, corr, None, cor2, None, None],
            [None, rok4, pill, pitt, pill, rok2, None],
            [None, None, None, cran, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        
        e = {'Crystal Golem Red': 15}
             
        self.encounters = {cran: {},
                           pitt: e,
                           walk: e,
                           wlk2: e,
                           corr: e,
                           cor2: e,
                           pill: e,
                           rok1: {},
                           rok2: {},
                           rok3: {},
                           rok4: {}
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
    
    def cranny(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.flags['Rising'] = True
            X = 3
            Y = 7
            return self.actions({'area': "Golem Cavern: Floor 2",
                                 'coordinates': (X, Y)})
        self.text = ("You come across a pile of glowing minerals.")
        if "Golem Cranny" not in self.c.flags:
            self.c.flags['Golem Cranny'] = True
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: What powers reside within?")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: These things definitely have" +
                              " some magic in 'em.")
        self.menu = ["Touch the crystals."]
        return self.actions()
    
    def pit(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.flags['Golem Cavern Pit 3'] = True
            X = 3
            Y = 4
            return self.actions({'area': "Simellierm Pit",
                                 'coordinates': (X, Y)})
        if "Golem Cavern Pit 3" in self.c.flags:
            self.imageIndex = 2
            self.menu = ["Descend deeper."]
        if "Going Down" in self.c.flags:
            del self.c.flags['Going Down']
            self.text = "You stumble into a tertiary chamber of the cave."
        elif "Golem Cavern Pit 3" in self.c.flags:
            self.text = "You reach a very deep hole."
        elif "Golem Cavern Sync 3" in self.c.flags:
            self.imageIndex = 2
            self.text = ""
            if self.c.hasMercenary("Qendresa"):
                self.text = "Qendresa: The earth has given way."
            elif self.c.hasMercenary("Barrie"):
                self.text = "Barrie: Whoa, boy! Look at that!"
            self.text += "\nToshe: I must be imagining things."
            self.text = self.text.strip()
            self.menu = ["Venture down the hole."]
        return self.actions()
    
    def walkway(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
        
    def walkway2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def corridor(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
        
    def corridor2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
        
    def pillars(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def rock1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        
        if selectionIndex == 0:
            self.rocksHit.add("Green")
            if "Blue" in self.rocksHit or "White" in self.rocksHit:
                self.rocksHit.discard("Blue")
                self.rocksHit.discard("White")
                self.text = ("The stone plunges into the earth before you" +
                             " have a chance to act.")
                self.text += "\nToshe: That's stupid."
            else:
                self.text = ("You break the stone, shattering it into a" +
                              " million pieces.")
        
        if "Golem Cavern Sync 3" in self.c.flags or "Green" in self.rocksHit:
            self.imageIndex = 3
        else:
            self.menu = ["Strike the green stone."]
        
        return self.actions()
    
    def rock2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        
        if selectionIndex == 0:
            self.rocksHit.add("Blue")
            if not self.rocksHit or "Red" in self.rocksHit and "Green" in self.rocksHit:
                self.text = ("You break the stone, shattering it into a" +
                              " million pieces.")
            else:
                self.rocksHit.discard("Red")
                self.rocksHit.discard("Green")
                self.rocksHit.discard("White")
                self.text = ("The stone plunges into the earth before you" +
                             " have a chance to act.")
                self.text += "\nToshe: That's stupid."
        
        if "Golem Cavern Sync 3" in self.c.flags or "Blue" in self.rocksHit:
            self.imageIndex = 3
        else:
            self.menu = ["Strike the blue stone."]
        
        return self.actions()
    
    def rock3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        
        self.text = ""
        
        if selectionIndex == 0:
            if self.rocksHit:
                self.rocksHit.discard("Green")
                self.rocksHit.discard("Blue")
                self.rocksHit.discard("White")
                self.text = ("The stone plunges into the earth before you" +
                             " have a chance to act.")
                self.text += "\nToshe: That's stupid."
            else:
                self.text = ("You break the stone, shattering it into a" +
                              " million pieces.")
            self.rocksHit.add("Red")
        
        if "Golem Cavern Sync 3" in self.c.flags or "Red" in self.rocksHit:
            self.imageIndex = 3
        else:
            self.menu = ["Strike the red stone."]
                
        self.text = self.text.strip() if self.text else None
        
        return self.actions()
    
    def rock4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        
        self.text = ""
        
        if selectionIndex == 0:
            if len(self.rocksHit) != 3:
                self.rocksHit.discard("Red")
                self.rocksHit.discard("Green")
                self.rocksHit.discard("Blue")
                self.text = ("The stone plunges into the earth before you" +
                             " have a chance to act.")
                self.text += "\nToshe: That's stupid."
            else:
                self.text = ("You break the stone, shattering it into a" +
                              " million pieces.")
                if len(self.rocksHit) == 3:
                    self.c.flags['Golem Cavern Sync 3'] = True
                    self.text += ("\nYou hear the earth shake in the near" +
                                  " distance.")
            self.rocksHit.add("White")
        
        if "Golem Cavern Sync 3" in self.c.flags or "White" in self.rocksHit:
            self.imageIndex = 3
        else:
            self.menu = ["Strike the murky stone."]
        
        if "Golem Prism" not in self.c.flags:
            self.c.flags['Golem Prism'] = True
            self.text = ("You encounter a dark, sunken gemstone buried" +
                         " in the ground.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: It feels...ominous.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Spooky!")
                
        self.text = self.text.strip() if self.text else None
        
        return self.actions()
