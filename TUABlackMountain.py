"""
File: TUABlackMountain.py
Author: Ben Gardner
Created: June 2, 2013
Revised: November 28, 2022
"""


import random


class BlackMountain:

    name = "Black Mountain"
    audio = "Ketchup Splat"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.hercegFields1
        wrp2 = self.hercegFields2
        wrp3 = self.mojkovacSummit1
        wrp4 = self.scutariPeninsula
        wrp5 = self.mojkovacSummit2
        wrp6 = self.westernKosovo
        nml1 = self.normal1
        nml2 = self.normal2
        notU = self.notUp
        notL = self.notLeft
        notR = self.notRight
        notD = self.notDown
        ltRt = self.leftRight
        upD1 = self.upDown1
        upD2 = self.upDown2
        upLt = self.upLeft
        upRt = self.upRight
        dnLt = self.downLeft
        dnRt = self.downRight
        rght = self.right
        entr = self.entrance
        trs1 = self.treasure1
        muds = self.mudslideTeacher
        trs2 = self.treasure2
        trs3 = self.treasure3
        trs4 = self.treasure4

        Xml1 = self.normal1X
        Xml2 = self.normal2X
        XotL = self.notLeftX
        XotR = self.notRightX
        XtRt = self.leftRightX
        XpDn = self.upDownX
        XpLt = self.upLeftX
        XpRt = self.upRightX
        XnLt = self.downLeftX
        XnRt = self.downRightX
        Xght = self.rightX
        sorE = self.sorceressEntrance
        sorc = self.sorceress
        
        self.spots = [
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
[None, sorc, None, None, None, trs3, notU, dnLt, None, dnRt, ltRt, wrp3, None, None, XnRt, XnLt, None, None, None],
[None, None, None, None, rght, nml1, nml2, nml1, notU, notR, None, None, None, wrp5, sorE, Xml2, XnLt, None, None],
[None, None, None, None, None, notL, nml1, nml2, nml1, nml2, dnLt, None, None, None, XpRt, Xml1, Xml2, XnLt, None],
[None, None, None, None, None, upRt, nml2, nml1, nml2, nml1, notR, None, None, None, None, XpRt, Xml1, XotR, None],
[None, None, None, None, None, None, upRt, notD, nml1, notD, notR, None, None, None, None, None, XotL, XpLt, None],
[None, None, None, None, None, None, None, None, upD2, None, upD2, None, None, None, None, None, XpDn, None, None],
[None, None, None, None, dnRt, dnLt, None, None, upD2, None, upD2, None, None, None, XnRt, XtRt, XpDn, None, None],
[None, None, None, None, notL, nml2, ltRt, ltRt, upLt, None, upD2, None, None, None, XpDn, None, XpDn, None, None],
[None, None, dnRt, notU, nml2, notR, None, None, None, None, upD2, None, None, None, XotL, XtRt, XpLt, None, None],
[None, dnRt, nml1, nml2, nml1, upLt, None, None, None, muds, upLt, None, None, None, XpDn, None, None, None, None],
[None, trs2, notD, nml1, upLt, None, None, None, rght, upLt, None, None, None, None, XpRt, XtRt, XnLt, None, None],
[None, None, None, upD1, None, None, None, None, None, None, None, None, None, None, None, None, XpDn, None, None],
[None, None, None, upD1, None, None, None, None, None, None, None, None, None, None, None, Xght, XotR, None, None],
[None, rght, entr, notD, ltRt, dnLt, None, None, None, None, None, None, None, None, None, None, wrp6, None, None],
[None, None, wrp1, None, None, upD1, None, None, None, None, None, None, None, None, None, None, None, None, None],
[None, None, None, None, None, upD1, None, None, None, None, None, None, None, None, None, None, None, None, None],
[None, None, None, wrp2, ltRt, nml1, notU, notU, dnLt, None, None, None, None, None, None, None, None, None, None],
[None, None, None, None, None, notL, nml1, nml2, notR, None, None, None, None, None, None, None, None, None, None],
[None, None, None, None, None, upRt, nml2, nml1, trs1, None, None, None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, upRt, notR, None, None, None, None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, upD1, None, None, None, None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, notL, notU, dnLt, None, None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, upRt, nml1, nml2, dnLt, None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None, notL, nml1, nml2, dnLt, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None, trs4, notD, nml1, notR, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None, None, None, upRt, notR, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None, None, None, None, upD1, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None, None, wrp4, ltRt, upLt, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]

        e1 = {'Vampire Bat': 7,
              'Skeleton': 7,
              'Skeleton Mage1': 4,
              'Skeleton Mage2': 4,
              'Cave Orc': 3}
        
        e2 = {'Vampire Bat': 5,
              'Skeleton': 5,
              'Skeleton Mage1': 3,
              'Skeleton Mage2': 3,
              'Cave Orc': 9}

        e3 = {'Cave Orc': 5,
              'Skeleton Soldier': 10,
              'Skeleton Archer': 10}

        self.encounters = {wrp1: {},
                           wrp2: {},
                           wrp3: {},
                           wrp4: {},
                           wrp5: {},
                           wrp6: {},
                           nml1: e1,
                           nml2: e1,
                           notU: e1,
                           notL: e1,
                           notR: e1,
                           notD: e1,
                           ltRt: {},
                           upD1: e1,
                           upD2: e2,
                           upLt: e1,
                           upRt: e1,
                           dnLt: e1,
                           dnRt: e1,
                           rght: e1,
                           entr: {},
                           trs1: e1,
                           muds: e1,
                           trs2: e1,
                           trs3: e1,
                           trs4: e1,
                           Xml1: e3,
                           Xml2: e3,
                           XotL: e3,
                           XotR: e3,
                           XtRt: e3,
                           XpDn: e3,
                           XpLt: e3,
                           XpRt: e3,
                           XnLt: e3,
                           XnRt: e3,
                           Xght: e3,
                           sorE: {},
                           sorc: {}
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

    def hercegFields1(self, selectionIndex=None):
        X = 4
        Y = 2
        return self.actions({'area': "Herceg Fields",
                             'coordinates': (X, Y)})
    
    def hercegFields2(self, selectionIndex=None):
        X = 5
        Y = 4
        return self.actions({'area': "Herceg Fields",
                             'coordinates': (X, Y)})

    def mojkovacSummit1(self, selectionIndex=None):
        X = 2
        Y = 6
        return self.actions({'area': "Mojkovac Summit",
                             'coordinates': (X, Y)})

    def scutariPeninsula(self, selectionIndex=None):
        X = 6
        Y = 2
        return self.actions({'area': "Scutari Peninsula",
                             'coordinates': (X, Y)})

    def mojkovacSummit2(self, selectionIndex=None):
        X = 10
        Y = 6
        return self.actions({'area': "Mojkovac Summit",
                             'coordinates': (X, Y)})

    def westernKosovo(self, selectionIndex=None):
        X = 3
        Y = 4
        return self.actions({'area': "Western Kosovo",
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

    def notUp(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def notLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notDown(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def leftRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.text = ("You receive a flashlight!"+
                         "\nYou turn it on and shine it on the man, realizing "+
                         "it's Gan."+
                         "\nToshe: Thanks. Wait, why are you here?"+
                         "\nGan: No need to thank me. Before I go, I must "+
                         "teach you something."+
                         "\nGan looks like he's fallen asleep."+
                         "\nYou are startled when Gan reaches to your face "+
                         "and shuts your eyelids."+
                         "\nGan vanishes.")
            self.c.flags['Gan Black Mountain'] = True
            return self.actions({'skill': "Recover",
                                 'cost': 0})            
        if 'Gan Black Mountain' not in self.c.flags:
            self.text = ("Old Chinese Man: Toshe, I have surprise for you.")
            self.menu = ["Be surprised."]
        elif ("Barrie Black Mountain Remark" not in self.c.flags and
              self.c.hasMercenary("Barrie")):
            self.c.flags['Barrie Black Mountain Remark'] = True
            self.text = ("Barrie: This looks like a nice place to live." +
                         " In fact, can we just relax here for a while?" +
                         "\nToshe: No." +
                         "\nBarrie: Come on.")
        return self.actions()

    def upDown1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Black Mountain Tunnel 1' not in self.c.flags:
            self.text = ("Toshe: Holy shit, this place is huge.")
            self.c.flags['Black Mountain Tunnel 1'] = True
        return self.actions()

    def upDown2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Black Mountain Tunnel 2' not in self.c.flags:
            self.text = ("Toshe: Where's the light at the end of the tunnel?")
            self.c.flags['Black Mountain Tunnel 2'] = True
        return self.actions()

    def upLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Stone Dick' not in self.c.flags:
            self.text = ("Toshe: That stone thing looks like a dick.")
            self.c.flags['Stone Dick'] = True
        return self.actions()

    def downLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def right(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("Toshe: Dead end.")
        return self.actions()

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Gan Black Mountain' not in self.c.flags:
            self.text = ("Old Chinese Man: Here, Toshe, you will need this."+
                         "\nYou receive a flashlight!"+
                         "\nYou turn it on and shine it on the man, realizing "+
                         "it's Gan."+
                         "\nToshe: Thanks. Wait, why are you here?"+
                         "\nGan: No need to thank me. Before I go, I must "+
                         "teach you something."+
                         "\nGan looks like he's fallen asleep."+
                         "\nYou are startled when Gan reaches to your face "+
                         "and shuts your eyelids."+
                         "\nGan vanishes.")
            self.c.flags['Gan Black Mountain'] = True
            return self.actions({'skill': "Recover",
                                 'cost': 0})
        return self.actions()

    def treasure1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Black Mountain Treasure 1' not in self.c.flags:
            self.text = ("You find a Leather Doublet!")
            self.c.flags['Black Mountain Treasure 1'] = True
            return self.actions({'item': "Leather Doublet"})
        return self.actions()

    def mudslideTeacher(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Mysterious Brown Wizard"
        if selectionIndex == 0:
            self.text = ("Toshe: I'm not a little boy, but ok."+
                         "\n"+npc+": Ti nivol mi!"+
                         "\nThe wizard flicks his wand and teleports away.")
            self.c.flags['Mudslide'] = True
            return self.actions({'skill': "Mudslide",
                                 'cost': 0})
        elif selectionIndex == 1:
            random.seed(self.c.level)
            self.text = ("Toshe: No, you creep!"+
                         "\n%s: Suit yourself, turdnugget." % npc+
                         "\nThe wizard teleports away, leaving magic dust.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: What a weird dude.")
            randomHpBoost = random.randint(-5, 15)
            if randomHpBoost < 0:
                self.text += ("\nYour maximum HP decreased by %s!" % -randomHpBoost)
            elif randomHpBoost > 0:
                self.text += ("\nYour maximum HP increased by %s!" % randomHpBoost)
            self.c.maxHp += randomHpBoost
            self.c.flags['Mudslide'] = True
        elif "Mudslide" not in self.c.flags:
            self.imageIndex = 15
            self.c.flags['New Song'] = "Buddha"
            self.text = (npc+": Hello, little boy. Would "+
                         "you like to learn magic today?")
            self.menu = ["\"Yes.\"",
                         "\"No!\""]
        return self.actions()

    def treasure2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Black Mountain Treasure 2' not in self.c.flags:
            self.text = ("You find a Battle Axe!")
            self.c.flags['Black Mountain Treasure 2'] = True
            return self.actions({'item': "Battle Axe"})
        return self.actions()

    def treasure3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Black Mountain Treasure 3' not in self.c.flags:
            self.text = ("You find a Brigandine!")
            self.c.flags['Black Mountain Treasure 3'] = True
            return self.actions({'item': "Brigandine"})
        return self.actions()

    def treasure4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Black Mountain Treasure 4' not in self.c.flags:
            self.text = ("You find a Magerobe!")
            self.c.flags['Black Mountain Treasure 4'] = True
            return self.actions({'item': "Magerobe"})
        return self.actions()

    def normal1X(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def normal2X(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def notLeftX(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notRightX(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def leftRightX(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upDownX(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upLeftX(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upRightX(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Stone Dick' not in self.c.flags:
            self.text = ("Toshe: That stone thing looks like a dick.")
            self.c.flags['Stone Dick'] = True
        return self.actions()

    def downLeftX(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downRightX(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def rightX(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("Toshe: Dead end.")
        return self.actions()

    def sorceressEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Black Mountain",
                                 'coordinates': (X, Y)})
        self.text = ("You notice a faint glow emanating from around the "+
                     "corner.")
        self.menu = ["Follow the light."]
        return self.actions()

    def sorceress(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        npc = "Sorceress"
        skill1 = "Fireball"
        skill2 = "Icicles"
        skill3 = "Quicksand"
        skillPrice1 = 300
        skillPrice2 = 300
        skillPrice3 = 300
        items = ["Yew Wand"]+[None]*8
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
            X = 14
            Y = 2
            return self.actions({'area': "Black Mountain",
                                 'coordinates': (X, Y)})
        else:
            self.text = (npc+": Does magic interest you?")
        return self.actions({'items for sale': items})
