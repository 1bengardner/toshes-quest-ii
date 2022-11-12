"""
File: TUALairOfTheMagi.py
Author: Ben Gardner
Created: October 27, 2022
Revised: November 12, 2022
"""


import random


class LairOfTheMagi:

    name = "Lair of the Magi"
    audio = "Perilous Hour"

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
        spid = self.spiderStairs
        arch = self.archway
        splt = self.split
        dnLt = self.downLeft
        dnRt = self.downRight
        upLt = self.upLeft
        upRt = self.upRight
        dnL2 = self.downLeft2
        dnR2 = self.downRight2
        upL2 = self.upLeft2
        upR2 = self.upRight2
        noRt = self.noRight
        noLt = self.noLeft
        strU = self.stairsUp
        strD = self.stairsDown
        encL = self.enclaveLeft
        encR = self.enclaveRight
        encU = self.enclaveUp
        noR2 = self.noRight2
        noL2 = self.noLeft2
        slit = self.arrowSlit
        cell = self.prisonCell
        spl2 = self.split2
        lvr1 = self.leverRoom1
        lvr2 = self.leverRoom2
        lvr3 = self.leverRoom3
        chm1 = self.chamber1
        chm2 = self.chamber2
        chm3 = self.chamber3
        sewr = self.sewerGrate
        towr = self.tower
        warp = self.warp
        roof = self.roof
        rid1 = self.riddle1
        rid2 = self.riddle2
        rid3 = self.riddle3
        rid4 = self.riddle4
        rid5 = self.riddle5
        rid6 = self.riddle6
        rid7 = self.riddle7
        rid8 = self.riddle8

        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, chm1, None, chm2, None, lvr3, None, roof, None, warp, None],
            [None, None, None, None, None, None, None, None, None, towr, None],
            [None, chm3, None, None, None, encU, None, None, None, None, None],
            [None, None, None, None, dnR2, sewr, dnL2, None, None, None, None],
            [None, lvr1, None, encL, noR2, None, noL2, encR, None, lvr2, None],
            [None, None, None, None, upR2, splt, upL2, None, None, None, None],
            [None, None, None, None, None, strD, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, strU, None, None, None, None, None],
            [None, None, None, None, rid4, spl2, rid5, None, None, None, None],
            [None, None, None, rid3, upLt, None, upRt, dnLt, None, None, None],
            [None, None, dnRt, upLt, None, None, None, rid6, dnLt, None, None],
            [None, slit, noRt, None, None, None, None, None, noLt, cell, None],
            [None, None, upRt, rid2, None, None, None, dnRt, upLt, None, None],
            [None, None, None, upRt, dnLt, None, dnRt, rid7, None, None, None],
            [None, None, None, None, rid1, splt, rid8, None, None, None, None],
            [None, None, None, None, None, arch, None, None, None, None, None],
            [None, None, None, None, None, spid, None, None, None, None, None],
            [None, None, None, None, None, entr, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None]]

        punishers = {
            "Arcane Sorcerer": 60,
            "Death Warrior": 40,
        }

        patrollers = {
            "Arcane Sorcerer": 11,
            "Death Warrior": 14,
            "Masked Magus": 8,
            "Time Wizard": 1,
        }

        zealots = {
            "Abomination": 32,
        }

        conjurers = {
            "Choronzon": 40,
        }

        magi = {
            "Corporeal Magus": 36,
        }

        self.encounters = {
            entr: {},
            spid: {},
            arch: {},
            splt: punishers,
            dnLt: patrollers,
            dnRt: patrollers,
            upLt: patrollers,
            upRt: patrollers,
            dnL2: zealots,
            dnR2: conjurers,
            upL2: zealots,
            upR2: conjurers,
            noRt: punishers,
            noLt: punishers,
            strU: {},
            strD: {},
            encL: {},
            encR: {},
            encU: {},
            noR2: conjurers,
            noL2: zealots,
            slit: {},
            cell: {},
            spl2: patrollers,
            lvr1: {},
            lvr2: {},
            lvr3: {},
            chm1: {},
            chm2: {},
            chm3: {},
            sewr: magi,
            towr: {},
            warp: {},
            roof: {},
            rid1: {},
            rid2: {},
            rid3: {},
            rid4: {},
            rid5: {},
            rid6: {},
            rid7: {},
            rid8: {},
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

    def roll(self, numberOfSides=100):
        return random.randint(1, numberOfSides)

    def colourActions(self):
        phrases = {
            'End with grey':
                "In the end, all will be shrouded in fog.",
            'Red-orange':
                "The inner flame is revealed just after the fire starts.",
            'Orange-turquoise':
                "Before visiting the ocean, tend to the goldfish.",
            'Yellow-green':
                "Basking in the sun grants good health immediately.",
            'Green-turquoise':
                "Algae can be seen just before the sea reaches high tide.",
            'Green-blue':
                "Sit in the grass, then look to the sky.",
            'Purple-pink':
                "Both are pretty, though the more royal immediately precedes the second.",
            'Pink-grey':
                "The cherry blossom blooms just before its colour fades.",
        }
        if "Colours" not in self.c.flags or len(self.c.flags['Colours']) == len(phrases):
            self.c.flags['Colours'] = set()

        colour = random.choice([phrase for phrase in phrases if phrase not in self.c.flags['Colours']])
        self.c.flags['Colours'].add(colour)
        self.text = "You pass through a dark, stone hall. You read a message engraved on the wall:\n\"%s\"" % phrases[colour]

        return self.actions()

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        
        if "Lair Entrance" not in self.c.flags:
            self.text = "You reach the palace entrance and see four spires atop its face."
            if self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie: It's go time, baby."
        else:
            self.text = "You reach the entrance to the lair."

        return self.actions()

    def spiderStairs(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []

        if "Masked Altercation" not in self.c.flags:
            self.c.flags['Masked Altercation'] = True
            self.view = "battle"
            return self.actions({'enemy': "Masked Magus",
                                 'mercenaries': self.c.mercenaries})

        if "Spider Steps" not in self.c.flags:
            self.c.flags['Spider Steps'] = True
            self.text = "You come to a series of putrid stairs covered in cobwebs."
            self.text += "\nToshe: Yuck."

        return self.actions()

    def archway(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []

        if "Dark Arch" not in self.c.flags:
            self.c.flags['Lair Entrance'] = True
            self.c.flags['Dark Arch'] = True
            if self.c.hasMercenary("Qendresa"):
                self.text = "Qendresa: This structure appears to be a lair of some sort."
            elif self.c.hasMercenary("Barrie"):
                self.text = "Barrie: It looks real dark beyond that arch."

        return self.actions()

    def split(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        
        if "Lair Fork" not in self.c.flags:
            self.c.flags['Lair Fork'] = True
            if self.c.hasMercenary("Barrie"):
                self.text = "Barrie: Looks like we got ourselves a fork in the road."
            else:
                self.text = "Toshe: The way ahead is blocked."

        return self.actions()

    def downLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def downRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def upLeft(self, selectionIndex=None):
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

    def downLeft2(self, selectionIndex=None):
        return self.downLeft(selectionIndex)

    def downRight2(self, selectionIndex=None):
        return self.downRight(selectionIndex)

    def upLeft2(self, selectionIndex=None):
        return self.upLeft(selectionIndex)

    def upRight2(self, selectionIndex=None):
        return self.upRight(selectionIndex)

    def noRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def noLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def stairsUp(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []

        if selectionIndex == 0:
            X = 5
            Y = 7
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})

        self.menu = ["Ascend the stairs."]

        return self.actions()

    def stairsDown(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []

        if selectionIndex == 0:
            X = 5
            Y = 9
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})

        self.menu = ["Descend the stairs."]

        return self.actions()

    def enclaveLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []

        if "Conjurer Altercation" not in self.c.flags:
            self.c.flags['Conjurer Altercation'] = True
            self.view = "battle"
            self.text = "Conjurer: You shall not enter the room of the conjurer!"
            return self.actions({'enemy': "Occult Conjurer",
                                 'mercenaries': self.c.mercenaries})

        if selectionIndex == 0:
            X = 1
            Y = 5
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})

        self.text = "There is a gate to the left with greenery just beyond it."
        self.menu = ["Open the gate."]

        return self.actions()

    def enclaveRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []

        if "Zealot Altercation" not in self.c.flags:
            self.c.flags['Zealot Altercation'] = True
            self.view = "battle"
            self.text = "Zealot: Halt! None may enter the flame worshipper's quarters!"
            return self.actions({'enemy': "Fire Zealot",
                                 'mercenaries': self.c.mercenaries})

        if selectionIndex == 0:
            X = 9
            Y = 5
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})

        self.text = "There is a gate to the right with greenery just beyond it."
        self.menu = ["Open the gate."]

        return self.actions()

    def enclaveUp(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []

        if "Magus Altercation" not in self.c.flags:
            self.c.flags['Magus Altercation'] = True
            self.view = "battle"
            self.text = "Predecessor: Shhhhaaah..."
            return self.actions({'enemy': "Magus Predecessor",
                                 'mercenaries': self.c.mercenaries})

        if selectionIndex == 0:
            X = 5
            Y = 1
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1 or selectionIndex == 2:
            self.view = "battle"
            self.text = "A Corporeal Magus appears!"
            return self.actions({'enemy': "Corporeal Magus",
                                 'mercenaries': self.c.mercenaries})

        self.text = "You enter a corridor with three doors."
        self.menu = [
            "Enter the top door.",
            "Enter the left door.",
            "Enter the right door.",
        ]

        return self.actions()

    def noRight2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def noLeft2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def arrowSlit(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        
        self.text = "You come across an unmanned arrowslit."
        self.text += "\nToshe: Hey, they could have used that to shoot me when I was outside."
        if self.c.hasMercenary("Barrie"):
            self.text += "\nBarrie: Well. Certainly glad they didn't!"
        elif self.c.hasMercenary("Qendresa"):
            self.text += "\nQendresa: Thankfully, they did not."

        return self.actions()

    def prisonCell(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []

        if "Jail Altercation" not in self.c.flags:
            self.c.flags['Jail Altercation'] = True
            self.view = "battle"
            return self.actions({'enemy': "Magus's Henchman",
                                 'mercenaries': self.c.mercenaries})
        
        self.text = "You enter an empty prison cell."
        if "Empty Jail" not in self.c.flags:
            self.c.flags['Empty Jail'] = True
            treasure = "Morning Star"
            if self.c.wisdom > self.c.dexterity and self.c.wisdom > self.c.strength:
                treasure = "Avadavra Wand"
            elif self.c.dexterity > self.c.strength:
                treasure = "Eucalyptus Bow"
            elif self.c.dexterity > 35:
                treasure = "Glaive"
            aOrAn = "an" if treasure in ("A", "E", "I", "O", "U")\
                    else "a"
            self.text += ("\nYou find %s %s!" % (aOrAn, treasure))
            return self.actions({'item': treasure})
        else:
            self.text += "\nToshe: They have a jail, but no prisoners. What the hell?"

        return self.actions()

    def split2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()
        
    def leverCommon(self, levers, selectionIndex=None):
        leverOrder = [
            "red",
            "orange",
            "yellow",
            "green",
            "turquoise",
            "blue",
            "purple",
            "pink",
            "grey",
        ]

        if selectionIndex is not None:
            selectedLever = levers[selectionIndex]
            if selectedLever in self.c.flags['Levers']:
                self.text = "You attempt to reverse the %s lever, but it won't budge." % selectedLever                
            elif len(self.c.flags['Levers']) < leverOrder.index(selectedLever):
                if len(self.c.flags['Levers']) < 3:
                    self.c.flags['Get A Clue 1'] = True
                elif len(self.c.flags['Levers']) < 6:
                    self.c.flags['Get A Clue 2'] = True
                elif len(self.c.flags['Levers']) < 8:
                    self.c.flags['Get A Clue 3'] = True
                self.view = "battle"
                self.c.flags['Levers'].clear()
                if self.roll(30) == 1:
                    self.text = "As you flip the %s lever, the switches all quickly reverse and the ground emits a deep rumble." % selectedLever
                    return self.actions({'enemy': "Dougou",
                                         'mercenaries': self.c.mercenaries})
                else:
                    self.text = "As you flip the %s lever, the switches all quickly reverse. A guard rushes in." % selectedLever
                    if "Last Guard Fight" in self.c.flags and self.c.flags['Last Guard Fight'] == "Touin DePenk":
                        guard = "Wonnen Daztinque"
                    else:
                        guard = "Touin DePenk"
                    self.c.flags['Last Guard Fight'] = guard
                    phrase = random.choice([
                        "I have you now!",
                        "You're all mine!",
                        "You'll feel this one for sure!",
                        "I'm gonna snatch you right up!",
                        "I can't wait to rip you a new one.",
                    ])
                    self.text += "\n%s: %s" % (guard.split(" ")[0], phrase)
                    return self.actions({'enemy': guard,
                                         'mercenaries': self.c.mercenaries})
            else:
                self.c.flags['Levers'].add(selectedLever)
                self.text = "You flip the %s lever and it begins to shine." % selectedLever
                if len(self.c.flags['Levers']) == len(leverOrder):
                    self.c.flags['Lair Levers Complete'] = True
                    self.text += "\nYou hear a pop sound not too far away."
                    self.text += "\nToshe: That's all of them."
        elif "Lever Room" not in self.c.flags:
            self.c.flags['Lever Room'] = True
            self.c.flags['Levers'] = set()
            if self.c.hasMercenary("Barrie"):
                self.text = "\nBarrie: Holy Hannah! What is that?"
        elif "Get A Clue 1" in self.c.flags:
            del self.c.flags['Get A Clue 1']
            self.text = "Toshe: There's gotta be some clue about the right order."
        elif "Get A Clue 2" in self.c.flags:
            del self.c.flags['Get A Clue 2']
            self.text = "Toshe: I bet I can discover something from those engravings downstairs."
        elif "Get A Clue 3" in self.c.flags:
            del self.c.flags['Get A Clue 3']
            self.text = "Toshe: Fuck! So close."
        else:
            self.text = "You enter a room with three levers."

        self.imageIndex += len([colour for colour in levers if colour in self.c.flags['Levers']])
        self.menu = ["Switch %s the %s lever." % ("off" if lever in self.c.flags['Levers'] else "on", lever) for lever in levers]
        self.menu.append("Leave the room.")

        return self.actions()
        

    def leverRoom1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        self.menu = []

        if selectionIndex == 3:
            X = 3
            Y = 5
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})

        levers = [
            "red",
            "turquoise",
            "purple",
        ]

        return self.leverCommon(levers, selectionIndex)

    def leverRoom2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 24
        self.text = None
        self.helpText = None
        self.menu = []

        if selectionIndex == 3:
            X = 7
            Y = 5
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})

        levers = [
            "yellow",
            "pink",
            "blue",
        ]

        return self.leverCommon(levers, selectionIndex)

    def leverRoom3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 28
        self.text = None
        self.helpText = None
        self.menu = []

        if selectionIndex == 3:
            X = 5
            Y = 3
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})

        levers = [
            "orange",
            "grey",
            "green",
        ]

        return self.leverCommon(levers, selectionIndex)

    def chamber1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 32
        self.text = None
        self.helpText = None
        self.menu = []

        if "Lair Archmages" not in self.c.flags:
            self.tempFlag = "Lair Archmages"
            self.text = "You slip through the sewer hole below and fall into a torchlit chamber several feet below. You are flanked by prison cells containing captive high wizards."
            if self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: The archmages of Igalo!"
            if self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie: Niplin must have been hiding them here all along."
            if [flag for flag in set(["Mudslide", "Floodtide", "Hot Coals"]) if flag in self.c.flags]:
                self.text += "\nArchmage: Please, Toshe, you must help us."
            else:
                self.text += "\nArchmage: Please, help us."
        elif selectionIndex == 0 and "Archmages Helped 1" not in self.c.flags:
            self.tempFlag = "Archmages Helped 1"
            self.text = "You attempt to pry open the cell bars, but they won't budge."
            self.text += "\nArchmage: These doors have been sealed with strong magic."
            if self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie attempts to open the cell with a blast of magic. The blast fades with no effect."
                self.text += "\nBarrie: Damn!"
            self.menu = [
                "Attempt to free the archmages again."
            ]
        elif selectionIndex == 0 and ("Archmages Helped 2" not in self.c.flags or "Pespozeor Sound" in self.c.flags and "Time Wizard" in self.c.flags and self.roll() > 50):
            self.tempFlag = "Archmages Helped 2"
            self.text = "You attempt once more to pry open the cell bars, but they won't budge."
            self.text += "\nArchmage: %s" % random.choice([
                "Unfortunately, a spell has been cast upon us, stripping us of our arcane power.",
                "It seems that our captors have placed a spell upon us, rendering us...quite fragile.",
                "There must be some other path forward. With our abilities in stasis, we cannot aid you.",
            ])
            self.text += "\nA Time Wizard teleports into the room."
            self.text += "\nTime Wizard: %s" % random.choice([
                "Let us put an end to this nonsense.",
                "I see we have a visitor.",
                "May I escort you out?",
                "Silence!",
            ])
            self.menu = ["Brace yourself."]
            if "Time Wizard" in self.c.flags:
                del self.c.flags['Time Wizard']
        elif selectionIndex == 0 and "Time Wizard" not in self.c.flags:
            self.c.flags['Time Wizard'] = True
            self.view = "battle"
            return self.actions({'enemy': "Time Wizard",
                                 'mercenaries': self.c.mercenaries})
        elif "Pespozeor Sound" not in self.c.flags and "Time Wizard" in self.c.flags:
            self.c.flags['Pespozeor Sound'] = True
            if self.c.hasMercenary("Barrie"):
                self.text = "Barrie: I can sense more coming. We're outnumbered."
            elif [flag for flag in set(["Mudslide", "Floodtide", "Hot Coals"]) if flag in self.c.flags]:
                self.text = "Archmage: Your presence is known here, Toshe."
            else:
                self.text = "Toshe: About time."
            self.text += "\nYou feel a deep vibration as a thud sounds from the next chamber."
            if self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: From what provenance is that noise?"
            else:
                self.text += "\nArchmage: That sound...a dire being..."
                self.text += "\nThe archmages retreat slightly."
        elif selectionIndex == 0:
            self.text = random.choice([
                "You attempt to open the cells in any way possible. The attempt fails.",
                "You search for a way to pick the locks, but cannot find a suitable material.",
                "You attempt to pick the locks with your weapon. It is futile.",
                "You look for holes in the cell wall to attempt a break-in, but find nothing.",
                "Before you strike the cell bars once more, an archmage speaks.\nArchmage: It is no use. Perhaps you shall find a way out for yourself and alert others."
            ])
        elif selectionIndex == 1:
            X = 3
            Y = 1
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})

        if "Time Wizard" in self.c.flags:
            self.menu = [
                "Attempt to free the archmages again.",
                "Enter the next chamber."
            ]
        elif not self.menu:
            self.menu = [
                "Help the archmages."
            ]
        return self.actions()

    def chamber2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 38
        self.text = None
        self.helpText = None
        self.menu = []

        if "Pespozeor Rendezvous" not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            if self.c.hasMercenary("Qendresa"):
                self.text = "Qendresa: Toshe...what is that?"
            else:
                self.text = "You enter the chamber ahead. It is illuminated with red torch flame."
            self.text += "\nYou see a gigantic beast ready to pounce."
            self.text += "\nPespozeor: Graaagh!!"
            self.tempFlag = "Pespozeor Rendezvous"
            self.menu = ["Face Pespozeor."]

        elif selectionIndex == 0 and "Pespozeor Final" not in self.c.flags:
            self.view = "battle"
            self.c.flags['Pespozeor Final'] = True
            return self.actions({'enemy': "Final Pespozeor",
                                 'mercenaries': self.c.mercenaries})
                                 
        elif selectionIndex == 0:
            X = 1
            Y = 3
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})            

        else:
            self.imageIndex = 33
            self.text = "The torches ahead glow bright green."
            self.menu = ["Proceed through the door."]

        return self.actions()

    def chamber3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 35
        self.text = None
        self.helpText = None
        self.menu = []

        if "Niplin 1" not in self.c.flags:
            self.tempFlag = "Niplin 1"
            self.text = "You step into a twisted throne room."
            self.text += "\nA broad figure emerges from a dark corner."
            self.text += "\nNiplin: You showed up."
            self.menu = [
                "\"Sure did.\"",
                "\"Who are you?\""
            ]
        elif "Niplin 2" not in self.c.flags:
            self.tempFlag = "Niplin 2"
            if selectionIndex == 0:
                self.text = "Toshe: Sure did."
                self.text += "\nNiplin: You've come to challenge me. You want to free the archmages."
                self.menu = [
                    "\"Yes, I do.\"",
                    "\"No, I want you dead.\""
                ]
            elif selectionIndex == 1:
                self.c.flags['New Song'] = "Drat"
                self.c.flags['Niplin has no manners'] = True
                self.text = "Toshe: Who are you?"
                self.text += "\nNiplin: You don't recognize me? Where are my manners..."
                self.text += "\nNiplin unsheathes his speckled greatsword as he steps closer."
                self.menu = ["Brace yourself."]
            elif selectionIndex is None:
                self.text = "Niplin: You've come to challenge me. You want to free the archmages."
                self.menu = [
                    "\"Yes, I do.\"",
                    "\"No, I want you dead.\""
                ]
        elif "Niplin has no manners" not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            self.tempFlag = "Niplin has no manners"
            if selectionIndex == 0:
                self.text = "Toshe: Yes, I do."
                self.text += "\nNiplin: Well, you know what they say."
                self.text += "\nNiplin slowly unsheathes his speckled greatsword."
                self.text += "\nNiplin: No good deed goes unpunished."
            elif selectionIndex == 1:
                self.text = "Toshe: No, I want you dead."
                self.text += "\nNiplin: Commence the serenade."
                self.text += "\nNiplin clasps the hilt of his sword and makes his way toward you."
            else:
                self.text = "Niplin: Have you decided to face your fears?"
                self.text += "\nNiplin draws his speckled greatsword and casually rests it over his shoulder."
            self.menu = ["Brace yourself."]
        elif "Niplin Battle" not in self.c.flags:
            self.c.flags['Niplin Battle'] = True
            self.view = "battle"
            return self.actions({'enemy': "Niplin",
                                 'mercenaries': self.c.mercenaries})
        elif "Niplin Aftermath" not in self.c.flags:
            self.audio = None
            self.c.flags['Niplin Aftermath'] = True
            self.text = "Niplin is knocked down by your final blow."
            self.text += "\nNiplin: Urgh..."
            self.text += "\nNiplin slowly kneels from his fallen position."
            self.text += "\nA white light shines upon him as he sheds his armour."
            self.text += "\nYou black out."
        elif "Riplin Encounter" not in self.c.flags:
            self.tempFlag = "Riplin Encounter"
            self.text = "You regain consciousness."
            self.text += "\nA fervent figure is looming over you, ready to strike."
            self.text += "\nToshe: What the fuck?"
            self.menu = ["Brace yourself."]
        elif "Riplin Battle" not in self.c.flags:
            self.c.flags['Riplin Battle'] = True
            self.view = "battle"
            return self.actions({'enemy': "Riplin",
                                 'mercenaries': self.c.mercenaries})
        elif "Riplin Aftermath" not in self.c.flags:
            self.c.flags['Riplin Aftermath'] = True
            self.text = "Riplin's body remains still on the cold stone floor."
            self.text += "\nRiplin: ...I underestimated you."
            self.text += "\nAn ominous orb rolls out from Riplin's unfurled glove."
            self.text += "\nRiplin: This orb contains my power. Use it."
            self.text += "\nYou find the Ominous Orb!"
            self.menu = [
                "Take Riplin's armour.",
                "Explore the throne room."
            ]
            return self.actions({'item': "Ominous Orb"})
        else:
            if selectionIndex == 0:
                if "Niplin's Armour" not in self.c.flags:
                    self.c.flags["Niplin's Armour"] = True
                    if self.c.dexterity < self.c.wisdom > self.c.strength:
                        armour = "Riplin's Mageplate"
                    elif self.c.strength >= 130 or self.c.dexterity < self.c.strength >= 100:
                        armour = "Riplin's Breastplate"
                    else:
                        armour = "Riplin's Greatvest"
                    self.text = "You find %s!" % armour
                    self.menu = ["Explore the throne room."]
                    return self.actions({'item': armour})
                else:
                    X = 9
                    Y = 2
                    return self.actions({'area': "Lair of the Magi",
                                         'coordinates': (X, Y)})
            elif selectionIndex == 1:
                self.text = "You search the throne room for interesting artifacts. Every decoration seems cursed."
                if self.c.hasMercenary("Qendresa"):
                    self.text += "\nQendresa: Come, Toshe. Let us proceed."
                elif self.c.hasMercenary("Barrie"):
                    self.text += "\nBarrie: You did it, bud. Now let's get a move on."
            if "Niplin's Armour" in self.c.flags:
                self.menu = ["Explore the throne room."]
            else:
                self.menu = [
                    "Take Riplin's armour.",
                    "Explore the throne room."
                ]

        return self.actions()

    def sewerGrate(self, selectionIndex=None):
        if "Lair Levers Complete" not in self.c.flags:
            return self.split2()
            
        self.view = "travel"
        self.imageIndex = 34
        self.text = None
        self.helpText = None
        self.menu = []

        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Lair of the Magi",
                                 'coordinates': (X, Y)})

        self.text = "You see a steaming sewer grate in the floor."
        self.menu = ["Crawl into the grate."]

        return self.actions()

    def tower(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 36
        self.text = None
        self.helpText = None
        self.menu = []
        
        if "Lair Tower" not in self.c.flags:
            self.c.flags['Lair Tower'] = True
            if self.c.hasMercenary("Qendresa"):
                self.text = "Qendresa: T-Toshe!"
            else:
                self.text = "Toshe: Oh shit!"
            self.text += "\nYou feel light energy take hold of you as you are rapidly propelled upward."
            self.text += "\nYour eyes shut involuntarily."
            self.text += "\nDistant speech from the archmages forms a chorus of reposeful voices."
            self.text += "\nArchmages: Toshe...Thank you...Igalo holds you in esteem..."
            self.text += "\nYou feel the chains of evil breaking apart."
            self.text += "\nYou come to and find yourself in the top chamber of a tower."
            if self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: What happened?"
                self.text += "\nToshe: No fucking idea. That was weird."
            if self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie: That was a trip. We're so high."

        return self.actions()

    def warp(self, selectionIndex=None):
        X = 7
        Y = 1
        return self.actions({'area': "Lair of the Magi",
                             'coordinates': (X, Y)})

    def roof(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 37
        self.text = None
        self.helpText = None
        self.menu = []
        
        self.text = ""
        
        if "Lair Roof" not in self.c.flags:
            self.c.flags['Lair Roof'] = True
            self.text = "You step out from the tower and find yourself on the roof of the lair by a tall spire."
            if self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie: Don't look down!"

        if selectionIndex == 0:
            self.c.flags['Gargoyle Kills Before This One'] = 0
            if "Gargoyle" in self.c.flags['Kills']:
                self.c.flags['Gargoyle Kills Before This One'] = self.c.flags['Kills']['Gargoyle']
            self.view = "battle"
            return self.actions({'enemy': "Gargoyle"})

        if 'Gargoyle Kills Before This One' in self.c.flags and (
             "Gargoyle" not in self.c.flags['Kills'] or
             self.c.flags['Gargoyle Kills Before This One'] == self.c.flags['Kills']['Gargoyle']):
            X = 1
            Y = 1
            return self.actions({'area': "Thessaloniki",
                                 'coordinates': (X, Y)})
        else:
            self.text += "\nA gargoyle coasting at eye-level directly approaches you."
            self.text += "\nGargoyle: %s" % random.choice([
                "Be thou looking for a flight?",
                "May I aid you this day?",
                "Visitor, what brings thee?",
                "Incoming!",
                "Human...?",
            ])
            if 'Gargoyle Kills Before This One' in self.c.flags:
                remarks = []
                if self.c.hasMercenary("Qendresa"):
                    remarks += [
                        "\nQendresa: " + remark for remark in [
                            "Perhaps you ought to befriend it. We need a way to get down.",
                            "Toshe, be kind. It is aged.",
                            "The poor gargoyle cannot see! Leave it alone.",
                            "This may be our chance to depart. Show it compassion"
                        ]
                    ]
                if self.c.hasMercenary("Barrie"):
                    remarks += [
                        "\nBarrie: " + remark for remark in [
                            "Don't let it get close. Gargoyles can be aggressive.",
                            "Give that garg some space, eh? They're territorial creatures.",
                            "Back off from it a bit!",
                            "Keep your distance."
                        ]
                    ]
                if not self.c.hasMercenary("Qendresa") and not self.c.hasMercenary("Barrie"):
                    remarks += [
                        "\nToshe: " + remark for remark in [
                            "Where are these things coming from?",
                            "How many gargoyles are there?",
                            "What the fuck? I just killed you.",
                            "Stop!"
                        ]
                    ]
                self.text += random.choice(remarks)
            self.menu = ["Brace yourself."]
        
        self.text = self.text.strip()

        return self.actions()

    def riddleMain(self, riddleNumber, phrase):
        if "Henchmen" not in self.c.flags:
            self.c.flags['Henchmen'] = set()
        if riddleNumber not in self.c.flags['Henchmen']:
            self.c.flags['Henchmen'].add(riddleNumber)
            self.c.flags['Jail Altercation'] = True
            self.view = "battle"
            return self.actions({'enemy': "Magus's Henchman",
                                 'mercenaries': self.c.mercenaries})
        else:
            self.text = "You read a message engraved on a wall of the stone hall:\n\"%s\"" % phrase

    def riddle1(self, selectionIndex=None):
        self.upRight(selectionIndex)

        self.riddleMain(1, "The inner flame is revealed just after the fire starts.")

        return self.actions()

    def riddle2(self, selectionIndex=None):
        self.downLeft(selectionIndex)

        self.riddleMain(2, "Before visiting the ocean, tend to the goldfish.")

        return self.actions()

    def riddle3(self, selectionIndex=None):
        self.downRight(selectionIndex)

        self.riddleMain(3, "Basking in the sun grants good health immediately.")

        return self.actions()

    def riddle4(self, selectionIndex=None):
        self.downRight(selectionIndex)

        self.riddleMain(4, "Sit in the grass, then look to the sky.")

        return self.actions()

    def riddle5(self, selectionIndex=None):
        self.downLeft(selectionIndex)

        self.riddleMain(5, "Algae can be seen just before the sea reaches high tide.")

        return self.actions()

    def riddle6(self, selectionIndex=None):
        self.upRight(selectionIndex)

        self.riddleMain(6, "The cherry blossom blooms just before its colour fades.")

        return self.actions()

    def riddle7(self, selectionIndex=None):
        self.upLeft(selectionIndex)

        self.riddleMain(7, "In the end, all will be shrouded in fog.")

        return self.actions()

    def riddle8(self, selectionIndex=None):
        self.upLeft(selectionIndex)

        self.riddleMain(8, "Both are pretty, though the more royal immediately precedes the second.")

        return self.actions()