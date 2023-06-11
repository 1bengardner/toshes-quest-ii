"""
File: TUAHiddenPassage.py
Author: Ben Gardner
Created: July 27, 2015
Revised: June 11, 2023
"""


import random


class HiddenPassage:

    name = "Hidden Passage"
    audio = "Buscagardzia"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.albanianDesert
        ent1 = self.entrance1
        tun1 = self.tunnel1
        bend = self.bend
        gann = self.gan
        splt = self.split
        toys = self.toys
        glow = self.glow
        tun2 = self.tunnel2
        ent2 = self.entrance2
        wrp2 = self.greece
        wrp3 = self.toMerchant
        mrch = self.merchant
        
        
        self.spots = [
            [None, None, None, None, None, None, None],
            [None, wrp1, None, mrch, None, None, None],
            [None, ent1, None, None, None, None, None],
            [None, tun1, None, None, None, None, None],
            [None, bend, gann, splt, toys, None, None],
            [None, None, None, glow, None, None, None],
            [None, None, None, tun2, wrp3, None, None],
            [None, None, None, ent2, None, None, None],
            [None, None, None, wrp2, None, None, None],
            [None, None, None, None, None, None, None]]
        
        e = {'Turbid Adurbid': 5,
             'Dark Asp': 6,
             'Skeleton Arcanist': 6,
             'Ninja': 4}
             
        self.encounters = {wrp1: {},
                           wrp2: {},
                           wrp3: {},
                           ent1: {},
                           tun1: e,
                           bend: e,
                           gann: {},
                           splt: e,
                           toys: {},
                           glow: e,
                           tun2: e,
                           mrch: {},
                           ent2: {}
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

    def albanianDesert(self, selectionIndex=None):
        X = 7
        Y = 35
        return self.actions({'area': "Albanian Desert",
                             'coordinates': (X, Y)})

    def greece(self, selectionIndex=None):
        X = 1
        Y = 7
        return self.actions({'area': "Greece",
                             'coordinates': (X, Y)})

    def toMerchant(self, selectionIndex=None):
        X = 3
        Y = 1
        return self.actions({'area': "Hidden Passage",
                             'coordinates': (X, Y)})

    def entrance1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        merc1 = "Qendresa"
        merc2 = "Barrie"
        if "Hidden Passage" not in self.c.flags:
            self.text = ("Toshe: I need to get to Greece and find out who" +
                         " really has the Key to Macedonia.")
            if self.c.hasMercenary(merc1):
                self.text += ("\n%s: Yes. We must also stop Giacomo." % merc1 +
                              " It is likely that he escaped through this" +
                              " wall.")
            elif self.c.hasMercenary(merc2):
                self.text += ("\n%s: Everything's comin' together now." % merc2)
            self.c.flags['Hidden Passage'] = True
        return self.actions()

    def tunnel1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def bend(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def gan(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and "Gan Passage" not in self.c.flags:
            self.text = ("You shine your flashlight on the man." +
                         "\nGan: Hello." +
                         "\nToshe: Hey! It's you again!" +
                         "\nGan: Yes. I meditate in this cave." +
                         "\nToshe: Well, it's actually a wall, but--" +
                         "\nGan: Come closer." +
                         "\nGan pulls you toward him and covers your mouth." +
                         "\nThings go black for a moment." +
                         "\nGan: You are learning well, pupil.")
            self.c.flags['Gan Passage'] = True
            return self.actions({'skill': "Inner Zen",
                                 'cost': 0})
        elif selectionIndex == 0:
            kills = self.c.flags['Kills']
            animalPowers = self.c.flags['Animal Powers']
            random.seed(self.c.xp)
            suffix = random.choice(["Stab", "Slice", "Smash", "Sever"])
            if self.c.hasItem("Ominous Orb"):
                self.text = ("Gan: Toshe, the orb you wield..." +
                             "\nGan hesitates in awe." +
                             "\nGan: Go right and you can take its power!")
            elif (("Giant Seal2" in kills and
                 "Giant Seal2" not in animalPowers) or
                ("Giant Shark2" in kills and
                 "Giant Shark2" not in animalPowers) or
                ("Giant Salamander2" in kills and
                 "Giant Salamander2" not in animalPowers) or
                ("Giant Scorpion2" in kills and
                 "Giant Scorpion2" not in animalPowers) or
                ("Giant Scarab2" in kills and
                 "Giant Scarab2" not in animalPowers)):
                self.text = ("Gan: Toshe, you are ready now." +
                             " Go right when you are prepared to ascend.")
                self.c.flags['Animal Ascension'] = True
            elif len(self.c.flags['Animal Powers']) == 5 and "Got Sigil" not in self.c.flags:
                self.c.flags['Got Sigil'] = True
                self.text = ("Gan: You are a true hero.")
                self.text += "\nGan gives you the Sigil of Ascension!"
                return self.actions({'item': "Sigil of Ascension"})
            elif len(self.c.flags['Animal Powers']) == 5:
                self.text = ("Gan: True power is a lifelong quest.")
            else:
                self.text = ("Gan: If you seek true power, you must become" +
                             " one with nature and all its beasts, small and" +
                             " large. Giant too. Specifically giant. Speak to" +
                             " me when you have done this.")
        elif "Gan Passage" not in self.c.flags:
            self.imageIndex = 9
            self.text = ("You see someone holding their chest, who" +
                         " looks like they may be in pain.")
            self.menu = ["Talk to the person."]
        elif ("Gan Passage" in self.c.flags and
              "Animal Powers" not in self.c.flags):
            self.text = ("Gan: If you seek true power, you must become" +
                         " one with nature and all its beasts, small and" +
                         " large. Giant too. Specifically giant. Speak to" +
                         " me when you have done this.")
            self.c.flags['Animal Powers'] = dict()
        # Check for any killed rare giants whose power has not been claimed
        elif ("Gan Passage" in self.c.flags):
            self.text = random.choice([
                "Gan: If I can sleep tonight and wake tomorrow, I am" +
                " grateful, for the road ahead may be daunting, but" +
                " it is many times worth the journey.",
                "Gan: What lies beyond is of no concern to me. What" +
                " matters is the present. Make use of today.",
                "Gan: I find the cave to be quite peaceful.",
                "Gan: The things I found useful once before are now" +
                " dated and inadequate. It is a constant struggle to" +
                " survive in this evolving world.",
                "Gan: Are you still here, Toshe?"])
            self.menu = ["Talk to Gan."]
            
        return self.actions()

    def split(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def toys(self, selectionIndex=None):
        def getSpecializationOptions(character):
            options = {
                "Warrior": [
                    "Flame Knight",
                    "Reckless Lancer",
                    "Executioner",
                    "Stalwart Slayer",
                ],
                "Archer": [
                    "Swift Sharpshooter",
                    "Headshot Hunter",
                    "Soul Sniper",
                    "Skulker",
                ],
                "Mage": [
                    "Blaze Mage",
                    "Stone Sage",
                    "Snow Sorcerer",
                    "Mystic",
                ],
                "Ranger": [
                    "Guardian",
                    "Scallywag",
                    "Defender",
                    "Son of Centaur",
                ],
                "Monk": [
                    "Adrenal Avenger",
                    "Sandman",
                    "Astral Assailant",
                    "Hermit",
                ],
                "Druid": [
                    "Spirit Seer",
                    "Weird Warlock",
                    "Critical Caster",
                    "Magic Marksman",
                ],
                "Balanced": [
                    "Squad Leader",
                    "Paladin",
                    "Vengeful Vigilante",
                    "Alchemist",
                ],
            }
            
            str = character.strength
            dex = character.dexterity
            wis = character.wisdom
            if str >= 50 or str > dex and str > wis:
                if dex >= 50:
                    if wis >= 50:
                        return options["Balanced"]
                    return options["Ranger"]
                elif wis >= 50:
                    return options["Monk"]
                return options["Warrior"]
            elif dex >= 50 or dex > str and dex > wis:
                if wis >= 50:
                    return options["Druid"]
                return options["Archer"]
            elif wis >= 50:
                return options["Mage"]
            else:
                return None

        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        if "Ready to Specialize" in self.c.flags and selectionIndex is not None:
            self.c.flags['Newly Specialized'] = True
            del self.c.flags['Ready to Specialize']
            if self.c.specialization is None:
                self.helpText = "You have chosen a specialization! As you defeat enemies, your specialization will rank up and grant you a bonus."
            if self.c.specialization == getSpecializationOptions(self.c)[selectionIndex]:
                self.text = "Toshe: Wow...I feel exactly the same. Maybe a little worse."
            elif "Respec" in self.c.flags:
                del self.c.flags['Respec']
                self.text = "Toshe: I feel like a new man."
            else:
                self.text = "Toshe: I feel strong."
            self.c.specialization = getSpecializationOptions(self.c)[selectionIndex]
            return self.actions({'sound': "Specialize"})
        elif (selectionIndex == 0 and (self.c.hasItem("Ominous Orb") or "Respec" in self.c.flags) or
              "Ready to Specialize" in self.c.flags):
            if not any(filter(lambda stat: stat >= 50, [
                self.c.strength,
                self.c.dexterity,
                self.c.wisdom
            ])):
                self.text = ("A Voice: You are not yet worthy! Return, once" +
                    " you are experienced enough.")
                return self.actions()

            self.text = ""
            if self.c.hasItem("Ominous Orb"):
                self.text += ("The Ominous Orb is released from your grasp.\n")
                self.c.removeItem(self.c.indexOfItem("Ominous Orb"))
            if "Respec" in self.c.flags:
                self.text += ("A Voice: Choose your new destiny, and erase the old!")
            else:
                self.text += ("A Voice: Choose your destiny!")
            self.menu = map(
                lambda specialization: "Become %s %s." % (
                    "an" if specialization[0] in ("A", "E", "I", "O", "U")
                        else "a",
                    specialization),
                getSpecializationOptions(self.c))
            self.c.flags['Ready to Specialize'] = True
        elif selectionIndex == 0:
            self.text = ("A Voice: Your rank will be recalibrated! Are you certain?")
            self.menu = ["Change specializations and recalibrate rank."]
            self.c.flags['Respec'] = True
        elif self.c.hasItem("Ominous Orb"):
            self.text = ("An ominous voice sounds." +
                         "\nAn Ominous Voice: Are you ready?")
            self.menu = ["\"I'm ready.\""]
        elif "Animal Ascension" in self.c.flags:
            suffix = None
            animal = None
            del self.c.flags['Animal Ascension']
            self.c.flags['Ascended'] = True
            kills = self.c.flags['Kills']
            animalPowers = self.c.flags['Animal Powers']
            suffix = random.choice(["Stab", "Slice", "Smash", "Sever"])
            if ( "Giant Seal2" in kills and
                 "Giant Seal2" not in animalPowers):
                self.text = ("You bask in the light as otarine" +
                             " energy flows into you.")
                self.c.flags['Animal Powers']['Giant Seal2'] = 1
                animal = "Seal"
            elif ("Giant Shark2" in kills and
                  "Giant Shark2" not in animalPowers):
                self.text = ("You bask in the light as piscine" +
                             " energy flows into you.")
                self.c.flags['Animal Powers']['Giant Shark2'] = 1
                animal = "Shark"
            elif ("Giant Salamander2" in kills and
                  "Giant Salamander2" not in animalPowers):
                self.text = ("You bask in the light as salamandrine" +
                             " energy flows into you.")
                self.c.flags['Animal Powers']['Giant Salamander2'] = 1
                animal = "Salamander"
            elif ("Giant Scorpion2" in kills and
                  "Giant Scorpion2" not in animalPowers):
                self.text = ("You bask in the light as venomous" +
                             " energy flows into you.")
                self.c.flags['Animal Powers']['Giant Scorpion2'] = 1
                animal = "Scorpion"
            elif ("Giant Scarab2" in kills and
                  "Giant Scarab2" not in animalPowers):
                self.text = ("You bask in the light as insectine" +
                             " energy flows into you.")
                self.c.flags['Animal Powers']['Giant Scarab2'] = 1
                animal = "Scarab"
            return self.actions({'skill': "%s %s" % (animal, suffix),
                                 'cost': 0,
                                 'save': True})
        elif self.c.specialization is not None and self.c.mastery > 1:
            self.text = ("A Voice: Are you not content with the path you have chosen?")
            self.menu = ["Change your specialization."]
            if "Respec" in self.c.flags:
                del self.c.flags['Respec']
        elif self.c.specialization is not None:
            self.text = ("A Voice: Now go and hone your new abilities.")
        else:
            self.text = ("Light shines in faintly through a singular round" +
                         " window in the cavern wall.")
        return self.actions()

    def glow(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tunnel2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if "Passage Merchant" not in self.c.flags:
            self.text = ("You spot a man to the right with a contraption for"+
                         " holding sacks on his back.")
        else:
            self.text = ("You see the merchant in the corner.")
        return self.actions()

    def entrance2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def merchant(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 6
            return self.actions({'area': "Hidden Passage",
                                 'coordinates': (X, Y)})
        npc = "Merchant"
        if "Buyback Items" not in self.c.flags:
            self.c.flags['Buyback Items'] = ["Chasmic Rucksack"] + [None]*8
        self.c.flags['Passage Merchant'] = True
        phrases = [
            "I'm a collector.",
            "Macedonia? Exit the tunnel, then go east and slightly north" +
            " until you reach the highlands.",
            "I'll buy and sell most anything."
        ]
        if self.c.mode == "Ultimate":
            phrases.append("You didn't think I'd give you this rucksack for free, did you?")
        self.text = npc+": " + random.choice(phrases)
        self.menu = ["Return to the tunnel."]
        return self.actions({'items for sale': self.c.flags['Buyback Items'],
                             'buyback': True})
