"""
File: TUASimelliermPit.py
Author: Ben Gardner
Created: May 28, 2020
Revised: October 26, 2022
"""


from TUAStatics import Static


class SimelliermPit:
    
    name = "Simellierm Pit"
    audio = "Sunken"

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
        strs = self.stairs
        left = self.left
        rght = self.right
        vism = self.vismurg
        visL = self.vismurgLeft
        visR = self.vismurgRight
        nooE = self.nookEntrance
        leav = self.leaves
        nook = self.nook
        fAir = self.freshAir if "Vismurg" in self.c.flags['Kills'] else None
        
        self.spots = [
            [None, None, None, None, None, None, None],
            [None, None, None, fAir, None, None, None],
            [None, nooE, visL, vism, visR, leav, None],
            [None, None, left, strs, rght, None, None],
            [None, nook, None, entr, None, None, None],
            [None, None, None, None, None, None, None]
        ]
        
        self.e = {'Wandering Giant': 64}
        e = self.e
        
        self.encounters = {entr: {},
                           fAir: {},
                           strs: e,
                           left: e,
                           rght: e,
                           visL: e,
                           visR: e,
                           nooE: e,
                           leav: e,
                           vism: e,
                           nook: {}
        }
    
    def movementActions(self):
        if self.e['Wandering Giant'] > 1:
            self.e['Wandering Giant'] /= 2

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions
    
    def freshAir(self, selectionIndex=None):
        if selectionIndex == 0:
            self.c.flags['Climbing Up'] = True
            X = 7
            Y = 7
            return self.actions({'area': "Herceg Bluffs",
                                 'coordinates': (X, Y)})
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = ["Climb up the ivy."]
        if "Vismurg Aftermath" not in self.c.flags:
            self.text = "Vismurg crumbles to dust."
            self.text += "\nToshe: Easy."
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: That was a guardian. Some sorcerer" +
                              " probably tried to control it and gave up.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: Which powerful magus could summon" +
                              " a golem of that size?")
            self.c.flags['Vismurg Aftermath'] = True
        else:
            self.text = "You come to an exit in the form of a tunnel of vines."
        return self.actions()
        
    
    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Simellierm Stairs" not in self.c.flags:
            self.c.flags['Simellierm Stairs'] = True
            self.text = ("You fall through the tunnel, landing in what" +
                         " appears to be an underground knoll, with a" +
                         " descending flight of stairs before you.")
            if self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie: Wow..."
            self.c.hp -= 20
            self.text += "\nToshe: Ow..."
            if self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: How unexpected!"
        return self.actions()
    
    def stairs(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def left(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def right(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def vismurg(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        
        if selectionIndex == 0 and "Simellierm Waterfall" in self.c.flags:
            self.view = "battle"
            return self.actions({'enemy': "Vismurg",
                                 'mercenaries': self.c.mercenaries})
        elif selectionIndex == 0:
            self.c.flags['New Song'] = "Drat"
            self.tempFlag = {'New Song': self.audio}
            self.c.flags['Simellierm Waterfall'] = True
            self.text = ("As you pass underneath the flowing water, you feel" +
                         " the entire cavern quake. Before your eyes adjust" +
                         " to the darkness, you feel something massive begin" +
                         " to rise from below the cave floor." +
                         "\nFinally, you are able to recognize the outline" +
                         " of what seems to be a golem whose size is" +
                         " multiplied tenfold." +
                         "\nVismurg: Graaagh!!")
            self.menu = ["Face Vismurg."]
        elif "Vismurg" not in self.c.flags['Kills']:
            self.text = ("You see a waterfall thinly veiling a passage within" +
                         " the knoll.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: This looks scary.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: I am not afraid. Let us proceed," +
                              " at once.")
            self.menu = ["Step into the waterfall."]
        elif "Vismurg Aftermath" in self.c.flags:
            self.text = ("You see a waterfall hiding a rocky passage within" +
                         " the knoll.")
        else:
            X = 3
            Y = 1
            return self.actions({'area': "Simellierm Pit",
                                 'coordinates': (X, Y)})
            
        return self.actions()
    
    def vismurgLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def vismurgRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def leaves(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        item = "Syvre Leaf"
        if selectionIndex == 0:
            self.c.flags['Simellierm Leaf'] = True
            self.text = "You pick a %s from the plant." % item
            return self.actions({'item': item})
        if "Simellierm Leaf" not in self.c.flags:
            self.text = "You smell the soothing scent of syvre nearby."
            self.menu = ["Pick some syvre."]
        return self.actions()
    
    def nookEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            return Static.ICA_DATA['Ica 7']
        if self.c.dexterity >= 75:
            self.text = ("You notice a disturbance in the leaves that "+
                         "you could pry into.")
            self.menu = ["Enter the disturbance."]
        else:
            self.text = ("You notice a disturbance in the leaves that "+
                         "perhaps you could pry into, were you more "+
                         "dextrous.")
        return self.actions()
    
    def nook(self, selectionIndex=None):
        thisIca = "Ica 7"
        self.c.flags[thisIca] = True
        self.view = "store"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        npc = "Ica"
        skill1 = "Venom Arrow"
        skillPrice1 = 5000
        tunic = "Earth Tunic"
        self.menu = ["Learn %s (%s euros)." % (skill1, skillPrice1),
                     "Leave."]
        if any(ica != thisIca and ica in self.c.flags for ica in Static.ICAS):
            self.menu += ["Travel to the next nook."]
        if selectionIndex == 0:
            return self.actions({'skill': skill1,
                                 'cost': skillPrice1,
                                 'items for sale': [tunic]+[None]*8})
        elif selectionIndex == 1:
            X = 1
            Y = 2
            return self.actions({'area': "Simellierm Pit",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 2:
            self.c.flags['Nooking'] = True
            i = Static.ICAS.index(thisIca)
            nextIca = [ica for ica in Static.ICAS[i+1:] + Static.ICAS[:i]
                       if ica in self.c.flags][0]
            return self.actions(Static.ICA_DATA[nextIca])
        elif "Nooking" in self.c.flags:
            self.text = (npc+" transports you to the next nook.")
            del self.c.flags['Nooking']
        elif npc not in self.c.flags:
            self.text = ("You crawl through the gap and find yourself "+
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
            self.text = ("You crawl through the gap and find yourself "+
                         "in a dark, damp nook."+
                         "\n"+npc+": What do you seek today, archer?")
        return self.actions({'items for sale': [tunic]+[None]*8})
