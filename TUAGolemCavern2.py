"""
File: TUAGolemCavern2.py
Author: Ben Gardner
Created: May 26, 2020
Revised: December 6, 2022
"""


class GolemCavern2:
    
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
        wlk2 = self.walkway2
        pill = self.pillars
        rok1 = self.rock1
        rok2 = self.rock2
        rok3 = self.rock3
        
        self.rocksHit = set()
        
        self.spots = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, rok2, None, None, None, None],
            [None, rok3, pill, pitt, wlk2, rok1, None],
            [None, None, None, cran, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        
        e = {'Crystal Golem Blue': 15}
        
        self.encounters = {cran: {},
                           pitt: e,
                           wlk2: e,
                           pill: e,
                           rok1: {},
                           rok2: {},
                           rok3: {}
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
            Y = 11
            return self.actions({'area': "Golem Cavern: Floor 1",
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
            self.c.flags['Golem Cavern Pit 2'] = True
            self.c.flags['Going Down'] = True
            X = 3
            Y = 3
            return self.actions({'area': "Golem Cavern: Floor 3",
                                 'coordinates': (X, Y)})
        if "Golem Cavern Pit 2" in self.c.flags:
            self.imageIndex = 2
            self.menu = ["Descend deeper."]
        if "Going Down" in self.c.flags:
            del self.c.flags['Going Down']
            self.text = "You stumble into a secondary chamber of the cave."
        elif "Rising" in self.c.flags:
            del self.c.flags['Rising']
            self.text = "You rise up through the hole whence you came."
        elif "Golem Cavern Pit 2" in self.c.flags:
            self.text = "You reach a hole leading deeper into the cavern."
        elif "Golem Cavern Sync 2" in self.c.flags:
            self.imageIndex = 2
            self.text = ""
            if self.c.hasMercenary("Qendresa"):
                self.text = "Qendresa: The earth has given way."
            elif self.c.hasMercenary("Barrie"):
                self.text = "Barrie: Whoa, boy! Look at that!"
            self.text += "\nToshe: That wasn't there before...was it?"
            self.text = self.text.strip()
            self.menu = ["Venture down the hole."]
        return self.actions()
        
    def walkway2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
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
            if "Red" in self.rocksHit:
                self.rocksHit.remove("Red")
                self.text = ("The stone plunges into the earth before you" +
                             " have a chance to act.")
                self.text += "\nToshe: That's stupid."
            else:
                self.text = ("You break the stone, shattering it into a" +
                              " million pieces.")
        
        if "Golem Cavern Sync 2" in self.c.flags or "Green" in self.rocksHit:
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
            if "Green" in self.rocksHit or "Red" in self.rocksHit:
                self.rocksHit.discard("Green")
                self.rocksHit.discard("Red")
                self.text = ("The stone plunges into the earth before you" +
                             " have a chance to act.")
                self.text += "\nToshe: That's stupid."
            else:
                self.text = ("You break the stone, shattering it into a" +
                              " million pieces.")
        
        if "Golem Cavern Sync 2" in self.c.flags or "Blue" in self.rocksHit:
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
            if len(self.rocksHit) != 2:
                self.rocksHit.discard("Green")
                self.rocksHit.discard("Blue")
                self.text = ("The stone plunges into the earth before you" +
                             " have a chance to act.")
                self.text += "\nToshe: That's stupid."
            else:
                self.text = ("You break the stone, shattering it into a" +
                              " million pieces.")
                if "Red Shatter" not in self.c.flags:
                    self.c.flags['Red Shatter'] = True
                    if self.c.hasMercenary("Qendresa"):
                        self.text += ("\nQendresa: It was beautiful.")
                if len(self.rocksHit) == 2:
                    self.c.flags['Golem Cavern Sync 2'] = True
                    self.text += ("\nYou hear the earth shake in the near" +
                                  " distance.")
            self.rocksHit.add("Red")
        
        if "Golem Cavern Sync 2" in self.c.flags or "Red" in self.rocksHit:
            self.imageIndex = 3
        else:
            self.menu = ["Strike the red stone."]
        
        if "Golem Garnet" not in self.c.flags:
            self.c.flags['Golem Garnet'] = True
            self.text = ("You encounter a stout, scarlet gemstone protruding" +
                         " from the earth.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: What a marvelous red rock." +
                              " It's magnificent!")
                self.text += ("\nToshe: Yeah.")
                
        self.text = self.text.strip() if self.text else None
        
        return self.actions()
