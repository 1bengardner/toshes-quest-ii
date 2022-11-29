"""
File: TUAAlbanianDesert.py
Author: Ben Gardner
Created: December 25, 2013
Revised: November 28, 2022
"""


import random
from TUAStatics import Static


class AlbanianDesert:

    name = "Albanian Desert"
    audio = "Duststorm"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"
        
        if "Gold Mined" not in self.c.flags:
            self.c.flags['Gold Mined'] = {1: 0,
                                          2: 0,
                                          3: 0,
                                          4: 0}

        wrp1 = self.westernKosovo1
        wrp2 = self.westernKosovo2
        wrp3 = self.westernKosovo3
        wrp4 = self.westernKosovo4
        wrp5 = self.westernKosovo5
        wrp6 = self.rumadanVillageEntrance
        wrp7 = self.rumadanVillageExit
        scut = self.scutariPassage
        nml1 = self.normal1
        nml2 = self.normal2
        nml3 = self.normal3
        notU = self.notUp
        notD = self.notDown
        notR = self.notRight
        notL = self.notLeft
        upRt = self.upRight
        upLt = self.upLeft
        dnRt = self.downRight
        nooE = self.nookEntrance
        dnLt = self.downLeft
        down = self.down
        left = self.left
        watU = self.waterUp
        watD = self.waterDown
        watR = self.waterRight
        watL = self.waterLeft
        waUR = self.waterDownLeft
        waUL = self.waterDownRight
        waDR = self.waterUpLeft
        waDL = self.waterUpRight
        gld1 = self.goldMine1
        gld2 = self.goldMine2
        gld3 = self.goldMine3
        gld4 = self.goldMine4
        hotC = self.hotCoalsTeacher
        wel1 = self.well1
        wel2 = self.well2
        cast = self.castle
        wal1 = self.wall1
        wal2 = self.wall2
        geys = self.geyser
        paca = None if "Oukkar" in self.c.flags['Kills'] or "Plugged Geyser" not in self.c.flags else self.alpaca
        
        
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, down, None, None, None, None, None, None, None, None, None],
            [None, None, notL, dnLt, None, wrp1, None, None, None, None, None, None],
            [None, None, notL, notR, None, notL, wrp2, None, None, None, None, None],
            [None, scut, nml1, nml2, notU, nml2, nml1, wrp3, wrp4, None, None, None],
            [None, notL, nml2, nml3, nml2, nml1, nml2, nml3, nml2, wrp5, None, None],
            [None, notL, nml3, nml2, nml1, watD, watD, watD, nml1, notR, None, None],
            [None, upRt, hotC, nml1, watR, None, None, None, watL, nml3, dnLt, None],
            [None, None, None, notL, watD, waDL, None, None, waUR, gld1, notR, None],
            [None, None, dnRt, waUL, None, watL, waDL, None, None, waUR, notR, None],
            [None, None, watU, None, None, watL, wel1, waDL, None, None, watU, None],
            [None, None, None, None, waDR, nml3, nml2, watR, None, watD, None, None],
            [None, None, None, waDR, nml3, watD, watD, nml2, watU, nml2, left, None],
            [None, None, None, notL, watR, None, None, watL, nml2, notR, None, None],
            [None, None, None, upRt, watR, None, None, watL, nml1, upLt, None, None],
            [None, None, None, None, notL, watU, watU, nml1, notR, None, None, None],
            [None, None, None, None, notL, nml2, gld2, nml2, nml3, dnLt, None, None],
            [None, None, None, None, notL, nml1, nml2, nml3, nml2, upLt, None, None],
            [None, None, None, None, wrp6, wrp6, wrp6, wrp6, wrp6, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, wrp7, wrp7, wrp7, wrp7, wrp7, None, None, None],
            [None, None, None, None, notL, nml1, notD, notD, upLt, None, None, None],
            [None, None, None, None, upRt, nml2, None, None, None, None, None, None],
            [None, None, None, None, None, upRt, cast, notU, notU, left, None, None],
            [None, None, None, None, None, None, None, notL, notR, None, None, None],
            [None, None, None, None, nooE, notU, notU, nml3, nml2, dnLt, None, None],
            [None, None, paca, None, notL, watD, watD, nml2, nml1, gld3, dnLt, None],
            [None, None, geys, notU, watR, None, None, watL, nml2, nml3, upLt, None],
            [None, None, None, upRt, watR, None, None, watL, nml3, upLt, None, None],
            [None, None, None, None, notL, watU, watU, wel2, notR, None, None, None],
            [None, None, None, None, notL, nml2, nml3, nml2, nml1, dnLt, None, None],
            [None, None, None, None, upRt, nml3, nml2, nml1, nml2, notR, None, None],
            [None, None, None, None, None, upRt, gld4, nml2, nml3, upLt, None, None],
            [None, None, None, None, None, None, notL, nml3, notR, None, None, None],
            [None, None, None, None, None, None, upRt, nml2, notR, None, None, None],
            [None, None, None, None, None, None, None, wal1, wal2, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None]]
        
        if self.c.level < 14:       # 25%
            e = {'Sand Digger': 13,
                 'Rumadan Horseman': 7,
                 'Warlock': 3}
        elif self.c.level == 14:    # 24%
            e = {'Rumadan Horseman': 6,
                 'Warlock': 10,
                 'Gold Golem': 6,
                 'Adurbid': 2}
        elif self.c.level == 15:    # 23%
            e = {'Warlock': 5,
                 'Gold Golem': 11,
                 'Adurbid': 5,
                 'Dust Dweller': 2}
        elif self.c.level == 16:    # 22%
            e = {'Gold Golem': 5,
                 'Adurbid': 10,
                 'Dust Dweller': 5,
                 'Albanian Gladiator': 2}
        elif self.c.level == 17:    # 21%
            e = {'Adurbid': 4,
                 'Dust Dweller': 9,
                 'Albanian Gladiator': 4,
                 'Gritty Assailant': 2}
        elif self.c.level == 18:    # 20%
            e = {'Dust Dweller': 4,
                 'Albanian Gladiator': 8,
                 'Gritty Assailant': 4,
                 'Shadow Sniper': 2}
        elif self.c.level == 19:    # 19%
            e = {'Albanian Gladiator': 4,
                 'Gritty Assailant': 7,
                 'Shadow Sniper': 4,
                 'Shadow Hunter': 2}
        elif self.c.level == 20:    # 18%
            e = {'Gritty Assailant': 4,
                 'Shadow Sniper': 6,
                 'Shadow Hunter': 4,
                 'Giant Scorpion1': 2}
        elif self.c.level > 20:     # 17%
            e = {'Shadow Sniper': 4,
                 'Shadow Hunter': 5,
                 'Giant Scorpion1': 4,
                 'Manticore': 2}

        if self.c.level < 14 or self.c.level > 16:
            e['Gold Golem'] = 2

        e['Mirage'] = 4
             
        self.encounters = {wrp1: {},
                           wrp2: {},
                           wrp3: {},
                           wrp4: {},
                           wrp5: {},
                           wrp6: {},
                           wrp7: {},
                           scut: {},
                           nml1: e,
                           nml2: e,
                           nml3: e,
                           notU: e,
                           notD: e,
                           notR: e,
                           notL: e,
                           upRt: e,
                           upLt: e,
                           dnRt: e,
                           nooE: e,
                           dnLt: e,
                           down: e,
                           left: e,
                           watU: e,
                           watD: e,
                           watR: e,
                           watL: e,
                           waUR: e,
                           waUL: e,
                           waDR: e,
                           waDL: e,
                           gld1: e,
                           gld2: e,
                           gld3: e,
                           gld4: e,
                           hotC: e,
                           wel1: {},
                           wel2: {},
                           cast: {},
                           wal1: {},
                           wal2: {},
                           geys: {},
                           paca: {}
                           }
    
    def movementActions(self):
        self.c.ep -= 3
        if self.c.ep < 0:
            excess = 0 - self.c.ep
            self.c.ep += excess
            self.c.hp -= excess

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def westernKosovo1(self, selectionIndex=None):
        X = 1
        Y = 5
        return self.actions({'area': "Western Kosovo",
                             'coordinates': (X, Y)})

    def westernKosovo2(self, selectionIndex=None):
        X = 2
        Y = 6
        return self.actions({'area': "Western Kosovo",
                             'coordinates': (X, Y)})

    def westernKosovo3(self, selectionIndex=None):
        X = 3
        Y = 7
        return self.actions({'area': "Western Kosovo",
                             'coordinates': (X, Y)})

    def westernKosovo4(self, selectionIndex=None):
        X = 4
        Y = 7
        return self.actions({'area': "Western Kosovo",
                             'coordinates': (X, Y)})

    def westernKosovo5(self, selectionIndex=None):
        X = 5
        Y = 8
        return self.actions({'area': "Western Kosovo",
                             'coordinates': (X, Y)})

    def rumadanVillageEntrance(self, selectionIndex=None):
        X = 2
        Y = 2
        return self.actions({'area': "Rumadan Village",
                             'coordinates': (X, Y)})

    def rumadanVillageExit(self, selectionIndex=None):
        X = 2
        Y = 6
        return self.actions({'area': "Rumadan Village",
                             'coordinates': (X, Y)})

    def scutariPassage(self, selectionIndex=None):
        if selectionIndex == 0:
            self.c.flags['Sliding'] = True
            X = 6
            Y = 4
            return self.actions({'area': "Scutari Peninsula",
                                 'coordinates': (X, Y)})
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Crawling" in self.c.flags:
            del self.c.flags['Crawling']
            self.text = ("You crawl up the sand passage.")
        else:
            self.text = ("There is a dark, sloping tunnel in the sand dune.")
        self.menu = ["Go through the tunnel."]
        return self.actions()

    def normal1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if "Albanian Desert" not in self.c.flags:
            self.text = ("You feel weakened by the desert heat.")
            self.c.flags['Albanian Desert'] = True
        return self.actions()

    def normal2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if "Albanian Desert" not in self.c.flags:
            self.text = ("You feel weakened by the desert heat.")
            self.c.flags['Albanian Desert'] = True
        return self.actions()

    def normal3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if "Albanian Desert" not in self.c.flags:
            self.text = ("You feel weakened by the desert heat.")
            self.c.flags['Albanian Desert'] = True
        return self.actions()

    def notUp(self, selectionIndex=None):
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

    def notRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if "Albanian Desert" not in self.c.flags:
            self.text = ("You feel weakened by the desert heat.")
            self.c.flags['Albanian Desert'] = True
        return self.actions()

    def notLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if "Albanian Desert" not in self.c.flags:
            self.text = ("You feel weakened by the desert heat.")
            self.c.flags['Albanian Desert'] = True
        return self.actions()

    def upRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upLeft(self, selectionIndex=None):
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

    def nookEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
            
        if selectionIndex == 0:
            return Static.ICA_DATA['Ica 5']
        if "Oukkar" in self.c.flags['Kills'] and self.c.dexterity >= 75:
            self.text = ("\nYou spot a hidden passage up into the dune "+
                         "that appears to be accessible.")
            self.menu = ["Enter the dune."]
        else:
            self.text = ("\nYou spot a passage up into the dune "+
                         "that looks like it may be accessible, were you more "+
                         "dextrous.")
        return self.actions()

    def downLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def down(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def left(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def waterUp(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def waterDown(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def waterRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def waterLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def waterDownLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        self.menu = []
        if ( "Qendresa Albanian Desert Remark" not in self.c.flags and
             self.c.hasMercenary("Qendresa")):
            self.c.flags['Qendresa Albanian Desert Remark'] = True
            self.text = "Qendresa: Look what has become of Albania..."
        return self.actions()

    def waterDownRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def waterUpLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 21
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def waterUpRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 22
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def goldMine1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 23
        self.text = None
        self.helpText = None
        self.menu = []

        goldMineId = 1
        
        return self.goldMineMain(goldMineId, selectionIndex)

    def goldMine2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 23
        self.text = None
        self.helpText = None
        self.menu = []

        goldMineId = 2
        
        return self.goldMineMain(goldMineId, selectionIndex)

    def goldMine3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 23
        self.text = None
        self.helpText = None
        self.menu = []

        goldMineId = 3
        
        return self.goldMineMain(goldMineId, selectionIndex)

    def goldMine4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 23
        self.text = None
        self.helpText = None
        self.menu = []

        goldMineId = 4
        
        return self.goldMineMain(goldMineId, selectionIndex)

    def goldMineMain(self, goldMineId, selectionIndex):
        if selectionIndex == 0:
            roll = random.randint(1, 5)
            if roll == 1:
                self.text = ("You mine some gold ore!")
                self.c.flags['Gold Mined'][goldMineId] = self.c.level+1
                return self.actions({'item': "Gold Ore"})
            else:
                hpLoss = random.randint(10, 50)
                self.text = ("You swing your weapon at the rock, recoiling"
                             " and injuring"+
                             " yourself for %s damage." % hpLoss+
                             "\nToshe: Fuck!")
                if self.c.hasMercenary("Qendresa"):
                    self.text += random.choice(
                        ["\nQendresa: Be careful.",
                         "\nQendresa: Try again, you are almost there.",
                         "\nQendresa: Shall I take a swing?" +
                         "\nToshe: I've got it."])
                self.c.hp -= hpLoss
                self.menu = ["Mine the gold rock."]
        elif self.c.level > self.c.flags['Gold Mined'][goldMineId]:
            self.text = "You come across a rock containing rare gold ore."
            self.menu = ["Mine the gold rock."]
        else:
            self.text = "You see a mined gold rock."
        return self.actions()

    def hotCoalsTeacher(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Mysterious Red Wizard"
        skill = "Hot Coals"
        if selectionIndex == 0:
            self.text = ("Toshe: I'm not a big cowboy, but ok."+
                         "\n"+npc+": Hserf tae!"+
                         "\nThe wizard flicks his wand and teleports away.")
            self.c.flags[skill] = True
            return self.actions({'skill': skill,
                                 'cost': 0})
        elif selectionIndex == 1:
            random.seed(self.c.level)
            self.text = ("Toshe: No way in hell, you psycho!"+
                         "\n%s: So be it. Fartface." % npc+
                         "\nThe wizard teleports away, leaving magic dust.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: That guy was a knucklehead.")
            randomHpBoost = random.randint(-5, 15)
            if randomHpBoost < 0:
                self.text += ("\nYour maximum HP decreased by %s!" % -randomHpBoost)
            elif randomHpBoost > 0:
                self.text += ("\nYour maximum HP increased by %s!" % randomHpBoost)
            self.c.maxHp += randomHpBoost
            self.c.flags[skill] = True
        elif skill not in self.c.flags:
            self.imageIndex = 24
            self.c.flags['New Song'] = "Buddha"
            self.text = (npc+": Howdy, big cowboy. Wanna "+
                         "fill that noggin with knowledge?")
            self.menu = ["\"Yes.\"",
                         "\"No!\""]
        return self.actions()

    def well1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 25
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            event = random.choice(["Energy", "Heal", "Poison"])
            self.text = "You drink some water. "
            if event == "Energy":
                self.text += ("You feel re-energized.")
                self.c.ep += 20
            elif event == "Heal":
                self.text += ("You feel restored.")
                self.c.hp += 20
            elif event == "Poison":
                self.text += ("You feel sick.")
                self.c.hp -= 30
        else:
            self.text = ("You come across an old well.")
            if "Well" not in self.c.flags:
                self.text = ("\nToshe: This is familiar.")
                self.c.flags['Well'] = True
        self.menu = ["Drink from the well."]
        return self.actions()

    def well2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 26
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            event = random.choice(["Energy", "Heal", "Chunk"])
            self.text = "You drink some water. "
            if event == "Energy":
                self.text += ("You feel re-energized.")
                self.c.ep += 20
            elif event == "Heal":
                self.text += ("You feel restored.")
                self.c.hp += 20
            elif event == "Chunk":
                self.text += ("There is a chunk of dirt in it.")
                self.c.hp -= 30
        else:
            self.text = ("You come across a dusty well.")
            if "Well" not in self.c.flags:
                self.text = ("\nToshe: This is familiar.")
                self.c.flags['Well'] = True
        self.menu = ["Drink from the well."]
        return self.actions()

    def castle(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 27
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 13
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})
        if "Berlusconi Castle" not in self.c.flags:
            self.text = ("Toshe: Why is there a giant castle in the middle of" +
                         " the desert?")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: This...this must be the hiding" +
                              " place of that despicable Italian president.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: That's a weird place to live.")
            self.c.flags['Berlusconi Castle'] = True
        self.menu = ["Enter the castle."]
        return self.actions()

    def wall1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 28
        self.text = None
        self.helpText = None
        self.menu = []
        return self.wall(selectionIndex)

    def wall2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 29
        self.text = None
        self.helpText = None
        self.menu = []
        return self.wall(selectionIndex)

    def wall(self, selectionIndex=None):
        if ( selectionIndex == 0 and
             "Greek Wall Hole" not in self.c.flags):
            self.text = ("You swing at the crack and a large pile of stone" +
                         " crumbles from the wall.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: That's how you make an entrance!")
            self.menu = ["Enter the wall."]
            self.c.flags['Greek Wall Hole'] = True
        elif (selectionIndex == 0 and
              "Greek Wall Hole" in self.c.flags):
            X = 1
            Y = 2
            return self.actions({'area': "Hidden Passage",
                                 'coordinates': (X, Y)})
        elif ("Blueprint" not in self.c.flags and
              "Greek Wall" not in self.c.flags):
            self.text = ("You reach a massive wall bordering Greece." +
                         "\nToshe: If only I could find a way around this" +
                         " wall.")
            self.c.flags['Greek Wall'] = True
        elif ("Blueprint" in self.c.flags and
              "Greek Wall Hole" not in self.c.flags):
            self.text = ("Toshe: Ok, so it says on the blueprint" +
                         " that there should be a hole at this crack.")
            self.menu = ["Hit the crack."]
        elif "Greek Wall Hole" in self.c.flags:
            self.menu = ["Enter the wall."]
        return self.actions()
        
    def geyser(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 30
        self.text = None
        self.helpText = None
        self.menu = []
        
        if selectionIndex == 0:
            self.c.flags['Plugged Geyser'] = True
            X = 2
            Y = 27
            return self.actions({'area': "Albanian Desert",
                                 'coordinates': (X, Y)})
        elif "Plugged Geyser" not in self.c.flags:
            self.c.flags['Oukkar Entrance Found'] = True
            self.text = ("There is a large geyser blocking the way." +
                         " The pressure" +
                         " is too strong to be stopped by physical means.")
        elif "Plugged Geyser Aftermath" not in self.c.flags:
            self.imageIndex = 31
            self.text = ("You form a layer of ice atop the geyser.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Way to stay coolheaded...in a" +
                              " heated situation.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: Yaouw!")
                if self.c.hasMercenary("Barrie"):
                    self.text += ("\nBarrie: That's a funny noise.")
                    self.text += ("\nQendresa: No, look to the horizon." +
                                  "\nQendresa points to a volcano in the distance.")
            self.c.flags['Plugged Geyser Aftermath'] = True
        elif "Oukkar" not in self.c.flags['Kills']:
            self.imageIndex = 31
            self.text = ("There is a magical force far ahead.")
        elif "Niplin" not in self.c.flags['Kills']:
            self.imageIndex = 32
            if "Volcano Aftermath" not in self.c.flags:
                self.c.flags['Volcano Aftermath'] = True
                self.text = ("You slide down the mountain. The volcano collapses behind you.")
            else:
                self.text = ("The hot sun still shines mightily.")
                if self.c.hasMercenary("Qendresa"):
                    self.text += ("\nQendresa: Come, let us continue our quest.")
        else:
            self.imageIndex = 33
            self.text = ("You stare into the horizon in wonder.")
            if self.c.hasMercenary("Qendresa"):
                self.text += random.choice(
                    ["\nQendresa: We have certainly come a long way.",
                     "\nQendresa: What are you thinking about?",
                     "\nQendresa: Yaouw once stood here."]
                )

        if ( "Hailstorm" in [skill.NAME for skill in self.c.skills] and
             "Plugged Geyser" not in self.c.flags):
            self.menu = ["Cast Hailstorm."]
            
        return self.actions()
        
    def alpaca(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 34
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 6
            Y = 9
            return self.actions({'area': "Yaouw Volcano",
                                 'coordinates': (X, Y)})
        if "Oukkar" not in self.c.flags['Kills']:
            self.text = ("Alpaca: Wehh..." +
                         "\nIt looks like there is transportation" +
                         " conveniently waiting for you.")
            self.menu = ["Ride the alpaca up to the volcano."]
        return self.actions()
