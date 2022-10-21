"""
File: TUAYaouwVolcano.py
Author: Ben Gardner
Created: June 1, 2020
Revised: September 19, 2022
"""

import random

class YaouwVolcano:

    name = "Yaouw Volcano"
    audio = "Evening Mist"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"
        
        if "Lava Spouts Hit" not in self.c.flags:
            self.c.flags['Lava Spouts Hit'] = set()
        
        entr = self.entrance
        trai = self.trail
        gass = self.gas
        drop = self.dropHole
        danc = self.danceParty
        spo1 = self.spout1
        spo2 = self.spout2
        spo3 = self.spout3
        spo4 = self.spout4
        exit = self.exit
        fall = self.firefall
        lake = self.fireLake
        tpRt = self.topRight
        btLt = self.bottomLeft
        wall = self.wall
        dcln = self.decline
        pitt = self.pit
        esca = self.escapeRoute
        frag = self.fragment
        
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, spo1, None, pitt, tpRt, None, wall, tpRt, dcln, lake, tpRt, spo2, None],
            [None, dcln, None, None, lake, None, pitt, None, None, None, None, None, None],
            [None, btLt, fall, None, dcln, fall, lake, tpRt, fall, wall, tpRt, fall, None],
            [None, None, dcln, None, btLt, None, dcln, None, lake, None, None, pitt, None],
            [None, None, btLt, fall, lake, None, None, None, dcln, None, None, dcln, None],
            [None, None, dcln, danc, dcln, None, drop, None, btLt, esca, None, lake, None],
            [None, pitt, wall, pitt, wall, None, gass, None, None, lake, None, pitt, None],
            [None, dcln, None, dcln, None, None, trai, None, None, dcln, None, dcln, None],
            [None, spo4, None, wall, exit, None, entr, None, frag, wall, None, spo3, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None]
        ]
        
        entrance = {
            'Greater Dragon': 1
        }
        sneaky = {
            'Fire Demon': 3
        }
        regular = {
            'Fire Imp': 13,
            'Fire Demon': 7,
            'Hellhound': 5
        }
        guards = {
            'Hellhound': 40
        }
        magical = {
            'Fire Imp': 35,
            'Fire Demon': 5
        }
        fiery = {
            'Fire Demon': 30,
            'Fire Imp': 10
        }
        rare = {
            'Animated Magma': 5
        }
        
        self.encounters = {
            entr: entrance,
            trai: entrance,
            gass: entrance,
            drop: sneaky,
            dcln: regular,
            lake: fiery,
            fall: magical,
            spo1: guards,
            spo2: guards,
            spo3: guards,
            spo4: guards,
            tpRt: regular,
            btLt: regular,
            wall: regular,
            pitt: {},
            danc: rare,
            exit: {},
            esca: {},
            frag: entrance
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
        
    def roll(self):
        return random.randint(1, 100)

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = "You arrive at the base of a tremendous volcano."
        if "Alpaca Abandonment" not in self.c.flags:
            self.text += " Your alpaca promptly abandons you."
            self.c.flags['Alpaca Abandonment'] = True
        elif "Volcano Turn Back" in self.c.flags and "Can't Turn Back" not in self.c.flags:
            self.c.flags['Can\'t Turn Back'] = True
            self.text += "\nToshe: Oh wait...I can't turn back. Shit."
        return self.actions()

    def trail(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if "Arpegie" not in self.c.flags and self.c.hasMercenary("Qendresa"):
            self.text = ("%s: There is evil afoot. Dark forces are brewing up ahead." % "Qendresa")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\n%s: Hush, hush. You needn't be so dramatic, my grace. It's just a volcano. At least one of these shows up in just about every RPG ever." % "Barrie")
                self.text += ("\n%s: And what is this Arpegie? I have not heard of such things." % "Qendresa")
            self.c.flags['Arpegie'] = True
        return self.actions()

    def gas(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        self.c.flags["Volcano Turn Back"] = True
        self.text = ("You feel an intense heat from the crevice as you near the summit." +
                     "\nToshe: I can still turn back now.")
        return self.actions()

    def dropHole(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 6
            Y = 4
            return self.actions({'area': "Yaouw Volcano",
                                 'coordinates': (X, Y)})
        self.text = "You peer down into the vast mouth of the fissure."
        if self.c.hasMercenary("Barrie"):
            self.text += ("\n%s: Bottoms up! Wait, that's not right...belly flop?" % "Barrie")
        self.menu = ["Jump into the hole."]
        return self.actions()

    def danceParty(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        boss = "Tectonic Beast"
        if len(self.c.flags['Lava Spouts Hit']) == 4 and boss not in self.c.flags['Kills'] and "In Battle" not in self.c.flags:
            self.view = "battle"
            self.text = "You are ambushed by an ancient beast!"
            self.c.flags['In Battle'] = True
            return self.actions({'enemy': boss,
                                 'mercenaries': self.c.mercenaries})
        if selectionIndex == 0:
            roll = self.roll()
            if roll < 55:
                hpLoss = random.randint(self.c.maxHp // 6, self.c.maxHp // 4)
                self.text = ("In attempting to disturb the spirits, you slip and burn your hand for %s damage.\nToshe: Shit!" % hpLoss)
                self.c.hp -= hpLoss
            elif roll < 80:
                self.c.flags['Teleporting'] = True
                X = [1, 11, 11, 1]
                Y = [1, 1, 9, 9]
                i = random.randint(0, 3)
                return self.actions({'area': "Yaouw Volcano",
                                     'coordinates': (X[i], Y[i])})
            else:
                self.view = "battle"
                self.text = "You awaken an ancient beast!\nTectonic Beast: Groooooar!!"
                self.c.flags['In Battle'] = True
                return self.actions({'enemy': boss,
                                     'mercenaries': self.c.mercenaries,
                                     'enemy modifiers': {
                                        'NAME': "Disturbed " + boss,
                                        'Stats': {
                                            'maxHp': 2 ** (4 - len(self.c.flags['Lava Spouts Hit'])),
                                            'defence': 2
                                        },
                                        'Multiplicative': True
                                    }})
        elif "In Battle" in self.c.flags:
            del self.c.flags['In Battle']
            if boss in self.c.flags['Kills']:
                self.text = "Toshe: That dude was massive."
                if self.c.hasMercenary("Barrie"):
                    self.text += ("\n%s: What the heck was that?" % "Barrie")
                if self.c.hasMercenary("Qendresa"):
                    self.text += ("\n%s: That magical being was a magma golem...with earthshifting abilities. The volcanic labyrinth appears to have changed." % "Qendresa")
                    if self.c.hasMercenary("Barrie"):
                        self.text += ("\n%s: Nonsense." % "Barrie")
                        self.text += ("\n%s whacks %s's bear butt with her shield." % ("Qendresa", "Barrie"))
            else:
                if self.c.hasMercenary("Qendresa"):
                    self.text = ("%s: Gather your bearings! Everyone!" % "Qendresa")
                    if self.c.hasMercenary("Barrie"):
                        self.text += ("\n%s: I've done that. Yes. I'm all collected." % "Barrie")
                elif self.c.hasMercenary("Barrie"):
                    self.text = ("%s: Mercy!" % "Barrie")
        else:
            self.text = "There appears to be molten liquid squirting from holes in the volcanic crust."
        if boss not in self.c.flags['Kills']:
            self.menu = ["Attempt to disturb the spirits."]
        if "Volcanic Crust" not in self.c.flags:
            self.text += "\nYou feel the presence of a mighty being."
            if self.c.hasMercenary("Barrie") and self.roll() > 50:
                self.text += ("\n%s: Is there some ritual going on here?" % "Barrie")
            elif self.c.hasMercenary("Qendresa"):
                self.text += ("\n%s: It may be dangerous to remain here for too long." % "Qendresa")
            self.c.flags['Volcanic Crust'] = True
        return self.actions()

    def spout1(self, selectionIndex=None):
        id = 1
        return self.lavaSpoutMain(selectionIndex, id)
        
    def spout2(self, selectionIndex=None):
        id = 2
        return self.lavaSpoutMain(selectionIndex, id)
        
    def spout3(self, selectionIndex=None):
        id = 3
        return self.lavaSpoutMain(selectionIndex, id)
        
    def spout4(self, selectionIndex=None):
        id = 4
        return self.lavaSpoutMain(selectionIndex, id)
        
    def lavaSpoutMain(self, selectionIndex, id):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.flags['Lava Spouts Hit'].add(id)
            self.c.flags['In Battle'] = True
            self.view = "battle"
            self.text = ("You disrupt the spirits' worship with a mighty blow!")
            return self.actions({'enemy': "Lava Spirit",
                                 'mercenaries': self.c.mercenaries})
        if "In Battle" in self.c.flags:
            del self.c.flags['In Battle']
            self.text = "Toshe: That hits the spout."
        if "Teleporting" in self.c.flags:
            self.text = "A magical force whisks you away, and you arrive at a lava spout."
            del self.c.flags['Teleporting']
        else:
            self.text = "You come across a lava spout."
        if "Lava Spout" not in self.c.flags:
            if self.c.hasMercenary("Barrie"):
                self.text += ("\n%s: Wow! That there's a fiery mound of flame if I've ever seen one!" % "Barrie")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\n%s: Dastardly spirits are lurking. Exercise caution." % "Qendresa")
            self.c.flags['Lava Spout'] = True
        if id not in self.c.flags['Lava Spouts Hit']:
            self.imageIndex = 5
            self.menu = ["Hit the spout."]
        elif self.c.hasMercenary("Qendresa"):
            self.text += ("\n%s: The elemental spirits have fled from this corner." % "Qendresa")
        else:
            self.text += " It is inactive."
        return self.actions()

    def exit(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 9
            return self.actions({'area': "Dune Hots Peak",
                                 'coordinates': (X, Y)})
        if "Tectonic Beast" in self.c.flags['Kills']:
            self.imageIndex = 8
            self.text = "You approach a magical growth on the volcano wall giving way to the peak."
            self.menu = ["Scale the wall."]
        else:
            self.text = "You come across a calm area with a crack in the wall, allowing you to peer into the sky."
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\n%s: There must be a way to escape to the surface." % "Qendresa")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\n%s: That crack looks like it's gonna give." % "Barrie")
            if len(self.c.flags['Lava Spouts Hit']) == 4:
                self.text += ("\n%s: I feel something vibrating down below!" % "Toshe")
        return self.actions()

    def firefall(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if "Firefall" not in self.c.flags:
            self.text = "You see a pool of lava up ahead, with fresh lava flowing into it."
            if self.c.hasMercenary("Barrie"):
                self.text += ("\n%s: Oh, scary! Not. Let's go, fella." % "Barrie")
            self.c.flags['Firefall'] = True
        return self.actions()

    def fireLake(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = ""
        self.helpText = None
        self.menu = []
        if "Fire Lake" not in self.c.flags:
            self.text = "You navigate around a fiery maw of flame."
            self.c.flags['Fire Lake'] = True
        if self.roll() > 70:
            self.text += ("\n%s: It's hot in here." % "Toshe")
            self.text = self.text.strip()
        if self.text == "":
            self.text = None
        return self.actions()

    def topRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def escapeRoute(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 4
            Y = 25
            return self.actions({'area': "Albanian Desert",
                                 'coordinates': (X, Y)})
        self.text = "You notice a cavern within the volcano wall. It looks like it goes back to Albania."
        if "Oukkar" not in self.c.flags['Kills']:
            self.text += "\nToshe: I don't think it's time to leave yet."
        self.menu = ["Depart to the desert."]
        return self.actions()

    def bottomLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def wall(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def decline(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = ""
        self.helpText = None
        self.menu = []
        if "Lava Jump" not in self.c.flags:
            self.text = "You prepare to jump."
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\n%s makes a religious gesture." % "Qendresa")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\n%s: Geronimo!!" % "Barrie")
            self.text += "\nYou leap into the volcano, landing on a pile of rubble and ash. A large draft cushions your fall."
            self.text += "\nToshe: I got lucky."
            self.c.flags['Lava Jump'] = True
        elif self.c.hasMercenary("Barrie") and self.roll() > 70:
            self.text = ("%s: This place is real warm!" % "Barrie")
        self.text = self.text.strip()
        if self.text == "":
            self.text = None
        return self.actions()

    def pit(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = ["Stare into the pit."]
        if selectionIndex == 0:
            self.text = "You stare deep into the abyss."
            if self.c.hasMercenary("Barrie") and self.roll() > 50:
                self.text += ("\n%s: Whoa bud. You need to chill out." % "Barrie")
            if self.c.hasMercenary("Qendresa") and self.roll() > 50:
                self.text += ("\n%s: Come away from there." % "Qendresa")
        elif "Fire Pit" not in self.c.flags:
            self.text = "You see a deep pit with a red hot lava pool below."
            self.c.flags['Fire Pit'] = True
        return self.actions()

    def fragment(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.text = ("You find a Garnet Fragment!")
            self.c.flags['Volcanic Fragment'] = True
            return self.actions({'item': "Garnet Fragment"})
        if "Volcanic Fragment" not in self.c.flags:
            self.text = ("You see something glowing wedged in the fissure.")
            self.menu = ["Pry out the glowing object."]
        return self.actions()