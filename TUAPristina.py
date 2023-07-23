"""
File: TUAPristina.py
Author: Ben Gardner
Created: April 6, 2014
Revised: July 23, 2023
"""


from random import randint
from random import choice


class Pristina:

    name = "Pristina"
    audio = "Peppermint Mocha"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.easternKosovo1
        wrp2 = self.easternKosovo2
        wrp3 = self.easternKosovo3
        wrp4 = self.easternKosovo4
        wrp5 = self.easternKosovo5
        wlk1 = self.walkway1
        wlk2 = self.walkway2
        wlk3 = self.walkway3
        wlk4 = self.walkway4
        wlk5 = self.walkway5
        wlk6 = self.walkway6
        dead = self.deadEnd
        catt = self.cat
        cor1 = self.corridor1
        cor2 = self.corridor2
        gat1 = self.gate1
        gat2 = self.gate2
        smtE = self.smithEntrance
        tvrE = self.tavernEntrance
        tmpE = self.templeEntrance
        acdE = self.academyEntrance
        traE = self.trafCafeEntrance
        jwlE = self.jewelcrafterEntrance
        hous = self.house
        wlk7 = self.walkway7
        tvrn = self.tavern
        bdrm = self.bedroom
        smth = self.smith
        acad = self.academy
        wzrd = self.wizard
        jwlr = self.jewelcrafter
        merc = self.mercenary
        marc = self.marciano

        self.spots = [
            [None, None, None, None, None, None, None, None, None],
            [None, None, dead, None, None, None, None, hous, None],
            [None, wrp1, wlk2, catt, cor2, gat1, cor1, wlk5, None],
            [None, wrp2, wlk1, smtE, None, tmpE, None, jwlE, None],
            [None, wrp3, wlk7, tvrE, None, acdE, None, traE, None],
            [None, wrp4, wlk3, wlk4, cor2, gat2, cor1, wlk6, None],
            [None, None, None, None, None, wrp5, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, tvrn, None, bdrm, None, smth, None, acad, None],
            [None, None, None, None, None, None, None, None, None],
            [None, wzrd, None, jwlr, None, merc, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, marc, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None]
            ]

        self.encounters = None

    def movementActions(self):
        if "Guards Talk" in self.c.flags:
            del self.c.flags['Guards Talk']

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def marcianoCheck(self):
        if "Marciano3" not in self.c.flags['Kills']:
            X = 1
            Y = 12
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        elif "Marciano Coward 2" not in self.c.flags:
            if self.c.isPolite:
                fLine = "\n%s: What a freaking doody-brain!" % self.c.NAME
            else:
                fLine = "\n%s: Fuckhead!" % self.c.NAME
            self.text = ("Marciano escapes into the forest."+
                         fLine)
            self.c.flags['Marciano Coward 2'] = True
            return self.actions()
        return False

    def easternKosovo1(self, selectionIndex=None):
        X = 9
        Y = 5
        return self.actions({'area': "Eastern Kosovo",
                             'coordinates': (X, Y)})

    def easternKosovo2(self, selectionIndex=None):
        X = 9
        Y = 6
        return self.actions({'area': "Eastern Kosovo",
                             'coordinates': (X, Y)})

    def easternKosovo3(self, selectionIndex=None):
        X = 9
        Y = 7
        return self.actions({'area': "Eastern Kosovo",
                             'coordinates': (X, Y)})

    def easternKosovo4(self, selectionIndex=None):
        X = 9
        Y = 8
        return self.actions({'area': "Eastern Kosovo",
                             'coordinates': (X, Y)})

    def easternKosovo5(self, selectionIndex=None):
        X = 12
        Y = 2
        return self.actions({'area': "Eastern Kosovo",
                             'coordinates': (X, Y)})

    def walkway1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        encounter = self.marcianoCheck()
        if encounter:
            return encounter
        elif "Tipsy Tuesday" not in self.c.flags:
            self.text = ("%s: I'll bet the president is somewhere" % self.c.NAME +
                         " around here.")
        return self.actions()

    def walkway2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        encounter = self.marcianoCheck()
        if encounter:
            return encounter
        return self.actions()

    def walkway3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        encounter = self.marcianoCheck()
        if encounter:
            return encounter
        return self.actions()

    def walkway4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def walkway5(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def walkway6(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def deadEnd(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if "Eastern Treasure" not in self.c.flags:
            self.text = ("You find a Fire Wand!")
            self.c.flags['Eastern Treasure'] = True
            return self.actions({'item': "Fire Wand"})
        return self.actions()

    def cat(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Cat"
        self.text = (npc + ": " + choice(
            [
                "Mrroooouw!",
                "Meow.",
                "Ziziwooo!",
                "Prrrrr."
             ]
            ) + choice(
                [
                    "",
                    "\nThe cat rubs itself against your leg.",
                    "\nThe cat rubs itself against your inner thigh.",
                    "\nThe cat purrs.",
                    "\nThe cat barfs up a hairball.",
                    "\nThe cat poops a little.",
                    "\nThe cat licks you.",
                    "\nThe cat licks its anus."
                 ]
                )
                     )
        if self.c.hasMercenary("Qendresa"):
            self.text += ("\nQendresa: What a pleasant feline!")
        return self.actions()

    def corridor1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You see a statue of a vicious animal.\n%s: What a menacing wolf." % self.c.NAME +
                     " Or is that some sort of hyena?")
        return self.actions()

    def corridor2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You see a statue of a bear.\n%s: Good bear." % self.c.NAME)
        return self.actions()

    def gate1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Guard"
        if ( not self.c.hasItem("Letter from the Mayor") and
             selectionIndex == 0 and "Guards Talk" in self.c.flags):
            self.text = ("%s 2: Well, nobody cares about" % npc +
                         " the Macedonian president except Macedonians!" +
                         "\n%s 1: Which country do you currently" % npc +
                         " reside in?" +
                         "\n%s: I've been traveling across Europe since I" % self.c.NAME +
                         " arrived in Montenegro." +
                         "\n%s 2: Montenegro? Get us a letter from" % npc +
                         " the mayor of Herceg Novi with his signature,"
                         " and we'll allow you through." +
                         "\nThe %ss snicker." % npc)
            del self.c.flags['Guards Talk']
            self.c.flags['Tipsy Tuesday'] = True
            self.menu = ["Approach the guards."]
        elif (not self.c.hasItem("Letter from the Mayor") and
              selectionIndex == 0):
            self.text = ("%s 1: Nobody may enter the gate unless" % npc +
                         " authorized by an official!" +
                         "\n%s: I need to talk to the president!" % self.c.NAME +
                         " it's urgent!" +
                         "\n%s 2: How urgent?" % npc +
                         "\n%s: ...Pretty urgent!" % self.c.NAME +
                         "\n%s 1: Where are you from?" % npc +
                         "\n%s: Macedonia!" % self.c.NAME +
                         "\n%s 2: Well, that's obvious." % npc +
                         "\nThe %ss snicker." % npc +
                         "\n%s: What's that supposed to mean? Huh?" % self.c.NAME)
            self.tempFlag = "Guards Talk"
            self.menu = ["Continue."]
        elif (self.c.hasItem("Letter from the Mayor") or
              "Unguarded Gate" in self.c.flags):
            X = 3
            Y = 8
            return self.actions({'area': "Presidential Path",
                                 'coordinates': (X, Y)})
        elif (not self.c.hasItem("Letter from the Mayor")):
            self.text = "%ss: Halt!" % npc
            self.menu = ["Approach the guards."]
        return self.actions()

    def gate2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def smithEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 5
            Y = 8
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        if "Asian Architecture" not in self.c.flags:
            self.text = ("%s: This building looks Oriental." % self.c.NAME)
            self.c.flags['Asian Architecture'] = True
        self.menu = ["Enter the blacksmith's."]
        return self.actions()

    def tavernEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        self.c.flags['Pristina'] = True
        if "Hot Air Balloon Price" in self.c.flags:
            self.c.euros -= self.c.flags['Hot Air Balloon Price']
            self.text = ("You pay the Hot Air Balloon Mafia "+
                         "%s " % (self.c.flags['Hot Air Balloon Price'])+
                         "euros and they fly you to Pristina.")
            del self.c.flags['Hot Air Balloon Price']
        elif selectionIndex == 0:
            X = 1
            Y = 8
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        if "Asian Architecture" not in self.c.flags:
            self.text = ("%s: This building looks Oriental." % self.c.NAME)
            self.c.flags['Asian Architecture'] = True
        self.menu = ["Enter the inn."]
        return self.actions()

    def templeEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 10
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        self.text = "You see magical dust flowing out from a grand building."
        self.menu = ["Enter the temple."]
        return self.actions()

    def academyEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 7
            Y = 8
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        self.menu = ["Enter the academy."]
        return self.actions()

    def trafCafeEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and self.c.euros >= 0:
            X = 3
            Y = 1
            return self.actions({'area': "Traf Cafe",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0 and self.c.euros < 0:
            self.text = ("%s: I can't go in looking like this." % self.c.NAME)  
        elif "Kicked Out" in self.c.flags:
            del self.c.flags['Kicked Out']
            self.c.flags['Got Kicked Out'] = True
            self.text = ("Better luck next time!")
        elif "Got Kicked Out" in self.c.flags:
            self.text = ("%s: The Traf Cafe...my old nemesis." % self.c.NAME)
        else:
            self.text = ("%s: That's a good-looking cafe." % self.c.NAME)
        self.menu = ["Enter the cafe."]
        return self.actions()

    def jewelcrafterEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 10
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        if "Jewelcrafter Entrance" not in self.c.flags:
            self.text = ("You see a very old straw house.")
            self.c.flags['Jewelcrafter Entrance'] = True
        self.menu = ["Visit the jewelcrafter."]
        return self.actions()

    def house(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 5
            Y = 10
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        if "Barrie" not in self.c.flags:
            self.text = ("You see a tiny house up ahead through the fog.")
            self.menu = ["Skip to the house."]
        else:
            self.text = ("You see Barrie's house.")
            self.menu = ["Skip to Barrie's house."]
        return self.actions()

    def walkway7(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        self.menu = []
        encounter = self.marcianoCheck()
        if encounter:
            return encounter
        self.text = ("You pass through a graveyard.")
        if randint(1, 10) == 10:
            self.view = "battle"
            enemy = choice(["Skeleton Soldier",
                            "Flaming Skeleton",
                            "Skeleton Mage1"])
            return self.actions({'enemy': enemy,
                                 'mercenaries': self.c.mercenaries})
        return self.actions()

    def tavern(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Bartender Zhang"
        if selectionIndex == 0:
            self.text = (npc+": "+choice(
["There are three stunning status ailments. Grounding stuns you for one turn, "+
 "paralysis stuns you with a 50% recovery chance, and freezing has a 25% "+
 "chance of recovery. Watch out for these ailments.",
 "When you are poisoned you will lose 2% of your maximum health when you "+
 "attack. "+
 "Do not worry. You can cleanse yourself of venom immediately after the fight.",
 "Fire skills can burn you. If you are burned, you'll receive damage for "+
 "a quarter of the original "+
 "hit every time you attack. Do not worry. Burns dissipate after battle.",
 "Hmm...my favourite mixed drink is the Black Baby. Mix a half ounce each of" +
 " vodka and blackberry schnapps. Ensure that the vodka is chilled."
 ]
))
        elif selectionIndex == 1:
            if self.c.euros >= 20 or self.c.euros == 0:
                if self.c.euros == 0:
                    self.text = (npc+": It is your right to drink. Ganbei.")
                else:
                    self.c.euros -= 20
                    self.text = (npc+": For you.")
                if npc+" Quest 1" not in self.c.flags:
                    self.text += (" Warrior."+
                                  " This is kind of...immoral."+
                                  " But I need you to do this for me."+
                                  " The guards are too overbearing."+
                                  " They are overrrunning Kosovo and harming"+
                                  " my business."+
                                  " Would you kill 5 guards?")
                    if "Border Guard" in self.c.flags['Kills']:
                        self.c.flags[npc+' Quest 1'] = \
                                           self.c.flags['Kills']['Border Guard']
                    else:
                        self.c.flags[npc+' Quest 1'] = 0
                elif (npc+" Quest 1 Complete" not in self.c.flags and
                      npc+" Quest 1" in self.c.flags and
                      "Border Guard" in self.c.flags['Kills'] and
                      self.c.flags['Kills']['Border Guard']-5 >=
                      self.c.flags[npc+' Quest 1']):
                    self.text += (" Xiexie."+
                                  "\n%s gives you 250 euros." % npc)
                    self.c.euros += 250
                    self.c.flags[npc+' Quest 1 Complete'] = True
                elif (npc+" Quest 1 Complete" in self.c.flags and
                      npc+" Quest 2" not in self.c.flags):
                    self.text += (" Again, I have a favour to ask of you."+
                                  " Could you destroy the black knights?"+
                                  " At least 10?")
                    self.c.flags[npc+' Quest 2'] = 0
                    if "Black Knight" in self.c.flags['Kills']:
                        self.c.flags[npc+' Quest 2'] += \
                                        self.c.flags['Kills']['Black Knight']
                elif (npc+" Quest 2 Complete" not in self.c.flags and
                      npc+" Quest 2" in self.c.flags and
                      "Black Knight" in self.c.flags['Kills'] and
                      self.c.flags['Kills']['Black Knight']-10 >=
                      self.c.flags[npc+' Quest 2']):
                        self.text += (" Xiexie."+
                                      "\n%s gives you 500 euros." % npc)
                        self.c.euros += 500
                        self.c.flags[npc+' Quest 2 Complete'] = True
                elif (npc+" Quest 2 Complete" in self.c.flags and
                      npc+" Quest 3" not in self.c.flags):
                    self.text += (" They are out to get me now."+
                                  " I have been found out."+
                                  " However, I have some extra information."+
                                  " The general is located at one of"+
                                  " corners of Kosovo."+
                                  " If he can be eliminated, his troops"+
                                  " lose direction."+
                                  " He must be eliminated.")
                    if "General Octavius" in self.c.flags['Kills']:
                        self.c.flags[npc+' Quest 3'] = \
                                    self.c.flags['Kills']['General Octavius']
                    else:
                        self.c.flags[npc+' Quest 3'] = 0
                elif (npc+" Quest 3 Complete" not in self.c.flags and
                      npc+" Quest 3" in self.c.flags and
                      "General Octavius" in self.c.flags['Kills'] and
                      self.c.flags['Kills']['General Octavius']-1 >=
                      self.c.flags[npc+' Quest 3']):
                    self.text += (" I feel success returning to my business."+
                                  "\n%s gives you 2000 euros." % npc)
                    self.c.euros += 2000
                    self.c.flags[npc+' Quest 3 Complete'] = True
                elif npc+" Quest 3 Complete" in self.c.flags:
                    self.text += (" Xiexie.")
            else:
                self.text = (npc+": The standard beverage price is 20 euros.")
        elif selectionIndex == 2:
            if (self.c.euros >= 50 or
                'Pristina Room Level' in self.c.flags):
                X = 3
                Y = 8
                return self.actions({'area': "Pristina",
                                     'coordinates': (X, Y)})
            else:
                self.text = (npc+": My rate is 50 euros for a night.")
        elif selectionIndex == 3:
            X = 3
            Y = 4
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        else:
            if "Rested" in self.c.flags:
                self.text = ("You fall asleep."+
                             "\nWhen you wake up, you return to the front "+
                             "to give %s your key." % npc+
                             "\n"+npc+": I hope you feel refreshed.")
                del self.c.flags['Rested']
                del self.c.flags['Pristina Room Level']
            elif ("Pristina Room Level" in self.c.flags and
                  self.c.flags['Pristina Room Level'] < self.c.level):
                self.text = (npc+": My apologies, but I have given"+
                             " away your room in your absence.")
                del self.c.flags['Pristina Room Level']
            elif npc not in self.c.flags:
                self.text = (npc+": Welcome to Zhang."+
                             " How may I be of service?")
                self.c.flags[npc] = True
            else:
                self.text = (npc+": "+
                             choice(["We just received fresh octopus from"+
                                     " the west.",
                                     "The president of Macedonia has an"+
                                     " outpost set up in Pristina.",
                                     "Would you like a drink? No?",
                                     "The gates to Macedonia have been shut"+
                                     " as ordered by the President.",
                                     "How is your journey?"]
                                    )
                             )
                self.text += (" How may I be of service?")

        if "Pristina Room Level" in self.c.flags:
            self.menu = ["Ask for advice.",
                         "Buy a drink (20 euros).",
                         "Return to your room.",
                         "Leave."]
        else:
            self.menu = ["Ask for advice.",
                         "Buy a drink (20 euros).",
                         "Get a room (50 euros).",
                         "Leave."]
        return self.actions()
    
    def bedroom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 21
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Zhang"
        if selectionIndex == 0:
            self.c.flags['Rested'] = True
            self.c.hp = self.c.maxHp
            self.c.ep = self.c.maxEp
            X = 1
            Y = 8
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 1
            Y = 8
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        if 'Pristina Room Level' not in self.c.flags:
            self.c.euros -= 50
            self.text = ("%s takes you to a room. " % npc+
                         "You give him 50 euros and he hands you a key.")
            self.c.flags['Pristina Room Level'] = self.c.level
        else:
            self.text = ("You walk inside your room and lock the door.")
        self.menu = ["Sleep.",
                     "Leave your room."]
        return self.actions()

    def smith(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 22
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Blacksmith"
        if selectionIndex == 0:
            rawMaterial = "Gold Ore"
            product = "Gold Bar"
            price = 500
            if  (self.c.hasItem(rawMaterial, 2) and
                 (self.c.euros >= price or self.c.euros == 0) and
                 not self.c.itemIsEquipped(rawMaterial)):
                self.c.removeItem(self.c.indexOfItem(rawMaterial))
                self.c.removeItem(self.c.indexOfItem(rawMaterial))
                if self.c.euros == 0:
                    self.text = (npc+": Sovereign citizen? On house.\n" +
                                 "The blacksmith smelts your ore and" +
                                 " returns with a golden bar.")
                else:
                    self.c.euros -= price
                    self.text = ("After you pay %s euros," % price +
                                 " the blacksmith smelts your ore and" +
                                 " returns with a golden bar.")
                self.menu = ["Smelt gold ore (500 euros, 2 ores).",
                             "Leave."]
                return self.actions({'item': product,
                                     'items for sale': ["Oak Bow",
                                                        "Pike",
                                                        "Partisan",
                                                        "Obsidian Crusher",
                                                        "Steel Hauberk",
                                                        "Steel Cuirass",
                                                        "Reinforced Buckler",
                                                        "Steel Defender",
                                                        "Force Gauntlets"]})
            elif not self.c.hasItem(rawMaterial, 2):
                self.text = (npc+": More ore. Need more ore. Two ore.")
            elif price > self.c.euros:
                self.text = (npc+": You need %s euros to cook." % price)
        elif selectionIndex == 1:
            X = 3
            Y = 3
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        elif "Pristina Blacksmith" not in self.c.flags:
            self.text = (npc+": Hi.")
            self.c.flags['Pristina Blacksmith'] = True
        elif ("Key Hunting" in self.c.flags and
              "Macedonian Gate Opened" not in self.c.flags):
            self.text = (npc+": Key? I can make gold bar, but not key." +
                         " For that, you need gold specialist.")
        else:
            self.text = npc+": "+choice(
                ["The fire is strong.",
                 "All weapons and armour are of highest quality.",
                 "I can smelt gold ore."])
        self.menu = ["Smelt gold ore (500 euros, 2 ores).",
                     "Leave."]
        return self.actions({'items for sale': ["Oak Bow",
                                                "Pike",
                                                "Partisan",
                                                "Obsidian Crusher",
                                                "Steel Hauberk",
                                                "Steel Cuirass",
                                                "Reinforced Buckler",
                                                "Steel Defender",
                                                "Force Gauntlets"]})

    def academy(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 23
        self.text = None
        self.helpText = None
        npc = "Knight Raoul"
        skill1 = "Steel Twister"
        skill2 = "Bloodrush Crush"
        skill3 = "Diamond Cutter"
        skillPrice1 = 3000 if self.c.mode != "Ultimate" else 0
        skillPrice2 = 3000 if self.c.mode != "Ultimate" else 0
        skillPrice3 = 3000 if self.c.mode != "Ultimate" else 0
        self.menu = ["Learn %s (%s euros)." % (skill1, skillPrice1),
                     "Learn %s (%s euros)." % (skill2, skillPrice2),
                     "Learn %s (%s euros)." % (skill3, skillPrice3),
                     "Leave."]
        if selectionIndex == 0:
            return self.actions({'skill': skill1,
                                 'cost': skillPrice1})
        elif selectionIndex == 1:
            return self.actions({'skill': skill2,
                                 'cost': skillPrice2})
        elif selectionIndex == 2:
            return self.actions({'skill': skill3,
                                 'cost': skillPrice3})
        elif selectionIndex == 3:
            X = 5
            Y = 4
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        elif self.c.mode == "Ultimate":
            self.text = (npc+": Well met, ultimate one. I see there is nothing new that I can tell you. Enjoy our services at no cost.")
        else:
            self.text = (npc+": Well met. I am here to instruct soldiers like yourself."+
                         " Let us train.")
        return self.actions()

    def wizard(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 24
        self.text = None
        self.helpText = None
        npc = "Scrombodogo"
        skill1 = "Duststorm"
        skill2 = "Hailstorm"
        skill3 = "Firestorm"
        skillPrice1 = 5000 if self.c.mode != "Ultimate" else 0
        skillPrice2 = 5000 if self.c.mode != "Ultimate" else 0
        skillPrice3 = 5000 if self.c.mode != "Ultimate" else 0
        items = ["Shooting Star"]+[None]*8
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
            X = 5
            Y = 3
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        elif npc not in self.c.flags:
            if self.c.mode == "Ultimate":
                self.text = (npc+": I am the mage Scrombodogo."+
                             " But it appears you need no introduction. I can tell you are quite the potent being. Allow me to grant you what magic teachings you require, free of charge.")
            else:
                self.text = (npc+": I am the mage Scrombodogo."+
                             " Together, we can wield the power of the elements."+
                             " Come, my friend, and be enlightened.")
            self.c.flags[npc] = True
        else:
            self.text = npc+": "+choice(
                ["Allow me to illuminate the way.",
                 "Have focus and power will come to you.",
                 "I feel a great energy in my presence."])
        return self.actions({'items for sale': items})

    def jewelcrafter(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 25
        self.text = None
        self.helpText = None
        npc = "Jin"
        item1 = "Jade Ward"
        item2 = "Aquamarine Ward"
        item3 = "Garnet Ward"
        price = 1000
        self.menu = ["Craft %s (%s euros, 2 gems)." % (item1, price),
                     "Craft %s (%s euros, 2 gems)." % (item2, price),
                     "Craft %s (%s euros, 2 gems)." % (item3, price),
                     "Leave."]
        if selectionIndex == 0:
            gem = "Jade Crystal"
            item = item1
            aOrAn = "an" if item[0] in ("A", "E", "I", "O", "U") else "a"
            if  (self.c.hasItem(gem, 2) and
                 (self.c.euros >= price or self.c.euros == 0) and
                 not self.c.itemIsEquipped(gem)):
                self.c.removeItem(self.c.indexOfItem(gem))
                self.c.removeItem(self.c.indexOfItem(gem))
                if self.c.euros == 0:
                    self.text = (npc + ": Normally, I do not work for free.\n"
                                 + npc + " nods stoically in acknowledgment and"
                                 + " chips away at your gem, then hands you "
                                 + aOrAn + " " + item + ".")
                else:
                    self.c.euros -= price
                    self.text = ("After you pay %s euros, " % price 
                                 + npc + " chips away at your gem, then hands you "
                                 + aOrAn + " " + item + ".")
                return self.actions({'item': item})
            elif not self.c.hasItem(gem, 2):
                self.text = (npc + ": You are missing a key ingredient.")
            elif price > self.c.euros:
                self.text = (npc+": I need more euros.")
        elif selectionIndex == 1:
            gem = "Aquamarine Shard"
            item = item2
            aOrAn = "an" if item[0] in ("A", "E", "I", "O", "U") else "a"
            if  (self.c.hasItem(gem, 2) and
                 (self.c.euros >= price or self.c.euros == 0) and
                 not self.c.itemIsEquipped(gem)):
                self.c.removeItem(self.c.indexOfItem(gem))
                self.c.removeItem(self.c.indexOfItem(gem))
                if self.c.euros == 0:
                    self.text = (npc + ": Normally, I do not work for free.\n"
                                 + npc + " nods stoically in acknowledgment and"
                                 + " chips away at your gem, then hands you "
                                 + aOrAn + " " + item + ".")
                else:
                    self.c.euros -= price
                    self.text = ("After you pay %s euros, " % price
                                 + npc + " chips away at your gem, then hands you "
                                 + aOrAn + " " + item + ".")
                return self.actions({'item': item})
            elif not self.c.hasItem(gem, 2):
                self.text = (npc + ": You are forgetting something.")
            elif price > self.c.euros:
                self.text = (npc+": I need more euros.")
        elif selectionIndex == 2:
            gem = "Garnet Fragment"
            item = item3
            aOrAn = "an" if item[0] in ("A", "E", "I", "O", "U") else "a"
            if  (self.c.hasItem(gem, 2) and
                 (self.c.euros >= price or self.c.euros == 0) and
                 not self.c.itemIsEquipped(gem)):
                self.c.removeItem(self.c.indexOfItem(gem))
                self.c.removeItem(self.c.indexOfItem(gem))
                if self.c.euros == 0:
                    self.text = (npc + ": Normally, I do not work for free.\n"
                                 + npc + " nods stoically in acknowledgment and"
                                 + " chips away at your gem, then hands you "
                                 + aOrAn + " " + item + ".")
                else:
                    self.c.euros -= price
                    self.text = ("After you pay %s euros, " % price
                                 + npc + " chips away at your gem, then hands you "
                                 + aOrAn + " " + item + ".")
                return self.actions({'item': item})
            elif not self.c.hasItem(gem, 2):
                self.text = (npc + ": I need more materials.")
            elif price > self.c.euros:
                self.text = (npc+": I need more euros.")
        elif selectionIndex == 3:
            X = 7
            Y = 3
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        elif npc not in self.c.flags:
            self.text = (npc+": I am the city jewelcrafter.")
            self.c.flags[npc] = True
        else:
            self.text = npc+": "+choice(
                ["My father came on a ship from China to explore the"+
                 " mountains to the west.",
                 "Gems shimmer; wards glow.",
                 "My cuts are of ultimate precision."])
        return self.actions()

    def mercenary(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 26
        self.text = None
        self.helpText = None
        self.menu = []
        npc1 = "Barrie"
        npc2 = "Qendresa"
        if "In Battle" in self.c.flags:
            del self.c.flags['In Battle']
        if ( "Ferocious Fang" not in self.c.flags['Kills'] and
             "In Battle" not in self.c.flags):
            self.c.flags['In Battle'] = True
            self.imageIndex = 18
            self.view = "battle"
            self.text = ("A tiger charges at you from behind the fog shroud.")
            return self.actions({'enemy': "Ferocious Fang",
                                 'mercenaries': self.c.mercenaries})
        elif "About to Leave" in self.c.flags and selectionIndex == 0:
            del self.c.flags['About to Leave']
            X = 7
            Y = 1
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        elif (selectionIndex == 0 and
              npc1 not in self.c.flags and
              "About to Leave" not in self.c.flags):
            self.text = ("%s: Sure." % self.c.NAME +
                         "\n%s: Yahoo!" % npc1 +
                         "\n%s joins your team." % npc1)
            self.c.flags[npc1] = True
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]
            return self.actions({'mercenary': npc1})
        elif (selectionIndex == 1 and
              npc1 not in self.c.flags):
            self.text = ("%s: No way, dude." % self.c.NAME +
                         "\n%s: What, is it because I'm hairy" % npc1 +
                         " or somethin'?")
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]
        elif ("Ferocious Fang" in self.c.flags['Kills'] and
              npc1 not in self.c.flags and
              "%s Talk" % npc1 not in self.c.flags):
            self.c.flags['New Song'] = "Buddha"
            self.c.flags['Barrie Talk'] = True
            self.text = ("%s: Hey there, chap!" % npc1 +
                         " You seem a little outta breath." +
                         "\n%s: I...I am. There was...a...tiger!" % self.c.NAME +
                         "\n%s: Oh! Hahah! Oh, that little guy?" % npc1 +
                         " That ol' growler? Fang's a good boy; he don't" +
                         " mean no harm. Don't sweat it." +
                         "\n%s is sweating profusely." % self.c.NAME +
                         "\n%s: Anyway, you off on an adventure" % npc1 +
                         " or somethin'?" +
                         "\n%s: Just trying to save Macedonia." % self.c.NAME +
                         "\n%s: I'll tag along. I could use the" % npc1 +
                         " exercise.")
            self.menu = ["\"Sure.\"",
                         "\"No way, dude.\""]
        elif ("Ferocious Fang" in self.c.flags['Kills'] and
              npc1 not in self.c.flags and
              "%s Talk" % npc1 in self.c.flags):
            self.text = ("%s: Hey there, chap!" % npc1 +
                         " Ready to slay foul demons and beasts?")
            self.menu = ["\"Sure.\"",
                         "\"No way, dude.\""]
        elif npc1 in self.c.flags:
            self.text = ("%s: I gotta give Fang some water" % npc1 +
                         " and polish my staff. Gimme a sec." +
                         "\n%s: " % self.c.NAME +
                         choice(["Woah, easy there.",
                                 "Sure thing, dude.",
                                 "I could use some of that polish" +
                                 " for my gear.",
                                 "Why is it so cold in your house?",
                                 "I need to take a piss." if self.c.isHumanoid else "I can wait."])
                         )
            if self.c.hasMercenary(npc2):
                self.text += ("\n%s: " % npc2 +
                              choice(
                                  ["What an interesting hovel.",
                                   "We shall continue in a moment.",
                                   "I shall clean my blade. It has been" +
                                   " bloodied by my foes.",
                                   "We mustn't waste too much time.",
                                   "Albania awaits."])
                              )
            for merc in self.c.mercenaries:
                merc.hp = merc.maxHp
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]        
        return self.actions()

    def marciano(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 27
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.view = "battle"
            return self.actions({'enemy': "Marciano3"})            
        if "Marciano3" not in self.c.flags['Kills']:
            self.c.flags['New Song'] = "Drat"
            self.text = ("Marciano: Last time I did not prepare" +
                         " properly. This time I will finish you." +
                         "\n%s: How do you just pop out of" % self.c.NAME +
                         " nowhere like that?" +
                         "\nMarciano: Silence!" +
                         "\nMarciano advances toward you.")   
            self.menu = ["Brace yourself."]
        elif "Marciano3" in self.c.flags['Kills']:
            X = 2
            Y = 3
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        return self.actions()
