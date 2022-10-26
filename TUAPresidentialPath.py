"""
File: TUAPresidentialPath.py
Author: Ben Gardner
Created: June 20, 2015
Revised: October 26, 2022
"""


class PresidentialPath:

    name = "Presidential Path"
    audio = "Jousting Tournament"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.pristina1
        wrp2 = self.pristina2
        wrp3 = self.pristina3
        pth1 = self.path1
        pth2 = self.path2
        pth3 = self.path3
        frk1 = self.fork1
        rks1 = self.rocks1
        rks2 = self.rocks2
        rks3 = self.rocks3
        pth4 = self.path4
        frk2 = self.fork2
        side = self.sidePath
        dead = self.deadEnd
        pth5 = self.path5
        bldg = self.building
        pres = self.presidentsOutpost
        conf = self.confrontation

        self.spots = [
            [None, None, None, None, None, None, None],
            [None, pres, None, bldg, None, conf, None],
            [None, None, None, pth5, None, None, None],
            [None, None, None, frk2, side, dead, None],
            [None, rks3, None, pth4, None, None, None],
            [None, rks2, rks1, frk1, None, None, None],
            [None, None, None, pth3, None, None, None],
            [None, None, None, pth2, None, None, None],
            [None, None, wrp2, pth1, wrp3, None, None],
            [None, None, None, wrp1, None, None, None],
            [None, None, None, None, None, None, None]
            ]

        e = {'Psion Sorcerer': 17,
             'Possessed Guard': 17,
             'Psion Adept': 3}

        if "Old Ruins Complete" not in self.c.flags:
            self.encounters = {wrp1: {},
                               wrp2: {},
                               wrp3: {},
                               pth1: {},
                               pth2: e,
                               pth3: e,
                               frk1: e,
                               rks1: e,
                               rks2: e,
                               rks3: {},
                               pth4: e,
                               frk2: e,
                               side: e,
                               dead: {},
                               pth5: e,
                               bldg: {},
                               pres: {},
                               conf: {}}
        else:
            self.encounters = None

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

    def pristina1(self, selectionIndex=None):
        X = 5
        Y = 3
        return self.actions({'area': "Pristina",
                             'coordinates': (X, Y)})

    def pristina2(self, selectionIndex=None):
        X = 4
        Y = 2
        return self.actions({'area': "Pristina",
                             'coordinates': (X, Y)})

    def pristina3(self, selectionIndex=None):
        X = 6
        Y = 2
        return self.actions({'area': "Pristina",
                             'coordinates': (X, Y)})

    def path1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Unguarded Gate" not in self.c.flags:
            self.text = ("Toshe: Looks like the guards left. I didn't even" +
                         " need this goddamn letter!")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: Stay alert. I can see more" +
                              " up ahead.")
                if self.c.hasMercenary("Barrie"):
                    self.text += ("\nBarrie: I can see them too. They look" +
                                  " a little out of it, though.")
            self.c.flags['Unguarded Gate'] = True
            del self.c.flags['Tipsy Tuesday']
        return self.actions()

    def path2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def path3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def fork1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if ("PP Observation" not in self.c.flags and
            ("Psion Sorcerer" in self.c.flags['Kills'] or
             "Psion Adept" in self.c.flags['Kills'] or
             "Possessed Guard" in self.c.flags['Kills'])):
            self.text = ("Toshe: It seems as though the evil wizards are" +
                         " controlling the guards.")
            self.c.flags['PP Observation'] = True
        return self.actions()

    def rocks1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def rocks2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def rocks3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if ( "PP Ambush" not in self.c.flags and
             "In Battle" not in self.c.flags):
            self.c.flags['PP Ambush'] = True
            self.c.flags['In Battle'] = True
            self.view = "battle"
            self.text = "You are ambushed by a summoned beast!"
            return self.actions({'enemy': "Psionic Beast",
                                 'mercenaries': self.c.mercenaries})
        elif "In Battle" in self.c.flags:
            if self.c.hasMercenary("Barrie"):
                self.text = ("Barrie: What a beast! I'm talking about" +
                             " myself, of course.")
            del self.c.flags['In Battle']
        return self.actions()

    def path4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def fork2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def sidePath(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def deadEnd(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if ( "PP Ambush" not in self.c.flags and
             "In Battle" not in self.c.flags):
            self.c.flags['PP Ambush'] = True
            self.c.flags['In Battle'] = True
            self.view = "battle"
            self.text = "You are ambushed by a summoned beast!"
            return self.actions({'enemy': "Psionic Beast",
                                 'mercenaries': self.c.mercenaries})
        elif "In Battle" in self.c.flags:
            if self.c.hasMercenary("Barrie"):
                self.text = ("Barrie: What a beast! I'm talking about" +
                             " myself, of course.")
            del self.c.flags['In Battle']
        return self.actions()

    def path5(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def building(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Presidential Path",
                                 'coordinates': (X, Y)})
            
        if "PP Guard 1" not in self.c.flags:
            X = 5
            Y = 1
            return self.actions({'area': "Presidential Path",
                                 'coordinates': (X, Y)})

        elif ("PP Guard 2" in self.c.flags and
              "PP Guards Slain" not in self.c.flags):
            self.c.flags['PP Guards Slain'] = True
            self.text = ("Toshe: That wasn't too tough. I should probably" +
                         " inform the president that I'm killing all of" +
                         " his guards.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: That would be a polite thing.")

        self.menu = ["Enter the outpost."]
        
        return self.actions()

    def presidentsOutpost(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = ["Leave."]
        if selectionIndex == 0:
            X = 3
            Y = 1
            return self.actions({'area': "Presidential Path",
                                 'coordinates': (X, Y)})            
        elif selectionIndex == 1:
            self.c.flags['Took Map'] = True
            self.text = "You pick up the map."
            return self.actions({'item': "Presidential Map"})
        if "Finding President" not in self.c.flags:
            self.c.flags['Finding President'] = True
            self.text = ("You enter the outpost and see no sign of the" +
                         " president." +
                         "\nToshe: \"Out to lunch?\" How did he manage to get out" +
                         " so easily?")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: He's probably a really high level!")
            self.text += ("\nYou notice on the floor what appears" +
                          " to be a map." +
                          "\nToshe: Maybe this will lead me to the key!")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Sounds like wishful thinking to me.")
        if "Took Map" not in self.c.flags:
            self.imageIndex = 13
            self.menu.append("Take the map.")
        return self.actions()

    def confrontation(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and "PP Guard 1" not in self.c.flags:
            self.c.flags['PP Guard 1'] = True
            self.view = "battle"
            return self.actions({'enemy': "Possessed Guard",
                                 'mercenaries': self.c.mercenaries})
        
        elif "PP Guard 1" not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            self.text = ("Two guards are blocking the entrance to the" +
                         " president's outpost." +
                         "\nToshe: Hi, I came to see the president." +
                         "\nGuards: You are not ready." +
                         "\nThe guards stare at you as they ready their" +
                         " weapons." +
                         "\nToshe: Guess I'll just have to do this the" +
                         " old fashioned way.")
            self.menu = ["Brace yourself."]
        
        elif "PP Guard 2" not in self.c.flags:
            self.c.flags['PP Guard 2'] = True
            self.view = "battle"
            return self.actions({'enemy': "Possessed Guard",
                                 'mercenaries': self.c.mercenaries})

        elif "PP Guard 2" in self.c.flags:
            X = 3
            Y = 1
            return self.actions({'area': "Presidential Path",
                                 'coordinates': (X, Y)})
        
        return self.actions()
