"""
File: TUACemetery.py
Author: Ben Gardner
Created: August 26, 2013
Revised: December 31, 2015
"""


from random import choice


class Cemetery:

    name = "Cemetery"
    audio = "Ned's Theme"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.mojkovacSummit
        skel = self.skeleton
        tam1 = self.tomasTam1
        nml1 = self.normal1
        nml2 = self.normal2
        tam2 = self.tomasTam2
        
        self.spots = [[None, None, None, None, None, None, None],
                      [None, None, wrp1, None, None, tam2, None],
                      [None, nml1, tam1, nml1, None, None, None],
                      [None, nml2, skel, nml2, None, None, None],
                      [None, nml1, nml2, nml1, None, None, None],
                      [None, None, None, None, None, None, None],]

        self.encounters = {wrp1: {},
                           skel: {},
                           tam1: {},
                           nml1: {},
                           nml2: {},
                           tam2: {}}

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

    def mojkovacSummit(self, selectionIndex=None):
        X = 6
        Y = 10
        return self.actions({'area': "Mojkovac Summit",
                             'coordinates': (X, Y)})

    def skeleton(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Skeleton"
        
        if selectionIndex == 0:
            self.c.flags['Skeleton Clan'] = True
            self.c.flags['Pirate Clan Kills'] = 0
            self.c.flags['Gryphon Clan Kills'] = 0
            self.text = (npc+": Cool. Go kick some living ass.")

        elif selectionIndex == 1:
            self.text = (npc+": Well, come back if you change your mind.")

        elif ("Skeleton Clan" in self.c.flags and
              self.c.flags['Pirate Clan Kills'] == 4 and
              self.c.flags['Gryphon Clan Kills'] == 4 and
              "Skeleton Clan Reward" not in self.c.flags):
            self.text = (npc+": Golly! You did it, huh! You did good "+
                         "work. Here. You are now one of us!"+
                         "\nThe "+npc.lower()+" gives you a shield.")
            self.c.flags['Skeleton Clan Reward'] = True
            return self.actions({'item': "Skeleton Shield"})

        elif "Skeleton Clan Reward" in self.c.flags:
            self.text = (npc+": We are immortal!")
                         
        elif "Skeleton Clan" in self.c.flags:
            self.text = (npc+": The pirates are on the ocean peninsula and "+
                         "the gryphons to the east.")
            
        elif (("Pirate Clan" in self.c.flags or
               "Gryphon Clan" in self.c.flags) and
              self.c.flags['Skeleton Clan Kills'] < 3):
            self.view = "battle"
            if ("Pirate Clan" in self.c.flags and
                self.c.flags['Skeleton Clan Kills'] == 0):
                self.text = (npc+": Don't try to fool me, I can smell the "+
                             "pirate on you, and I don't even have a nose!")
            elif ("Gryphon Clan" in self.c.flags and
                  self.c.flags['Skeleton Clan Kills'] == 0):
                self.text = (npc+": I heard you made a deal with the "+
                             "gryphons. Bad choice.")
            self.c.flags['Skeleton Clan Kills'] += 1
            return self.actions({'enemy': choice(["Skeleton Archer Unfleeable",
                                                  "Skeleton Soldier Unfleeable",
                                                  "Skeleton Mage1 Unfleeable",
                                                  "Skeleton Mage2 Unfleeable"]),
                                 'mercenaries': self.c.mercenaries})
        
        elif ("Skeleton Clan Kills" in self.c.flags
              and self.c.flags['Skeleton Clan Kills'] == 3):
            self.view = "battle"
            self.c.flags['Skeleton Clan Kills'] += 1
            return self.actions({'enemy': "Skeleton Commander"})
        
        elif ("Skeleton Clan Kills" in self.c.flags
              and self.c.flags['Skeleton Clan Kills'] >= 4):
            self.text = (npc+": I surrender!")
            
        else:
            self.text = (npc+": Oh, hello. Don't be alarmed, I'm just a "+
                         "lonely skeleton. Alas, not many of my kind remain "+
                         "around here. We are feuding with the pirates and "+
                         "gryphons. I know it sounds ridiculous, but I "+
                         "didn't start the war; they attacked first! "+
                         "The point is, we need an edge to win this. "+
                         "Would you like to help me?")
            self.menu = ["\"Yes.\"",
                         "\"No.\""]
        return self.actions()

    def tomasTam1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 5
            Y = 1
            return self.actions({'area': "Cemetery",
                                 'coordinates': (X, Y)})
        elif ("The Watchmaking Facility Complete" in self.c.flags and
              "Ghost of Tomas" not in self.c.flags):
            self.text = ("You notice a peculiar tombstone standing out from "+
                         "the rest. It has Tomas Tam's name engraved on it."+
                         "\nToshe: I guess this is where they buried him. That's "+
                         "a weird coincidence.")
            self.menu = ["Investigate the tombstone."]
        elif ("Ghost of Tomas" in self.c.flags and
              "Ghost of Tomas Conclusion" not in self.c.flags):
            self.text = ("Tomas Tam: I swear on my soul--I will get my "+
                         "revenge, Toshe!"+
                         "\nTomas Tam disintegrates."+
                         "\nYou notice a cryptic message on his tombstone. "+
                         "It appears to be an anagram written in French.")
            self.c.flags['Ghost of Tomas Conclusion'] = True
        elif "Ghost of Tomas Conclusion" not in self.c.flags:
            self.imageIndex = 2
            self.text = ("Toshe: This place is kind of creepy. What am I "+
                         "doing here?")
        elif ("Qendresa Cemetery Remark" not in self.c.flags and
              self.c.hasMercenary("Qendresa")):
            self.c.flags['Qendresa Cemetery Remark'] = True
            self.text = "Qendresa: Rest the souls of those buried here."
        return self.actions()

    def normal1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def normal2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tomasTam2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.view = "battle"
            self.c.flags['Ghost of Tomas'] = True
            return self.actions({'enemy': "Ghost of Tomas"})
        elif "Ghost of Tomas" in self.c.flags:
            X = 2
            Y = 2
            return self.actions({'area': "Cemetery",
                                 'coordinates': (X, Y)})
        elif "Ghost of Tomas" not in self.c.flags:
            self.text = ("A ghost suddenly shoots up from the tombstone."+
                         "\nToshe: ...Tomas?"+
                         "\nTomas Tam: It is I! Ha ha ha, I have risen from the "+
                         "dead!"+
                         "\nToshe: Why?"+
                         "\nTomas Tam: I seek ultimate revenge! I used the power "+
                         "of your little friend's soul to reincarnate in ghost "+
                         "form!"+
                         "\nToshe: No! Why? Dragan was my only friend!"+
                         "\nTomas Tam: Ha ha ha!"+
                         "\nToshe: You'll pay for this, you bitch!")
            self.menu = ["Attack Tomas Tam."]
        return self.actions()
