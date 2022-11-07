"""
File: TUADuneHotsPeak.py
Author: Ben Gardner
Created: April 20, 2021
Revised: November 6, 2022
"""

import random
import time
from TUAStatics import Static

class DuneHotsPeak:

    name = "Dune Hot's Peak"
    audio = "Night Rain"

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
        onee = self.one
        twoo = self.two
        clea = self.clearing
        nooE = self.nookEntrance
        nook = self.nook
        
        self.spots = [
            [None, None, None, None, None, None, None],
            [None, None, None, clea, None, None, None],
            [None, onee, twoo, nooE, twoo, onee, None],
            [None, twoo, onee, twoo, onee, twoo, None],
            [None, onee, twoo, onee, twoo, onee, None],
            [None, twoo, onee, twoo, onee, twoo, None],
            [None, onee, twoo, onee, twoo, onee, None],
            [None, twoo, onee, twoo, onee, twoo, None],
            [None, onee, twoo, onee, twoo, onee, None],
            [None, None, None, entr, None, None, None],
            [None, nook, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        
        self.encounters = {
            entr: {},
            onee: {},
            twoo: {},
            clea: {},
            nooE: {},
            nook: {},
        }
        
        self.nextEvent = {
            "targetTime": (0, 99999999999),
            "event": None
        }
        self.timeUnit = 0.08
    
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
        
    def roll(self):
        return random.randint(1, 100)

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = "Ahead lies a desolate array of dunes."
        roll = self.roll()
        if self.c.hasMercenary("Barrie") and roll > 70:
            self.text += ("\n%s: Watch for those duners, bro." % "Barrie")
        if self.c.hasMercenary("Barrie") and 50 < roll < 71:
            self.text += ("\n%s: Whoa. Let's take it slow." % "Barrie")
        if self.c.hasMercenary("Qendresa") and 76 > roll > 25:
            self.text += ("\n%s: We must tread carefully." % "Qendresa")
        if self.c.hasMercenary("Barrie") and roll < 25:
            self.text += ("\n%s: Don't get sand in your eyes!" % "Barrie")
        if self.c.hasMercenary("Qendresa") and roll > 75:
            self.text += ("\n%s: Let us mind our step." % "Qendresa")
        return self.actions()

    def one(self, selectionIndex=None):
        self.imageIndex = 0
        return self.common()

    def two(self, selectionIndex=None):
        self.imageIndex = 1
        return self.common()

    def common(self, selectionIndex=None):
        self.view = "travel"
        self.text = ""
        self.helpText = None
        self.menu = []
        
        if "Fazed Text" in self.c.flags:
            self.text = self.c.flags['Fazed Text']
            del self.c.flags['Fazed Text']
        else:
            actionResults = self.performEventActions()
            if actionResults:
                return actionResults
            
        self.chooseNextEvent()
        
        self.text = self.text.strip()
        if self.text == "":
            self.text = None
            
        return self.actions()
        
    def performEventActions(self):
        def faceDragon(noticeSuffix):
            self.text += noticeSuffix
            self.c.flags['Fazed Text'] = ""
            self.view = "battle"
            return self.actions({'enemy': "Elder Dragon",
                                 'mercenaries': self.c.mercenaries})
        def enterWhirlwind(noticeSuffix):
            self.text += noticeSuffix
            self.c.flags['Fazed Text'] = self.text
            X = random.randint(1, 5)
            Y = random.randint(min(self.c.y+1, 8), 8)
            return self.actions({'area': "Dune Hots Peak",
                                 'coordinates': (X, Y)})
        def enterSandstorm(noticeSuffix):
            self.text += noticeSuffix
            self.c.flags['Fazed Text'] = self.text
            X = random.randint(1, 5)
            Y = min(self.c.y+1, 8)
            self.c.ep /= 2
            self.text += "\nToshe: " + random.choice([
                "I feel tired.",
                "That hit hard, man.",
                "I'm so dust."
            ])
            return self.actions({'area': "Dune Hots Peak",
                                 'coordinates': (X, Y)})
        def stumble(noticeSuffix):
            self.text += noticeSuffix
            self.c.flags['Fazed Text'] = self.text
            X = self.c.x
            Y = min(self.c.y+2, 8)
            return self.actions({'area': "Dune Hots Peak",
                                 'coordinates': (X, Y)})
        def faceDuner(noticeSuffix):            
            self.text += noticeSuffix
            self.c.flags['Fazed Text'] = ""
            self.view = "battle"
            return self.actions({'enemy': "Duner",
                                 'mercenaries': self.c.mercenaries})
    
        target = self.nextEvent['targetTime']
        event = self.nextEvent['event']
        # Too early
        if time.time() < target[0]:
            self.text = "As you attempt to scurry through the sand..."
            if event == "Dragon":
                return faceDragon("a dragon is alerted to your presence!")
            elif event == "Sandstorm":
                return enterSandstorm("you head into a sandstorm and get blown back!")
            elif event == "Whirlwind":
                return enterWhirlwind("you are caught by a surprise whirlwind!")
            elif event == "Stumble":
                return stumble("you lose footing and slide down a dune!")
            elif event == "Fall":
                return faceDuner("you trip straight into a surfacing duner!")
        # Too late
        elif time.time() > target[1]:
            self.text = "As you overcautiously trudge through across the desert..."
            if event == "Dragon":
                return faceDragon("a dragon comes up from behind!")
            elif event == "Sandstorm":
                return enterSandstorm("a dusty sandstorm whisks you away!")
            elif event == "Whirlwind":
                return enterWhirlwind("a nearby whirlwind takes hold of you!")
            elif event == "Stumble":
                return stumble("the sand shifts, setting you back!")
            elif event == "Fall":
                return faceDuner("you sink into the maw of a duner!")
        elif time.time() < target[0] + self.timeUnit * 5:
            self.text = "You almost trip into a dune in your haste!"
            if self.c.hasMercenary("Barrie"):
                if self.roll() > 50:
                    self.text += "\nBarrie: Slow down, bud!"
                else:
                    self.text += "\nBarrie: False start!"
        
    def chooseNextEvent(self):        
        roll = self.roll()
        if roll > 90:
            self.text += "\nThe wind howls."
            if self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: Step slowly. Stay behind the dune for protection."
            elif self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Give pause." +
                              "\nToshe: I'm not holding your paws.")
            self.nextEvent = {
                "targetTime": (
                    time.time() + self.timeUnit * 35,
                    time.time() + self.timeUnit * 90),
                "event": "Whirlwind"
            }
        elif roll > 86:
            self.text += "\nYou can hear a loud dragon roar from a nearby dune."
            if self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie: Let's go, quick!"
            elif self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: Make haste!"
            else:
                self.text += "\nToshe: Shit!"
            self.nextEvent = {
                "targetTime": (
                    time.time() + self.timeUnit * 8,
                    time.time() + self.timeUnit * 28),
                "event": "Dragon"
            }
        elif roll > 80:
            self.text += "\nYou see silhouettes of dragons far away."
            if self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: Stand still. Wait for them to pass."
            else:
                self.text += "\nToshe: I need to keep a low profile."
            if self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie: That's right. Easy does it."
            self.nextEvent = {
                "targetTime": (
                    time.time() + self.timeUnit * 40,
                    time.time() + self.timeUnit * 80),
                "event": "Dragon"
            }
        else:
            self.nextEvent = {
                "targetTime": (
                    time.time() + self.timeUnit * random.randint(10, 20),
                    time.time() + self.timeUnit * random.randint(40, 80)),
                "event": random.choice([
                    "Whirlwind",
                    "Sandstorm",
                    "Stumble",
                    "Fall"])
            }
            secondRoll = self.roll()
            if self.c.hasMercenary("Qendresa") and secondRoll > 70:
                self.text += ("\n%s: Proceed. However, we must keep quiet." % "Qendresa")
            if self.c.hasMercenary("Qendresa") and self.c.hasMercenary("Barrie") and 70 < secondRoll < 90:
                self.text += ("\n%s: My lips are sealed." % "Barrie")
            if self.c.hasMercenary("Qendresa") and 71 > secondRoll > 50:
                self.text += ("\n%s: Careful. Slow feet will help keep our balance." % "Qendresa")
            if self.c.hasMercenary("Qendresa") and self.c.hasMercenary("Barrie") and secondRoll < 51:
                self.text += ("\n%s: I'm on my tippy-toes!" % "Barrie")
            if self.c.hasMercenary("Qendresa") and secondRoll < 25:
                self.text += ("\n%s: Softly. We must not make any sound." % "Qendresa")
            if secondRoll < 15:
                self.text += "\nToshe: Sh-shit!"
            if not self.text:
                self.text = "Toshe: It's fucking hot."
    
    def nookEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = ""
        self.helpText = None
        self.menu = []
        
        if "Fazed Text" in self.c.flags:
            self.text = self.c.flags['Fazed Text']
            del self.c.flags['Fazed Text']
            
        if selectionIndex == 0:
            return Static.ICA_DATA['Ica 5']
        if self.c.dexterity >= 75:
            self.text += ("\nYou encounter a shiftsand that "+
                          "you can sink into.")
            self.menu = ["Enter the shiftsand."]
        else:
            self.text += ("\nYou encounter a shiftsand that "+
                          "you may be able to sink into, were you more "+
                          "dextrous.")
        self.text = self.text.strip()
        return self.actions()
    
    def nook(self, selectionIndex=None):
        thisIca = "Ica 5"
        self.c.flags[thisIca] = True
        self.view = "store"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        npc = "Ica"
        skill1 = "Rapid Burst"
        skillPrice1 = 5000
        tunic = "Fire Tunic"
        self.menu = ["Learn %s (%s euros)." % (skill1, skillPrice1),
                     "Leave."]
        if any(ica != thisIca and ica in self.c.flags for ica in Static.ICAS):
            self.menu += ["Travel to the next nook."]
        if selectionIndex == 0:
            return self.actions({'skill': skill1,
                                 'cost': skillPrice1,
                                 'items for sale': [tunic]+[None]*8})
        elif selectionIndex == 1:
            X = 3
            Y = 2
            return self.actions({'area': "Dune Hots Peak",
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
        
    def clearing(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        
        if selectionIndex == 0:
            if "Thunderous Crack" not in self.c.flags:
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = {'New Song': self.audio}
                self.imageIndex = 3
                self.c.flags['Thunderous Crack'] = True
                self.text = "You lay back and relax, pleased to have a rare moment without dust in your face.\n...\nYou awaken to a thunderous crack! Opening your eyes, you see the sky has turned black."
                self.text += "\nAn electrical tornado forms. From it emerges a birdlike monstrosity."
                self.text += "\nOukkar: Graaagh!!"
                self.menu = ["Face Oukkar."]
            elif "Oukkar" not in self.c.flags['Kills']:
                self.imageIndex = 4
                self.view = "battle"
                return self.actions({'enemy': "Oukkar",
                                     'mercenaries': self.c.mercenaries})
            else:
                self.c.flags["Spire Descent"] = True
                X = 2
                Y = 27
                return self.actions({'area': "Albanian Desert",
                                     'coordinates': (X, Y)})
        elif "Oukkar" not in self.c.flags['Kills']:
            self.text = "You reach a clearing where the once-distant mountains appear close."
            if self.c.hasMercenary("Barrie") and self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: This is quite serene. Let us bask in the silence."
                self.text += "\nBarrie: Yeah, let's enjoy this moment."
            elif self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie: Ahh...let's sit back and enjoy this view."
            else:
                self.text += "\nToshe: This looks sick."
            self.menu = ["Take in the view."]
        elif "Spire Descent" not in self.c.flags:
            self.imageIndex = 5
            self.text = "Oukkar forcefully collapses into the spire, creating a burning fissure."
            if self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie: This ain't lookin' good."
            if self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: We must leave at once!"
            if not self.c.hasMercenary("Barrie") and not self.c.hasMercenary("Qendresa"):
                self.text += "\nToshe: I gotta get the fuck out of here."
            self.menu = ["Descend the spire."]
        else:
            self.imageIndex = 6
            self.text = "You arrive at the clearing which was once a volcanic spire."
            self.menu = ["Slide down to the desert."]
        return self.actions()
        