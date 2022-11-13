"""
File: TUAHercegFields.py
Author: Ben Gardner
Created: May 26, 2013
Revised: November 13, 2022
"""


from TUAStatics import Static


class HercegFields:

    name = "Frolicking Fields"
    audio = "Chicken Ball"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.hercegNovi
        wrp2 = self.blackMountain1
        wrp3 = self.blackMountain2
        entr = self.entrance
        pth1 = self.path1
        outE = self.outpostEntrance
        bck1 = self.back1
        bck2 = self.back2
        bkRt = self.backRight
        bkLt = self.backLeft
        nml1 = self.normal1
        nml2 = self.normal2
        rght = self.right
        left = self.left
        turn = self.turn
        dead = self.deadEnd
        pth3 = self.path3
        pth4 = self.path4
        fst1 = self.forest1
        fst2 = self.forest2
        nooE = self.nookEntrance
        pth5 = self.path5
        nook = self.nook
        outp = self.outpost
        pth6 = self.path6
        pth7 = self.path7
        mntn = self.mountain
        lMtn = self.leftMountain
        rMtn = self.rightMountain
        bMtn = self.mountainMaw
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, wrp2, None, nook, None, outp, None],
            [None, None, None, None, bMtn, None, None, None, None, None],
            [None, None, None, None, pth7, None, None, None, None, None],
            [None, lMtn, mntn, mntn, pth6, rMtn, wrp3, None, None, None],
            [None, left, nml1, nml2, pth1, rght, None, None, None, None],
            [None, left, fst2, fst1, pth5, rght, None, None, None, None],
            [None, left, fst1, fst2, pth4, fst1, nooE, None, None, None],
            [None, left, fst2, fst1, pth4, rght, None, None, None, None],
            [None, left, nml1, nml2, pth3, nml2, turn, dead, None, None],
            [None, left, nml2, nml1, outE, nml1, rght, None, None, None],
            [None, left, nml1, nml2, pth1, nml2, nml1, turn, dead, None],
            [None, bkLt, bck1, bck2, entr, bck2, bck1, bkRt, None, None],
            [None, None, None, None, wrp1, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None]]

        e1 = {'Goblin': 5,
              'Sean': 5,
              'Rumadan Man': 5,
              'Ent': 2,
              'Rumadan Warrior': 3}
        e2 = {'Goblin': 8,
              'Ent': 15,
              'Arcane Asp': 2}
        self.encounters = {wrp1: {},
                           entr: {},
                           pth1: e1,
                           outE: {},
                           bck1: e1,
                           bck2: e1,
                           bkRt: e1,
                           bkLt: e1,
                           nml1: e1,
                           nml2: e1,
                           rght: e1,
                           left: e1,
                           turn: e1,
                           dead: {},
                           pth3: e1,
                           pth4: e2,
                           fst1: e2,
                           fst2: e2,
                           nooE: {},
                           pth5: e2,
                           nook: {},
                           outp: {},
                           pth6: e1,
                           pth7: e1,
                           mntn: e1,
                           lMtn: e1,
                           rMtn: e1,
                           bMtn: e1,
                           wrp2: {},
                           wrp3: {}}
    
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

    def hercegNovi(self, selectionIndex=None):
        X = 7
        Y = 3
        return self.actions({'area': "Herceg Novi",
                             'coordinates': (X, Y)})

    def blackMountain1(self, selectionIndex=None):
        X = 2
        Y = 14
        return self.actions({'area': "Black Mountain",
                             'coordinates': (X, Y)})

    def blackMountain2(self, selectionIndex=None):
        X = 4
        Y = 17
        return self.actions({'area': "Black Mountain",
                             'coordinates': (X, Y)})

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def path1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def outpostEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 8
            Y = 1
            return self.actions({'area': "Herceg Fields",
                                 'coordinates': (X, Y)})
        self.text = ("You spot an outpost not too far away.")
        self.menu = ["Enter outpost."]
        return self.actions()

    def back1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def back2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def backRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def backLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def normal1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def normal2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def right(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def left(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def turn(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def deadEnd(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        if ( 'Dr. Grabh' not in self.c.flags['Kills'] and
             'Daniel Quest 3' in self.c.flags and
             "In Battle" not in self.c.flags):
            self.c.flags['In Battle'] = True
            self.view = "battle"
            return self.actions({'enemy': "Dr. Grabh",
                                 'mercenaries': self.c.mercenaries,
                                 'flash': True,})
        if "In Battle" in self.c.flags:
            del self.c.flags['In Battle']
        return self.actions()

    def path3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def path4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def forest1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def forest2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def nookEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            return Static.ICA_DATA['Ica 1']
        if self.c.dexterity >= 15:
            self.text = ("You notice a small opening in the tree roots that "+
                         "you could squeeze through.")
            self.menu = ["Enter the tree."]
        else:
            self.text = ("You notice a small opening in the tree roots that "+
                         "you might be able to squeeze through, were you more "+
                         "dextrous.")
        return self.actions()

    def path5(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def nook(self, selectionIndex=None):
        thisIca = "Ica 1"
        self.c.flags[thisIca] = True
        self.view = "store"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        npc = "Ica"
        skill1 = "Power Lob"
        skill2 = "Rock Shot"
        skillPrice1 = 100
        skillPrice2 = 200
        tunic = "Tunic"
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
            X = 6
            Y = 7
            return self.actions({'area': "Herceg Fields",
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
        elif npc not in self.c.flags:
            self.text = ("You crawl through the tree roots and find yourself "+
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
        else:
            self.text = ("You crawl through the tree roots and find yourself "+
                         "in a dark, damp nook."+
                         "\n"+npc+": What do you seek today, archer?")
        return self.actions({'items for sale': [tunic]+[None]*8})

    def outpost(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        npc = "Knight"
        self.menu = ["Learn Deep Thrust (100 euros).",
                     "Learn Rumble Strike (200 euros).",
                     "Learn Helix Swing (400 euros).",
                     "Leave."]
        if selectionIndex == 0:
            return self.actions({'skill': "Deep Thrust",
                                 'cost': 100})
        elif selectionIndex == 1:
            return self.actions({'skill': "Rumble Strike",
                                 'cost': 200})
        elif selectionIndex == 2:
            return self.actions({'skill': "Helix Swing",
                                 'cost': 400})
        elif selectionIndex == 3:
            X = 4
            Y = 10
            return self.actions({'area': "Herceg Fields",
                                 'coordinates': (X, Y)})
        else:
            self.text = (npc+": Welcome to the Knights' Outpost. We are a "+
                     "branch of the Knights of Igalo. We offer training for "+
                     "a fee.")
        return self.actions()

    def path6(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 21
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def path7(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 22
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You read a sign:"+
                     "\n\"Black Mountain: Enter with caution.\"")
        return self.actions()

    def mountain(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 23
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def leftMountain(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 24
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def rightMountain(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 25
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("There is a small passage going into the mountain.")
        return self.actions()

    def mountainMaw(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 26
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Black Mountain Entrance' not in self.c.flags:
            self.text = ("Toshe: This entrance looks ancient.")
            self.c.flags['Black Mountain Entrance'] = True
        return self.actions()
