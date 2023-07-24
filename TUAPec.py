"""
File: TUAPec.py
Author: Ben Gardner
Created: September 14, 2013
Revised: July 23, 2023
"""


from random import choice


class Pec:

    name = "Pec"
    audio = "Morning Walk"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.westernKosovo
        twn1 = self.town1
        twn2 = self.town2
        twn3 = self.town3
        tvrn = self.tavern
        bdrm = self.bedroom
        smth = self.smith
        acad = self.academy
        wzrd = self.wizard
        yogi = self.yogi
        merc = self.mercenary
        
        self.spots = [
            [None, None, None, None, None, None, None],
            [None, None, None, twn1, twn2, twn3, None],
            [None, None, None, wrp1, None, None, None],
            [None, None, None, None, None, None, None],
            [None, tvrn, None, bdrm, None, smth, None],
            [None, None, None, None, None, None, None],
            [None, acad, None, wzrd, None, yogi, None],
            [None, None, None, None, None, None, None],
            [None, None, None, merc, None, None, None],
            [None, None, None, None, None, None, None]]

        self.encounters = {}

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

    def westernKosovo(self, selectionIndex=None):
        X = 7
        Y = 6
        return self.actions({'area': "Western Kosovo",
                             'coordinates': (X, Y)})
    
    def town1(self, selectionIndex=None):
        if selectionIndex == 0:
            X = 1
            Y = 4
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 5
            Y = 4
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = ["Enter the inn.",
                     "Enter the blacksmith's."]
            
        return self.actions()

    def town2(self, selectionIndex=None):
        if selectionIndex == 0:
            X = 1
            Y = 6
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 3
            Y = 6
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 2:
            X = 5
            Y = 6
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = ["Enter the academy.",
                     "Enter the wizard's hut.",
                     "Enter the yogi's hut."]
        return self.actions()

    def town3(self, selectionIndex=None):
        if selectionIndex == 0:
            X = 3
            Y = 8
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})        
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = ["Enter the house."]
        return self.actions()

    def tavern(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Bartender Igor"
        if selectionIndex == 0:
            self.text = (npc+": "+choice(
["Do you want to know the damage formula? Take your power "+
 "and multiply it by your primary stat, which depends on your weapon.",
 "Bows take two hands. You can't wear a shield with one. The advantage is "+
 "bows always strike first.",
 "You can use two hands to play. W, S, A, D to move and "+
 "J, K, L to fight.",
 "Skills only work with certain weapons. You can't shoot a fireball "+
 "with a bow in your hands!",
 "If you take off your weapon you will resort to using your fists.",
 "If you are hit by a water attack "+
 "that takes away more than a third of your health, you may drown. "+
 "Do not worry. You may also live.",
 "Some weapons have elemental powers. These work against enemy "+
 "element weaknesses, but will not inflict any ailments.",
 "You can learn skills all over the world, usually from instructors. "+
 "If you are lucky, though, you may find one of the few wandering masters "+
 "scattered throughout Europe.",
 "If you want to make a nice drink, try this: pour cold Sour Apple Schnapps "+
 "in a glass and add a shot of cold Jagermeister. Mix and enjoy "+
 "this Rotten Apple."
 ]
))
        elif selectionIndex == 1:
            if self.c.euros >= 10 or self.c.euros == 0:
                if self.c.euros == 0:
                    self.text = npc+": Hey now...I'll just put it on your tab."
                else:
                    self.c.euros -= 10
                    self.text = (npc+": There you go.")
                if npc+" Quest 1" not in self.c.flags:
                    self.text += (" Ahem. %s, can you do something for me? " % ("Madam" if self.c.isFemale else "Sir")+
                                  "I've been looking for a nice local meat to "+
                                  "serve after the nearby cattle farm shut "+
                                  "due to monster invasion. With that weapon "+
                                  "of yours, I'm sure you can find something "+
                                  "around here. Just bring me back some raw "+
                                  "meat. Beef, pork, poultry...anything.")
                    if "Unholy Crow" in self.c.flags['Kills']:
                        self.c.flags[npc+' Quest 1'] = \
                                            self.c.flags['Kills']['Unholy Crow']
                    else:
                        self.c.flags[npc+' Quest 1'] = 0
                elif (npc+" Quest 1 Complete" not in self.c.flags and
                      npc+" Quest 1" in self.c.flags and
                      "Unholy Crow" in self.c.flags['Kills'] and
                      self.c.flags['Kills']['Unholy Crow']-1 >=
                      self.c.flags[npc+' Quest 1']):
                    self.text += (" I...I suppose crow meat will do. Thanks."+
                                  "\nIgor gives you 50 euros.")
                    self.c.euros += 50
                    self.c.flags[npc+' Quest 1 Complete'] = True
                elif (npc+" Quest 1 Complete" in self.c.flags and
                      npc+" Quest 2" not in self.c.flags):
                    self.text += (" My patrons are concerned with how "+
                                  "sanitary it is to consume crow. I think "+
                                  "some fresh seafood would be nice. There's "+
                                  "a lake a ways away with an abundance of "+
                                  "jellyfish. Get me a few of those, say 6, "+
                                  "and I can make a stew out of that.")
                    self.c.flags[npc+' Quest 2'] = 0
                    if "Toxic Jellyfish" in self.c.flags['Kills']:
                        self.c.flags[npc+' Quest 2'] += \
                                     self.c.flags['Kills']['Toxic Jellyfish']
                    if "Lion's Mane Jellyfish" in self.c.flags['Kills']:
                        self.c.flags[npc+' Quest 2'] += \
                                     self.c.flags['Kills']['Lion\'s Mane Jellyfish']
                elif (npc+" Quest 2 Complete" not in self.c.flags and
                      npc+" Quest 2" in self.c.flags):
                    kills = 0
                    if 'Toxic Jellyfish' in self.c.flags['Kills']:
                        kills += self.c.flags['Kills']['Toxic Jellyfish']
                    if 'Lion\'s Mane Jellyfish' in self.c.flags['Kills']:
                        kills += self.c.flags['Kills']['Lion\'s Mane Jellyfish']

                    if kills-6 >= self.c.flags[npc+' Quest 2']:
                        self.text += (" Those jellyfish stink. Thanks, though."+
                                      "\nIgor gives you 150 euros.")
                        self.c.euros += 150
                        self.c.flags[npc+' Quest 2 Complete'] = True
                elif (npc+" Quest 2 Complete" in self.c.flags and
                      npc+" Quest 3" not in self.c.flags):
                    self.text += (" Some customers have been getting sick "+
                                  "from the food. I'm going to try something "+
                                  "different. I was thinking swordfish would "+
                                  "be nice, but I wouldn't want to put you in "+
                                  "danger. Let's keep it simple and get some "+
                                  "octopus. 3 octopi, please.")
                    if "Mystical Octopus" in self.c.flags['Kills']:
                        self.c.flags[npc+' Quest 3'] = \
                                    self.c.flags['Kills']['Mystical Octopus']
                    else:
                        self.c.flags[npc+' Quest 3'] = 0
                elif (npc+" Quest 3 Complete" not in self.c.flags and
                      npc+" Quest 3" in self.c.flags and
                      "Mystical Octopus" in self.c.flags['Kills'] and
                      self.c.flags['Kills']['Mystical Octopus']-3 >=
                      self.c.flags[npc+' Quest 3']):
                    self.text += (" Perfect."+
                                  "\nIgor gives you 300 euros.")
                    self.c.euros += 300
                    self.c.flags[npc+' Quest 3 Complete'] = True
                elif npc+" Quest 3 Complete" in self.c.flags:
                    self.text += (" You know, it's not the most tasty, but "+
                                  "you can't beat octopus in terms of "+
                                  "nutrition.")
            else:
                self.text = (npc+": Sorry, %s. Can't serve you if you don't " % ("madam" if self.c.isFemale else "sir")+
                             "have the cash.")
        elif selectionIndex == 2:
            if (self.c.euros >= 30 or
                'Pec Room Level' in self.c.flags):
                X = 3
                Y = 4
                return self.actions({'area': "Pec",
                                     'coordinates': (X, Y)})
            else:
                self.text = (npc+": A room is 30 euros, %s." % ("madam" if self.c.isFemale else "sir"))
        elif selectionIndex == 3:
            X = 3
            Y = 1
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        else:
            if "Rested" in self.c.flags:
                self.text = ("You fall asleep."+
                             "\nWhen you wake up, you return to the front "+
                             "to give Igor your key."+
                             "\n"+npc+": How was that?")
                del self.c.flags['Rested']
                del self.c.flags['Pec Room Level']
            elif ("Pec Room Level" in self.c.flags and
                  self.c.flags['Pec Room Level'] < self.c.level):
                self.text = (npc+": %s!" % ("Madam" if self.c.isFemale else "Sir")+
                             " While you were away, I had the lock changed."+
                             " Please remember to return your key.")
                del self.c.flags['Pec Room Level']
            elif npc not in self.c.flags:
                self.text = (npc+": This is Pec, the town of stone. "+
                             "How may I serve you?")
                self.c.flags[npc] = True
            else:
                self.text = (npc+": "+
                             choice(["Our food is exquisite...or at least "+
                                     "exotic.",
                                     "Nothing compares to a hot air "+
                                     "balloon ride.",
                                     "This is a great place for a romantic "+
                                     "evening.",
                                     "Hello, %s." % ("miss" if self.c.isFemale else "sir"),
                                     "Ignore the banging. It's just the "+
                                     "blacksmith."]
                                    )
                             )
                self.text += (" How may I serve you?")

        if "Pec Room Level" in self.c.flags:
            self.menu = ["Ask for advice.",
                         "Buy a drink (10 euros).",
                         "Return to your room.",
                         "Leave."]
        else:
            self.menu = ["Ask for advice.",
                         "Buy a drink (10 euros).",
                         "Get a room (30 euros).",
                         "Leave."]
        return self.actions()
    
    def bedroom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Bartender Igor"
        if selectionIndex == 0:
            self.c.flags['Rested'] = True
            self.c.hp = self.c.maxHp
            self.c.ep = self.c.maxEp
            X = 1
            Y = 4
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 1
            Y = 4
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        if 'Pec Room Level' not in self.c.flags:
            self.c.euros -= 30
            self.text = ("Igor takes you to a room. "+
                         "You give him 30 euros and he hands you a key.")
            self.c.flags['Pec Room Level'] = self.c.level
        else:
            self.text = ("You walk inside your room and lock the door.")
        self.menu = ["Sleep.",
                     "Leave your room."]
        return self.actions()

    def smith(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Blacksmith"
        if selectionIndex == 0:
            X = 3
            Y = 1
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        if "Pec Blacksmith" not in self.c.flags:
            self.text = (npc+": Hello! I'm here to make you metal objects.")
            self.c.flags['Pec Blacksmith'] = True
        elif ("Key Hunting" in self.c.flags and
              "Macedonian Gate Opened" not in self.c.flags):
            self.text = (npc+": Well, keys are too delicate for me to" +
                         " work with. A nice crafted gold key is a task" +
                         " better suited to a goldsmith. I think there might" +
                         " be one far west of here.")
        else:
            self.text = npc+": "+choice(
                ["Let me fix you up a weapon real quick.",
                 "Take your pick.",
                 "Any special requests today?"])
        self.menu = ["Leave."]
        return self.actions({'items for sale': ["Heavy Mace",
                                                "Birch Bow",
                                                "Sacred Tomahawk",
                                                "Iron Hauberk",
                                                "Iron Cuirass",
                                                "Tower Shield",
                                                "Power Gauntlets",
                                                "Kite Shield",
                                                "Reinforced Buckler"]})

    def academy(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        npc = "Knight Deltraz"
        skill1 = "Shield Breaker"
        skill2 = "Steadfast Slash"
        skill3 = "Carnivorous Blow"
        skillPrice1 = 500 if self.c.mode != "Ultimate" else 0
        skillPrice2 = 1000 if self.c.mode != "Ultimate" else 0
        skillPrice3 = 2000 if self.c.mode != "Ultimate" else 0
        self.menu = ["Learn %s (%s euros)." % (skill1, skillPrice1),
                     "Learn %s (%s euros)." % (skill2, skillPrice2),
                     "Learn %s (%s euros)." % (skill3, skillPrice3),
                     "Leave."]
        if selectionIndex == 0:
            return self.actions({'skill': skill1,
                                 'cost': skillPrice1})
        elif selectionIndex == 1:
            return self.actions({'skill': skill2,
                                 'cost': skillPrice2})
        elif selectionIndex == 2:
            return self.actions({'skill': skill3,
                                 'cost': skillPrice3})
        elif selectionIndex == 3:
            X = 4
            Y = 1
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        elif self.c.mode == "Ultimate":
            self.text = (npc+": Welcome to the Grand Academy of Macedonia, great one. We have been awaiting your arrival. We are at your service.")
        else:
            self.text = (npc+": Welcome to the Grand Academy of Macedonia. "+
                         "Relocation "+
                         "was forced upon us due to the sudden emergence of "+
                         "bizarre monsters. As thus, we are awaiting orders "+
                         "from the president of Macedonia. As to his current "+
                         "location, I am unsure. Incidentally, we can train "+
                         "you at the academy to become a more competent "+
                         "fighter.")
        return self.actions()

    def wizard(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        npc = "Drumbol"
        skill1 = "Smoulder"
        skill2 = "Avalanche"
        skill3 = "Whirlpool"
        skillPrice1 = 1500 if self.c.mode != "Ultimate" else 0
        skillPrice2 = 1500 if self.c.mode != "Ultimate" else 0
        skillPrice3 = 1500 if self.c.mode != "Ultimate" else 0
        items = ["Wand of Kosovo"]+[None]*8
        self.menu = ["Learn %s (%s euros)." % (skill1, skillPrice1),
                     "Learn %s (%s euros)." % (skill2, skillPrice2),
                     "Learn %s (%s euros)." % (skill3, skillPrice3),
                     "Leave."]
        if selectionIndex == 0:
            return self.actions({'skill': skill1,
                                 'cost': skillPrice1,
                                 'items for sale': items})
        elif selectionIndex == 1:
            return self.actions({'skill': skill2,
                                 'cost': skillPrice2,
                                 'items for sale': items})
        elif selectionIndex == 2:
            return self.actions({'skill': skill3,
                                 'cost': skillPrice3,
                                 'items for sale': items})
        elif selectionIndex == 3:
            X = 4
            Y = 1
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        elif "Drumbol" not in self.c.flags:
            if self.c.mode == "Ultimate":
                self.text = (npc+": My! Your form, it is magnificent! Please, let me demonstrate my smoulder! It may pass your muster! By the way, I'm Drumbol.")
            else:
                self.text = (npc+": I am the renowned Drumbol the smoulderer. According to the dictionary, that means I am handsome and also darkly passionate. I'm getting a little old for that nonsense. However, I am darkly passionate about magic. I can teach you to smoulder, too.")
            self.c.flags['Drumbol'] = True
        else:
            self.text = npc+": "+choice(
                ["Back in my heyday, I would cast dastardly storms and ice spells with ease.",
                 "Have you come across any lightning magic? No? I'm stunned. Colour me shocked.",
                 "Alakazam!"])
        return self.actions({'items for sale': items})

    def yogi(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        npc = "Master Chi"
        skill1 = "Restore"
        skill2 = "Reinvigorate"
        skill3 = "Revitalize"
        skillPrice1 = 1000 if self.c.mode != "Ultimate" else 0
        skillPrice2 = 5000 if self.c.mode != "Ultimate" else 0
        skillPrice3 = 25000 if self.c.mode != "Ultimate" else 0
        self.menu = ["Learn %s (%s euros)." % (skill1, skillPrice1),
                     "Learn %s (%s euros)." % (skill2, skillPrice2),
                     "Learn %s (%s euros)." % (skill3, skillPrice3),
                     "Leave."]
        if selectionIndex == 0:
            return self.actions({'skill': skill1,
                                 'cost': skillPrice1})
        elif selectionIndex == 1:
            return self.actions({'skill': skill2,
                                 'cost': skillPrice2})
        elif selectionIndex == 2:
            return self.actions({'skill': skill3,
                                 'cost': skillPrice3})
        elif selectionIndex == 3:
            X = 4
            Y = 1
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})
        elif "Master Chi" not in self.c.flags:
            if self.c.mode == "Ultimate":
                self.text = ("%s: I have seen you in my dream. " % npc +
                             "Let us connect our souls.")
            else:
                self.text = ("%s: Welcome. I am %s, the yogi. "  % (npc, npc) +
                             "Come, and be one with the soul.")
            self.c.flags['Master Chi'] = True
        else:
            self.text = npc+": "+choice(
                ["Ommmmmm.",
                 "Relax. Smiling increase the length of life.",
                 "Get money. Get learn. Get soul."])
        return self.actions()

    def mercenary(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.tempFlag = None
        self.menu = []        
        if 'Qendresa' not in self.c.flags:
            npc = "Woman"
        else:
            npc = "Qendresa"
            
        if 'Qendresa Crest' in self.c.flags:
            self.imageIndex = 10
            
        if 'About to Leave' in self.c.flags and selectionIndex == 0:
            del self.c.flags['About to Leave']
            X = 5
            Y = 1
            return self.actions({'area': "Pec",
                                 'coordinates': (X, Y)})

        elif ('Qendresa Crest' in self.c.flags and
              'Qendresa' not in self.c.flags and selectionIndex == None):
            self.text = ("%s: Will you join me?" % npc)
            self.menu = ["Join forces.",
                         "Decline."]
                    
        elif 'Qendresa Story' not in self.c.flags and selectionIndex == None:
            self.text = ("%s: Warrior, what brings you to my home?" % npc +
                         "\n%s: Uh, oops. I thought I could just walk in." % self.c.NAME +
                         "\n%s: No, I am curious." % npc +
                         " Is there a reason you came?")
            self.menu = ["\"No, why?\"",
                         "\"Yes, I am looking for the president.\""
                         ]
            
        elif ('Qendresa Intro' not in self.c.flags and selectionIndex == 0 and
              'Qendresa No' not in self.c.flags):
            self.c.flags['New Song'] = "Buddha"
            self.text = ("%s: No, why?" % self.c.NAME +
                         "\n%s: I come from a family of great fighters:" % npc +
                         " the Osekus."+
                         " My family defended Albania for eons. That was"+
                         " until the day a massive storm left the land in"+
                         " desolation. Almost the entire population was"+
                         " wiped out. Those left behind were subject to"+
                         " torture by the evil Italian president, who took"+
                         " control of Albania. This happened over two decades"+
                         " ago and Albania is mostly inhabited by Romadans"+
                         " now, but the Italian government is still looking"+
                         " for me, the last link in the Oseku family. I"+
                         " cannot go anywhere without equipment."+
                         " Warrior, do you think you could help me get back"+
                         " on my feet?")
            self.menu = ["Help the woman.",
                         "Decline to help."]
            self.tempFlag = "Qendresa Intro"
            
        elif ('Qendresa Intro' not in self.c.flags and selectionIndex == 1 and
              'Qendresa No' not in self.c.flags):
            self.text = ("%s: Yes, I'm looking for the president of" % self.c.NAME+
                         " Macedonia."+
                         "\n%s: Sorry, I do not know anything about" % npc +
                         " that.")
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]

        elif 'Qendresa Story' not in self.c.flags and selectionIndex == 0:
            if 'Qendresa No' in self.c.flags:
                del self.c.flags['Qendresa No']
                self.text = ("%s: Fine. What do you need?" % self.c.NAME)
            else:
                self.text = ("%s: Sure. What do you need?" % self.c.NAME)
            self.text += ("\n%s: I first need a weapon." % npc +
                          " If you could"+
                          " somehow obtain an Espadon, I shall be able to"+
                          " sunder aggressive beasts blocking my way home.")
            self.c.flags['Qendresa Intro'] = True
            self.c.flags['Qendresa Story'] = True
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]
            
        elif ('Qendresa Story' not in self.c.flags and selectionIndex == 1 and
              'Qendresa No' not in self.c.flags):
            del self.c.flags['Qendresa Intro']
            self.text = ("%s: No, sorry." % self.c.NAME+
                         "\n%s: Please, I need your help. I need to" % npc +
                         " return home.")
            self.menu = ["Help the woman.",
                         "Refuse to help."]
            self.tempFlag = "Qendresa No"

        elif ('Qendresa Story' not in self.c.flags and selectionIndex == 1 and
              'Qendresa No' in self.c.flags):
            del self.c.flags['Qendresa No']
            self.text = ("%s: No, I'm not helping you." % self.c.NAME)
            if not self.c.isFemale:
                self.text += (
                         "\n%s: Some warrior you are!" % npc +
                         "\nYou receive a slap across the face, "+
                         "dealing 15 damage.")
                self.c.hp -= 15
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]

        elif ('Qendresa Espadon' not in self.c.flags and
              self.c.hasItem("Espadon") and
              not self.c.itemIsEquipped("Espadon")):
            self.c.removeItem(self.c.indexOfItem("Espadon"))
            self.text = ("%s: Thank you." % npc +
                         " I will need some protection as well. I would"+
                         " be grateful if you could find a Steel Cuirass"+
                         " for me.")
            self.c.flags['Qendresa Espadon'] = True
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]

        elif ('Qendresa Espadon' not in self.c.flags):
            self.text = ("%s: Warrior, please bring me an Espadon." % npc)
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]

        elif ('Qendresa Cuirass' not in self.c.flags and
              self.c.hasItem("Steel Cuirass") and
              not self.c.itemIsEquipped("Steel Cuirass")):
            self.c.removeItem(self.c.indexOfItem("Steel Cuirass"))
            self.text = ("%s: Great. I am beginning to feel like" % npc+
                         " an Oseku."+
                         " The final piece of equipment I am missing is"+
                         " my family's crest: the Oseku Shield. It was"+
                         " lost in Albania after the storm. I have faith"+
                         " in you, warrior. You must find it.")
            self.c.flags['Qendresa Cuirass'] = True
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]

        elif ('Qendresa Cuirass' not in self.c.flags):
            self.text = ("%s: Can you get me a Steel Cuirass?" % npc)
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]

        elif ('Qendresa Crest' not in self.c.flags and
              self.c.hasItem("Oseku Shield") and
              not self.c.itemIsEquipped("Oseku Shield")):
            self.imageIndex = 10
            self.c.removeItem(self.c.indexOfItem("Oseku Shield"))
            self.text = ("%s: The Oseku Shield! My set of equipment is" % npc+
                         " complete! Now I may take back what is mine and"+
                         " the good people's of Albania! I shall teach that"+
                         " tyrant a lesson! Alas, I have no companion with"+
                         " whom to adventure...warrior, I would be"+
                         " honoured to have you accompany me on my journey."+
                         " We would form a great team.")
            self.c.flags['Qendresa Crest'] = True
            self.menu = ["Join forces.",
                         "Decline."]

        elif ('Qendresa Crest' not in self.c.flags):
            self.text = ("%s: Please, warrior. My family crest means" % npc+
                         " everything to me."+
                         "\n%s: I'll find it. Don't worry." % self.c.NAME)
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]

        elif ('Qendresa' not in self.c.flags and selectionIndex == 0):
            self.text = ("%s: I might as well after all that work." % self.c.NAME+
                         "\n%s: To Albania!" % npc+
                         "\n%s: I don't even know your name yet." % self.c.NAME)
            npc = "Qendresa"
            self.text += ("\n%s: My name is Qendresa. What is yours?" % npc+
                          "\n{0}: I'm {0}.".format(self.c.NAME)+
                          "\n%s: %s, lead me to the Italian" % (npc, self.c.NAME)+
                          " president."+
                          "\n%s: Ok, ok already." % self.c.NAME+
                          "\n%s joins your team." % npc)
            self.c.flags['Qendresa'] = True
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]
            return self.actions({'mercenary': "Qendresa"})

        elif ('Qendresa' not in self.c.flags and selectionIndex == 1):
            self.text = ("%s: No, thanks." % self.c.NAME+
                         "\n%s: Come back when you change your mind," % npc+
                         " warrior.")
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]

        elif ('Qendresa' in self.c.flags):
            self.imageIndex = 11
            self.text = ("%s: We shall take a quick rest then" % npc+
                         " continue our quest."+
                         "\n%s: " % self.c.NAME+
                         choice(["We shall.",
                                 "Can't we stay a little longer? I'm tired.",
                                 "You don't even have a bed. How do you sleep?",
                                 "I'm so hungry.",
                                 "Don't you ever pee?" + (" I mean, I can go in a bush, but you..." if self.c.isFemale else "")])
                         )
            if self.c.hasMercenary("Barrie"):
                self.text += ("\n%s: " % "Barrie" +
                              choice(
                                  ["I'm ready to kick some tail!",
                                   "Onward!",
                                   "Let me just scratch this itch. Aah...",
                                   "I'm good. Let's roll!",
                                   "Don't worry, fighters, I brought" +
                                   " honey, too!"])
                              )
            for merc in self.c.mercenaries:
                merc.hp = merc.maxHp
            self.tempFlag = "About to Leave"
            self.menu = ["Leave."]
            
        return self.actions()
