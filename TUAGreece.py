"""
File: TUAGreece.py
Author: Ben Gardner
Created: August 3, 2015
Revised: November 14, 2022
"""


import random
from TUAStatics import Static


class Greece:

    name = "Greek Plains"
    audio = "Impulse Response"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.hiddenPassage
        wrp2 = self.thessaloniki
        wrp3 = self.athens
        nml1 = self.normal1
        nml2 = self.normal2
        nml3 = self.normal3
        notL = self.notLeft
        notU = self.notUp
        notR = self.notRight
        notD = self.notDown
        upLt = self.upLeft
        upRt = self.upRight
        dnLt = self.downLeft
        dnRt = self.downRight
        wall = self.wall
        bigN = self.bigNigel
        fDis = self.fortressInTheDistance
        fort = self.fortress
        nooE = self.nookEntrance
        gate = self.gate
        lths = self.lighthouse
        nook = self.nook
        shdL = self.shadeLeft
        shdR = self.shadeRight
        shdM = self.shadeMiddle
        shdC = self.shadeCorner
        marc = self.marciano
        
        
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, nook, None, marc, None, None, dnRt, notU, wrp2, None, None, None, None, None, None, None],
            [None, None, None, None, None, dnRt, nml2, nml3, notR, None, None, None, None, None, None, None],
            [None, None, None, None, None, notL, nml3, nml1, upLt, None, None, None, None, None, None, None],
            [None, None, None, None, dnRt, nml3, nml1, upLt, None, None, None, None, None, None, None, None],
            [None, None, None, None, notL, nml1, notR, None, None, None, None, None, None, None, None, None],
            [None, wrp1, None, dnRt, nml1, nml2, notR, None, None, None, None, None, None, None, None, None],
            [None, wall, nooE, nml1, nml2, nml3, notR, None, None, None, None, None, None, None, None, None],
            [None, notL, nml1, nml2, nml3, nml1, notR, None, None, None, None, None, None, None, None, None],
            [None, upRt, nml2, nml3, nml1, nml2, nml3, dnLt, None, None, None, None, None, None, None, None],
            [None, None, notL, nml1, nml2, nml3, nml1, notR, None, None, None, None, None, None, None, None],
            [None, None, upRt, nml2, shdC, shdM, shdC, nml3, dnLt, None, None, None, None, None, None, None],
            [None, None, None, notL, shdL, bigN, shdR, nml1, notR, None, None, None, None, None, None, None],
            [None, None, None, notL, shdC, shdM, shdC, nml2, nml3, dnLt, None, None, None, None, None, None],
            [None, None, None, notL, nml3, nml1, nml2, nml3, nml1, nml2, dnLt, None, None, None, None, None],
            [None, None, None, upRt, nml1, nml2, nml3, nml1, nml2, nml3, nml1, dnLt, None, None, None, None],
            [None, None, None, None, upRt, nml3, nml1, nml2, nml3, nml1, nml2, nml3, dnLt, None, None, None],
            [None, None, None, None, None, notL, nml2, nml3, nml1, nml2, nml3, nml1, notR, None, None, None],
            [None, None, None, None, fort, fDis, notD, notD, notD, notD, nml1, nml2, lths, gate, wrp3, None],
            [None, None, None, None, None, None, None, None, None, None, upRt, notD, notD, upLt, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
        
        e = {'Psilos': 7,
             'Ekdromos': 5,
             'Hoplite': 3,
             'Giant Scarab1': 5}

        gs = {'Giant Scarab1': 5}
             
        self.encounters1 = {wrp1: {},
                           wrp2: {},
                           wrp3: {},
                           nml1: e,
                           nml2: e,
                           nml3: e,
                           notL: e,
                           notU: e,
                           notR: e,
                           notD: e,
                           upLt: e,
                           upRt: e,
                           dnLt: e,
                           dnRt: e,
                           wall: e,
                           bigN: {},
                           fDis: e,
                           fort: {},
                           nooE: {},
                           gate: {},
                           lths: {},
                           nook: {},
                           shdL: e,
                           shdR: e,
                           shdM: e,
                           shdC: e,
                            marc: {},
                           }

        self.encounters2 = {wrp1: {},
                           wrp2: {},
                           wrp3: {},
                           nml1: gs,
                           nml2: gs,
                           nml3: gs,
                           notL: gs,
                           notU: gs,
                           notR: gs,
                           notD: gs,
                           upLt: gs,
                           upRt: gs,
                           dnLt: gs,
                           dnRt: gs,
                           wall: gs,
                           bigN: {},
                           fDis: gs,
                           fort: {},
                           nooE: {},
                           gate: {},
                           lths: gs,
                           nook: {},
                           shdL: gs,
                           shdR: gs,
                           shdM: gs,
                           shdC: gs,
                            marc: {}
                           }

        self.encounters = self.encounters1
    
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

    def marcianoCheck(self):
        if "Marciano5" not in self.c.flags['Kills']:
            X = 3
            Y = 1
            return self.actions({'area': "Greece",
                                 'coordinates': (X, Y)})
        elif "Marciano Coward 4" not in self.c.flags:
            self.text = ("Marciano escapes north."+
                         "\nToshe: Run, and don't come back!")
            self.c.flags['Marciano Coward 4'] = True
            return self.actions()
        return False

    def hiddenPassage(self, selectionIndex=None):
        X = 3
        Y = 7
        return self.actions({'area': "Hidden Passage",
                             'coordinates': (X, Y)})

    def thessaloniki(self, selectionIndex=None):
        X = 2
        Y = 8
        return self.actions({'area': "Thessaloniki",
                             'coordinates': (X, Y)})

    def athens(self, selectionIndex=None):
        X = 2
        Y = 3
        return self.actions({'area': "Athens",
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

    def normal3(self, selectionIndex=None):
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

    def notUp(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notRight(self, selectionIndex=None):
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

    def upLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def wall(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        merc1 = "Qendresa"
        merc2 = "Barrie"
        if "Greece" not in self.c.flags:
            self.text = ("Toshe: Greece--the sworn enemy of Macedonia." +
                         " From what I saw in the ruins, I know they're" +
                         " up to no good.")
            if self.c.hasMercenary(merc1):
                self.text += ("\n%s: There is most certainly a" % merc1 +
                              " dark presence about.")
            if self.c.hasMercenary(merc2):
                self.text += ("\n%s: I smell honey." % merc2)
            self.c.flags['Greece'] = True
        return self.actions()

    def bigNigel(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        npc = "Big Nigel"
        rm1 = "Jade Ward"
        rm2 = "Aquamarine Ward"
        rm3 = "Garnet Ward"
        product = "Diamond Ward"
        self.menu = ["Craft %s." % (product)]
        if selectionIndex == 0:
            if  (self.c.hasItem(rm1) and
                 self.c.hasItem(rm2) and
                 self.c.hasItem(rm3) and
                 not self.c.itemIsEquipped(rm1) and
                 not self.c.itemIsEquipped(rm2) and
                 not self.c.itemIsEquipped(rm3)):
                self.c.removeItem(self.c.indexOfItem(rm1))
                self.c.removeItem(self.c.indexOfItem(rm2))
                self.c.removeItem(self.c.indexOfItem(rm3))
                self.text = ("%s crushes your three wards into" % npc +
                             " a %s." % product)
                return self.actions({'item': product})
            elif (not self.c.hasItem(rm1) or
                  not self.c.hasItem(rm2) or
                  not self.c.hasItem(rm3)):
                self.text = (npc + ": I will need three different coloured" +
                             " wards.")
            elif (self.c.itemIsEquipped(rm1) or
                  self.c.itemIsEquipped(rm2) or
                  self.c.itemIsEquipped(rm3)):
                self.text = (
                    npc+": You need to take that ward off before I" +
                    " can crush that.")
        elif npc not in self.c.flags:
            self.text = (npc + ": Heheheh...how are you today, sir?" +
                         " Do you have wards? I'm trying to practice my" +
                         " crushing. I can crush three" +
                         " coloured wards into a diamond ward." +
                         " I'll show you.")
            self.c.flags[npc] = True
        else:
            self.text = (npc+random.choice([
                ": Nah, I don't know \"Old Nigel.\" Who the hell is that?",
                ": Do you have wards?",
                ": In Pristina, you can make wards out of gems."]))
        return self.actions()

    def fortressInTheDistance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        if ( "Distant Fortress" not in self.c.flags and
             "Greek Fortress" not in self.c.flags):
            self.text = ("You see a huge fortress in the distance.")
            self.c.flags['Distant Fortress'] = True
        return self.actions()

    def fortress(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        npc1 = "Guard"
        npc2 = "Escort"
        if selectionIndex == 0 and not self.c.hasItem("Key Mold"):
            X = 5
            Y = 1
            return self.actions({'area': "Greek Fortress",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0 and self.c.hasItem("Key Mold"):
            self.imageIndex = 15
            self.text = ("Toshe: I don't really wanna go back in there.")
            self.menu = ["Enter the fortress."]
        elif "Coliseum Complete" not in self.c.flags:
            self.text = ("%s: I'm sorry, sir. No visitors are allowed" % npc1 +
                         " inside the fortress without an escort.")
        else:
            self.imageIndex = 15
            if "Greek Fortress" not in self.c.flags:
                self.text = ("Toshe: Wow, I've always wanted to see" +
                             " what it's like inside." +
                             "\n%s: Today, sir, you will." % npc2)
                if self.c.hasMercenary("Qendresa"):
                    self.text += (" Please, madam, follow behind.")
                if self.c.hasMercenary("Barrie"):
                    self.text += ("\nThe escort turns to Barrie and pauses." +
                                  "\n%s: ...You as well, hairy-sir." % npc2)
            if "Fortress Intervention" in self.c.flags:
                self.c.flags['Fortress Escaped'] = True
            self.menu = ["Enter the fortress."]
        return self.actions()

    def nookEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            return Static.ICA_DATA['Ica 4']
        if self.c.dexterity >= 60:
            self.text = ("You see a tiny hole in the wall that "+
                         "you could crawl through.")
            self.menu = ["Enter the hole."]
        else:
            self.text = ("You see a tiny hole in the wall that you "+
                         "could possibly crawl through, were you more "+
                         "dextrous.")
        return self.actions()

    def gate(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def lighthouse(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        encounter = self.marcianoCheck()
        if encounter:
            return encounter
        if ( "Coliseum Complete" in self.c.flags and
             "Greek Fortress" not in self.c.flags):
            self.text = ("Escort: We shall continue to march left, sir.")
        return self.actions()

    def nook(self, selectionIndex=None):
        thisIca = "Ica 4"
        self.c.flags[thisIca] = True
        self.view = "store"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        npc = "Ica"
        skill1 = "Piercing Quad"
        skill2 = "Freezing Arrow"
        skillPrice1 = 3000
        skillPrice2 = 200
        tunic = "Elven Tunic"
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
            X = 2
            Y = 7
            return self.actions({'area': "Greece",
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
            self.text = ("You crawl through the hole and find yourself "+
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
            self.text = ("You crawl through the hole and find yourself "+
                         "in a dark, damp nook."+
                         "\n"+npc+": What do you seek today, archer?")
        return self.actions({'items for sale': [tunic]+[None]*8})

    def shadeLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def shadeRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 21
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def shadeMiddle(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 22
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def shadeCorner(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 23
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def marciano(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.view = "battle"
            return self.actions({'enemy': "Marciano5"})            
        if "Marciano5" not in self.c.flags['Kills']:
            self.c.flags['New Song'] = "Drat"
            self.text = ("Marciano: This is the end, my friend."
                         "\nToshe: ...That's it? At least you rhymed this time." +
                         "\nMarciano: Silence!" +
                         "\nMarciano advances toward you.")   
            self.menu = ["Brace yourself."]
        elif "Marciano5" in self.c.flags['Kills']:
            X = 12
            Y = 18
            return self.actions({'area': "Greece",
                                 'coordinates': (X, Y)})
        return self.actions()
