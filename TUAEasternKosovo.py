"""
File: TUAEasternKosovo.py
Author: Ben Gardner
Created: April 1, 2014
Revised: November 17, 2022
"""


import random
from TUAStatics import Static


class EasternKosovo:

    name = "Eastern Kosovo"
    audio = "Groundhog"

    def __init__(self, character):
        self.TREE_ITEMS = [
            "Stick",
            "Macedonian Mace",
            "Ash Bow",
            "Bardiche",
            "Impwood Wand"
            ]
        
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.westernKosovo
        wrp2 = self.pristina1
        wrp3 = self.pristina2
        wrp4 = self.pristina3
        wrp5 = self.pristina4
        wrp6 = self.pristina5
        nml1 = self.normal1
        nml2 = self.normal2
        mtns = self.mountains
        notU = self.notUp
        notR = self.notRight
        notL = self.notLeft
        notD = self.notDown
        upRt = self.upRight
        upLt = self.upLeft
        dnRt = self.downRight
        dnLt = self.downLeft
        nooE = self.nookEntrance
        tree = self.tree
        dung = self.dungeon
        nook = self.nook
        wizE = self.wizardEntrance
        wizr = self.wizard
        safe = self.safetyZone
        pth1 = self.path1
        pth2 = self.path2
        gate = self.gate

        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, nook, None, None, None, None, None, nooE, None, None, None, None, wrp6, None],
            [None, None, None, None, None, None, dnRt, mtns, dnLt, None, None, None, pth1, None],
            [None, None, None, None, dnRt, notU, mtns, nml2, notR, None, None, None, pth2, None],
            [None, None, None, dnRt, mtns, mtns, nml2, nml1, nml2, dnLt, None, None, gate, None],
            [None, None, dnRt, mtns, nml1, nml2, tree, nml2, nml1, mtns, wrp2, None, None, None],
            [None, None, notL, nml1, tree, nml1, nml2, nml1, dung, nml1, wrp3, None, None, None],
            [None, wrp1, safe, nml2, nml1, nml2, wizE, nml2, nml1, nml2, wrp4, None, None, None],
            [None, None, notL, nml1, nml2, tree, nml2, nml1, tree, nml1, wrp5, None, None, None],
            [None, None, upRt, notD, notD, nml2, nml1, nml2, nml1, upLt, None, None, None, None],
            [None, None, None, None, None, upRt, nml2, nml1, upLt, None, None, wizr, None, None],
            [None, None, None, None, None, None, upRt, upLt, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]

        e = {'Duelist': 4,
             'Border Guard': 5,
             'White Knight': 3,
             'Black Knight': 3,
             'Giant Salamander1': 5
             }

        self.encounters = {wrp1: {},
                           wrp2: {},
                           wrp3: {},
                           wrp4: {},
                           wrp5: {},
                           wrp6: {},
                           nml1: e,
                           nml2: e,
                           mtns: e,
                           notU: e,
                           notR: e,
                           notL: e,
                           notD: e,
                           upRt: e,
                           upLt: e,
                           dnRt: e,
                           dnLt: e,
                           nooE: {},
                           tree: e,
                           dung: {},
                           nook: {},
                           wizE: e,
                           wizr: {},
                           safe: {},
                           pth1: e,
                           pth2: e,
                           gate: {}
                           }

        self.nookNpc = None

    def setTreeEvent(self):
        self.c.flags['Tree Roll'] = random.randint(1, 100)
        self.c.flags['Tree Item'] = random.choice(self.TREE_ITEMS)
    
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

    def westernKosovo(self, selectionIndex=None):
        X = 7
        Y = 6
        return self.actions({'area': "Western Kosovo",
                             'coordinates': (X, Y)})

    def pristina1(self, selectionIndex=None):
        X = 2
        Y = 2
        return self.actions({'area': "Pristina",
                             'coordinates': (X, Y)})

    def pristina2(self, selectionIndex=None):
        X = 2
        Y = 3
        return self.actions({'area': "Pristina",
                             'coordinates': (X, Y)})

    def pristina3(self, selectionIndex=None):
        X = 2
        Y = 4
        return self.actions({'area': "Pristina",
                             'coordinates': (X, Y)})

    def pristina4(self, selectionIndex=None):
        X = 2
        Y = 5
        return self.actions({'area': "Pristina",
                             'coordinates': (X, Y)})

    def pristina5(self, selectionIndex=None):
        X = 5
        Y = 5
        return self.actions({'area': "Pristina",
                             'coordinates': (X, Y)})
    
    def normal1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def normal2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def mountains(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if ( "General Octavius" not in self.c.flags['Kills'] and
             "Zhang Quest 3" in self.c.flags and
             "In Battle" not in self.c.flags):
            self.c.flags['In Battle'] = True
            self.view = "battle"
            return self.actions({'enemy': "General Octavius",
                                 'mercenaries': self.c.mercenaries,
                                 'flash': True,})
        if "In Battle" in self.c.flags:
            del self.c.flags['In Battle']
        return self.actions()

    def notUp(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if "Eastern Treasure" not in self.c.flags:
            self.text = ("You find a Macedonian Mace!")
            self.c.flags['Eastern Treasure'] = True
            return self.actions({'item': "Macedonian Mace"})
        return self.actions()

    def notRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notDown(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def nookEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            return Static.ICA_DATA['Ica 3']
        if self.c.dexterity >= 45:
            self.text = ("You see a tiny opening in the bushes that "+
                         "you could sneak into.")
            self.menu = ["Enter the opening."]
        else:
            self.text = ("You see a tiny opening in the bushes that looks "+
                         "like one that you could sneak into, were you more "+
                         "dextrous.")
        return self.actions()

    def tree(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.helpText = None
        self.text = ""
        self.menu = ["Shake the tree."]
        beehiveText = "You agitate a beehive of angry bees."
        if selectionIndex == 0:            
            if "Tree Roll" not in self.c.flags:
                random.seed(self.c.seed1)
                self.setTreeEvent()                

            # Acorns
            if 1 <= self.c.flags['Tree Roll'] <= 45:
                self.setTreeEvent()
                damage = random.randint(4, 8)
                self.c.hp -= damage
                self.text = ("A pile of acorns lands on your head, dealing "+
                              "%s damage." % damage)

            # Imp
            elif 46 <= self.c.flags['Tree Roll'] <= 70:
                self.setTreeEvent()
                self.view = "battle"
                self.text = ("An imp hops out of the tree!")
                return self.actions({'enemy': "Pestering Imp",
                                     'mercenaries': self.c.mercenaries})

            # Squirrel Attack
            elif 71 <= self.c.flags['Tree Roll'] <= 77:
                self.setTreeEvent()
                damage = random.randint(10, 30)
                self.c.hp -= damage
                self.text = ("Squirrels jump out from the tree at you "+
                              "to scratch your face, dealing "+
                              "%s damage." % damage)

            # Dead Squirrel
            elif 78 <= self.c.flags['Tree Roll'] <= 83:
                self.setTreeEvent()
                damage = random.randint(20, 40)
                self.c.hp -= damage
                self.text = ("A dead squirrel falls out of the tree "+
                              "onto your head, dealing "+
                              "%s damage." % damage)

            # Euros
            elif 84 <= self.c.flags['Tree Roll'] <= 89:
                self.setTreeEvent()
                euros = random.randint(10, 99)
                self.c.euros += euros
                self.text = ("Euros fall out of the tree. "+
                              "You collect %s euros!" % euros)

            # Acorns in Eye
            elif self.c.flags['Tree Roll'] == 90:
                self.setTreeEvent()
                damage = random.randint(50, 99)
                self.c.hp -= damage
                self.text = ("A pile of acorns lands in your eye, dealing "+
                              "%s damage." % damage)

            # Beehive - Drone
            elif 91 <= self.c.flags['Tree Roll'] <= 94:
                self.setTreeEvent()
                self.text = beehiveText
                self.view = "battle"
                return self.actions({'enemy': "Drone Bee",
                                     'mercenaries': self.c.mercenaries})

            # Beehive - Guard
            elif 95 <= self.c.flags['Tree Roll'] <= 97:
                self.setTreeEvent()
                self.text = beehiveText
                self.view = "battle"
                return self.actions({'enemy': "Guard Bee",
                                     'mercenaries': self.c.mercenaries})

            # Beehive - Queen
            elif 98 <= self.c.flags['Tree Roll'] <= 99:
                self.setTreeEvent()
                self.text = beehiveText
                self.view = "battle"
                return self.actions({'enemy': "Queen Bee",
                                     'mercenaries': self.c.mercenaries})

            # Beehive - Item
            elif self.c.flags['Tree Roll'] == 100:
                item = self.c.flags['Tree Item']
                aOrAn = "An" if item[0] in ("A", "E", "I", "O", "U") else "A"
                self.text = ("%s %s falls from the tree!" % (aOrAn, item))
                self.setTreeEvent()
                return self.actions({'item': item})
            
        elif self.c.hasMercenary("Barrie"):
            self.text = ("Barrie: I swear..." +
                         "\nBarrie sniffs the air rapidly." +
                         "\nBarrie: I smell delicious liquid gold nearby.")
            
        else:
            self.text = ("You see an oddly shaped tree that" +
                         " could be fun to shake.")
            
        return self.actions()

    def dungeon(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 6
            return self.actions({'area': "Old Ruins",
                                 'coordinates': (X, Y)})
        if "Old Ruins Complete" in self.c.flags:
            self.imageIndex = 13
            self.text = ("You approach an old ruins. There is a" +
                         " set of stairs leading downwards.")
            self.menu = ["Descend into the ruins."]
        elif "Finding President" in self.c.flags:
            self.imageIndex = 13
            self.text = ("You approach an old ruins. There is a" +
                         " set of stairs leading downwards." +
                         " The location matches where the \"X\" is" +
                         " on your map."
                         "\nToshe: Is this where the key is...?")
            self.menu = ["Descend into the ruins."]
        return self.actions()

    def nook(self, selectionIndex=None):
        thisIca = "Ica 3"
        self.c.flags[thisIca] = True
        self.view = "store"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        if self.nookNpc is None and random.randint(1, 100) == 100 or self.nookNpc == "Old Nigel":
            self.imageIndex = 15
            npc = "Old Nigel"
            self.nookNpc = "Old Nigel"
            skill1 = "Fling Dung"
            skill2 = "Smoke Bomb"
            skillPrice1 = 20000
            skillPrice2 = 100000
        else:
            npc = "Ica"
            self.nookNpc = "Ica"
            skill1 = "Sap Shot"
            skill2 = "Bullseye Bolt"
            skillPrice1 = 500
            skillPrice2 = 1000
        tunic = "Eucalyptic Tunic"
        self.menu = ["Learn %s (%s euros)." % (skill1, skillPrice1),
                     "Learn %s (%s euros)." % (skill2, skillPrice2),
                     "Leave."]
        if any(ica != thisIca and ica in self.c.flags for ica in Static.ICAS):
            self.menu += ["Travel to the next nook."]
        if selectionIndex == 0:
            return self.actions({'skill': skill1,
                                 'cost': skillPrice1,
                                 'items for sale': [tunic]+[None]*8})
        elif selectionIndex == 1:
            return self.actions({'skill': skill2,
                                 'cost': skillPrice2,
                                 'items for sale': [tunic]+[None]*8})
        elif selectionIndex == 2:
            X = 7
            Y = 1
            return self.actions({'area': "Eastern Kosovo",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 3:
            self.c.flags['Nooking'] = True
            i = Static.ICAS.index(thisIca)
            nextIca = [ica for ica in Static.ICAS[i+1:] + Static.ICAS[:i]
                       if ica in self.c.flags][0]
            return self.actions(Static.ICA_DATA[nextIca])
        elif "Nooking" in self.c.flags:
            self.text = (npc+" transports you to the next nook.")
            del self.c.flags['Nooking']
        elif npc == "Ica" and npc not in self.c.flags:
            self.imageIndex = 14
            self.text = ("You crawl through the bushes and find yourself "+
                         "in a dark, damp nook. To your surprise, there's "+
                         "someone else inside."+
                         "\nWoman: Quick, get in here. It is not safe outside. "+
                         "There are monsters."+
                         "\nToshe: Yeah, I noticed. Who are you?"+
                         "\n"+npc+": I am "+npc+". I take refuge in the "+
                         "trees. I protect the peace and serenity of the "+
                         "forest. I craft special tunics for use by fellow "+
                         "archers. I can teach you the way of the bow.")
            self.c.flags['Ica'] = True
        elif npc == "Ica":
            self.text = ("You crawl through the bushes and find yourself "+
                         "in a dark, damp nook."+
                         "\n"+npc+": What do you seek today, archer?")
        elif npc == "Old Nigel":
            self.text = ("You crawl through the bushes and find yourself "+
                         "in a dark, damp nook."+
                         "\n"+npc+": What do you seek today, friend?")
        return self.actions({'items for sale': [tunic]+[None]*8})

    def wizardEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        npc = "Old Nigel"
        self.menu = []
        if selectionIndex == 0:
            X = 11
            Y = 10
            return self.actions({'area': "Eastern Kosovo",
                                 'coordinates': (X, Y)})
        self.text = (npc+": Let Old Nigel teach you some tricks! Ha ha...")
        if self.c.hasMercenary("Barrie"):
            self.text += ("\nBarrie leans over to speak discreetly." +
                          "\nBarrie: I wouldn't trust this guy. He" +
                          " looks old.")
        self.menu = ["Let Old Nigel teach you some tricks."]
        if "Old Nigel" not in self.c.flags:
            self.text = ("You see an old man hiding in the shade.")
            self.menu = ["Greet the old man."]
        return self.actions()

    def wizard(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        npc = "Old Nigel"
        skill1 = "Poison Cloud"
        skill2 = "Melting Touch"
        skill3 = "Mist"
        skillPrice1 = 3000
        skillPrice2 = 3000
        skillPrice3 = 3000
        items = ["Fire Wand"]+[None]*8
        self.menu = ["Learn %s (%s euros)." % (skill1, skillPrice1),
                     "Learn %s (%s euros)." % (skill2, skillPrice2),
                     "Learn %s (%s euros)." % (skill3, skillPrice3),
                     "Leave."]
        if selectionIndex == 0:
            return self.actions({'skill': skill1,
                                 'cost': skillPrice1,
                                 'items for sale': items})
        elif selectionIndex == 1:
            return self.actions({'skill': skill2,
                                 'cost': skillPrice2,
                                 'items for sale': items})
        elif selectionIndex == 2:
            return self.actions({'skill': skill3,
                                 'cost': skillPrice3,
                                 'items for sale': items})
        elif selectionIndex == 3:
            X = 6
            Y = 7
            return self.actions({'area': "Eastern Kosovo",
                                 'coordinates': (X, Y)})            
        elif "Old Nigel" not in self.c.flags:
            self.text = (npc+": Nigel, that's my name.")
            self.c.flags['Old Nigel'] = True
        else:
            self.text = (npc+random.choice([
                ": This Nigel is getting old...",
                ": Stay awhile.",
                ": Listen here, you!"]))
        return self.actions({'items for sale': items})

    def safetyZone(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Eastern Kosovo" not in self.c.flags:
            self.text = ("Toshe: There's a lot of rogue knights patrolling this" +
                         " place. I better watch my step.")
            self.c.flags['Eastern Kosovo'] = True
        return self.actions()

    def path1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def path2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def gate(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 3
            return self.actions({'area': "Macedonia",
                                 'coordinates': (X, Y)})
        if "Macedonian Gate Opened" in self.c.flags:
            self.imageIndex = 19
            self.text = ("You approach an unlocked gate.")
            self.menu = ["Enter the gate."]
        elif self.c.hasItem("The Key to Macedonia"):
            self.text = ("You approach a gate sealed by dark forces." +
                         "\nToshe: It looks like those dark forces are" +
                         " blocking the keyhole.")
        else:
            self.text = ("You approach a gate sealed by dark forces." +
                         "\nToshe: If only I had the key to Macedonia.")
        return self.actions()
