"""
File: TUAAdriaticSea.py
Author: Ben Gardner
Created: February 3, 2013
Revised: October 25, 2022
"""


import random


class AdriaticSea:
    
    name = "Adriatic Sea"
    audio = "8 Bit Blast"

    def __init__(self, character):
        """The temporary flag exists so that if the player saves and exits,
        they will have to resume from the same place instead of allowing the
        flag to jump them to the next state. The flag is consolidated once the
        player changes state (via movement or menu selection)."""
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "swim"
        if "Swimming HP Loss" not in self.c.flags:
            self.c.flags['Swimming HP Loss'] = 0

        wrp1 = self.bayOfKotor1
        wrp2 = self.bayOfKotor2
        wrp3 = self.galijula
        wrp4 = self.abyssWarp
        wrp5 = self.bayOfKotor3
        nrml = self.normal
        vPth = self.verticalPath
        hPth = self.horizontalPath
        hole = self.hole
        left = self.leftWall
        rght = self.rightWall
        frnt = self.frontWall
        gate = self.gate
        back = self.backWall
        lake = self.lakeEntrance
        trsr = self.treasure
        tide = self.floodtideTeacher
        pas2 = self.passage2
        pas3 = self.passage3
        pas4 = self.passage4
        pas5 = self.passage5
        pas6 = self.passage6
        pas7 = self.passage7
        abys = self.abyss
        fall = self.fallSpot
        crak = self.crackTreasure
        if "Melted Ice" not in self.c.flags:    # Have not yet melted ice
            pas1 = None
        else:
            pas1 = self.passage1
        if "Boat" not in self.c.flags:  # First visit to Adriatic Sea
            ckpt = None # Checkpoint
            ckpL = None # Left checkpoint
            ckpR = None
            flsE = frnt # False end
            flsB = back # False beginning
            boat = self.lifeboatEntrance
            self.encounters = None
        else:
            ckpt = nrml
            ckpL = left
            ckpR = rght
            flsE = nrml
            flsB = nrml
            boat = nrml
            e = {'Giant Shark1': 5,
                 'Swordfish': 10,
                 'Mystical Octopus': 2,
                 'Barracuda': 2,
                 'Sponge': 1}
            e2 = {'Hungry Bear': 25,
                  'Galijula Crab': 8,
                  'Sponge': 1}
            e3 = {'Ice Guardian': 10}
            self.encounters = {wrp1: {},
                               wrp2: {},
                               wrp3: {},
                               wrp4: {},
                               wrp5: {},
                               nrml: e,
                               vPth: e,
                               hPth: e,
                               hole: {},
                               left: e,
                               rght: e,
                               frnt: e,
                               gate: e,
                               back: e,
                               lake: {},
                               trsr: e,
                               tide: e,
                               pas1: e2,
                               pas2: e2,
                               pas3: e2,
                               pas4: e2,
                               pas5: e2,
                               pas6: e2,
                               pas7: e2,
                               abys: e3,
                               fall: {},
                               crak: e,}
            
        self.spots = [[None, None, None, None, None, None, None, None, None, None, None, None],
                      [None, wrp1, None, wrp2, None, None, None, wrp5, None, None, None, None],
                      [None, left, None, vPth, frnt, None, None, vPth, frnt, frnt, None, None],
                      [None, left, frnt, vPth, rght, None, None, vPth, nrml, crak, None, None],
                      [None, left, nrml, vPth, rght, None, None, back, nrml, rght, None, None],
                      [None, left, tide, vPth, rght, None, None, None, left, fall, None, None],
                      [None, left, nrml, vPth, trsr, rght, None, None, left, nrml, rght, None],
                      [None, left, hPth, vPth, rght, None, None, None, left, back, fall, None],
                      [None, left, nrml, nrml, rght, None, None, None, pas7, None, None, None],
                      [None, left, nrml, vPth, rght, None, None, None, pas3, None, None, None],
                      [None, left, nrml, vPth, rght, None, None, None, pas1, None, None, None],
                      [None, ckpL, ckpt, ckpt, ckpR, None, None, None, pas3, None, None, None],
                      [None, left, flsE, flsE, rght, None, None, None, pas1, None, None, None],
                      [None, left, hPth, boat, rght, None, wrp4, None, pas4, None, None, None],
                      [None, back, vPth, back, back, None, wrp4, None, wrp3, None, None, None],
                      [None, None, gate, None, None, None, abys, None, pas6, None, None, None],
                      [None, frnt, vPth, frnt, frnt, None, pas7, None, pas5, None, None, None],
                      [None, left, nrml, nrml, hole, pas1, pas2, pas3, pas4, None, None, None],
                      [None, left, flsB, flsB, rght, None, None, None, None, None, None, None],
                      [None, ckpL, ckpt, ckpt, ckpR, None, None, None, None, None, None, None],
                      [None, left, nrml, nrml, rght, None, None, None, None, None, None, None],
                      [None, left, nrml, vPth, rght, None, None, None, None, None, None, None],
                      [None, left, nrml, vPth, rght, None, None, None, None, None, None, None],
                      [None, left, hPth, vPth, back, None, None, None, None, None, None, None],
                      [None, left, vPth, rght, None, None, None, None, None, None, None, None],
                      [None, back, vPth, back, None, None, None, None, None, None, None, None],
                      [None, None, gate, None, None, None, None, None, None, None, None, None],
                      [None, None, gate, None, None, None, None, None, None, None, None, None],
                      [None, None, lake, None, None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None, None, None, None, None]]

        if "Swordfish" in self.c.flags['Kills']:
            self.swordfishKills = self.c.flags['Kills']['Swordfish']
        else:
            self.swordfishKills = 0

    def movementActions(self):
        self.c.hp -= 1
        self.c.flags['Swimming HP Loss'] += 1

    def checkWritings(self):
        if "Writings" not in self.c.flags and "Boat" in self.c.flags:
            self.c.flags['Writings'] = set()
        if ("Ghost of Tomas Conclusion" in self.c.flags and
         "All Tomas Writings Found" not in self.c.flags and
         "Swordfish" in self.c.flags['Kills']):
            if self.c.flags['Kills']['Swordfish'] > self.swordfishKills:
                self.swordfishKills = self.c.flags['Kills']['Swordfish']
                writings = {'Sunken', 'Writings', 'Opaquely', 'Reveal', 'Death',
                            'Fictitious', 'Inside', 'Soulless', 'Hearts'}
                availableWritings = writings.difference(self.c.flags[
                    'Writings'])
                foundWriting = random.choice(list(availableWritings))
                if not self.text:
                    self.text = ""
                else:
                    self.text += "\n"
                self.text += ("You pick up a small piece of parchment from "+
                              "the sea floor that says \"%s.\"" % foundWriting)
                self.c.flags['Writings'].add(foundWriting)
                if self.c.flags['Writings'] == writings:
                    self.text += (
                        "\nToshe: It seems like all the pieces of paper fit "+
                        "together."+
                        "\nYou have a Mysterious Parchment!")
                    self.c.flags['All Tomas Writings Found'] = True
                    return {'item': "Mysterious Parchment"}
                elif 'Secret Lab' not in self.c.flags:
                    self.text += (
                        "\nToshe: I should keep this. I will definitely need "+
                        "this for later.")
                else:
                    self.text +=(
                        "\nToshe: I need this to get into Tomas's headquarters. "+
                        "There must be more around here.")
                    
    def actions(self, newActions=None):
        additionalActions = self.checkWritings()
        if additionalActions:
            newActions = additionalActions
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def bayOfKotor1(self, selectionIndex=None):
        X = 1
        Y = 2
        return self.actions({'area': "Bay of Kotor",
                             'coordinates': (X, Y)})

    def bayOfKotor2(self, selectionIndex=None):
        X = 3
        Y = 2
        return self.actions({'area': "Bay of Kotor",
                             'coordinates': (X, Y)})

    def galijula(self, selectionIndex=None):
        X = 4
        Y = 12
        return self.actions({'area': "Galijula",
                             'coordinates': (X, Y)})

    def abyssWarp(self, selectionIndex=None):
        X = 6
        Y = 15
        return self.actions({'area': "Adriatic Sea",
                             'coordinates': (X, Y)})

    def bayOfKotor3(self, selectionIndex=None):
        X = 7
        Y = 2
        return self.actions({'area': "Bay of Kotor",
                             'coordinates': (X, Y)})

    def normal(self):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Adriatic Sea" not in self.c.flags:
            self.text = ("There are some fish swimming around, " +
                    "whose blurred outlines you can barely make out. " +
                    "Ahead of you are the " +
                    "glimmering silhouettes of limestone, faintly " +
                    "illuminated by what little sunlight pierces through the " +
                    "murky water." +
                    "\nYou should surface before you run out of oxygen." +
                    "\nToshe: Shit! I really need to take a dump!")
            self.helpText = ("Click on the directional arrows on the right to "+
                             "swim through the water.")
            self.c.flags["Adriatic Sea"] = True
        
        return self.actions()

    def verticalPath(self):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if ("Boat Path" not in self.c.flags
            and "Boat" not in self.c.flags):
            self.text = ("A straight path of sand lines the sea floor. You " +
                    "conclude that this body of water must be a vast " +
                    "ocean, or something similarly large, judging by the " +
                    "depth.")
            self.c.flags["Boat Path"] = True
        
        return self.actions()
    
    def horizontalPath(self):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if ("Boat Path 2" not in self.c.flags
            and "Boat" not in self.c.flags):
            self.text = ("You approach a rightward bend in the sand path.")
            self.c.flags["Boat Path 2"] = True
        
        return self.actions()

    def hole(self, selectionIndex=None): # Secret hole spot
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.flags['Melted Ice'] = True
            X = 4
            Y = 17
            return self.actions({'area': "Adriatic Sea",
                                 'coordinates': (X, Y)})
        elif "Melted Ice" not in self.c.flags:
            self.c.flags['Aldreed Entrance Found'] = True
            self.text = ("There is a large passage in the sediment. The opening " +
                    "is frozen, and it looks like it has been that way for " +
                    "years.")
        elif "Melted Ice Aftermath" not in self.c.flags:
            self.imageIndex = 25
            self.text = ("You melt the ice with your touch.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: A secret passage!")
            self.c.flags['Melted Ice Aftermath'] = True
        elif "Galijula Complete" not in self.c.flags:
            self.imageIndex = 25
            self.text = ("There is a magical force deep inside the tunnel.")
        else:
            self.imageIndex = 13
            self.text = ("There is a large hole in the sediment.")

        if ( "Melting Touch" in [skill.NAME for skill in self.c.skills] and
             "Melted Ice" not in self.c.flags):
            self.menu = ["Cast Melting Touch."]
        
        return self.actions()

    def leftWall(self):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        if ("Adriatic Sea Left Wall" not in self.c.flags
            and "Boat" not in self.c.flags):
            self.text = ("There is a wall of sediment to your left.")
            self.c.flags["Adriatic Sea Left Wall"] = True
        if ("Blocked Path" not in self.c.flags
            and "Boat" not in self.c.flags):
            self.helpText = ("This way is blocked. Try a different direction.")
            self.c.flags["Blocked Path"] = True
        
        return self.actions()

    def rightWall(self):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        if ("Adriatic Sea Right Wall" not in self.c.flags
            and "Boat" not in self.c.flags):
            self.text = ("A wall blocks your path on the right.")
            self.c.flags["Adriatic Sea Right Wall"] = True
        if ("Blocked Path" not in self.c.flags
            and "Boat" not in self.c.flags):
            self.helpText = ("This way is blocked. Try a different direction.")
            self.c.flags["Blocked Path"] = True
        
        return self.actions()

    def frontWall(self):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if ("Adriatic Sea Front Wall" not in self.c.flags
            and "Boat" not in self.c.flags):
            self.text = ("You come to a halt in front of a rock wall.")
            self.c.flags["Adriatic Sea Front Wall"] = True
        if ("Blocked Path" not in self.c.flags
            and "Boat" not in self.c.flags):
            self.helpText = ("This way is blocked. Try a different direction.")
            self.c.flags["Blocked Path"] = True
        
        return self.actions()

    def gate(self):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if ("Blocked Path" not in self.c.flags
            and "Boat" not in self.c.flags):
            self.helpText = ("The left and right directions are blocked. You "+
                             "should continue forward.")
            self.c.flags["Blocked Path"] = True
        
        return self.actions()

    def lifeboatEntrance(self, selectionIndex=None):
        if selectionIndex == 0:
            self.view = "battle"
            self.imageIndex = 8
            self.c.hp -= 2
            self.text = ("As you near the boat, you feel something sharp "+
                         "puncture your leg. It's a swordfish!")
            self.helpText = ("Click the sword to attack, "+
                             "the shield to defend, or the boot to try "+
                             "running away.")
            self.c.flags['Boat'] = True
            return self.actions({'enemy': "Wounded Swordfish"})            
            
        elif "Boat" in self.c.flags:
            X = 1
            Y = 1
            return self.actions({'area': "Boat at Sea",
                                 'coordinates': (X, Y)})
        
        self.view = "travel"
        self.imageIndex = 8
        self.text = ("You look towards the sun and see a boat on the " +
                     "water's surface." +
                     "\nToshe: Good, I'm not the only one stranded out here. " +
                     "Maybe they have a toilet up there.")
        self.helpText = ("Choose an option from the right and click select.")
        self.menu = ["Investigate the boat."]
        
        return self.actions()

    def backWall(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if ("Blocked Path" not in self.c.flags
            and "Boat" not in self.c.flags):
            self.helpText = ("Backward is blocked off by rocks. The way out "+
                             "is probably up ahead.")
            self.c.flags["Blocked Path"] = True
        return self.actions()

    def lakeEntrance(self, selectionIndex=None):
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Scutari Peninsula",
                                 'coordinates': (X, Y)})
        self.view = "travel"
        self.imageIndex = 10
        self.text = "You see sunrays piercing through the water from above."
        if self.c.hasMercenary("Barrie"):
            self.text += ("\nBarrie: I love to swim.")
        self.helpText = None
        self.menu = ["Swim up to the surface."]
        return self.actions()

    def treasure(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            random.seed(self.c.seed1)
            self.c.flags['Adriatic Sea Treasure'] = True
            treasure = random.choice(
                ["Mace",
                 "Double Axe",
                 "Long Sword",
                 "Spear",
                 "Heavy Mace",
                 "Macedonian Mace",
                 "Steel Hauberk",
                 "Steel Cuirass",
                 "Glowing Mail",
                 "Misty Axe",
                 "Euros"])
            if treasure == "Euros":
                euros = random.choice([200, 500, 1000])
                self.text = ("You find %s euros!" % euros)
                self.c.euros += euros
                return self.actions({'save': True})
            else:
                aOrAn = "an" if treasure[0] in ("A", "E", "I", "O", "U")\
                        else "a"
                self.text = ("You find %s %s!" % (aOrAn, treasure))
                return self.actions({'item': treasure,
                                     'save': True})
        elif "Adriatic Sea Treasure" not in self.c.flags:
            self.imageIndex = 11
            self.text = ("You see a large chest.")
            self.menu = ["Take the loot (game will be saved)."]
        return self.actions()

    def crackTreasure(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            random.seed(self.c.seed1)
            self.c.flags['Crack Treasure'] = True
            treasure = random.choice(
                ["Macedonian Mace",
                 "Glowing Mail",
                 "Khabir's Shaft",
                 "Glaive",
                 "Morning Star",
                 "Dragon Skin",
                 "Luminescent Barrier",
                 "Misty Axe",
                 "Euros"])
            if treasure == "Euros":
                euros = random.choice([2000, 5000, 10000])
                self.text = ("You find %s euros!" % euros)
                self.c.euros += euros
                return self.actions({'save': True})
            else:
                aOrAn = "an" if treasure[0] in ("A", "E", "I", "O", "U")\
                        else "a"
                self.text = ("You find %s %s!" % (aOrAn, treasure))
                return self.actions({'item': treasure,
                                     'save': True})
        elif "Crack Treasure" not in self.c.flags:
            self.imageIndex = 11
            self.text = ("You see a large chest.")
            self.menu = ["Take the loot (game will be saved)."]
        return self.actions()

    def floodtideTeacher(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Mysterious Blue Wizard"
        if selectionIndex == 0:
            self.text = ("Toshe: I'm not a small sir, but ok."+
                         "\n"+npc+": Doog nikcil regnif!"+
                         "\nThe wizard flicks his wand and teleports away.")
            self.c.flags['Floodtide'] = True
            return self.actions({'skill': "Floodtide",
                                 'cost': 0})
        elif selectionIndex == 1:
            random.seed(self.c.level + 1)
            self.text = ("Toshe: No, weirdo!"+
                         "\n%s: Fine then, dillhead." % npc+
                         "\nThe wizard teleports away, leaving magic dust.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: That fella was no wizard.")
            randomHpBoost = random.randint(-5, 15)
            if randomHpBoost < 0:
                self.text += ("\nYour maximum HP decreased by %s!" % -randomHpBoost)
            elif randomHpBoost > 0:
                self.text += ("\nYour maximum HP increased by %s!" % randomHpBoost)
            self.c.maxHp += randomHpBoost
            self.c.flags['Floodtide'] = True
        elif "Floodtide" not in self.c.flags:
            self.imageIndex = 12
            self.c.flags['New Song'] = "Buddha"
            self.text = (npc+": Greetings, small sir. Care "+
                         "to learn a spell?")
            self.tempFlag = {'New Song': self.audio}
            self.menu = ["\"Yes.\"",
                         "\"No!\""]
        return self.actions()

    def passage1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        if ("Ice Passage" not in self.c.flags):
            self.c.flags['Ice Passage'] = True
            self.text = ("Toshe: It's freezing cold in here.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: I feel fine.")
        return self.actions()

    def passage2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def passage3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def passage4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def passage5(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def passage6(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def passage7(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        self.menu = []
        if "Sliding Down" in self.c.flags:
            self.text = ("You slide down the mountain, plummeting" +
                         " directly into the sea.")
            del self.c.flags['Sliding Down']
        elif ("Tight Passage" not in self.c.flags):
            self.c.flags['Tight Passage'] = True
            self.text = ("Toshe: It's getting tight.")
        return self.actions()

    def abyss(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 21
        self.text = None
        self.helpText = None
        self.menu = []
        if random.randint(0, 7) == 7:
            self.text = "Toshe: How far away is that light coming from?"
        return self.actions()

    def fallSpot(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if "Fell in a Hole" in self.c.flags:
            self.text = ("You take a wrong step, breaking" +
                         " through a crack in the ice." +
                         "\nToshe: Shit!")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Back in the water again!")
            del self.c.flags['Fell in a Hole']
        return self.actions()
