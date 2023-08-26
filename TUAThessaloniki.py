"""
File: TUAThessaloniki.py
Author: Ben Gardner
Created: August 3, 2015
Revised: August 25, 2023
"""


import random


class Thessaloniki:

    name = "Thessalonian Highlands"
    audio = "Shining Armour"

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
        if "Conclusion" in self.c.flags:
            pthL = self.pathToLitochoro
            lito = self.litochoro
        else:
            pthL = dnRt
            lito = None
        pth1 = self.path1
        pth2 = self.path2
        gate = self.gate
        dist = self.palaceInTheDistance
        lair = self.lairOfTheMagi
        
        
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, lair, None, None, None, None, None, None, None, None, dist, None, None],
            [None, None, None, None, None, None, gate, None, lito, None, notL, dnLt, None],
            [None, None, None, None, None, None, pth2, None, pthL, notU, nml2, upLt, None],
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
                           dist: {},
                           lair: {},
                           pthL: {},
                           lito: {},
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

    def litochoro(self, selectionIndex=None):
        X = 1
        Y = 5
        return self.actions({'area': "Litochoro",
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
            self.text = ("%s: I can feel the suspense rising." % self.c.NAME)
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
                         "\n%s: This looks like the way to Macedonia." % self.c.NAME)
        return self.actions()

    def path2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        if "Macedonian Gate Opened" in self.c.flags:
            self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        if "Phalanx Captain" not in self.c.flags:
            self.view = "battle"
            self.text = "Phalanx Captain: Halt, Macedonian."
            self.c.flags['Phalanx Captain'] = True
            return self.actions({'enemy': "Phalanx Captain",
                                 'mercenaries': self.c.mercenaries,})
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
                             " slowly turn the key. The gate doors open and" +
                             " let out a brilliant light.")
                self.helpText = ("Once you enter, you will not be able" +
                                 " to come back.")
                self.menu = ["Enter the gate."]
            elif (not self.c.hasItem("The Key to Macedonia") and
                  not self.c.hasItem("Key Mold")):
                self.text = ("\n%s: The glorious gates of Macedonia!" % self.c.NAME +
                             " I need to somehow get the key from the Greeks.")
                if ( "Athens" not in self.c.flags and
                     self.c.hasMercenary("Qendresa")):
                    self.text += ("\nQendresa: Perhaps in Athens you may" +
                                  " find one with a key." +
                                  "\n%s: Where's that?" % self.c.NAME +
                                  "\nQendresa: It is southeast of Albania." +
                                  "\n%s: Ok. Let's check it out." % self.c.NAME)
                elif ("Coliseum" in self.c.flags and
                      "Coliseum Complete" not in self.c.flags and
                      self.c.hasMercenary("Barrie")):
                    self.text += ("\nBarrie: Did ya hear what the coliseum fella" +
                                  " said? I'll wager that our ticket's in that" +
                                  " fortress visit.")
                    
            elif (not self.c.hasItem("The Key to Macedonia") and
                  not self.c.hasItem("Gold Bar")):
                self.c.flags['Key Hunting'] = True
                self.text = ("%s: I have a mold, but no key. I need some" % self.c.NAME +
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
                self.text = ("%s: I need to smith this key from the mold I" % self.c.NAME +
                             " took. Who might be able to do that?")
                if self.c.hasMercenary("Qendresa"):
                    self.text += ("\nQendresa: Might there be a blacksmith who" +
                                  " specializes in fine metals?")

            elif self.c.hasItem("The Key to Macedonia"):
                self.text = ("%s: Finally. My homeland. I must take back" % self.c.NAME +
                             " what's mine!" +
                             "\nYou can make out the outline of a shadowy" +
                             " figure past the gates.")
                if ( self.c.hasMercenary("Qendresa") and
                     self.c.hasMercenary("Barrie")):
                    self.text += ("\n%s: Guys, this is something I need to" % self.c.NAME +
                                  " do on my own." +
                                  "\nBarrie: Oh..." +
                                  "\nQendresa: We understand. Bring justice" +
                                  " to your homeland!" +
                                  "\nBarrie: ...Yeah!" +
                                  "\nQendresa salutes you, and Barrie raises" +
                                  " a fist in the air as you step up to the" +
                                  " keyhole.")
                elif self.c.hasMercenary("Qendresa"):
                    self.text += ("\n%s: Hey, Qendresa. I'm going in" % self.c.NAME +
                                  " solo." +
                                  "\nQendresa: I believe in you, warrior." +
                                  " You can do this without me.")
                elif self.c.hasMercenary("Barrie"):
                    self.text += ("\n%s: Barrie, we've been through a" % self.c.NAME +
                                  " lot together, but I'm gonna have to leave" +
                                  " you behind on this one." +
                                  "\nBarrie: Do your thing, chappy %s." % ("gal" if self.c.isFemale else "boy"))
                self.menu = ["Open the gate."]
                
        else:
            self.imageIndex = 15
            if selectionIndex == 0:
                X = 3
                Y = 3
                return self.actions({'area': "Macedonia",
                                     'coordinates': (X, Y)})
            else:
                self.text = ("%s: My homeland." % self.c.NAME +
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
        self.menu = [
            "Stare into the river.",
            "Head back."
        ]
        
        if selectionIndex == 1:
            X = 10
            Y = 1
            return self.actions({'area': "Thessaloniki",
                                 'coordinates': (X, Y)})

        if selectionIndex == 2 or "Palace Ointment" in self.c.flags:
            self.menu = [
                "Enter Niplin's Lair.",
                "Head back."
            ]
            self.imageIndex = 26
            if "Palace Ointment" in self.c.flags:
                self.text = "You see Niplin's Lair across the river with a bridge leading to it."
            else:
                self.c.flags['Palace Ointment'] = True
                self.c.removeItem(self.c.indexOfItem("Olympian Ointment"))
                self.text = "You pour a jar of Olympian Ointment into the river."
                if self.c.hasMercenary("Barrie"):
                    self.text += "\nBarrie: %s, what are you thinking, man?" % self.c.NAME
                self.text += "\nThe bridge to Niplin's Lair rises from the water!"
                if self.c.hasMercenary("Qendresa"):
                    self.text += "\nQendresa: Brilliant."
                if self.c.hasMercenary("Barrie"):
                    self.text += "\nBarrie: Ok, that happened."
        elif "Niplin" in self.c.flags['Kills']:
            self.imageIndex = 24
            if selectionIndex is None:
                if "Gargoyle Trip" not in self.c.flags:
                    self.c.flags['Gargoyle Trip'] = True
                    self.text = "Gargoyle: Hmph. Thou arens't quarrelling? Odd. Let us assist thees."
                    if self.c.hasMercenary("Qendresa"):
                        self.text += "\nQendresa: Yes, please! Ah!"
                    if self.c.hasMercenary("Qendresa") and self.c.hasMercenary("Barrie"):
                        self.text += "\nThe gargoyle grabs you and Qendresa with its claws. The two of you manage to snag and carry Barrie with one hand each, just in time before taking off."
                    elif self.c.hasMercenary("Qendresa") or self.c.hasMercenary("Barrie"):
                        teammate = "Qendresa" if self.c.hasMercenary("Qendresa") else "Barrie"
                        self.text += "\nThe gargoyle lifts you and %s, swiftly flying away." % teammate
                    self.text += "\nYou land softly in the Thessalonian Highlands, and the gargoyle departs."
                else:
                    self.text = "You see Niplin's hallowed lair across the river."
                    if self.c.hasMercenary("Qendresa") and (not self.c.hasMercenary("Barrie") or "Easy there tiger" in self.c.flags):
                        self.text += "\nQendresa: The archmages have been freed."
                        if self.c.hasMercenary("Barrie"):
                            self.text += "\nBarrie: Yeah, thanks to us kicking evil butt! We don't have to go back there again."
                    elif self.c.hasMercenary("Barrie"):
                        self.text += "\nBarrie: We kicked Niplin's butt."
                        if "Easy there tiger" not in self.c.flags and self.c.hasMercenary("Qendresa"):
                            self.c.flags['Easy there tiger'] = True
                            self.text += "\nQendresa: We kicked Riplin's butt!"
                            self.text += "\nBarrie: We ripped Riplin's butt!"
                            self.text += "\nQendresa: We nipped Niplin's nut!"
                            self.text += "\nBarrie: Easy there, tiger."
                            self.text += "\nFang growls softly."
                    else:
                        self.text += "\n%s: The world is a better place now." % self.c.NAME
                    if self.c.hasItem("Olympian Ointment") and "Palace Ointment" not in self.c.flags and self.c.specialization is not None:
                        self.menu.append("Apply Olympian Ointment.")
        elif False not in [boss in self.c.flags['Kills'] for boss in ["Oukkar", "Aldreed", "Vismurg"]]:
            self.menu = [
                "Enter the palace.",
                "Head back."
            ]
            self.imageIndex = 23
            self.text = "You see an illuminated palace across the river with a bridge leading to it."
            if "All Beacons Lit" not in self.c.flags:
                self.c.flags['All Beacons Lit'] = True
                if self.c.hasMercenary("Barrie"):
                    self.text += "\nBarrie: We did it! Let's get our groove on."
                if self.c.hasMercenary("Qendresa"):
                    self.text += "\nQendresa: The three beasts must have acted as magical guardians to this structure."
                self.text += "\n%s: Yes! We can get in now." % self.c.NAME
        else:
            if False not in [boss in self.c.flags['Kills'] for boss in ["Oukkar", "Aldreed"]]:
                self.imageIndex = 22
                self.text = "You see a palace across the river with two lit beacons: blue and red."
            elif False not in [boss in self.c.flags['Kills'] for boss in ["Oukkar", "Vismurg"]]:
                self.imageIndex = 21
                self.text = "You see a palace across the river with two lit beacons: green and red."
            elif False not in [boss in self.c.flags['Kills'] for boss in ["Aldreed", "Vismurg"]]:
                self.imageIndex = 20
                self.text = "You see a palace across the river with two lit beacons: green and blue."
            elif "Oukkar" in self.c.flags['Kills']:
                self.imageIndex = 19
                self.text = "You see a palace across the river with a lit red beacon."
            elif "Aldreed" in self.c.flags['Kills']:
                self.imageIndex = 18
                self.text = "You see a palace across the river with a lit blue beacon."
            elif "Vismurg" in self.c.flags['Kills']:
                self.imageIndex = 17
                self.text = "You see a palace across the river with a lit green beacon."
            else:
                self.text = "You see a palace across the river with three unlit beacons."
            
            self.text += "\n%s: I feel like something is missing." % self.c.NAME
            if self.c.hasMercenary("Barrie"):
                if "Vismurg" not in self.c.flags['Kills']:
                    if 'Vismurg Entrance Found' not in self.c.flags:
                        self.text += "\nBarrie looks to be deep in thought."
                        self.text += "\nBarrie: I have a feeling something is amok inside the Bluffs."
                        self.text += "\n%s: What do you mean inside?" % self.c.NAME
                        self.text += "\nBarrie: Seriously, we gotta head back to Herceg."
                        self.text += "\n%s: If you say." % self.c.NAME
                    elif "Avalanche" not in [skill.NAME for skill in self.c.skills] and "Moved Boulders" not in self.c.flags:
                        self.text += "\nBarrie taps his foot, thinking."
                        self.text += "\nBarrie: There's a powerful force here. Remember the boulders in Herceg Bluffs? You need a spell to blast those. That's my intel."
                    elif "Moved Boulders" not in self.c.flags:
                        self.text += "\nBarrie: What if you used Avalanche on the Herceg mountains?"
                    else:
                        self.text += "\nBarrie: We need to check out the Golem Cavern in the Billowing Bluffs. I can sense it."
                elif "Aldreed" not in self.c.flags['Kills']:
                    if 'Aldreed Entrance Found' not in self.c.flags:
                        self.text += "\nBarrie is pacing."
                        self.text += "\nBarrie: Ok, we should go for a deep, long swim."
                        self.text += "\n%s: I'm trying to enter that palace, and you want to swim? What's wrong with you?" % self.c.NAME
                        self.text += "\nBarrie: There must be something in the water."
                    elif "Melting Touch" not in [skill.NAME for skill in self.c.skills] and "Melted Ice" not in self.c.flags:
                        self.text += "\nBarrie scratches his nose."
                        self.text += "\nBarrie: Let's explore: there's that frozen passage down in the sea. What could melt that? Magic. That's what."
                    elif "Melted Ice" not in self.c.flags:
                        self.text += "\nBarrie: You have the touch. Use it. To melt ice."
                    elif "Galijula" not in self.c.flags:
                        self.text += "\nBarrie: We gotta go back in that underwater cave thing in the sea. Trust me."                        
                    else:
                        self.text += "\nBarrie: Hear me out...what if there's something hidden in Galijula?"
                elif "Oukkar" not in self.c.flags['Kills']:
                    if 'Oukkar Entrance Found' not in self.c.flags:
                        self.text += "\nBarrie: Oukkay, just one more beacon to light! Don't call me Seuss; just go where it's bright!"
                        if self.c.isPolite:
                            lameLine = "\n%s: That was really lame." % self.c.NAME
                        else:
                            lameLine = "\n%s: That was lame as fuck." % self.c.NAME
                        self.text += lameLine
                        self.text += "\nBarrie: If you'd rather, I can show you where the sun don't shine."
                    elif "Hailstorm" not in [skill.NAME for skill in self.c.skills] and "Plugged Geyser" not in self.c.flags:
                        self.text += "\nBarrie: We gotta light that last beacon. But how?"
                        self.text += "\n%s: There's something with that geyser in the desert." % self.c.NAME
                        self.text += "\nBarrie: True, true. We know fire melts ice. But what could chill and clog a steaming geyser?"
                    elif "Plugged Geyser" not in self.c.flags:
                        self.text += "\nBarrie: Hail thee!"
                        if self.c.hasMercenary("Qendresa"):
                            self.text += "\nQendresa bows."
                        self.text += "\n%s: What did I do?" % self.c.NAME
                        self.text += "\nBarrie: It's what you're about to do, friend. Call upon your storm and lead us to sandy victory!"
                    else:
                        self.text += "\nBarrie: To Yaouw!"
                        
            elif self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: It seems that a mage-like force is obstructing us. Bear with me...perhaps we can combat magic with magic? Pristina is brimming with wizardry. We may be able to find help there."

        if selectionIndex == 0:
            if ("Niplin" not in self.c.flags['Kills'] and "All Beacons Lit" in self.c.flags
                or "Palace Ointment" in self.c.flags):
                X = 5
                Y = 19
                return self.actions({'area': "Lair of the Magi",
                                     'coordinates': (X, Y)})
            elif "Niplin" in self.c.flags['Kills'] and not self.c.hasItem("Ominous Orb") and self.c.specialization is None and "Ready to Specialize" not in self.c.flags:
                self.text = "You watch a small purple sphere float to shore from the water. It begins rolling toward you. As you bend down to pick it up, it changes course and rolls directly into your hand."
                self.text += "\nYou find the Ominous Orb!"
                return self.actions({'item': "Ominous Orb"})
            else:
                self.text = "You see your reflection."

        return self.actions()
        
    def pathToLitochoro(self):
        self.view = "travel"
        self.imageIndex = 9
        self.text = "You see a small town up ahead."
        self.helpText = None
        self.menu = []
        return self.actions()
