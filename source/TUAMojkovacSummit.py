"""
File: TUAMojkovacSummit.py
Author: Ben Gardner
Created: June 8, 2013
Revised: August 20, 2023
"""


from TUAStatics import Static


class MojkovacSummit:

    name = "Summit of Presage"
    audio = "Fortune Cookie"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.blackMountain1
        wrp2 = self.watchmakingFacility
        wrp3 = self.blackMountain2
        wrp4 = self.cemetery
        wrp5 = self.valley1
        wrp6 = self.valley2
        nml1 = self.normal1
        nml2 = self.normal2
        nooE = self.nookEntrance
        mtn1 = self.mountain1
        nml3 = self.normal3
        nml4 = self.normal4
        mtn2 = self.mountain2
        fire = self.forestFire
        bldg = self.burningBuilding
        gate = self.cemeteryGate
        nook = self.nook
        marc = self.marciano
        nml5 = self.normal5
        
        self.spots = [
[None, None, None, None, None, None, None, None, None, None, None, None, None],
[None, marc, None, None, None, None, bldg, None, None, None, None, None, None],
[None, None, None, None, None, None, fire, None, None, None, None, None, None],
[None, None, None, nook, None, None, nml3, None, None, None, None, None, None],
[None, None, None, None, None, None, wrp6, None, None, None, None, None, None],
[None, None, None, nooE, None, None, None, None, None, None, None, None, None],
[None, wrp1, mtn1, nml2, nml1, wrp5, None, wrp5, nml2, nml5, mtn2, wrp3, None],
[None, None, None, None, None, None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, wrp5, None, None, None, None, None, None],
[None, None, None, None, None, None, nml4, None, None, None, None, None, None],
[None, None, None, None, None, None, gate, None, None, None, None, None, None],
[None, None, None, None, None, None, wrp4, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None, None, None, None, None, None]]

        e = {'Goblin Ranger': 5,
             'Orc': 5,
             'Mountain Goblin': 5,
             'Giant Seal1': 5}
        e2 = {'Goblin Ranger': 2,
              'Orc': 2,
              'Mountain Goblin': 2,
              'Giant Seal1': 11}

        self.encounters = {wrp1: {},
                           wrp2: {},
                           wrp3: {},
                           wrp4: {},
                           wrp5: {},
                           wrp6: {},
                           nml1: e,
                           nml2: e,
                           nooE: {},
                           mtn1: e,
                           nml3: e2,
                           nml4: e2,
                           mtn2: {},
                           fire: e,
                           bldg: {},
                           gate: {},
                           nook: {},
                           marc: {},
                           nml5: {}}

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

    def blackMountain1(self, selectionIndex=None):
        X = 10
        Y = 1
        return self.actions({'area': "Black Mountain",
                             'coordinates': (X, Y)})

    def watchmakingFacility(self, selectionIndex=None):
        X = 6
        Y = 10
        return self.actions({'area': "Mojkovac Summit",
                             'coordinates': (X, Y)})

    def blackMountain2(self, selectionIndex=None):
        X = 14
        Y = 2
        return self.actions({'area': "Black Mountain",
                             'coordinates': (X, Y)})

    def cemetery(self, selectionIndex=None):
        X = 2
        Y = 2
        return self.actions({'area': "Cemetery",
                             'coordinates': (X, Y)})
    
    def valley1(self, selectionIndex=None):
        X = 3
        Y = 3
        return self.actions({'area': "Mojkovac Valley",
                             'coordinates': (X, Y)})
    
    def valley2(self, selectionIndex=None):
        X = 3
        Y = 2
        return self.actions({'area': "Mojkovac Valley",
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

    def nookEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            return Static.ICA_DATA['Ica 2']
        if self.c.dexterity >= 30 or "All Access Pass" in self.c.flags:
            self.text = ("You notice a small passage between the rocks where "+
                         "you could fit through.")
            self.menu = ["Enter the passage."]
        else:
            self.text = ("You notice a small passage between the rocks where "+
                         "you could probably fit through, were you more "+
                         "dextrous.")
        return self.actions()

    def mountain1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Mojkovac Summit' not in self.c.flags:
            self.text = ("%s: Phew! Finally!" % self.c.NAME)
            self.c.flags['Mojkovac Summit'] = True
        return self.actions()

    def normal3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = "Horse: Niehg!"
        return self.actions()

    def normal4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def mountain2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if ("Dragan" in self.c.flags and
            "The Watchmaking Facility Complete" not in self.c.flags):
            self.c.flags['Dragan Block'] = True
            X = 9
            Y = 6
            return self.actions({'area': "Mojkovac Summit",
                                 'coordinates': (X, Y)})
        elif "The Watchmaking Facility Complete" not in self.c.flags:
            self.c.flags['Walk Block'] = True
            X = 9
            Y = 6
            return self.actions({'area': "Mojkovac Summit",
                                 'coordinates': (X, Y)})
        elif "Marciano2" not in self.c.flags['Kills']:
            X = 1
            Y = 1
            return self.actions({'area': "Mojkovac Summit",
                                 'coordinates': (X, Y)})
        elif "Marciano Coward" not in self.c.flags:
            self.text = ("Marciano escapes into the mountain."+
                         "\n%s: Pussy!" % self.c.NAME)
            self.c.flags['Marciano Coward'] = True
        return self.actions()

    def forestFire(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if "Ghost of Tomas" not in self.c.flags:
            self.text = ("There is a great fire in the distance.")
        elif "Ghost of Tomas" in self.c.flags:
            self.imageIndex = 11
        return self.actions()

    def burningBuilding(self, selectionIndex=None):
        if selectionIndex == 0:
            X = 3
            Y = 4
            return self.actions({'area': "The Watchmaking Facility",
                                 'coordinates': (X, Y)})
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        if "Dragan" not in self.c.flags:
            self.text = ("%s: It looks like a bad idea to go in alone." % self.c.NAME)
        elif "The Watchmaking Facility Complete" not in self.c.flags:
            self.text = ("Dragan: Time is of the essence here.")
            self.menu = ["Enter the watchmaking facility."]
        elif "Ghost of Tomas" in self.c.flags:
            self.imageIndex = 10
            self.text = ("%s: Ashes to ashes..." % self.c.NAME)
        return self.actions()

    def cemeteryGate(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You pass through the cemetery gate.")
        return self.actions()

    def nook(self, selectionIndex=None):
        thisIca = "Ica 2"
        self.c.flags[thisIca] = True
        self.view = "store"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        npc = "Miru"
        skill1 = "Stiff Shot"
        skill2 = "Flaming Arrow"
        skillPrice1 = 300 if self.c.mode != "Ultimate" else 0
        skillPrice2 = 200 if self.c.mode != "Ultimate" else 0
        tunic = "Woodland Tunic"
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
            X = 3
            Y = 5
            return self.actions({'area': "Mojkovac Summit",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 3:
            self.c.flags['Nooking'] = True
            i = Static.ICAS.index(thisIca)
            nextIca = [ica for ica in Static.ICAS[i+1:] + Static.ICAS[:i]
                       if ica in self.c.flags][0]
            return self.actions(Static.ICA_DATA[nextIca])
        elif "Nooking" in self.c.flags:
            self.text = "You are transported into %s's nook." % npc
            del self.c.flags['Nooking']
        elif npc not in self.c.flags:
            self.text = ("You crawl through the rock passage and find yourself "+
                         "in a dark, damp nook. To your surprise, there's "+
                         "someone else inside."+
                         "\nGirl: What are you doing?"+
                         "\n%s: I was going to ask you that." % self.c.NAME+
                         "\n"+npc+": My name is "+npc+". I hide here to "+
                         "practice making tunics so that I don't cause "+
                         "trouble. Do you want to see my shot?")
            self.c.flags[npc] = True
        else:
            self.text = ("You crawl through the rock passage and find yourself "+
                         "in a dark, damp nook."+
                         "\n"+npc+": Hi.")
        return self.actions({'items for sale': [tunic]+[None]*8})

    def marciano(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Marciano"
        if selectionIndex == 0:
            self.view = "battle"
            return self.actions({'enemy': "Marciano2"})
        elif 'Marciano2' in self.c.flags['Kills']:
            X = 10
            Y = 6
            return self.actions({'area': "Mojkovac Summit",
                                 'coordinates': (X, Y)})
        
        self.c.flags['New Song'] = "Drat"
        self.text = (npc+": We meet again. This time, we fight to the death."+
                     "\n%s: Where the hell did you come from?" % self.c.NAME+
                     "\nMarciano: Silence!"+
                     "\nMarciano advances toward you.")
        self.menu = ["Brace yourself."]
        return self.actions()

    def normal5(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Dragan Block" in self.c.flags:
            self.text = ("Dragan: We shall not travel east until we finish "+
                         "our business up north.")
            del self.c.flags['Dragan Block']
        elif "Walk Block" in self.c.flags:
            self.text = ("%s: I feel like I have unfinished business here." % self.c.NAME)
            del self.c.flags['Walk Block']
        return self.actions()
