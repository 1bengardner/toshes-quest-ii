"""
File: TUABerlusconiCastle.py
Author: Ben Gardner
Created: July 14, 2015
Revised: October 25, 2022
"""


import random


class BerlusconiCastle:

    name = "Berlusconi Castle"
    audio = "Castle Stronghold"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.albanianDesert
        entr = self.entrance
        crn1 = self.corner1
        crd1 = self.corridor1
        crn2 = self.corner2
        crd2 = self.corridor2
        tnl1 = self.tunnel1
        tnl2 = self.tunnel2
        sts1 = self.stairs1
        crd3 = self.corridor3
        crd4 = self.corridor4
        pllr = self.pillars
        bend = self.bend
        tnl3 = self.tunnel3
        tnl4 = self.tunnel4
        tnl5 = self.tunnel5
        crn3 = self.corner3
        crn4 = self.corner4
        sts2 = self.stairs2
        sts3 = self.stairs3
        crd5 = self.corridor5
        clrn = self.clearing
        jail = self.jailCells
        sts4 = self.stairs4
        hall = self.hall
        chbr = self.chamber
        sts5 = self.stairs5
        arc1 = self.archway1
        arc2 = self.archway2
        door = self.doorway
        lect = self.lectern
        wrp2 = self.warp2
        wrp3 = self.warp3
        sil1 = self.silvio1
        sil2 = self.silvio2
        sil3 = self.silvio3
        
        
        self.spots = [
            [None, None, None, None, None, None, None],
            [None, None, sts1, None, sil1, None, None],
            [None, None, crd3, None, None, None, None],
            [None, None, crd4, None, sil2, None, None],
            [None, bend, pllr, None, None, None, None],
            [None, tnl3, None, None, sil3, None, None],
            [None, tnl4, None, None, None, None, None],
            [None, tnl5, None, None, None, None, None],
            [None, crn3, crn4, None, None, None, None],
            [None, None, None, None, None, lect, None],
            [None, None, None, tnl2, None, door, None],
            [None, None, crn2, tnl1, None, arc2, None],
            [None, crn1, crd1, crd2, None, wrp3, None],
            [None, entr, None, sts2, None, None, None],
            [None, wrp1, None, sts3, None, wrp2, None],
            [None, None, None, crd5, None, sts5, None],
            [None, arc1, None, clrn, jail, sts4, None],
            [None, wrp3, None, hall, chbr, None, None],
            [None, None, None, None, None, None, None]]
        
        e1 = {'Royal Knight': 10,
              'Royal Cryomancer': 4,
              'Royal Pyromancer': 4,
              'Royal Sentinel': 2}

        e2 = {'Royal Knight': 10,
              'Royal Cryomancer': 4,
              'Royal Pyromancer': 4,
              'Flame Templar': 4}
             
        self.encounters = {wrp1: {},
                           entr: {},
                           crn1: e1,
                           crd1: e1,
                           crn2: e1,
                           crd2: e1,
                           tnl1: e1,
                           tnl2: e1,
                           sts1: e1,
                           crd3: e1,
                           crd4: e1,
                           pllr: e2,
                           bend: e2,
                           tnl3: e2,
                           tnl4: e2,
                           tnl5: e2,
                           crn3: e2,
                           crn4: {},
                           sts2: e1,
                           sts3: e1,
                           crd5: e1,
                           clrn: e1,
                           jail: e1,
                           sts4: e1,
                           hall: e1,
                           chbr: e1,
                           sts5: e1,
                           arc1: {},
                           arc2: {},
                           door: {},
                           lect: {},
                           wrp2: {},
                           wrp3: {},
                           sil1: {},
                           sil2: {},
                           sil3: {}
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

    def albanianDesert(self, selectionIndex=None):
        X = 6
        Y = 23
        return self.actions({'area': "Albanian Desert",
                             'coordinates': (X, Y)})

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Silvio"
        merc1 = "Qendresa"
        if "Silvio Berlusconi1" not in self.c.flags['Kills']:
            X = 4
            Y = 1
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})
        elif "Silvio Coward 1" not in self.c.flags:
            self.text = ("%s: Oh dear, it's getting late. I am" % npc +
                         " an important man, after all, so I must get" +
                         " back to my business. Hope you have a lovely time" +
                         " in my castle! Hahaha!" +
                         "\nSilvio vanishes from sight.")
            self.c.flags['Silvio Coward 1'] = True    
            if self.c.hasMercenary(merc1):
                self.text += ("\n%s: We shall find you, Silvio." % merc1 +
                              " You shall pay for your crimes against" +
                              " humanity.")
        return self.actions()

    def corner1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def corridor1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def corner2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if "Lesser Dragon" not in self.c.flags['Kills']:
            self.text = ("You feel heat emanate from a large pit to the left.")
        return self.actions()

    def corridor2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tunnel1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tunnel2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 2
            Y = 1
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})
        self.text = ("You see a set of stairs zigzagging downward.")
        self.menu = ["Descend to the lower level."]
        return self.actions()

    def stairs1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 10
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})
        self.text = ("You reach a set of stairs going up.")
        self.menu = ["Ascend to the upper level."]
        return self.actions()

    def corridor3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def corridor4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def pillars(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if "Berlusconi Heat" not in self.c.flags:
            self.text = ("Toshe: Woah, it's getting hot.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Woo, boy!")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: I am quite familiar with the heat.")
            self.c.flags['Berlusconi Heat'] = True
        return self.actions()

    def bend(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tunnel3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tunnel4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        if "Berlusconi Menacing" not in self.c.flags:
            self.text = ("Toshe: These tunnels are menacing.")   
            self.c.flags['Berlusconi Menacing'] = True         
        return self.actions()

    def tunnel5(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def corner3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def corner4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        merc1 = "Qendresa"
        merc2 = "Barrie"
        if ( "Silvio Berlusconi2" in self.c.flags['Kills'] and
             "Lesser Dragon" not in self.c.flags['Kills']):
            self.text = "Toshe: Of course there's a dragon in this dungeon."
            if self.c.hasMercenary(merc1):
                self.text += ("\n%s: My surprise would be unwarranted" % merc1 +
                              " at this point.")
            if self.c.hasMercenary(merc2):
                self.text += ("\n%s: Let's slay it." % merc2)
            self.c.flags['Lesser Dragon'] = True
            self.view = "battle"
            return self.actions({'enemy': "Lesser Dragon",
                                 'mercenaries': self.c.mercenaries})
        if selectionIndex == 0:
            self.text = ("You pull down the lever." +
                         "\nThe castle walls rumble.")
            self.c.flags['Berlusconi Lever Pulled'] = True
        elif "Berlusconi Lever Pulled" in self.c.flags:
            self.text = ("You enter a room with a pulled down lever" +
                         " protruding from the wall.")
        elif ( "Silvio Berlusconi2" not in self.c.flags['Kills']):
            self.text = ("You enter a room with a" +
                         " lever in the corner." +
                         "\nToshe: Hmpf. A dead end.")
        elif "Berlusconi Lever Pulled" not in self.c.flags:
            self.imageIndex = 16
            self.text = ("You enter a room with a lever protruding from the" +
                         " wall.")
            self.menu = ["Pull the lever."]
        return self.actions()

    def stairs2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def stairs3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def corridor5(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def clearing(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 21
        self.text = None
        self.helpText = None
        self.menu = []
        merc1 = "Qendresa"
        if ( self.c.hasMercenary(merc1) and
             "Silvio Berlusconi2" not in self.c.flags['Kills']):
            self.text = ("%s: I can sense Silvio's corrupt presence." % merc1)
        return self.actions()

    def jailCells(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 22
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Prisoner"
        if selectionIndex == 0 and random.randint(0, 1) == 0:
            self.text = ("You bash your weapon against the cell bar." +
                         "\nSentinel: Hey! What the hell?")
            self.view = "battle"
            return self.actions({'enemy': "Royal Sentinel",
                                 'mercenaries': self.c.mercenaries})
        elif selectionIndex == 0:
            self.text = ("You smash your weapon against the surprisingly" +
                         " flimsy cell bar. It bends a little bit.")
            self.c.flags['Berlusconi Prisoners Freed'] += 1
            self.menu = ["Help the prisoners."]
        elif ( "Berlusconi Prisoners Freed" not in self.c.flags or
             self.c.flags['Berlusconi Prisoners Freed'] < 3):
            self.c.flags['Berlusconi Prisoners Freed'] = 0
            self.text = "%s" % npc + random.choice([
                "s: Please, help us!",
                "s: Save our souls!",
                ": What crime have I committed?",
                ": I'm innocent!",
                ": You...can you spare some bread?",
                ": Stranger, please lend a hand!",
                ": Get me out of here!"])
            self.menu = ["Help the prisoners."]
            
        if ( self.c.flags['Berlusconi Prisoners Freed'] == 3 and
             "Prisoners Freed" not in self.c.flags):
            self.text += ("\n%ss: Bless your soul!" % npc +
                          "\nThe prisoners break free from the cell.")
            self.menu = []
            self.c.flags['Prisoners Freed'] = True
        return self.actions()

    def stairs4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 23
        self.text = None
        self.helpText = None
        self.menu = []
        if ( "Silvio Berlusconi2" in self.c.flags['Kills'] and
             "Berlusconi Lever Thought" not in self.c.flags):
            self.text = ("Toshe: There's probably a switch that opens" +
                         " up that door.")
            self.c.flags['Berlusconi Lever Thought'] = True
        return self.actions()

    def hall(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 24
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def chamber(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 25
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def stairs5(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 26
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def warp2(self, selectionIndex=None):
        if "Berlusconi Lever Pulled" not in self.c.flags:
            X = 1
            Y = 16
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})
        else:
            X = 5
            Y = 11
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})

    def warp3(self, selectionIndex=None):
        X = 5
        Y = 15
        return self.actions({'area': "Berlusconi Castle",
                             'coordinates': (X, Y)})

    def archway1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 27
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Silvio"
        merc1 = "Qendresa"
        if "Silvio Berlusconi2" not in self.c.flags['Kills']:
            X = 4
            Y = 3
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})
        elif "Silvio Coward 2" not in self.c.flags:
            self.text = ("%s: Well, it was nice getting to know" % npc +
                         " one another. I really must go now."
                         "\nSilvio escapes into his chamber. The" +
                         " large stone door slams shut behind him." +
                         "\nToshe: Come out, you fucking pussy!")
            self.c.flags['Silvio Coward 2'] = True    
            if self.c.hasMercenary(merc1):
                self.text += ("\n%s: He cannot hide forever." % merc1)
        return self.actions()

    def archway2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 28
        self.text = None
        self.helpText = None
        self.menu = []
        if "Berlusconi Door Opened" not in self.c.flags:
            self.text = ("Toshe: Looks like that lever did something good.")
            self.c.flags['Berlusconi Door Opened'] = True            
        return self.actions()

    def doorway(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 29
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Silvio"
        if "Silvio Berlusconi3" not in self.c.flags['Kills']:
            self.text = ("%s: Oops! I forgot to feed the dragon again!" % npc)
        return self.actions()

    def lectern(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 30
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Silvio"
        merc1 = "Qendresa"
        merc2 = "Barrie"
        if "Silvio Berlusconi3" not in self.c.flags['Kills']:
            X = 4
            Y = 5
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0:
            self.text = ("You find the Greek Wall Blueprint!" +
                         "\nToshe: Why would he have this?")
            self.c.flags['Blueprint'] = True
            return self.actions({'item': "Greek Wall Blueprint"})
        elif "Silvio Coward 3" not in self.c.flags:
            self.text = ("%s: Albania is already mine." % npc +
                         " I cannot be stopped! Hahahaha!"
                         "\nSilvio disappears in a puff of smoke." +
                         "\nToshe: ...What was he talking about?")
            self.c.flags['Silvio Coward 3'] = True
            if self.c.hasMercenary(merc2):
                self.text += ("\n%s: Does he think he can conquer" % merc2 +
                              " the world or somethin'?")
            if self.c.hasMercenary(merc1):
                self.text += ("\n%s: It sounds like Silvio has bigger" % merc1 +
                              " plans. We must stop him before it's too late.")
            self.text += ("\nYou notice a scroll on the lectern.")
            self.menu = ["Take the scroll."]
        elif "Blueprint" not in self.c.flags:
            self.text += ("There is a scroll on the lectern.")
            self.menu = ["Take the scroll."]
        return self.actions()

    def silvio1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Man"
        npcU = "Silvio"
        merc1 = "Qendresa"
        merc2 = "Barrie"
        if selectionIndex == 0:
            self.c.flags['Met Silvio'] = True
            self.view = "battle"
            return self.actions({'enemy': "Silvio Berlusconi1",
                                 'mercenaries': self.c.mercenaries})
        elif "Silvio Berlusconi1" in self.c.flags['Kills']:
            X = 1
            Y = 13
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})

        self.c.flags['New Song'] = "Drat"
        self.menu = ["Brace yourself."]
        if not self.c.hasMercenary(merc1):
            self.text = ("%s: Welcome to my castle." % npc +
                         "\nToshe: Thank you. Who are you?" +
                         "\n%s: I am Silvio." % npcU +
                         "\nToshe: The Italian president?" +
                         "\n%s: You must have seen me on TV! This must" % npcU +
                         " be exciting for you." +
                         "\nToshe: Not really. On TV they say how corrupt" +
                         " you are." +
                         "\n%s: That's unfortunate. I try to keep a" % npcU +
                         " good image, but sometimes I slip up. I'm only" +
                         " human. No matter, let me give you a good show." +
                         " I'll make it exciting just for you.")            
        elif self.c.hasMercenary(merc1):
            self.text = ("%s: Welcome to my castle, friends!" % npc +
                         "\n%s: Silence, Silvio! You brought war to a" % merc1 +
                         " once-peaceful country. You are the reason" +
                         " my homeland is in ruin!" +
                         "\n%s: Feisty little Albanian. All that" % npcU +
                         " resentment toward a man who brought his country" +
                         " back on its feet after a financial downturn and" +
                         " went on to become the richest nation in Europe." +
                         " I'm more patriotic than you'll ever be." +
                         "\n%s: You are not a patriot." % merc1 +
                         " You are a disgusting man. I have no more words" +
                         " for you. Let our blades talk." +
                         "\n%s: Hahaha! Very well, very well." % npcU)
        if self.c.hasMercenary(merc2):
            self.text += ("\n%s: Quit stalling and fight already!" % merc2)
        self.text += ("\nSilvio advances toward you.")
        
        return self.actions()

    def silvio2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 28
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Silvio"
        merc1 = "Qendresa"
        merc2 = "Barrie"
        if selectionIndex == 0:
            self.text = "%s: Shall we dance?" % npc
            self.c.flags['Silvio Pursuit'] = True
            self.view = "battle"
            return self.actions({'enemy': "Silvio Berlusconi2",
                                 'mercenaries': self.c.mercenaries})
        elif "Silvio Berlusconi2" in self.c.flags['Kills']:
            X = 1
            Y = 16
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})

        self.c.flags['New Song'] = "Drat"
        self.menu = ["Brace yourself."]
        if not self.c.hasMercenary(merc1):
            self.text = ("%s: Well, look who's still here!" % npc +
                         "\nToshe: You're a real menace." +
                         "\n%s: I am Silvio." % npc +
                         "\nToshe: No shit." +
                         "\n%s: Such language. Anyway, I believe" % npc +
                         " we had some unfinished business. Let's" +
                         " bring closure to this agreement.")            
        elif self.c.hasMercenary(merc1):
            self.text = ("Toshe: Ok Silvio, it's time to end this bullshit." +
                         "\n%s: But I've only just begun!" % npc +
                         "\n%s: You need to be taught a lesson." % merc1 +
                         "\n%s: I'm not a very good listener." % npc +
                         "\n%s: Words are useless. My blade shall" % merc1 +
                         " do the teaching." +
                         "\n%s: You really like that line, eh?" % npc +
                         "\n%s: My espadon shall silence you." % merc1 +
                         "\n%s: Espa-what? Sorry, Alboonian isn't my" % npc +
                         " native tongue.")      
            if self.c.hasMercenary(merc2):
                self.text += ("\n%s: Ok, I've had it." % merc2 +
                              " Let's pulverize this clown.")
            else:
                self.text += ("\nToshe: That's enough out of you.")
        
        return self.actions()


    def silvio3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 30
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Silvio"
        merc1 = "Qendresa"
        merc2 = "Barrie"
        if selectionIndex == 0:
            self.c.flags['Silvio Vanquished'] = True
            self.view = "battle"
            return self.actions({'enemy': "Silvio Berlusconi3",
                                 'mercenaries': self.c.mercenaries})
        elif "Silvio Berlusconi3" in self.c.flags['Kills']:
            X = 5
            Y = 9
            return self.actions({'area': "Berlusconi Castle",
                                 'coordinates': (X, Y)})

        self.c.flags['New Song'] = "Drat"
        self.menu = ["Brace yourself."]
        if not self.c.hasMercenary(merc1):
            self.text = ("%s: You're a persistent one. Hahaha!" % npc +
                         "\nToshe: And you're still a menace." +
                         "\n%s: I am still Silvio." % npc +
                         "\nToshe: ...Why are you here?" +
                         "\n%s: That's the question, is it not?" % npc +
                         " Who would inhabit such a place? This desolate" +
                         " wasteland offers nothing. Yet the people of" +
                         " Albania still cling to their home." +
                         " What good is a nation without a good ruler?" +
                         " I am exactly what Albania needs. Now, if" +
                         " you'll be excused, you've wasted enough of" +
                         " my time. Off you go.")            
        elif self.c.hasMercenary(merc1):
            self.text = ("%s: Oh, hello, friends!" % npc)      
            if self.c.hasMercenary(merc2):
                self.text += ("\n%s: You're cornered!" % merc2)
            self.text += ("\n%s: Your reign ends here." % merc1 +
                          "\n%s: But...I've only just begun." % npc +
                          "\nToshe: What does that mean?" +
                          "\n%s: Hahahaha! Fools! You've fallen" % npc +
                          " for my trick!" +
                          "\n%s: A trick? How?" % merc1 +
                          "\n%s: It will all become clear when your" % npc +
                          " world crumbles before you.")      
            if self.c.hasMercenary(merc2):
                self.text += ("\n%s: He's just talkin' nonsense!" % merc2)
            self.text += ("\nSilvio rushes toward you.")
        
        return self.actions()
