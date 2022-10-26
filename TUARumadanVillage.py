"""
File: TUARumadanVillage.py
Author: Ben Gardner
Created: January 9, 2014
Revised: October 26, 2022
"""


import random


class RumadanVillage:

    name = "Rumadan Village"
    audio = "Sand in my Eye"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.albanianDesert1
        wrp2 = self.albanianDesert2
        gat1 = self.gate1
        entr = self.entrance
        swdE = self.swordManEntrance
        tvrE = self.tavernEntrance
        sttE = self.statManEntrance
        bttm = self.bottom
        gat2 = self.gate2
        cnr1 = self.corner1
        cnr2 = self.corner2
        cnr3 = self.corner3
        cnr4 = self.corner4
        rInn = self.rumadaInn
        bdrm = self.bedroom
        swdM = self.swordMan
        sttM = self.statMan
        marc = self.marciano
        mshM = self.mushroomMan
        
        self.spots = [
            [None, None, None, None, None],
            [None, None, wrp1, None, None],
            [None, None, gat1, None, None],
            [None, cnr1, entr, cnr2, None],
            [None, swdE, tvrE, sttE, None],
            [None, cnr3, bttm, cnr4, None],
            [None, None, gat2, None, None],
            [None, None, wrp2, None, None],
            [None, None, None, None, None],
            [None, rInn, None, bdrm, None],
            [None, None, None, None, None],
            [None, swdM, None, sttM, None],
            [None, None, None, None, None],
            [None, marc, None, mshM, None],
            [None, None, None, None, None]]
        
        e = {'Rumadan Man': 6,
             'Rumadan Warrior': 2,
             'Rumadan Assassin': 3,
             'Rumadan Ruffian': 3,
             'Rumadan Horseman': 3,
             'Rumadan Disciple': 2,
             'Rumadan Guru': 2}
             
        self.encounters = {wrp1: {},
                           wrp2: {},
                           gat1: {},
                           entr: e,
                           swdE: e,
                           tvrE: e,
                           sttE: e,
                           bttm: e,
                           gat2: {},
                           cnr1: e,
                           cnr2: e,
                           cnr3: e,
                           cnr4: e,
                           rInn: {},
                           bdrm: {},
                           swdM: {},
                           sttM: {},
                           marc: {},
                           mshM: {}
                           }
    
    def movementActions(self):
        self.c.ep -= 3

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def calculateResetPrice(self, resets):
        price = 0
        for i in range(1, resets + 2):
            price += 10 + self.c.level / 4 * (i - 1)
        return price

    def marcianoCheck(self):
        if "Marciano4" not in self.c.flags['Kills']:
            X = 1
            Y = 13
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        elif "Marciano Coward 3" not in self.c.flags:
            self.text = ("Marciano escapes into a sand dune."+
                         "\nToshe: You goddamn coward!")
            self.c.flags['Marciano Coward 3'] = True
            return self.actions()
        return False

    def albanianDesert1(self, selectionIndex=None):
        X = 6
        Y = 17
        return self.actions({'area': "Albanian Desert",
                             'coordinates': (X, Y)})

    def albanianDesert2(self, selectionIndex=None):
        X = 6
        Y = 21
        return self.actions({'area': "Albanian Desert",
                             'coordinates': (X, Y)})

    def gate1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Rumadan Village" not in self.c.flags:
            self.text = ("Toshe: This must be what's left of the" +
                         " Rumadan empire.")
            self.c.flags['Rumadan Village'] = True
        return self.actions()

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Rumadan Hideout",
                                 'coordinates': (X, Y)})
        if "Jazidhu" not in self.c.flags['Kills']:
            self.text = "You see a suspicious looking hole."
        else:
            self.text = "You see a hole leading to a hideout."
        self.menu = ["Enter the hole."]
        return self.actions()

    def swordManEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 11
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        if "Inviting Hut" not in self.c.flags:
            self.text = ("You see an inviting hut up ahead.")
            self.c.flags['Inviting Hut'] = True
            
        if "Sword Man" not in self.c.flags:
            self.menu = ["Enter the hut."]
        else:
            self.menu = ["Enter the Sword Man's hut."]
        return self.actions()

    def tavernEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex != None:
            self.view = "battle"
            self.text = "Man: %s" % random.choice([
                "Leave, now! You do not belong here!",
                "He's a foreigner!",
                "You will be removed from these premises!"])
            return self.actions({'enemy': "Rumadan Man",
                                 'mercenaries': self.c.mercenaries})
        self.text = ("You see a bunch of buildings: a blacksmith," +
                     " an inn, a magician and an animal tamer.")
        self.menu = ["Enter the blacksmith's.",
                     "Enter the inn.",
                     "Enter the magician's.",
                     "Visit the animal tamer."]
        return self.actions()

    def statManEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 11
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        
        if "Mysterious Hut" not in self.c.flags:
            self.text = ("You approach a mysterious hut.")
            self.c.flags['Mysterious Hut'] = True
            
        if "Jazikh" not in self.c.flags:
            self.menu = ["Enter the hut."]
        else:
            self.menu = ["Enter Jazikh's hut."]
        return self.actions()

    def bottom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        encounter = self.marcianoCheck()
        if encounter:
            return encounter
        return self.actions()

    def gate2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def corner1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def corner2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 9
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        if "Bayezin" not in self.c.flags:
            self.text = ("You stand in front of a complex. One dwelling" +
                         " has a sign which reads \"Rumada Inn.\"")
        self.menu = ["Enter the Rumada Inn."]
        return self.actions()

    def corner3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 13
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        if "Greek Wall Hole" not in self.c.flags:
            self.text = ("Wife: My husband is not home right now. Come" +
                         " back another time.")
        else:
            self.text = "Mushroom Man's Wife: The Mushroom Man is inside."
            self.menu = ["Enter the house."]
        return self.actions()

    def corner4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def rumadaInn(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Bayezin"
        price = 200
        if selectionIndex == 0:
            self.text = (npc+": "+random.choice(
["Ok, if you wanna know something, don't forget to drink water." +
 " You can get drained pretty quickly out there in the heat if you don't" +
 " watch your energy reserves.",
 "But I'm not a bartender.",
 "Stay away from the central plaza. All of the Rumadans are out for blood.",
 "If you're a warrior, keep an elemental weapon on you at all times. You" +
 " never know when you'll need it.",
 "You can switch gear in battle by hitting the inventory button. Comes in" +
 " handy sometimes!",
 "You can't poison monsters that don't have blood. I learned that the hard" +
 " way.",
 "Hey dude, you should grab some sort of healing spell if you plan on" +
 " going further.",
 "Greece is just south of here, but there's a big wall around it. Their" +
 " security's gotten really tight lately."
 ]
))
        elif selectionIndex == 1:
            if (self.c.euros >= price or
                'Rumadan Village Room Level' in self.c.flags):
                X = 3
                Y = 9
                return self.actions({'area': "Rumadan Village",
                                     'coordinates': (X, Y)})
            else:
                self.text = (npc+": It's %s euros, dude; sorry." % price)
        elif selectionIndex == 2:
            X = 3
            Y = 3
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        else:
            if "Rested" in self.c.flags:
                self.text = ("You fall asleep."+
                             "\nWhen you wake up, you return to the front "+
                             "to give %s your key." % npc+
                             "\n"+npc+": Hey, man. Feeling better?")
                del self.c.flags['Rested']
                del self.c.flags['Rumadan Village Room Level']
            elif ("Rumadan Village Room Level" in self.c.flags and
                  self.c.flags['Rumadan Village Room Level'] < self.c.level):
                self.text = (npc+": Hey, sorry, you left for a while so"+
                             " I thought you left. Still need a room?")
                del self.c.flags['Rumadan Village Room Level']
            elif npc not in self.c.flags:
                self.text = (npc+": Hey dude. I'm not a...Rumadan." +
                             " I won't try to kill you or anything." +
                             " You can stay here" +
                             " if you want.")
                self.c.flags[npc] = True
            else:
                self.text = (npc+": "+
                             random.choice([
                                 "Sorry, no alcohol here.",
                                 "I inherited this place from my dad." +
                                 " I really don't know what to do with" +
                                 " my life so I just keep this place" +
                                 " running.",
                                 "The new inn is taking away a lot of" +
                                 " tourist business.",
                                 "It's a long walk to Macedonia from here.",
                                 "Hey, man!"
                                 ])
                             )
                self.text += (" What can I do for you?")

        if "Rumadan Village Room Level" in self.c.flags:
            self.menu = ["Ask for advice.",
                         "Return to your room.",
                         "Leave."]
        else:
            self.menu = ["Ask for advice.",
                         "Get a room (%s euros)." % price,
                         "Leave."]
        return self.actions()

    def bedroom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Bayezin"
        price = 200
        if selectionIndex == 0:
            self.c.flags['Rested'] = True
            self.c.hp = self.c.maxHp
            self.c.ep = self.c.maxEp
            X = 1
            Y = 9
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 1
            Y = 9
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        if "Rumadan Village Room Level" not in self.c.flags:
            self.c.euros -= price
            self.text = ("%s takes you to a room. " % npc +
                        "You give him %s euros and he hands you a key." % price)
            self.c.flags['Rumadan Village Room Level'] = self.c.level
        else:
            self.text = ("You walk inside your room and lock the door.")
        self.menu = ["Sleep.",
                     "Leave your room."]
        return self.actions()

    def swordMan(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Sword Man"
        skill = "Aerial Assault"
        skillPrice = 5000
        rawMaterial1 = "Garnet Fragment"
        rawMaterial2 = "Aquamarine Shard"
        product = "Bloodmoon Sword"
        craftPrice = 1000
        self.menu = ["Learn %s (%s euros)." % (skill, skillPrice),
                     "Craft a sword (1000 euros, 1 fragment, 1 shard).",
                     "Leave."]
        if selectionIndex == 0:
            return self.actions({'skill': skill,
                                 'cost': skillPrice})
        elif selectionIndex == 1:
            if  (self.c.hasItem(rawMaterial1) and
                 self.c.hasItem(rawMaterial2) and
                 self.c.euros >= craftPrice and
                 not self.c.itemIsEquipped(rawMaterial1) and
                 not self.c.itemIsEquipped(rawMaterial2)):
                self.c.removeItem(self.c.indexOfItem(rawMaterial1))
                self.c.removeItem(self.c.indexOfItem(rawMaterial2))
                self.c.euros -= craftPrice
                self.text = ("After you pay %s euros " % craftPrice +
                             " and hand over your gems, the %s" % npc +
                             " returns with a %s." % product)
                return self.actions({'item': product})
            elif craftPrice > self.c.euros:
                self.text = (npc+": I'll need %s euros." % craftPrice)
            elif (not self.c.hasItem(rawMaterial1) or
                  not self.c.hasItem(rawMaterial2)):
                self.text = (npc+": I'll need a garnet and an aquamarine" +
                             " to craft this magnificent blade.")
        elif selectionIndex == 2:
            X = 1
            Y = 4
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        elif "Sword Man" not in self.c.flags:
            self.text = (npc+": Hello. Let me introduce myself." +
                         " I am he who is known as \"Sword Man,\"" +
                         " and I am the most masterful swordsman in this" +
                         " land. If you seek to become more skilful," +
                         " I am the one to learn from.")
            self.c.flags['Sword Man'] = True
        else:
            self.text = npc+": "+random.choice(
                ["My sword's power is unrivaled.",
                 "I can teach you to strike like a champion.",
                 "Bring me a garnet fragment and an aquamarine shard." +
                 " Your slashes will cut through diamond with the sword" +
                 " I can craft."])
        return self.actions()

    def statMan(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        npc = "Jazikh"
        offerText = "Reallocate a %s point (%s euros)."
        # Set the price of a stat reset
        if "Stat Reset Count" not in self.c.flags:
            self.c.flags['Stat Reset Count'] = 0
        resets = self.c.flags['Stat Reset Count']
        price = self.calculateResetPrice(resets)
        self.menu = [offerText % ("strength", price),
                     offerText % ("dexterity", price),
                     offerText % ("wisdom", price),
                     "Leave."]
        if selectionIndex == 0 or selectionIndex == 1 or selectionIndex == 2:
            if price > self.c.euros:
                self.text = (npc+": Stingy! I can't help you unless you're" +
                             " willing to pay %s euros." % price)
                return self.actions()
            elif ((selectionIndex == 0 and self.c.strength == 0) or
                  (selectionIndex == 1 and self.c.dexterity == 0) or
                  (selectionIndex == 2 and self.c.wisdom == 0)):
                self.text = ("Toshe: I feel like that would be a terrible idea.")
                return self.actions()
            elif self.c.euros >= price:
                if selectionIndex == 0:
                    self.c.strength -= 1
                elif selectionIndex == 1:
                    self.c.dexterity -= 1
                elif selectionIndex == 2:
                    self.c.wisdom -= 1
                self.c.flags['Stat Reset Count'] += 1
                self.c.euros -= price
                self.c.statPoints += 1
                self.text = ("%s: %s" % (npc,
                                          random.choice(
                                              ["Shazam!",
                                               "Szaffle!",
                                               "Zikhoolo.",
                                               "Pharash.",
                                               "Craianjea.",
                                               "Wizoolio!",
                                               "Fargaran.",
                                               "Jolonbikh.",
                                               "Lynalper.",
                                               "Turbondal.",
                                               "Gharbunkh.",
                                               "Yuzeldi.",
                                               "Hoobgella.",
                                               "Filgrendain!",
                                               "Inpoldikh.",
                                               "Rentendkoj.",
                                               "Bytikhun."])))
                resets = self.c.flags['Stat Reset Count']
                price = self.calculateResetPrice(resets)
                self.menu = [offerText % ("strength", price),
                             offerText % ("dexterity", price),
                             offerText % ("wisdom", price),
                             "Leave."]
                return self.actions()
        elif selectionIndex == 3:
            X = 3
            Y = 4
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        elif npc not in self.c.flags:
            self.text = (npc+": Greetings, foreigner. I am Jazikh, the mystic." +
                         " If you would like to reallocate your talent, I" +
                         " can help you, for a price.")
            self.c.flags[npc] = True
        else:
            self.text = npc+": "+random.choice(
                ["Sorry, I will not give a discount to repeat customers.",
                 "What would you like to regret today?",
                 "My nephew joined a gang in his youth." +
                 " I never see him anymore."])
        return self.actions()

    def marciano(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.view = "battle"
            return self.actions({'enemy': "Marciano4"})            
        if "Marciano4" not in self.c.flags['Kills']:
            self.c.flags['New Song'] = "Drat"
            self.text = ("Marciano: I've been waiting. This feud shall" +
                         " end now. Your blood shall spill upon these sands."
                         "\nToshe: Were you just waiting in this village the" +
                         " whole time?" +
                         "\nMarciano: Silence!" +
                         "\nMarciano advances toward you.")   
            self.menu = ["Brace yourself."]
        elif "Marciano4" in self.c.flags['Kills']:
            X = 2
            Y = 5
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        return self.actions()

    def mushroomMan(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Mushroom Man"
        if selectionIndex == 0:
            X = 1
            Y = 5
            return self.actions({'area': "Rumadan Village",
                                 'coordinates': (X, Y)})
        elif npc not in self.c.flags:
            self.text = (npc + ": I travelled here all the way from the" +
                         " Orient with just my fungi. The Rumadans wanted me" +
                         " to leave, but they let me stay when they realized" +
                         " what a great tourist attraction my mushrooms are.")
            self.c.flags[npc] = True
        else:
            self.text = npc+": " + random.choice(
                ["Look at my Big Mushroom.",
                 "Check out my Thick Mushroom.",
                 "Do you like what you see?"])
        self.menu = ["Leave."]
        return self.actions({'items for sale': ["Nutritious Mushroom",
                                                "Delicious Mushroom",
                                                "Big Mushroom",
                                                "Thick Mushroom",
                                                "Jagged Mushroom",
                                                "Magical Mushroom",
                                                None,
                                                None,
                                                None]})
