"""
File: TUALitochoro.py
Author: Ben Gardner
Created: April 23, 2023
Revised: April 29, 2023
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
        teaPrice = 50
        moreActions = None
        if selectionIndex == 0:
            self.text = (npc+": "+random.choice(
["Deep, deep under the city lurks a minotaur. Not just any minotaur, mind you. Oh, heavens, not Daedalus's minotaur. He was...disposed of years ago. No, this minotaur is something else. Men have been driven to insanity trying to hunt it down. Never mind that. How about some tea, dear?",
 "A few bold adventurers have come to ascend Mount Olympus, like yourself. If you plan to go, you should know that it will change each time.",
 "Myth has it that the beasts that dwell atop Olympus will match their strength to their challenger.",
 "Upon the mountain you may find an ancient serum. You can use it to \"alter the state of the natural world.\" At least, that's what an oriental man told me.\nToshe raises an eyebrow.\n%s: Oh, my sweet pea! You know us old folk don't know the proper terms these days!" % npc,
 "The view here is lovely. I really enjoy my mornings watching the sun rise and sipping Earl Grey from my favourite mug."
 ]
))
        elif selectionIndex == 1:
            if self.c.euros < teaPrice:
                self.text = (npc+": Oops, tea costs %s euros." % teaPrice)
            else:
                self.c.euros -= teaPrice
                self.text = (npc+": Here is some %s, dear." % random.choice([
                    "Earl Grey",
                    "spearmint tea",
                    "chamomile tea",
                    "lavender mint tea",
                    "ironwort tea",
                ]))
                mythicalCreatures = [
                    "Nemean Lion",
                    "Teumessian Fox",
                    "Stymphalian Bird",
                    "Cerberus",
                    "Chimera",
                    "Hydra",
                    "Cychreides",
                    "Skolopendra",
                    "Pterripus",
                    "Gorgon",
                    "Harpy",
                    "Minotaur",
                    "Centaur",
                    "Satyr",
                    "Siren"
                ]
                if npc+" Quest 1" not in self.c.flags:
                    self.text += (" Are you enjoying all the nice weather we're having? Well, I have a lovely soup I like to make from time to time. It has the flesh of Olympian beasts in it. Could you be a dear and fetch me a pile of mythical meat? Thank you so much, sweetheart.")
                    self.c.flags[npc+' Quest 1'] = 0
                    for creature in mythicalCreatures:
                        if creature in self.c.flags['Kills']:
                            self.c.flags[npc+' Quest 1'] += self.c.flags['Kills'][creature]
                elif (npc+" Quest 1 Complete" not in self.c.flags and
                      npc+" Quest 1" in self.c.flags):
                    kills = 0
                    for creature in mythicalCreatures:
                        if creature in self.c.flags['Kills']:
                            self.c.flags[npc+' Quest 1'] += self.c.flags['Kills'][creature]
                    if kills >= self.c.flags[npc+' Quest 1'] + 10:
                        self.text += (" Oh! This is just lovely. I would like you to have this."+
                                      "\n%s gives you a scintillous ring!" % npc)
                        moreActions = {'item': "Scintillous Ring"}
                        self.c.flags[npc+' Quest 1 Complete'] = True
                elif npc+" Quest 2" not in self.c.flags:
                    self.text += (" Oh, I wanted to tell you something. I still have my grandmother's famous sauce recipe. Now, guess what's inside? That's right, Skolopendra skin! That means you get to find me some!")
                    if "Skolopendra" in self.c.flags['Kills']:
                        self.c.flags[npc+' Quest 2'] = \
                                           self.c.flags['Kills']['Skolopendra']
                    else:
                        self.c.flags[npc+' Quest 2'] = 0
                elif (npc+" Quest 2 Complete" not in self.c.flags and
                      npc+" Quest 2" in self.c.flags and
                      "Skolopendra" in self.c.flags['Kills'] and
                      self.c.flags['Kills']['Skolopendra'] >=
                      self.c.flags[npc+' Quest 2'] + 3):
                    self.text += (" Wonderful! Just one moment...here, taste!"+
                                  "\n%s gives you a taste of the thick sauce." % npc+
                                  "\nYou gain 10 stat points!")
                    self.c.statPoints += 10
                    self.c.flags[npc+' Quest 2 Complete'] = True
                elif npc+" Quest 3" not in self.c.flags:
                    self.text += (" Now, as you know, the Hydra is a beast that can regrow its heads. Each hydra has one main head: That's the one that controls the body. It can also be steeped to brew a delicious tea. Would you be a dear and slay 9 hydra for me and bring me their main heads?")
                    if "Hydra" in self.c.flags['Kills']:
                        self.c.flags[npc+' Quest 3'] = \
                                           self.c.flags['Kills']['Hydra']
                    else:
                        self.c.flags[npc+' Quest 3'] = 0
                elif (npc+" Quest 3 Complete" not in self.c.flags and
                      npc+" Quest 3" in self.c.flags and
                      "Hydra" in self.c.flags['Kills'] and
                      self.c.flags['Kills']['Hydra'] >=
                      self.c.flags[npc+' Quest 3'] + 9):
                    self.text += (" This is just splendid. You did wonderfully."+
                                  "\n%s leans you over and pecks you on the temple, and hands you a curved object." % npc+
                                  "\n%s: This is a special minotaur horn. It once belonged to Theseus. I hope that you can put it to use." % npc+
                                  "\nYou got the purple horn!")
                    moreActions = {'item': "Purple Horn"}
                    self.c.flags[npc+' Quest 3 Complete'] = True
                elif npc+" Quest 3 Complete" in self.c.flags:
                    self.text += (" Enjoying all the nice weather?")
                else:
                    self.text += (" How is your quest?")                    
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
                         "Buy a drink (%s euros)." % teaPrice,
                         "Return to your room.",
                         "Leave."]
        else:
            self.menu = ["Ask for advice.",
                         "Buy a drink (%s euros)." % teaPrice,
                         "Get a room (%s euros)." % price,
                         "Leave."]
        return self.actions(moreActions) if moreActions else self.actions()

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