"""
File: TUAAthens.py
Author: Ben Gardner
Created: August 5, 2015
Revised: December 31, 2015
"""


import random


class Athens:

    name = "Athens"
    audio = "Nemea"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.greece
        wrp2 = self.coliseum
        entr = self.entrance
        rdLt = self.roadLeft
        colL = self.coliseumLeft
        btLt = self.bottomLeft
        tvrE = self.tavernEntrance
        gate = self.gate
        colD = self.coliseumDown
        outs = self.outskirts
        rdRt = self.roadRight
        colR = self.coliseumRight
        btRt = self.bottomRight
        rght = self.right
        tvrn = self.tavern
        bdrm = self.bedroom
        
        
        self.spots = [
            [None, None, None, None, None, None, None, None],
            [None, tvrn, None, None, tvrE, None, None, None],
            [None, None, None, rdLt, gate, rdRt, None, None],
            [None, wrp1, entr, colL, wrp2, colR, rght, None],
            [None, None, None, btLt, colD, btRt, None, None],
            [None, bdrm, None, None, outs, None, None, None],
            [None, None, None, None, None, None, None, None]
            ]
        
        e = {'Greek Footman': 20,
             'Greek Mage': 20}
             
        self.encounters1 = {wrp1: {},
                            wrp2: {},
                            entr: e,
                            rdLt: e,
                            colL: e,
                            btLt: e,
                            tvrE: e,
                            gate: e,
                            colD: e,
                            outs: e,
                            rdRt: e,
                            colR: e,
                            btRt: e,
                            rght: e,
                            tvrn: {},
                            bdrm: {}
                            }
        self.encounters2 = None

        self.encounters = self.encounters2
    
    def movementActions(self):
        if self.disguised():
            self.encounters = self.encounters2
        else:
            self.encounters = self.encounters1

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def disguised(self):
        return (self.c.itemIsEquipped("Greek Armour") or
                self.c.itemIsEquipped("Greek Robe"))

    def getRandomText(self):
        excerpts = [
            "You read a large poster that says \"SAVING IS PROHIBITED IN THE" +
            " COLISEUM.\"",
            "Athenian: My son wants to enter the coliseum when he grows up." +
            " I told him he had better begin training tomorrow.",
            "Athenian: Yesterday, you said tomorrow. Don't let your dreams" +
            " be dreams.",
            "Athenian: The champions are rarely defeated. Usually it's only" +
            " because people get suspicious of what they're hiding in the" +
            " fortress, so they just let some lucky shmuck win every now" +
            " and then.",
            "Athenian: Noel up north past the coliseum makes a lot of cash" +
            " from injured warriors.",
            "Athenian: I'm so proud to be Greek! Only the truest fighters" +
            " may enter the coliseum!",
            "Athenian: Hey, you look...different..." +
            "\nToshe: Nope, I'm just like you."
            ]
        return random.choice(excerpts) if random.randint(1, 4) == 1 else None

    def greece(self, selectionIndex=None):
        X = 13
        Y = 18
        return self.actions({'area': "Greece",
                             'coordinates': (X, Y)})

    def coliseum(self, selectionIndex=None):
        if self.disguised():
            X = 2
            Y = 2
            return self.actions({'area': "Coliseum",
                                 'coordinates': (X, Y)})
        else:
            self.c.flags["Kicked Out"] = True
            X = 2
            Y = 3
            return self.actions({'area': "Athens",
                                 'coordinates': (X, Y)})            

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0 if random.randint(0, 25) == 25 else 2
        self.text = None
        self.helpText = None
        self.menu = []
        if "Athens" not in self.c.flags:
            self.text = ("Town Crier: Athens! The bloody battleground wherein" +
                         " the greatest warriors test their might! Welcome!")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: This sounds like a test I could pass!")
                if self.c.hasMercenary("Qendresa"):
                    self.text += ("\nQendresa: You are a wizard, not a" +
                                  " warrior, and therefore you shant test" +
                                  " your might." +
                                  "\nBarrie: Way to kill the mood." +
                                  "\nToshe: I think this is a test for me" +
                                  " only. I'm supposed to enter the" +
                                  " battleground alone." +
                                  "\nBarrie: We'll root for you then!")
            self.c.flags['Athens'] = True
        elif "Kicked Out" in self.c.flags:
            self.c.flags['Not Disguised'] = True
            self.text = ("Guard: Out! You're not supposed to be here, filthy" +
                         " Macedonian!" +
                         "\nYou get thrown out of the coliseum.")
            del self.c.flags['Kicked Out']
        return self.actions()

    def roadLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = self.getRandomText()
        return self.actions()

    def coliseumLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = self.getRandomText()
        if ( "Greek Fortress" not in self.c.flags and
             "Coliseum Complete" in self.c.flags):
            self.text = ("Escort: Sir, let us continue westward to the" +
                         " fortress, yes?" +
                         "\nToshe: That sounds great.")
        return self.actions()

    def bottomLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = self.getRandomText()
        return self.actions()

    def tavernEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Athens",
                                 'coordinates': (X, Y)})
        if "Noel" not in self.c.flags:
            self.text = ("You approach a very old building at the end of " +
                         "the road.")
            self.menu = ["Enter the building."]
        else:
            self.menu = ["Enter the rest house."]
        return self.actions()

    def gate(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = self.getRandomText()
        return self.actions()

    def coliseumDown(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = self.getRandomText()
        return self.actions()

    def outskirts(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = self.getRandomText()
        return self.actions()

    def roadRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = self.getRandomText()
        return self.actions()

    def coliseumRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = self.getRandomText()
        return self.actions()

    def bottomRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = self.getRandomText()
        return self.actions()

    def right(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = self.getRandomText()
        return self.actions()

    def tavern(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Noel"
        price = 500
        if selectionIndex == 0:
            self.text = (npc+": "+random.choice(
["I have no advice for you, son; you seem to have wisdom beyond your" +
 " years. Stay vigilant."
 ]
))
        elif selectionIndex == 1:
            if (self.c.euros >= price or
                "Athens Room Level" in self.c.flags):
                X = 1
                Y = 5
                return self.actions({'area': "Athens",
                                     'coordinates': (X, Y)})
            else:
                self.text = (npc+": The price is %s euros." % price)
        elif selectionIndex == 2:
            X = 4
            Y = 1
            return self.actions({'area': "Athens",
                                 'coordinates': (X, Y)})
        else:
            if "Rested" in self.c.flags:
                self.text = ("You fall asleep."+
                             "\nWhen you wake up, you return to the front "+
                             "to give %s your key." % npc+
                             "\n"+npc+": You look much better now.")
                del self.c.flags['Rested']
                del self.c.flags['Athens Room Level']
            elif ("Athens Room Level" in self.c.flags and
                  self.c.flags['Athens Room Level'] < self.c.level):
                self.text = (npc+": Long time, no see!")
                del self.c.flags['Athens Room Level']
            elif npc not in self.c.flags:
                self.text = (npc+": Ho-ho-hello! Please, rest!")
                self.c.flags[npc] = True
            else:
                self.text = (npc+": "+
                             random.choice([
                                 "Welcome to my rest house.",
                                 "A wounded fighter!",
                                 "I just washed the sheets in the river." +
                                 " They should be okay for another two months.",
                                 "Ho-ho-hello!",
                                 "Did you just come from the coliseum?"
                                 ])
                             )
                self.text += (" Do you need to rest?")

        if "Athens Room Level" in self.c.flags:
            self.menu = ["Ask for advice.",
                         "Return to your room.",
                         "Leave."]
        else:
            self.menu = ["Ask for advice.",
                         "Get a room (%s euros)." % price,
                         "Leave."]
        return self.actions()

    def bedroom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Noel"
        price = 500
        if selectionIndex == 0:
            self.c.flags['Rested'] = True
            self.c.hp = self.c.maxHp
            self.c.ep = self.c.maxEp
            X = 1
            Y = 1
            return self.actions({'area': "Athens",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 1
            Y = 1
            return self.actions({'area': "Athens",
                                 'coordinates': (X, Y)})
        if "Athens Room Level" not in self.c.flags:
            self.c.euros -= price
            self.text = ("%s takes you to a room. " % npc +
                        "You give him %s euros and he hands you a key." % price)
            self.c.flags['Athens Room Level'] = self.c.level
        else:
            self.text = ("You walk inside your room and lock the door.")
        self.menu = ["Sleep.",
                     "Leave your room."]
        return self.actions()

