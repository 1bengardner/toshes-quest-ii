"""
File: TUALitochoro.py
Author: Ben Gardner
Created: April 23, 2023
Revised: April 27, 2023
"""


import random


class Litochoro:

    name = "Litochoro"
    audio = "Litochoro"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"
        
        thes = self.thessaloniki
        entr = self.entrance
        tvrn = self.tavern
        bdrm = self.bedroom
        
        self.spots = [
            [None, None, None],
            [None, bdrm, None],
            [None, None, None],
            [None, tvrn, None],
            [None, None, None],
            [None, entr, None],
            [None, thes, None],
            [None, None, None],
        ]

        self.encounters = None

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

    def thessaloniki(self, selectionIndex=None):
        X = 8
        Y = 3
        return self.actions({'area': "Thessaloniki",
                             'coordinates': (X, Y)})

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 3
            return self.actions({'area': "Litochoro",
                                 'coordinates': (X, Y)})
        if "Litochoro Man" not in self.c.flags:
            self.c.flags['Litochoro Man'] = True
            self.text = ("You fortunately spot a clothed man working on "+
                         "the balcony."+
                         "\nClothed Man: Welcome to Litochoro!"+
                         "\nToshe: Thanks.")
        self.menu = [
            "Enter the inn.",
        ]
        return self.actions()

    def tavern(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Melanippe"
        price = 500
        if selectionIndex == 0:
            self.text = (npc+": "+random.choice(
["Deep, deep under the city lurks a minotaur. Not just any minotaur, mind you. Oh, heavens, not Daedalus's minotaur. He was...disposed of years ago. No, this minotaur is something else. Men have been driven to insanity trying to hunt it down. Never mind that. How about some tea, dear?",
 "A few bold adventurers have come to ascend Mount Olympus, like yourself. If you plan to go, you should know that it will change each time.",
 "Myth has it that the beasts that dwell atop Olympus will match their strength to their challenger.",
 "Upon the mountain you may find an ancient serum. You can use it to \"alter the state of the natural world.\" At least, that's what an oriental man told me.\nToshe raises an eyebrow.\n%s: Oh, my sweet pea! You know us old folk don't know the proper terms these days!" % npc,
 "The view here is lovely. I really enjoy my mornings watching the sun rise and sipping Earl Grey from my favourite mug."
 ]
))
        elif selectionIndex == 2:
            if (self.c.euros >= price or
                "Litochoro Room Level" in self.c.flags):
                X = 1
                Y = 1
                return self.actions({'area': "Litochoro",
                                     'coordinates': (X, Y)})
            else:
                self.text = (npc+": Oh, shoot, it's %s euros a night. I keep telling my husband that if he charged less, we would have more visitors! Sorry, dear." % price)
        elif selectionIndex == 3:
            X = 1
            Y = 5
            return self.actions({'area': "Litochoro",
                                 'coordinates': (X, Y)})
        else:
            if "Rested" in self.c.flags:
                self.text = ("You fall asleep."+
                             "\nWhen you wake up, you return to the front "+
                             "to give %s your key." % npc+
                             "\n"+npc+": Enjoy your time in Litochoro!")
                del self.c.flags['Rested']
                del self.c.flags['Litochoro Room Level']
            elif ("Litochoro Room Level" in self.c.flags and
                  self.c.flags['Litochoro Room Level'] < self.c.level):
                self.text = (npc+": Long time, no see!")
                del self.c.flags['Litochoro Room Level']
            elif npc not in self.c.flags:
                self.text = (npc+": Hello, I am Melanippe. You look like you've come from very far away, dear.")
                self.c.flags[npc] = True
            else:
                self.text = (npc+": "+
                             random.choice([
                                 "My dear! May I make you a cup of tea?",
                                 "We have a visitor!",
                                 "Please watch your step. I just mopped the floor.",
                                 "Long time, no see!",
                                 "Stay as long as you like."
                                 ])
                             )

        if "Litochoro Room Level" in self.c.flags:
            self.menu = ["Ask for advice.",
                         "TODO",#"Buy a drink (50 euros).",
                         "Return to your room.",
                         "Leave."]
        else:
            self.menu = ["Ask for advice.",
                         "TODO",#"Buy a drink (50 euros).",
                         "Get a room (%s euros)." % price,
                         "Leave."]
        return self.actions()

    def bedroom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Melanippe"
        price = 500
        if selectionIndex == 0:
            self.c.flags['Rested'] = True
            self.c.hp = self.c.maxHp
            self.c.ep = self.c.maxEp
            X = 1
            Y = 3
            return self.actions({'area': "Litochoro",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 1
            Y = 3
            return self.actions({'area': "Litochoro",
                                 'coordinates': (X, Y)})
        if "Litochoro Room Level" not in self.c.flags:
            self.c.euros -= price
            self.text = ("%s takes you to a room. " % npc +
                        "You give her %s euros and she hands you a key." % price)
            self.c.flags['Litochoro Room Level'] = self.c.level
        else:
            self.text = ("You walk inside your room and lock the door.")
        self.menu = ["Sleep.",
                     "Leave your room."]
        return self.actions()