"""
File: TUABayOfKotor.py
Author: Ben Gardner
Created: May 17, 2013
Revised: September 18, 2022
"""


class BayOfKotor:

    name = "Bay of Kotor"
    audio = "Jig of the Wind Fish"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        hcg1 = self.herceg1
        hcg2 = self.herceg2
        hcg3 = self.herceg3
        hcg4 = self.herceg4
        dock = self.dock
        shr1 = self.shore1
        shr2 = self.shore2
        shr3 = self.shore3
        left = self.leftSea
        rght = self.rightSea
        chu1 = self.churchEntrance
        chu2 = self.church
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, hcg1, hcg2, hcg3, hcg4, None, None, chu2, None],
            [None, left, chu1, dock, shr1, shr2, shr3, rght, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None]]

        encounters = {'Crab': 5,
                      'Blood Carp': 5,
                      'Sea Goblin': 5,
                      'Kotor Crab': 25}
        self.encounters = {dock: {},
                           left: {},
                           chu1: {},
                           chu2: {},
                           hcg1: {},
                           hcg2: {},
                           hcg3: {},
                           hcg4: {},
                           shr1: encounters,
                           shr2: encounters,
                           shr3: encounters,
                           rght: encounters}
                           
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

    def herceg1(self):
        X = 5
        Y = 5
        return self.actions({'area': "Herceg Novi",
                             'coordinates': (X, Y)})

    def herceg2(self):
        X = 6
        Y = 5
        return self.actions({'area': "Herceg Novi",
                             'coordinates': (X, Y)})

    def herceg3(self):
        X = 7
        Y = 5
        return self.actions({'area': "Herceg Novi",
                             'coordinates': (X, Y)})
    
    def herceg4(self):
        X = 8
        Y = 5
        return self.actions({'area': "Herceg Novi",
                             'coordinates': (X, Y)})
    
    def dock(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = ""
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.flags['On Ferry'] = True
            self.c.euros -= 40
            X = 4
            Y = 3
            return self.actions({'area': "Scutari Peninsula",
                                 'coordinates': (X, Y)})
            
        if 'Bay of Kotor' not in self.c.flags:
            self.text = ("Toshe: Yes."+
                         "\nYou exit the ship and breathe in the Montenegrin "+
                         "air."+
                         "\nMatsamot: Here we are, finally. The beautiful "+
                         "Montenegro. Enjoy the weather and the coastal view "+
                         "from Herceg Novi. If you need a place to rest, "+
                         "there is an inn at the center of the city. I'm "+
                         "sure they will be understanding of your financial "+
                         "situation. Look around, smell the roses, enjoy. "+
                         "Just don't get too close to the shore or the fish "+
                         "may bite!"+
                         "\nToshe: I can't sit around for long. I need to get "+
                         "to Macedonia to tell the president what happened!")
            self.c.flags['Bay of Kotor'] = True
        elif "Swimming HP Loss" in self.c.flags:
            self.c.hp += self.c.flags['Swimming HP Loss']
            del self.c.flags['Swimming HP Loss']
            self.c.flags['Bay Surface'] = True
            self.text = ("You gasp for a breath of air.")
        if ("Matsamot Ride Offering" not in self.c.flags and
            "Bay Surface" in self.c.flags):
            if self.text:
                self.text += "\n"
            self.text += (
                     "Matsamot: Hey, did you just swim all the way "+
                     "from the other side? I can give you a ferry "+
                     "ride for just 40 euros. Let me know next time.")
            self.c.flags['Matsamot Ride Offering'] = True
        else:
            self.text = ("You arrive at the dock."+
                         "\nMatsamot: I'll let you know when the next ship's "+
                         "setting sail.")
        if "Matsamot Ride Offering" in self.c.flags:
            self.menu = ["Take a ferry to the peninsula (40 euros)."]
        return self.actions()

    def shore1(self):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Bay of Kotor Shore' not in self.c.flags:
            self.text = ("You approach a rocky shore teeming with small "+
                         "critters.")
            self.c.flags['Bay of Kotor Shore'] = True
        elif ("Barrie Bay Remark" not in self.c.flags and
              self.c.hasMercenary("Barrie")):
            self.c.flags['Barrie Bay Remark'] = True
            self.text = ("Barrie: Down by the bay..." +
                         "\nToshe: ..." +
                         "\nBarrie: Where the watermelons grow..." +
                         "\nToshe: Stop." +
                         "\nBarrie: Back to my home..." +
                         "\nToshe: Stop that." +
                         "\nBarrie: I dare not go..." +
                         "\nToshe: Stop singing!")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nBarrie: For if I do..." +
                              "\nQendresa jabs Barrie with the knob of" +
                              " her hilt." +
                              "\nBarrie: Yow!")
        return self.actions()

    def shore2(self):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Bay of Kotor Shore' not in self.c.flags:
            self.text = ("You approach a rocky shore teeming with small "+
                         "critters.")
            self.c.flags['Bay of Kotor Shore'] = True
        return self.actions()

    def shore3(self):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Bay of Kotor Shore' not in self.c.flags:
            self.text = ("You approach a rocky shore teeming with small "+
                         "critters.")
            self.c.flags['Bay of Kotor Shore'] = True
        return self.actions()

    def churchEntrance(self, selectionIndex=None):
        if selectionIndex == 0:
            X = 9
            Y = 1
            return self.actions({'area': "Bay of Kotor",
                                 'coordinates': (X, Y)})
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You see a weathered church up ahead.")
        self.menu = ["Enter the Church."]
        return self.actions()

    def leftSea(self):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("Man: Hail Montenegro!")
        if "Swimming HP Loss" in self.c.flags:
            self.c.hp += self.c.flags["Swimming HP Loss"]
            del self.c.flags['Swimming HP Loss']
            self.c.flags['Bay Surface'] = True
            self.text = ("You gasp for a breath of air."+
                         "\nMan: It's the loch ness monster!")
        return self.actions()

    def rightSea(self):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Bay of Kotor Shore' not in self.c.flags:
            self.text = ("You approach a rocky shore teeming with small "+
                         "critters.")
            self.c.flags['Bay of Kotor Shore'] = True
        return self.actions()

    def church(self, selectionIndex=None):
        if selectionIndex == 0:
            X = 2
            Y = 2
            return self.actions({'area': "Bay of Kotor",
                                 'coordinates': (X, Y)})
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You hear a deep voice that reverberates throughout "+
                     "the church.\n")
        if "Silvio Slain" in self.c.flags:
            self.text += ("\"I sense great peace in the lands.\"")
        elif "Got Key" in self.c.flags:
            self.text += ("\"Now is the time to save your homeland.\"")
        elif "Fortress Escaped" in self.c.flags:
            self.text += ("\"Craft a gold bar and find a goldsmith who" +
                          " can forge The Key to Macedonia.\"")
        elif "Coliseum Complete" in self.c.flags:
            self.text += ("\"Enter the Fortress of Greece, west of Athens." +
                          " Search for anything suspicious.\"")
        elif "Coliseum" in self.c.flags:
            self.text += ("\"Win the coliseum to gain entry to the Fortress" +
                          " of Greece.\"")
        elif "Not Disguised" in self.c.flags:
            self.text += ("\"Disguise yourself as a Greek to get into the" +
                          " coliseum.\"")
        elif "Athens" in self.c.flags:
            self.text += ("\"Scour Athens for a clue to the whereabouts" +
                          " of The Key to Macedonia.\"")
        elif "Greece" in self.c.flags:
            self.text += ("\"Make your way to Athens, the" +
                          " headquarters of Greece.\"")
        elif "Greek Wall Hole" in self.c.flags:
            self.text += ("\"Navigate through the tunnel under the wall" +
                          " to find an exit to Greece.\"")
        elif "Blueprint" in self.c.flags:
            self.text += ("\"Use the blueprint to guide you to a hole" +
                          " in the Greek wall, south of the castle.\"")
        elif "Silvio Vanquished" in self.c.flags:
            self.text += ("\"Take the scroll from the castle lectern.\"")
        elif "Lesser Dragon" in self.c.flags:
            self.text += ("\"Find Silvio and vanquish him once and for all.\"")
        elif "Silvio Pursuit" in self.c.flags:
            self.text += ("\"Activate a switch on Silvio's castle dungeon" +
                          " floor to advance to his chamber.\"")
        elif "Met Silvio" in self.c.flags:
            self.text += ("\"Catch Silvio in his castle to end his evil" +
                          " pursuits.\"")
        elif "Greek Wall" in self.c.flags:
            self.text += ("\"It would be wise to enter the desert castle" +
                          " if you wish to succeed in your endeavor.\"")
        elif "Rumadan Village" in self.c.flags:
            self.text += ("\"Keep going south past the desert village to" +
                          " Greece.\"")
        elif "Old Ruins Complete" in self.c.flags:
            self.text += ("\"Express your wrath in the only way" +
                          " you know. Trek to Greece, south of Albania," +
                          " and you will soon be faced with another hurdle.\"")
        elif "Old Ruins Encounter" in self.c.flags:
            self.text += ("\"Explore the Old Ruins for a key moment" +
                          " in your quest.\"")
        elif "Took Map" in self.c.flags:
            self.text += ("\"Follow the map, which marks a location" +
                          " east in Eastern Kosovo--two paces left" +
                          " of Pristina.\"")
        elif "Finding President" in self.c.flags:
            self.text += ("\"Take the map in the president's outpost" +
                          " for a clue as to where he might be.\"")
        elif "Unguarded Gate" in self.c.flags:
            self.text += ("\"Proceed through the Presidential Path" +
                          " to get to the president.\"")
        elif "Got Letter" in self.c.flags:
            self.text += ("\"Show the mayor's letter to the" +
                          " guards in Pristina and you will be" +
                          " surprised.\"")
        elif "Tipsy Tuesday" in self.c.flags:
            self.text += ("\"Get a letter from the mayor of Herceg" +
                          " Novi to gain access to the gate in" +
                          " Pristina.\"")
        elif "Secret Lab Lever" in self.c.flags:
            self.text += ("\"Find the President of Macedonia to" +
                          " the east of Kosovo to acquire the key to" +
                          " Macedonia.\"")
        elif "Secret Lab Unlocked" in self.c.flags:
            self.text += ("\"Shut off the power supply to the laboratory "+
                          "and you will find a greater problem.\"")
        elif "All Tomas Writings Found" in self.c.flags:
            self.text += ("\"Travel east through the Black Mountain to "+
                          "Western Kosovo and you will uncover the truth.\"")
        elif "Writings" in self.c.flags and "Ghost of Tomas" in self.c.flags and "Secret Lab" in self.c.flags:
            self.text += ("\"Find all of the lost documents to gain access "+
                          "to a secret hideout.\"")
        elif "Secret Lab" in self.c.flags and "Ghost of Tomas" in self.c.flags:
            self.text += ("\"Use the message on Tomas's tombstone to find "+
                          "out his guard's passcode.\"")
        elif "Ghost of Tomas" in self.c.flags:
            self.text += ("\"Decrypt the writing on Tomas's tombstone to "+
                          "discover what's guarding his prized possessions in "+
                          "Western Kosovo.\"")
        elif "The Watchmaking Facility Complete" in self.c.flags:
            self.text += ("\"Bury the body. You will find a lost "+
                          "relative in the cemetery south of Mojkovac "+
                          "Valley.\"")
        elif "Dragan" in self.c.flags:
            self.text += ("\"There is great evil in the watchmaking "+
                          "facility north of Mojkovac Valley. Go now.\"")
        elif "Mojkovac Summit" in self.c.flags:
            self.text += ("\"You will meet a friend in Mojkovac Valley. "+
                          "The two of you will face a great fiery obstacle "+
                          "in an old building.\"")
        elif "Daniel Quest 2 Complete" in self.c.flags:
            self.text += ("\"You must go northeast through the Black Mountain "+
                          "to proceed. Train in the fields first if you are "+
                          "too weak.\"")
        else:
            self.text = ("You enter the church."+
                         "\nToshe: This place is empty. Maybe I should come back on "+
                         "Sunday.")
        self.menu = ["Leave the Church."]
        return self.actions()
