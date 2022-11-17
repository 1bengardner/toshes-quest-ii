"""
File: TUAWesternKosovo.py
Author: Ben Gardner
Created: September 6, 2013
Revised: November 17, 2022
"""


from random import choice
from random import randint


class WesternKosovo:

    name = "Western Kosovo"
    audio = "Nose Honk"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.blackMountain
        wrp2 = self.pec
        wrp3 = self.easternKosovo
        wrp4 = self.albanianDesert1
        wrp5 = self.albanianDesert2
        wrp6 = self.albanianDesert3
        wrp7 = self.albanianDesert4
        wrp8 = self.albanianDesert5
        entr = self.entrance
        pth1 = self.path1
        pth2 = self.path2
        nml1 = self.normal1
        nml2 = self.normal2
        notU = self.notUp
        dnRt = self.downRight
        upDn = self.upDown
        dead = self.deadEnd
        notL = self.notLeft
        notR = self.notRight
        stns = self.stones
        twn1 = self.townStones1
        dist = self.distantStones
        tree = self.tree
        tLab = self.tomasLab
        grph = self.gryphon
        twn2 = self.townStones2
        gate = self.gate
        ball = self.balloon
        
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, grph, None, ball, None, None, None, None, None, None],
            [None, None, None, None, None, dead, None, None, None, None],
            [None, None, None, wrp1, None, upDn, None, None, None, None],
            [None, dnRt, notU, entr, notU, notR, None, None, None, None],
            [None, notL, nml2, pth1, tLab, notR, None, wrp2, None, None],
            [None, wrp4, nml1, pth2, stns, twn1, twn2, gate, wrp3, None],
            [None, None, wrp5, tree, dist, notR, None, None, None, None],
            [None, None, None, wrp6, wrp7, notR, None, None, None, None],
            [None, None, None, None, None, wrp8, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None]
            ]

        e = {'Goblin Thug': 5,
             'Rebel Archer': 5,
             'Earth Mage': 4,
             'Rumadan Assassin': 4,
             'Unholy Crow': 2}
             
        self.encounters = {wrp1: {},
                           wrp2: {},
                           wrp3: {},
                           wrp4: {},
                           wrp5: {},
                           wrp6: {},
                           wrp7: {},
                           wrp8: {},
                           entr: e,
                           pth1: e,
                           pth2: e,
                           nml1: e,
                           nml2: e,
                           notU: e,
                           dnRt: e,
                           upDn: e,
                           dead: e,
                           notL: e,
                           notR: e,
                           stns: e,
                           twn1: {},
                           dist: e,
                           tree: {},
                           tLab: {},
                           grph: {},
                           twn2: {},
                           gate: {},
                           ball: {}
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

    def blackMountain(self, selectionIndex=None):
        X = 16
        Y = 13
        return self.actions({'area': "Black Mountain",
                             'coordinates': (X, Y)})

    def pec(self, selectionIndex=None):
        X = 3
        Y = 1
        return self.actions({'area': "Pec",
                             'coordinates': (X, Y)})

    def easternKosovo(self, selectionIndex=None):
        X = 2
        Y = 7
        return self.actions({'area': "Eastern Kosovo",
                             'coordinates': (X, Y)})

    def albanianDesert1(self, selectionIndex=None):
        X = 5
        Y = 3
        return self.actions({'area': "Albanian Desert",
                             'coordinates': (X, Y)})

    def albanianDesert2(self, selectionIndex=None):
        X = 6
        Y = 4
        return self.actions({'area': "Albanian Desert",
                             'coordinates': (X, Y)})

    def albanianDesert3(self, selectionIndex=None):
        X = 7
        Y = 5
        return self.actions({'area': "Albanian Desert",
                             'coordinates': (X, Y)})

    def albanianDesert4(self, selectionIndex=None):
        X = 8
        Y = 5
        return self.actions({'area': "Albanian Desert",
                             'coordinates': (X, Y)})

    def albanianDesert5(self, selectionIndex=None):
        X = 9
        Y = 6
        return self.actions({'area': "Albanian Desert",
                             'coordinates': (X, Y)})
    
    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Western Kosovo" not in self.c.flags:
            self.text = ("Toshe: I'm finally out of that fucking cave!")
            self.c.flags['Western Kosovo'] = True
        return self.actions()

    def path1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def path2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def normal1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def normal2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notUp(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if ("General Octavius" not in self.c.flags['Kills'] and
            "Zhang Quest 3" in self.c.flags):
            self.view = "battle"
            return self.actions({'enemy': "General Octavius",
                                 'mercenaries': self.c.mercenaries})
        return self.actions()

    def upDown(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def deadEnd(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You see the president's outpost far ahead to the east.")
        if ( "Secret Lab Lever" in self.c.flags and
             "Finding President" not in self.c.flags):
            self.text += ("\nToshe: That's where I need to go.")
        return self.actions()

    def notLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def stones(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You see some hoodoos scattered throughout the area.")
        return self.actions()

    def townStones1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def distantStones(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tree(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            if randint(1, 100) < 40 + self.c.dexterity:
                X = 1
                Y = 1
                return self.actions({'area': "Western Kosovo",
                                     'coordinates': (X, Y)})
            else:
                hpLoss = randint(3, 30)
                self.c.hp -= hpLoss
                self.text = ("You climb halfway up the tree before slipping" +
                             " and landing on your back, causing %s" % hpLoss +
                             " damage.")
                self.menu = ["Climb the tree."]
        else:
            self.text = ("There is an enormous tree here.")
            self.menu = ["Climb the tree."]
        return self.actions()

    def tomasLab(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = ""
        self.helpText = None
        self.menu = []
        passcodeLetters = {0: ['c', 's', 't', 'e'],
                           1: ['t', 'l', 'w', 'o'],
                           2: ['o', 'm', 'i', 'l'],
                           3: ['r', 'u', 'w', 'a'],
                           4: ['m', 'n', 's', 'd'],
                           5: ['f', 'l', 'h', 't'],
                           6: ['i', 'r', 'e', 'a'],
                           7: ['r', 'e', 'm', 's'],
                           8: ['e', 'h', 's', 'n']}

        if ("Secret Lab Unlocked" in self.c.flags and
            selectionIndex == 0):
            X = 2
            Y = 12
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})

        elif (selectionIndex == 0 and
              self.passcodeGuess == "swordfish" and
              self.c.hasItem("Mysterious Parchment")):
            self.text += ("You feed your soggy pieces of parchment into the "+
                          "machine.\n")
            self.c.flags['Secret Lab Unlocked'] = True
            self.c.removeItem(self.c.indexOfItem("Mysterious Parchment"))
            
        elif (selectionIndex is not None and
              "Secret Lab Unlocked" not in self.c.flags):
            letterGuess = passcodeLetters[self.letterNumber][selectionIndex]
            self.passcodeGuess += letterGuess
            self.letterNumber += 1
            self.text = ("You enter \"%s.\"" % letterGuess)
            if self.letterNumber < 9:
                self.menu = [("Enter \"%s.\"" % c)
                             for c in passcodeLetters[self.letterNumber]]
            
        elif "Secret Lab Unlocked" not in self.c.flags:
            self.passcodeGuess = ""
            self.letterNumber = 0
            if "Secret Lab" not in self.c.flags:
                self.text = ("You approach a large hoodoo with an "+
                             "entrance sealed by what could be either magic "+
                             "or high technology. \"Tomas Tam\" is painted "+
                             "across the front."+
                             "\nToshe: This must be Tomas's headquarters...\n")
                self.c.flags['Secret Lab'] = True
            self.text += ("70-M45: 70-M45 requesting credentials. Enter the "+
                          "passcode.")
            
            self.menu = [("Enter \"%s.\"" % c)
                         for c in passcodeLetters[self.letterNumber]]
            
        if "Secret Lab Unlocked" in self.c.flags:
            self.text += ("70-M45: User recognized. Proceed.")
            self.menu = ["Enter."]
        
        elif (selectionIndex is not None and
              self.letterNumber == 9 and
              self.passcodeGuess == "swordfish" and
              "All Tomas Writings Found" not in self.c.flags):
            hpLoss = randint(25, 75)
            self.c.hp -= hpLoss
            self.text += ("\n70-M45: Insert documents for scanning."+
                          "\nToshe: Documents? I don't have no stinking "+
                          "documents!"+
                          "\n70-M45: Access not granted."+
                          "\n70-M45 electrifies you, dealing %s damage."
                          % hpLoss)
        
        elif (selectionIndex is not None and
              self.letterNumber == 9 and
              self.passcodeGuess == "swordfish" and
              "All Tomas Writings Found" in self.c.flags and
              self.c.hasItem("Mysterious Parchment")):
            self.text += ("\n70-M45: Insert documents for scanning.")
            self.menu = ["Insert documents for scanning."]
        
        elif (selectionIndex is not None and
              self.letterNumber == 9 and
              self.passcodeGuess == "swordfish" and
              "All Tomas Writings Found" in self.c.flags):
            self.text += ("\n70-M45: Insert docu...mentsssseooorrbffff--" +
                          "\n70-M45 malfunctions and unlocks the seal to" +
                          " the entrance." +
                          "\nToshe: I love technology.")
            self.c.flags['Secret Lab Unlocked'] = True
            self.menu = ["Proceed."]

        elif (selectionIndex is not None and
              self.letterNumber == 9):
            hpLoss = randint(25, 75)
            self.c.hp -= hpLoss
            self.text += ("\n70-M45: Access not granted."+
                          "\n70-M45 electrifies you, dealing %s damage."
                          % hpLoss)
            
        return self.actions()

    def gryphon(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = ["Climb down the tree."]
        npc = "Gryphon"
        
        if (selectionIndex == 0):
            X = 3
            Y = 7
            return self.actions({'area': "Western Kosovo",
                                 'coordinates': (X, Y)})
        if selectionIndex == 1:
            self.c.flags['Gryphon Clan'] = True
            self.c.flags['Pirate Clan Kills'] = 0
            self.c.flags['Skeleton Clan Kills'] = 0
            self.text = (npc+": Godspeed.")

        elif selectionIndex == 2:
            self.text = (npc+": You know where to find us.")

        elif ("Gryphon Clan" in self.c.flags and
              self.c.flags['Skeleton Clan Kills'] == 4 and
              self.c.flags['Pirate Clan Kills'] == 4 and
              "Gryphon Clan Reward" not in self.c.flags):
            self.text = (npc+": We are eternally grateful for what "+
                         "you have done. This grand oak is peaceful "+
                         "once again. Take this as a symbol of our "+
                         "allegiance."+
                         "\nThe "+npc.lower()+" gives you a shield.")
            self.c.flags['Gryphon Clan Reward'] = True
            return self.actions({'item': "Gryphon Kite"})

        elif "Gryphon Clan Reward" in self.c.flags:
            self.text = (npc+": Flight and freedom!")
                         
        elif "Gryphon Clan" in self.c.flags:
            self.text = (npc+": You will find the pirates somewhere on the "+
                         "Scutari Peninsula and the skeletons south of "+
                         "Mojkovac Valley.")
            
        elif (("Pirate Clan" in self.c.flags or
               "Skeleton Clan" in self.c.flags) and
              self.c.flags['Gryphon Clan Kills'] < 3):
            self.view = "battle"
            if ("Pirate Clan" in self.c.flags and
                self.c.flags['Gryphon Clan Kills'] == 0):
                self.text = (npc+": You must not have heard of the legend of "+
                             "the phoenix.")
            elif ("Skeleton Clan" in self.c.flags and
                  self.c.flags['Gryphon Clan Kills'] == 0):
                self.text = (npc+": You shall go down as quickly as you "+
                             "rose.")
            self.c.flags['Gryphon Clan Kills'] += 1
            return self.actions({'enemy': choice(["Light Gryphon",
                                                  "Dark Gryphon",
                                                  "Mixed Gryphon",
                                                  "Magical Gryphon"]),
                                 'mercenaries': self.c.mercenaries})
        
        elif ("Gryphon Clan Kills" in self.c.flags
              and self.c.flags['Gryphon Clan Kills'] == 3):
            self.view = "battle"
            self.c.flags['Gryphon Clan Kills'] += 1
            return self.actions({'enemy': "Phoenix"})
        
        elif ("Gryphon Clan Kills" in self.c.flags
              and self.c.flags['Gryphon Clan Kills'] >= 4):
            self.text = (npc+": We will rise from the ashes one day...")
            
        else:
            self.text = (npc+": Good day. We are "+
                         "currently at war with the pirates and skeletons. "+
                         "We would settle this conflict peacefully. "+
                         "However, extra measures must be taken to resume "+
                         "order around here. Would you care to lend a wing in "+
                         "battle?")
            self.menu += ["\"Yes.\"",
                          "\"No.\""]
        return self.actions()

    def townStones2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 1
            return self.actions({'area': "Western Kosovo",
                                 'coordinates': (X, Y)})
        if "Balloon Man" not in self.c.flags:
            self.text = ("You see a hot air balloon rising.")
            self.menu = ["Investigate the hot air balloon."]
        else:
            self.text = ("You see the Hot Air Balloon Mafia in the distance.")
            self.menu = ["Walk to the Hot Air Balloon Mafia."]
        return self.actions()

    def gate(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        if "Pec" not in self.c.flags:
            self.text = ("You approach a city entrance.")
        else:
            self.text = ("You approach the entrance to Pec.")
        return self.actions()

    def balloon(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        flightPrice1 = 300
        flightPrice2 = 150
        flightPrice3 = 100
        npc = "Balloon Man"
        self.menu = ["Leave.",
                     "Fly to Herceg Novi (%s euros)." % flightPrice1,
                     "Fly to Mojkovac Valley (%s euros)." % flightPrice2]
        if "Pristina" in self.c.flags:
            self.menu += ["Fly to Pristina (%s euros)." % flightPrice3]
        if selectionIndex == 0:
            X = 6
            Y = 6
            return self.actions({'area': "Western Kosovo",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            self.c.flags['Hot Air Balloon Price'] = flightPrice1
            X = 5
            Y = 3
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 2:
            self.c.flags['Hot Air Balloon Price'] = flightPrice2
            X = 3
            Y = 2
            return self.actions({'area': "Mojkovac Valley",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 3:
            self.c.flags['Hot Air Balloon Price'] = flightPrice2
            X = 3
            Y = 4
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        if npc not in self.c.flags:
            self.text = (npc+": Yo, we're the Hot Air Balloon Mafia. We run "+
                         "these skies. If ya wanna ride, ya gotta gimme the "+
                         "dough. Let's see the euro.")
            self.c.flags[npc] = True
        else:
            self.text = (npc+": Where ya wanna go, buddy?")
        return self.actions()
