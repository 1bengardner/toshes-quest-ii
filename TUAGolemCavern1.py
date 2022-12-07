"""
File: TUAGolemCavern1.py
Author: Ben Gardner
Created: May 26, 2017
Revised: December 6, 2022
"""


class GolemCavern1:
    
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

        entr = self.entrance
        pitt = self.pit
        walk = self.walkway
        wlk2 = self.walkway2
        rok1 = self.rock1
        rok2 = self.rock2
        warp = self.warp
        
        self.rocksHit = set()
        
        self.spots = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, rok1, walk, pitt, wlk2, rok2, None],
            [None, None, None, entr, None, None, None],
            [None, None, None, warp, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        
        e = {'Crystal Golem Green': 15}
             
        self.encounters = {entr: {},
                           pitt: e,
                           walk: e,
                           wlk2: e,
                           rok1: {},
                           rok2: {},
                           warp: {}
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
    
    def warp(self, selectionIndex=None):
        X = 7
        Y = 7
        return self.actions({'area': "Herceg Bluffs",
                             'coordinates': (X, Y)})
    
    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Golem Cavern" not in self.c.flags:
            self.c.flags['Golem Cavern'] = True
            self.text = ("You enter the cave and see glimmering, hulking" +
                         " beasts stomping in the distance.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: For what reason might these" +
                              " fine golems take habitation within such" +
                              " vile, musty crannies?")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: I find it rather cozy in here.")
            self.text += ("\nToshe: I think this is a cave.")
        return self.actions()
    
    def pit(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.flags['Golem Cavern Pit 1'] = True
            self.c.flags['Going Down'] = True
            X = 3
            Y = 7
            return self.actions({'area': "Golem Cavern: Floor 2",
                                 'coordinates': (X, Y)})
        if "Golem Cavern Pit 1" in self.c.flags:
            self.imageIndex = 2
            self.menu = ["Descend deeper."]
        if "Rising" in self.c.flags:
            del self.c.flags['Rising']
            self.text = "You rise up through the hole whence you came."
        elif "Golem Cavern Pit 1" in self.c.flags:
            self.text = "You reach a hole leading deeper into the cavern."
        elif "Golem Cavern Sync 1" in self.c.flags:
            self.imageIndex = 2
            self.text = ""
            if self.c.hasMercenary("Qendresa"):
                self.text = "Qendresa: The earth has given way."
            elif self.c.hasMercenary("Barrie"):
                self.text = "Barrie: Whoa, boy! Look at that!"
            self.text += "\nToshe: That wasn't there before."
            self.text = self.text.strip()
            self.menu = ["Venture down the hole."]
        elif "Golem Drophole" not in self.c.flags:
            self.c.flags['Golem Drophole'] = True
            if self.c.hasMercenary("Qendresa"):
                self.text = ("Qendresa: It appears that the ground here wants" +
                             " to fissure.")
                self.text += ("\nToshe: Yeah. The dirt is soft here.")
            else:
                self.text = ("Toshe: The ground feels soft.")                
        return self.actions()
    
    def walkway(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
        
    def walkway2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
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
        
        self.text = ""
        
        if selectionIndex == 0:
            self.rocksHit.add("Green")
            if "Blue" in self.rocksHit:
                self.rocksHit.remove("Blue")
                self.text = ("The stone plunges into the earth before you" +
                             " have a chance to act.")
                self.text += "\nToshe: That's stupid."
            else:
                self.text = ("You break the stone, shattering it into a" +
                              " million pieces.")
        
        if "Golem Cavern Sync 1" in self.c.flags or "Green" in self.rocksHit:
            self.imageIndex = 3
        else:
            self.menu = ["Strike the green stone."]
        
        if "Golem Jade" not in self.c.flags:
            self.c.flags['Golem Jade'] = True
            self.text = ("You come across a large, verdant gemstone rising" +
                         " from the ground.")
            self.text += ("\nToshe: What a gem!")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Oh, man! Punny!")
                self.text += ("\nToshe raises an eyebrow.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: It is, quite. A gem indeed.")
                if self.c.hasMercenary("Barrie"):
                    self.text += ("\nBarrie rolls his eyes.")
                    self.text += ("\nBarrie: Alright, alright. Just hit" +
                                  " the thing already.")
        
        self.text = self.text.strip() if self.text else None
        
        return self.actions()
    
    def rock2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        
        self.text = ""
        
        if selectionIndex == 0:
            self.rocksHit.add("Blue")
            self.text = ("You break the stone, shattering it into a" +
                          " million pieces.")
            if "Blue Shatter" not in self.c.flags:
                self.c.flags['Blue Shatter'] = True
                if self.c.hasMercenary("Barrie"):
                    self.text += ("\nBarrie: Wh-wh-what have you done?!")
            if "Green" in self.rocksHit:
                self.c.flags["Golem Cavern Sync 1"] = True
                self.text += ("\nYou hear the earth shake in the near" +
                              " distance.")
        
        if "Golem Cavern Sync 1" in self.c.flags or "Blue" in self.rocksHit:
            self.imageIndex = 3
        else:
            self.menu = ["Strike the blue stone."]
        
        if "Golem Aquamarine" not in self.c.flags:
            self.c.flags['Golem Aquamarine'] = True
            self.text = ("You encounter a tall, azure gemstone emerging" +
                         " from the cave floor.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Nice colour on that sucker." +
                              " Yeah...real nice.")
                self.text += ("\nBarrie the bear is in a daze.")
                
        self.text = self.text.strip() if self.text else None
        
        return self.actions()
