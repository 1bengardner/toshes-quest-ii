"""
File: TUAScutariPeninsula.py
Author: Ben Gardner
Created: August 30, 2013
Revised: June 4, 2023
"""


from random import choice, randint


class ScutariPeninsula:

    name = "Scutari Peninsula"
    audio = "Frothy Cappuccino"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.blackMountain
        mtnE = self.mountainEntrance
        shr1 = self.shore1
        shr2 = self.shore2
        ship = self.pirateShip
        lke1 = self.lake1
        lke2 = self.lake2
        lke3 = self.lake3
        lke4 = self.lake4
        shr3 = self.shore3
        dstE = self.desertEntrance
        prte = self.pirate
        
        self.spots = [
            [None, None, None, None, None, None, None, None, None],
            [None, lke4, None, prte, None, None, None, None, None],
            [None, lke3, None, None, None, shr1, mtnE, wrp1, None],
            [None, lke2, None, None, ship, shr2, None, None, None],
            [None, lke1, None, None, None, shr3, dstE, None, None],
            [None, None, None, None, None, None, None, None, None]]

        e1 = {'Goblin Thug': 6,
              'Earth Mage': 6,
              'Romadan Ruffian': 4,
              'Golem': 4}
        e2 = {'Giant Water Spider': 10,
              'Toxic Jellyfish': 10}

        self.encounters = {wrp1: {},
                           mtnE: e1,
                           shr1: e1,
                           shr2: e1,
                           ship: {},
                           lke1: e2,
                           lke2: e2,
                           lke3: e2,
                           lke4: e2,
                           shr3: e1,
                           dstE: {},
                           prte: {}}

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

    def blackMountain(self, selectionIndex=None):
        X = 10
        Y = 28
        return self.actions({'area': "Black Mountain",
                             'coordinates': (X, Y)})

    def mountainEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if ('Scutari Peninsula' not in self.c.flags and
            'Desert Passage' not in self.c.flags):
            self.text = ("You feel the cool breeze of the ocean.")
            self.c.flags['Scutari Peninsula'] = True
        return self.actions()

    def shore1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def shore2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def pirateShip(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = ""
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 1
            return self.actions({'area': "Scutari Peninsula",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 1
            Y = 4
            return self.actions({'area': "Scutari Peninsula",
                                 'coordinates': (X, Y)})
        if "On Ferry" in self.c.flags:
            del self.c.flags['On Ferry']
            self.text = ("You pay the fare and Matsamot takes you across "+
                         "the ocean.\n")
        self.text += ("You see a wrecked ship with some people inside and "+
                     "a shallow lake with calm water.")
        if ( "Qendresa Peninsula Remark" not in self.c.flags and
             self.c.hasMercenary("Qendresa")):
            self.c.flags['Qendresa Peninsula Remark'] = True
            self.text += ("\nQendresa: You can get to Albania directly" +
                          " from here.")
        self.menu = ["Enter the ship.",
                     "Swim in the lake."]
        return self.actions()

    def lake1(self, selectionIndex=None):
        self.movementVerb = "swim"
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 4
            Y = 3
            return self.actions({'area': "Scutari Peninsula",
                                 'coordinates': (X, Y)})
        self.menu = ["Get out."]
        return self.actions()

    def lake2(self, selectionIndex=None):
        self.movementVerb = "swim"
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def lake3(self, selectionIndex=None):
        self.movementVerb = "swim"
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def lake4(self, selectionIndex=None):
        self.movementVerb = "swim"
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 2
            Y = 28
            return self.actions({'area': "Adriatic Sea",
                                 'coordinates': (X, Y)})
            
        self.text = ("The way forward is blocked.")
        if "Swimming HP Loss" in self.c.flags:
            self.c.hp += self.c.flags["Swimming HP Loss"]
            del self.c.flags['Swimming HP Loss']
            self.text = ("You gasp for a breath of air.")
        self.menu = ["Dive down."]
        return self.actions()

    def shore3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        if "Peninsula Treasure" not in self.c.flags:
            self.c.flags['Peninsula Treasure'] = True
            self.text = "You find a Studded Buckler!"
            return self.actions({'item': "Studded Buckler"})
        return self.actions()

    def desertEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.flags['Crawling'] = True
            X = 1
            Y = 4
            return self.actions({'area': "Albanian Desert",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            self.c.removeItem(self.c.indexOfItem("Olympian Ointment"))
            self.text = "You apply a jar of Olympian Ointment to the hole."
            if randint(1, 10) == 1:
                self.text += "\nA Diggler crawls out!"
                self.view = "battle"
                return self.actions({'enemy': "Diggler",
                                     'mercenaries': self.c.mercenaries,})
            elif randint(1, 4) == 1:
                self.text += "\nA Garnet Fragment rolls out!"
                return self.actions({'item': "Garnet Fragment"})
            elif randint(1, 3) == 1:
                self.text += "\nA Jade Crystal rolls out!"
                return self.actions({'item': "Jade Crystal"})
            elif randint(1, 2) == 1:
                self.text += "\nAn Aquamarine Shard rolls out!"
                return self.actions({'item': "Aquamarine Shard"})
            else:
                self.text += "\nA piece of gold ore rolls out!"
                return self.actions({'item': "Gold Ore"})
                
        if "Sliding" in self.c.flags and "Desert Passage" not in self.c.flags:
            self.c.flags['Desert Passage'] = True
            del self.c.flags['Sliding']
            self.text = ("You slide down the sandy slope, crashing"+
                         " into a pile of rocks at the bottom."+
                         "\nToshe: Yow!")
            self.c.hp -= 20
            self.menu = ["Crawl through the hole."]
        elif "Sliding" in self.c.flags:
            del self.c.flags['Sliding']
            self.text = ("You slide down the sandy slope.")
            self.menu = ["Crawl through the hole."]
        elif "Desert Passage" in self.c.flags:
            self.text = ("There is a small hole in the mountain.")
            self.menu = ["Crawl through the hole."]
            if self.c.hasItem("Olympian Ointment"):
                self.menu.append("Apply Olympian Ointment.")
        else:
            self.imageIndex = 9
            self.text = ("There is a small hole in the mountain, but it is "+
                         "packed in with boulders.")
        return self.actions()

    def pirate(self, selectionIndex=None):
        self.movementVerb = "walk"
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = ["Leave."]
        npc = "Pirate"

        if (selectionIndex == 0):
            X = 4
            Y = 3
            return self.actions({'area': "Scutari Peninsula",
                                 'coordinates': (X, Y)})
             
        elif selectionIndex == 1:
            self.c.flags['Pirate Clan'] = True
            self.c.flags['Skeleton Clan Kills'] = 0
            self.c.flags['Gryphon Clan Kills'] = 0
            self.text = (npc+": Yo-ho-ho and a bottle of rum. "+
                         "Blow the man down!")

        elif selectionIndex == 2:
            self.text = (npc+": Lilylivered landlubber, ye.")

        elif ("Pirate Clan" in self.c.flags and
              self.c.flags['Skeleton Clan Kills'] == 4 and
              self.c.flags['Gryphon Clan Kills'] == 4 and
              "Pirate Clan Reward" not in self.c.flags):
            self.text = (npc+": Avast, me hearties! A fine job ye've done. "+
                         "Take this token, and may the sea be with ye."+
                         "\nThe "+npc.lower()+" gives you a shield.")
            self.c.flags['Pirate Clan Reward'] = True
            return self.actions({'item': "Swash Buckler"})

        elif "Pirate Clan Reward" in self.c.flags:
            self.text = (npc+": These waters be ours!")
                         
        elif "Pirate Clan" in self.c.flags:
            self.text = (npc+": There be a "+
                         "graveyard through the mountain and a nest across "+
                         "the desert.")
            
        elif (("Skeleton Clan" in self.c.flags or
               "Gryphon Clan" in self.c.flags) and
              self.c.flags['Pirate Clan Kills'] < 3):
            self.view = "battle"
            if ("Skeleton Clan" in self.c.flags and
                self.c.flags['Pirate Clan Kills'] == 0):
                self.text = (npc+": Yarr! Walk the plank and join the rest "+
                             "of yer skeleton crew!")
            elif ("Gryphon Clan" in self.c.flags and
                self.c.flags['Pirate Clan Kills'] == 0):
                self.text = (npc+": Avast, scallywag! The only good bird is "+
                             "a dead one, except for me parrot.")
            self.c.flags['Pirate Clan Kills'] += 1
            return self.actions({'enemy': choice(["Buccaneer",
                                                  "Swashbuckler",
                                                  "Pirate Kid",
                                                  "Pirate Lady"]),
                                 'mercenaries': self.c.mercenaries})
        
        elif ("Pirate Clan Kills" in self.c.flags
              and self.c.flags['Pirate Clan Kills'] == 3):
            self.view = "battle"
            self.c.flags['Pirate Clan Kills'] += 1
            return self.actions({'enemy': "Pirate Captain"})
        
        elif ("Pirate Clan Kills" in self.c.flags
              and self.c.flags['Pirate Clan Kills'] >= 4):
            self.text = (npc+": Shiver me timbers!")
            
        else:
            self.text = (npc+": Ahoy, we be marooned! Our ship's "+
                         "waterlogged, our crew's "+
                         "been kidnapped and our booty's been pillaged! "+
                         "I know who these villains be. It's the skeletons "+
                         "and the gryphons. Be ye in a plunderin' mood, matey?")
            self.menu += ["\"Yes.\"",
                          "\"No.\""]
        return self.actions()
