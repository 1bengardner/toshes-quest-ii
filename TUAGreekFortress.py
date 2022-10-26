"""
File: TUAGreekFortress.py
Author: Ben Gardner
Created: August 22, 2015
Revised: October 26, 2022
"""


import random


class GreekFortress:

    name = "Greek Fortress"
    audio = "Infiltrator"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"
        
        if ( "Fortress Intervention" in self.c.flags and
             "Fortress Escaped" not in self.c.flags):
            self.audio = "Drastic"

        warp = None
        if "Fortress Intervention" in self.c.flags:
            warp = self.greece
        entr = self.entrance
        hal1 = self.hallway1
        hal2 = self.hallway2
        hal3 = self.hallway3
        crn1 = self.corner1
        mold = self.keyMoldRoom
        crn2 = self.corner2
        chc1 = self.church1
        strs = self.stairs
        chc2 = self.church2
        
        self.spots = [
            [None, None, None, None, None, None, None],
            [None, crn1, hal3, hal2, hal1, entr, None],
            [None, mold, None, None, None, warp, None],
            [None, crn2, chc1, strs, None, None, None],
            [None, None, None, None, None, chc2, None],
            [None, None, None, None, None, None, None]]
        
        e = {'Greek Guardian': 22,
             'Golden Guardian': 3}
             
        self.encounters1 = {warp: {},
                            entr: e,
                            hal1: e,
                            hal2: e,
                            hal3: e,
                            crn1: e,
                            mold: e,
                            crn2: e,
                            chc1: e,
                            strs: e,
                            chc2: e
                            }
        self.encounters2 = None

        self.encounters = self.encounters2
    
    def movementActions(self):
        if ( "Fortress Intervention" in self.c.flags and
             "Fortress Escaped" not in self.c.flags):
            self.encounters = self.encounters1
        else:
            self.encounters = self.encounters2

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def greece(self, selectionIndex=None):
        X = 4
        Y = 18
        return self.actions({'area': "Greece",
                             'coordinates': (X, Y)})

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.text = ("It's an ordinary sheet of parchment.")
        elif "Greek Fortress" not in self.c.flags:
            self.text = ("The gate closes shut and a guard follows" +
                         " behind you." +
                    "\nEscort: Welcome to the great fortress. Let me first" +
                         " take you to the altar where you can get a better" +
                         " view." +
                         "\nToshe: Cool." +
                         "\nYou notice a small sheet of parchment hanging on" +
                         " a ledge." +
                         "\nToshe: Maybe I can find out what the" +
                         " Greeks are hiding in here." +
                         "\nEscort: What?" +
                         "\nToshe: Nothing.")
            self.c.flags['Greek Fortress'] = True
        else:
            self.text = ("You reach the fortress entrance.")
        self.menu = ["Examine the sheet of parchment."]
        return self.actions()

    def hallway1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.text = ("You get a view of various Greek soldiers" +
                         " patrolling the plains.")
        elif "Greek Fortress Hallway" not in self.c.flags:
            self.text = ("Escort: Let us continue left along this corridor.")
            self.c.flags['Greek Fortress Hallway'] = True
        else:
            pass
        self.menu = ["Look out the window."]
        return self.actions()

    def hallway2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.text = ("You see a guard snoozing.")
        elif selectionIndex == 1:
            self.text = ("You look directly into the sun." +
                         "\nToshe: Ouch!")
        else:
            self.text = ("You see two windows.")
        self.menu = ["Look out the left window.",
                     "Look out the right window."]
        return self.actions()

    def hallway3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and "Fortress Intervention" not in self.c.flags:
            self.text = ("Guard: Hey, what are you doing?" +
                         " Follow the escort.")
        elif selectionIndex == 0:
            self.text = ("You see an army of hoplites prepared for battle.")
        else:
            self.text = ("You see a large window.")
        self.menu = ["Look out the window."]
        return self.actions()

    def corner1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.text = ("You search the ledge for anything interesting but" +
                         " find nothing.")
        else:
            self.text = ("You see a large ledge with two latticed windows.")
        self.menu = ["Examine the ledge."]
        return self.actions()

    def keyMoldRoom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        if "Brick Pushed" in self.c.flags:
            self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = ["Search the crevice."]
        if "Brick Pushed" in self.c.flags:
            self.menu.append("Search the doorway.")
            
        if selectionIndex == 0:
            self.text = ("You peek inside the crevice and find nothing of" +
                         " interest.")
            if ( "Brick Pushed" not in self.c.flags and
                 "Altar Rendezvous" not in self.c.flags):
                self.text += ("\nEscort: Hey, what are you looking at?")
                if self.c.hasMercenary("Barrie"):
                    self.text += (
                             "\nBarrie: We're just admiring the" +
                             " fine brickwork, sir." +
                             "\nEscort: Yes, marvelous, isn't it?")
                else:
                    self.text += (" Let us continue.")
        elif selectionIndex == 1 and not self.c.hasItem("Key Mold"):
            self.text = ("You look inside the doorway and find a key mold!")
            self.c.flags['Got Key Mold'] = True
            return self.actions({'item': "Key Mold"})
        elif selectionIndex == 1:
            self.text = ("You look inside to find the doorway empty.")
        elif ("Brick Pushed" in self.c.flags and
              "Got Key Mold" not in self.c.flags):
            self.text = ("You return to the metallurgy room, now" +
                         " with two indentations. One" +
                         " resembles a doorway." +
                         "\nToshe: There must be some clue as to what the" +
                         " Greeks' plans are in this fortress.")
        elif "Key Mold Room" not in self.c.flags:
            self.text = ("You follow the escort to a large open room with" +
                         " an old-looking indentation in the wall." +
                         "\nEscort: This is the room where our finest" +
                         " metallurgists used to" +
                         " tinker until we recently moved the equipment" +
                         " to another location.")
            self.c.flags['Key Mold Room'] = True
        elif "Fortress Intervention" not in self.c.flags:
            self.text = ("You return to the room with the crack in" +
                         " the wall.")
        return self.actions()

    def corner2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
            
        if selectionIndex == 0:
            self.text = ("With the escort's back turned, you silently" +
                         " push the brick into the wall. You hear a click.")
            self.c.flags['Brick Pushed'] = True
        elif "Brick Room" not in self.c.flags:
            self.text = ("The escort pauses for a moment and points upward." +
                         "\nEscort: In ancient times, Stymphalian birds would" +
                         " fly in through the window. The Greek guards would" +
                         " fend them off with ease. Their bronze beaks were" +
                         " no match for our titanium shields." +
                         "\nAs your escort starts toward the next room, you" +
                         " notice a protruding brick in the wall.")
            self.c.flags['Brick Room'] = True
        elif ("Fortress Intervention" not in self.c.flags and
              "Brick Pushed" not in self.c.flags):
            self.text = ("You return to the room with the protruding brick.")

        if "Brick Pushed" not in self.c.flags:
            self.imageIndex = 6
            self.menu = ["Push the brick."]
            
        return self.actions()

    def church1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if "Church Room" not in self.c.flags:
            self.text = ("Escort: Here we stand directly below the altar. Are" +
                         " you religious, sir?" +
                         "\nToshe: Not really. But I do go to church now and" +
                         " then."
                         "\nEscort: That's fine.")
            self.c.flags['Church Room'] = True
        return self.actions()

    def stairs(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 5
            Y = 4
            return self.actions({'area': "Greek Fortress",
                                 'coordinates': (X, Y)})
        if ( "Got Key Mold" not in self.c.flags and
             "Altar Rendezvous" not in self.c.flags):
            self.text = ("Guard: Hermes..." +
                         "\nThe guard whispers something discreetly to the" +
                         " escort." +
                         "\nEscort: Ahem. Excuse me, I require a moment in" +
                         " private." +
                         "\nThe escort and guard go upstairs and" +
                         " lock the door behind them." +
                         "\nToshe: Perfect. This gives me time to snoop" +
                         " around.")
            self.c.flags['Altar Rendezvous'] = True
        elif ("Got Key Mold" in self.c.flags and
              "Fortress Intervention" not in self.c.flags):
            self.text = ""
            if "Altar Rendezvous" in self.c.flags:
                self.text = ("The escort returns from the room upstairs" +
                             " with the guard.\n")
            self.text += ("Escort: Now, sir, come upstairs and join me in" +
                          " this moment of glory!" +
                          "\nThe escort seems peculiarly excited.")
            self.menu = ["Go upstairs."]
        return self.actions()

    def church2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if "Conversion 1" not in self.c.flags:
            self.text = ("Escort: Sir..." +
                         "\nThe escort ushers the guard out from behind the" +
                         " pews." +
                         "\nEscort: ...we've brought you here for a" +
                         " very specific, very important reason. We are" +
                         " looking to appoint a new regiment commander for" +
                         " the Greek army. As a man who is a talented" +
                         " soldier with leadership skills, we thought you" +
                         " to be the best candidate. Loukas here would" +
                         " be your second-in-command." +
                         "\nLoukas: It would be my pleasure to accompany" +
                         " you in battle.")
            self.menu = ["Accept.",
                         "Decline."]
            self.tempFlag = "Conversion 1"

        elif "Conversion 2" not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            if selectionIndex == 0:
                self.text = ("Escort: It's great to have you join us--" +
                             "\nLoukas: Hermes! His cape!" +
                             "\nBoth men stare in shock at your cape." +
                             "\nToshe: What?" +
                             "\nEscort: That...that is..." +
                             "\nLoukas: That is most certainly a Macedonian" +
                             " emblem. I must vanquish this traitor." +
                             "\nToshe: Oh man, not again.")
            elif selectionIndex == 1:
                self.text = ("Toshe: Sorry, I refuse." +
                             "\nLoukas: Then I'll have to kill you." +
                             "\nToshe: What?")
            self.menu = ["Brace yourself."]
            self.tempFlag = "Conversion 2"

        elif "Loukas Encounter" not in self.c.flags:
            self.view = "battle"
            self.c.flags['Loukas Encounter'] = True
            return self.actions({'enemy': "Greek Champion",
                                 'mercenaries': self.c.mercenaries})

        elif "Fortress Intervention" not in self.c.flags:
            self.audio = "Drastic"
            self.text = ("Loukas: Warn the guards..." +
                         "\nThe escort bolts out of the room and" +
                         " sounds his bugle." +
                         "\nToshe: Sheesh, I gotta get outta here quick!")
            self.menu = ["Go downstairs."]
            self.tempFlag = "Fortress Intervention"

        else:
            X = 3
            Y = 3
            return self.actions({'area': "Greek Fortress",
                                 'coordinates': (X, Y)})            
            
        return self.actions()
