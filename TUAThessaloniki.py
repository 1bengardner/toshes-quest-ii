"""
File: TUAThessaloniki.py
Author: Ben Gardner
Created: August 3, 2015
Revised: October 23, 2022
"""


import random


class Thessaloniki:

    name = "Thessalonian Highlands"
    audio = "Impulse Response"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"
        
        wrp1 = self.greece1
        wrp2 = self.greece2
        nml1 = self.normal1
        nml2 = self.normal2
        nml3 = self.normal3
        notL = self.notLeft
        notU = self.notUp
        notR = self.notRight
        notD = self.notDown
        upLt = self.upLeft
        dnLt = self.downLeft
        dnRt = self.downRight
        pth1 = self.path1
        pth2 = self.path2
        gate = self.gate
        dist = self.palaceInTheDistance
        lair = self.lairOfTheMagi
        
        
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, lair, None, None, None, None, None, None, None, None, dist, None, None],
            [None, None, None, None, None, None, gate, None, None, None, notL, dnLt, None],
            [None, None, None, None, None, None, pth2, None, dnRt, notU, nml2, upLt, None],
            [None, None, None, None, None, dnRt, pth1, notU, nml1, nml2, notR, None, None],
            [None, None, None, dnRt, notU, nml2, nml3, nml1, nml2, nml3, upLt, None, None],
            [None, None, dnRt, nml1, nml2, nml3, nml1, nml2, nml3, upLt, None, None, None],
            [None, None, notL, nml2, nml3, notD, notD, notD, upLt, None, None, None, None],
            [None, wrp1, nml2, notD, upLt, None, None, None, None, None, None, None, None],
            [None, None, wrp2, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None]]
        
        e = {'Thessalonian Psilos': 7,
             'Thessalonian Ekdromos': 5,
             'Thessalonian Hoplite': 3,
             'Golden Guardian': 1}
             
        self.encounters = {wrp1: {},
                           wrp2: {},
                           nml1: e,
                           nml2: e,
                           nml3: e,
                           notL: e,
                           notU: e,
                           notR: e,
                           notD: e,
                           upLt: e,
                           dnLt: e,
                           dnRt: e,
                           pth1: e,
                           pth2: e,
                           gate: {},
                           dist: e,
                           lair: {}
                           }
    
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

    def greece1(self, selectionIndex=None):
        X = 7
        Y = 1
        return self.actions({'area': "Greece",
                             'coordinates': (X, Y)})

    def greece2(self, selectionIndex=None):
        X = 8
        Y = 2
        return self.actions({'area': "Greece",
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
        if "Thessaloniki" not in self.c.flags:
            self.c.flags['Thessaloniki'] = True
            self.text = ("Toshe: I can feel the suspense rising.")
        return self.actions()

    def normal3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notUp(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def notDown(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def path1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        if "Macedonian Gate Opened" in self.c.flags:
            self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        if "Thessaloniki Clearing" not in self.c.flags:
            self.c.flags['Thessaloniki Clearing'] = True
            self.text = ("You see a path up ahead." +
                         "\nToshe: This looks like the way to Macedonia.")
        return self.actions()

    def path2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        if "Macedonian Gate Opened" in self.c.flags:
            self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You can see the gates of Macedonia up ahead.")
        return self.actions()

    def gate(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        if "Macedonian Gate Opened" not in self.c.flags:
            if selectionIndex == 0:
                self.c.flags['Macedonian Gate Opened'] = True
                self.imageIndex = 15
                self.text = ("You insert the key in the keyhole and" +
                             " slowly turn the key. The gate shoots up and" +
                             " lets out a brilliant light.")
                self.helpText = ("Once you enter, you will not be able" +
                                 " to come back.")
                self.menu = ["Enter the gate."]
            elif (not self.c.hasItem("The Key to Macedonia") and
                  not self.c.hasItem("Key Mold")):
                self.text = ("\nToshe: The glorious gates of Macedonia!" +
                             " I need to somehow get the key from the Greeks.")
                if ( "Athens" not in self.c.flags and
                     self.c.hasMercenary("Qendresa")):
                    self.text += ("\nQendresa: Perhaps in Athens you may" +
                                  " find one with a key." +
                                  "\nToshe: Where's that?" +
                                  "\nQendresa: It is southeast of Albania." +
                                  "\nToshe: Ok. Let's check it out.")
                elif ("Coliseum" in self.c.flags and
                      "Coliseum Complete" not in self.c.flags and
                      self.c.hasMercenary("Barrie")):
                    self.text += ("\nBarrie: Did ya hear what the coliseum fella" +
                                  " said? I'll wager that our ticket's in that" +
                                  " fortress visit.")
                    
            elif (not self.c.hasItem("The Key to Macedonia") and
                  not self.c.hasItem("Gold Bar")):
                self.c.flags['Key Hunting'] = True
                self.text = ("Toshe: I have a mold, but no key. I need some" +
                             " metal so a key can be forged.")
                if ( not self.c.hasItem("Gold Ore") and
                     self.c.hasMercenary("Qendresa")):
                    self.text += ("\nQendresa: Gold is plentiful in Albania.")
                elif (self.c.hasItem("Gold Ore") and
                      self.c.hasMercenary("Barrie")):
                    self.text += ("\nBarrie: Hey, chap. Why not find someone to" +
                                  " turn that ore of yours into metal?")
                    
            elif not self.c.hasItem("The Key to Macedonia"):
                self.c.flags['Key Hunting'] = True
                self.text = ("Toshe: I need to smith this key from the mold I" +
                             " took. Who might be able to do that?")
                if self.c.hasMercenary("Qendresa"):
                    self.text += ("\nQendresa: Might there be a blacksmith who" +
                                  " specializes in fine metals?")

            elif self.c.hasItem("The Key to Macedonia"):
                self.text = ("Toshe: Finally. My homeland. I must take back" +
                             " what's mine!" +
                             "\nYou can make out the outline of a shadowy" +
                             " figure past the gates.")
                if ( self.c.hasMercenary("Qendresa") and
                     self.c.hasMercenary("Barrie")):
                    self.text += ("\nToshe: Guys, this is something I need to" +
                                  " do on my own." +
                                  "\nBarrie: Oh..." +
                                  "\nQendresa: We understand. Bring justice" +
                                  " to your homeland!" +
                                  "\nBarrie: ...Yeah!" +
                                  "\nQendresa salutes you, and Barrie raises" +
                                  " a fist in the air as you step up to the" +
                                  " keyhole.")
                elif self.c.hasMercenary("Qendresa"):
                    self.text += ("\nToshe: Hey, Qendresa. I'm going in" +
                                  " solo." +
                                  "\nQendresa: I believe in you, warrior." +
                                  " You can do this without me.")
                elif self.c.hasMercenary("Barrie"):
                    self.text += ("\nToshe: Barrie, we've been through a" +
                                  " lot together, but I'm gonna have to leave" +
                                  " you behind on this one." +
                                  "\nBarrie: Do your thing, chappy boy.")
                self.menu = ["Open the gate."]
                
        else:
            self.imageIndex = 15
            if selectionIndex == 0:
                X = 3
                Y = 3
                return self.actions({'area': "Macedonia",
                                     'coordinates': (X, Y)})
            else:
                self.text = ("Toshe: My homeland." +
                             " Once beautiful, now tarnished." +
                             " I will restore you to your former glory.")
                self.menu = ["Enter the gate."]
                
        return self.actions()

    def palaceInTheDistance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 25
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Thessaloniki",
                                 'coordinates': (X, Y)})
        self.text = "You see a grand palace in the distance."
        self.menu = ["Hike up to the palace."]
        return self.actions()

    def lairOfTheMagi(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
