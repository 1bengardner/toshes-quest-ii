"""
File: TUAOldRuins.py
Author: Ben Gardner
Created: June 28, 2015
Revised: October 26, 2022
"""


import random


class OldRuins:

    name = "Old Ruins"
    audio = "Galaxy X"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        sprl = self.spiral
        entr = self.entrance
        fork = self.fork
        ltRt = self.leftRight
        tunl = self.tunnel
        strs = self.stairs
        pole = self.pole
        notL = self.notLeft
        strt = self.straight
        dnLt = self.downLeft
        tres = self.treasure
        crnr = self.corner
        pres = self.president

        self.spots = [
            [None, None, None, None, None, None],
            [None, crnr, ltRt, dnLt, None, None],
            [None, pole, None, strt, None, None],
            [None, strs, None, notL, tres, None],
            [None, tunl, ltRt, fork, None, None],
            [None, None, None, entr, None, None],
            [None, sprl, None, None, None, None],
            [None, None, None, pres, None, None],
            [None, None, None, None, None, None]
            ]

        e = {'Ancient Goblin': 26,
             'Florc': 8,
             'Shorc': 10,
             'Hermit': 6}

        self.encounters = {sprl: {},
                           entr: e,
                           fork: e,
                           ltRt: e,
                           tunl: e,
                           strs: e,
                           pole: e,
                           notL: e,
                           strt: e,
                           dnLt: e,
                           tres: e,
                           crnr: {},
                           pres: {}}

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

    def spiral(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Old Ruins Encounter" not in self.c.flags:
            self.c.flags['Old Ruins Encounter'] = True
            self.text = ("Hermit: Get out!")
            self.view = "battle"
            return self.actions({'enemy': "Hermit",
                                 'mercenaries': self.c.mercenaries})
        elif ((random.randint(1, 2) == 1 and
               (selectionIndex == 0 or selectionIndex == 1)) or
              ("Secret Lab Lever" not in self.c.flags and
               selectionIndex == 1)):
            self.text = ("You noisily lose your footing on a step, alerting a" +
                         " nearby hungry beast.")
            self.view = "battle"
            return self.actions({'enemy': "Florc",
                                 'mercenaries': self.c.mercenaries})
        elif selectionIndex == 0:
            X = 8
            Y = 6
            return self.actions({'area': "Eastern Kosovo",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 3
            Y = 5
            return self.actions({'area': "Old Ruins",
                                 'coordinates': (X, Y)})
        self.text = ("You traverse the long spiral staircase.")
        if "Old Ruins" not in self.c.flags:
            self.text += ("\nThe hermit escapes downstairs." +
                          "\nToshe: What idiot practices magic down here?" +
                          " Anyway, this flashlight Gan gave me is actually" +
                          " surprisingly useful.")
            self.c.flags['Old Ruins'] = True
        elif "Secret Lab Lever" not in self.c.flags:
            self.text += ("\nToshe: Looks like I won't be able to" +
                          " get downstairs. There's too many fucking monsters!")
        self.menu = ["Go upstairs.",
                     "Go downstairs."]
        return self.actions()
    
    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 6
            return self.actions({'area': "Old Ruins",
                                 'coordinates': (X, Y)})   
        self.text = ("You reach the entrance of the lowest floor of the ruins.")
        if ( "Barrie Old Ruins Remark" not in self.c.flags and
             self.c.hasMercenary("Barrie")):
            self.c.flags['Barrie Old Ruins Remark'] = True
            self.text += ("\nBarrie: What a dark, gloomy place. Perfect" +
                          " for sleeping.")
        self.menu = ["Ascend up to ground level."]
        return self.actions()

    def fork(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def leftRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if random.randint(1, 6) == 6:
            self.imageIndex = 14
            damage = random.randint(25, 75)
            self.text = ("You step onto a bundle of spikes, injuring" +
                         " yourself for %s damage." % damage)
            self.c.hp -= damage
        elif self.c.hasMercenary("Qendresa"):
            self.text = ("Qendresa: I can sense danger nearby. Watch" +
                         " your step.")
        return self.actions()

    def tunnel(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def stairs(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def pole(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def straight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def treasure(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        if ( selectionIndex == 0 and
             "Enraged Hermit" not in self.c.flags['Kills'] and
             "In Battle" not in self.c.flags):
            self.c.flags['In Battle'] = True
            self.view = "battle"
            self.text = "Hermit: Your time is up."
            return self.actions({'enemy': "Enraged Hermit",
                                 'mercenaries': self.c.mercenaries})
        if ( selectionIndex == 0 and
             "Enraged Hermit" in self.c.flags['Kills']):
            self.c.flags['Old Ruins Treasure'] = True
            self.text = ("You find Moon Armour!")
            return self.actions({'item': "Moon Armour"})
            
        if "In Battle" in self.c.flags:
            del self.c.flags['In Battle']

        if "Old Ruins Treasure" not in self.c.flags:
            self.imageIndex = 10
            self.text = ("You stumble upon a curious chest.")
            self.menu = ["Take the loot."]
            
        return self.actions()

    def corner(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        if "President 1" not in self.c.flags:
            X = 3
            Y = 7
            return self.actions({'area': "Old Ruins",
                                 'coordinates': (X, Y)})
        elif "Old Ruins Complete" not in self.c.flags:
            self.text = ("The second guard escapes in a cloud of smoke." +
                         " When the smoke clears, he is nowhere to be found." +
                         "\nToshe: ...I can't believe it. I just murdered" +
                         " the president, and I still don't have the key!" +
                         " I will destroy every Greek warrior until I" +
                         " find that key!")
            self.tempFlag = "Old Ruins Complete"
        return self.actions()

    def president(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        if "President 1" not in self.c.flags:
            self.menu = ["Tell the president about the possessed guards.",
                         "Ask the president why he is here.",
                         "Ask the president for the key."]
            if selectionIndex == 0:
                self.text = ("Toshe: Your guards are being possessed by" +
                             " evil wizards!" +
                             "\nThe president pauses for a moment." +
                             "\nPresident: There is nothing I can do about" +
                             " that, unfortunately.")
            elif selectionIndex == 1:
                self.text = ("Toshe: Why are you in these old ruins?" +
                             "\nThe president pauses for a moment." +
                             "\nPresident: I came here to escape the dark" +
                             " forces at work around my outpost.")
            elif selectionIndex == 2:
                self.text = ("Toshe: Honourable sir, I need to"
                             " return to Macedonia to stop the monsters" +
                             " from generating and rid my country of" +
                             " evil forces. Please, can you let me in?" +
                             "\nThe president pauses for a moment." +
                             "\nPresident: I have the key." +
                             "\nToshe: Can I have it?" +
                             "\nPresident: ...I cannot give it to you," +
                             " unfortunately. This is the only key left." +
                             "\nToshe: Then come with me! We have to save" +
                             " our homeland!" +
                             "\nPresident: I cannot return to Macedonia." +
                             "\nToshe: Why are you being so difficult!?" +
                             "\nPresident: It's safer here.")
                self.menu = ["Ask once more."]
                self.tempFlag = "President 1"
            else:
                self.text = ("You see two guards and an important-looking man" +
                             " standing together in the corner of the ruins." +
                             "\nToshe: Hi. Are you...are you the president?" +
                             "\nPresident: The President of Macedonia? Yes," +
                             " yes, I am." +
                             "\nThe president is slow and controlled in his" +
                             " words.")

        elif "President 2" not in self.c.flags:
            self.text = ("Toshe: Please, just give the key to me." +
                         "\nPresident: I'm sorry. I--I can't." +
                         "\nToshe: Then you leave me with no other" +
                         " choice. Guards, stand down!")
            self.menu = ["Attack the president."]
            self.tempFlag = "President 2"

        elif "President Encounter" not in self.c.flags:
            self.view = "battle"
            self.c.flags['President Encounter'] = True
            return self.actions({'enemy': "President of Macedonia",
                                 'mercenaries': self.c.mercenaries})

        elif "President 3" not in self.c.flags:
            self.text = ("Toshe: This is just a dumb badge! Give me the key!" +
                         "\nPresident: I...I don't have the key." +
                         "\nToshe: What?!" +
                         "\nPresident: I did it to protect my family." +
                         "\nToshe: What are you talking about?" +
                         "\nPresident: The guards...they're going to" +
                         " kill my family! I have failed...Macedonia" +
                         " is going to fall into ruins...the guards" +
                         " have the key--" +
                         "\nGuard: Enough!" +
                         "\nThe guard plunges his blade into the back of" +
                         " the president.")
            self.menu = ["Continue."]
            self.tempFlag = "President 3"

        elif "President 4" not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            self.text = ("President: Ugh..." +
                         "\nGuard: Haha! Now don't you feel silly?" +
                         " You've completed your task. Now I must" +
                         " dispose of you." +
                         "\nAs the guards turn around, you recognize" +
                         " their familiar uniforms to be the same as" +
                         " the two guards in Pristina. You also notice Greek" +
                         " emblems on their armour." +
                         "\nToshe: You'll pay for this!")
            self.menu = ["Brace yourself."]
            self.tempFlag = "President 4"

        elif "Greek Guard Encounter" not in self.c.flags:
            self.view = "battle"
            self.c.flags['Greek Guard Encounter'] = True
            return self.actions({'enemy': "Greek Guard",
                                 'mercenaries': self.c.mercenaries})

        else:
            X = 1
            Y = 1
            return self.actions({'area': "Old Ruins",
                                 'coordinates': (X, Y)})            
        
        return self.actions()
