"""
File: TUAMojkovacValley.py
Author: Ben Gardner
Created: August 18, 2013
Revised: November 24, 2022
"""


from random import choice


class MojkovacValley:

    name = "Mojkovac Valley"
    audio = "The Olden Days"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.summit1
        wrp2 = self.summit2
        wrp3 = self.summit3
        wrp4 = self.summit4
        entr = self.entrance
        cntr = self.center
        left = self.left
        rght = self.right
        hous = self.house
        tvrn = self.tavern
        bedr = self.bedroom
        smth = self.smith
        clth = self.clothier
        merc = self.mercenary
        
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, wrp2, None, None, tvrn, None, merc, None],
            [None, left, hous, cntr, rght, None, None, None, None, None],
            [None, None, wrp1, entr, wrp3, None, clth, None, bedr, None],
            [None, None, None, wrp4, None, None, smth, None, None, None],
            [None, None, None, None, None, None, None, None, None, None]]

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

    def summit1(self, selectionIndex=None):
        X = 4
        Y = 6
        return self.actions({'area': "Mojkovac Summit",
                             'coordinates': (X, Y)})

    def summit2(self, selectionIndex=None):
        X = 6
        Y = 3
        return self.actions({'area': "Mojkovac Summit",
                             'coordinates': (X, Y)})

    def summit3(self, selectionIndex=None):
        X = 8
        Y = 6
        return self.actions({'area': "Mojkovac Summit",
                             'coordinates': (X, Y)})

    def summit4(self, selectionIndex=None):
        X = 6
        Y = 9
        return self.actions({'area': "Mojkovac Summit",
                             'coordinates': (X, Y)})

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Ryfil the Kid"
        if selectionIndex == 0:
            self.c.flags['Rifled The Kid'] = True
            self.view = "battle"
            return self.actions({'enemy': "Ryfil the Kid"})
            
        if "Ryfil the Kid" in self.c.flags['Kills']:
            self.text = "You see Ryfil's dead body on the ground."
        elif self.c.equippedWeapon.CATEGORY == "Gun":
            if "Rifled The Kid" in self.c.flags:
                self.text = npc+": Don't shoot!"                
            else:
                self.text = npc+": I-is that a real gun?"
            self.menu = ["Aim at Ryfil."]
        elif "Ryfil the Kid" not in self.c.flags:
            self.text = (npc+": Hey, A'm Ryfil; Ry fa' sha't. But evrywan "+
                         "just calls me \"Ryfil the Kid\" fa' sam reasan. "+
                         "Prabably bacause A'm the anly kid in Makavass!")
            self.c.flags['Ryfil the Kid'] = True
        else:
            self.text = npc+": "+choice(
                ["That ald watchmakin' buildin' is ten times "+
                 "alder than me. And naw look!",
                 "If ya go turn back arand ya can see tomstans. Spooky.",
                 "Makavass was a big city befare. Evil villens took aver and "+
                 "naw it's just a valley.",
                 "It's nat safe to go atside the valley. There's green "+
                 "gablins and angry man-eatin' animals an the summit...and "+
                 "who knaws what's beyand?!",
                 "Hey, why ya keep callin' me Ryfil for? Just say \"Ry!\"",
                 "Speech impadimant? Are ya name-callin' me?"])
        return self.actions()

    def center(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if "Hot Air Balloon Price" in self.c.flags:
            self.c.euros -= self.c.flags['Hot Air Balloon Price']
            self.text = ("You pay the Hot Air Balloon Mafia "+
                         "%s " % (self.c.flags['Hot Air Balloon Price'])+
                         "euros and they fly you to Mojkovac Valley.")
            del self.c.flags['Hot Air Balloon Price']
        if selectionIndex == 0:
            X = 6
            Y = 1
            return self.actions({'area': "Mojkovac Valley",
                                 'coordinates': (X, Y)})
        self.menu = ["Enter the inn."]
        return self.actions()
    
    def left(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Mojkovac Valley Treasure' not in self.c.flags:
            self.text = ("You find a Dark Dagger!")
            self.c.flags['Mojkovac Valley Treasure'] = True
            return self.actions({'item': "Dark Dagger"})
        return self.actions()

    def right(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 6
            Y = 4
            return self.actions({'area': "Mojkovac Valley",
                                 'coordinates': (X, Y)})
        self.menu = ["Enter the blacksmith's."]
        return self.actions()

    def house(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 8
            Y = 1
            return self.actions({'area': "Mojkovac Valley",
                                 'coordinates': (X, Y)})
        if 'Dragan' not in self.c.flags:
            self.text = ("There is an inviting house up ahead. The doors are "+
                         "all open.")
            self.menu = ["Enter the house."]
        else:
            self.menu = ["Enter Dragan's house."]
        return self.actions()

    def tavern(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Bartender Adam"
        if selectionIndex == 0:
            self.text = (npc+": "+choice(
["Magical spells cut right through defences. The only way to defend against "+
 "them is with elemental resistances.",
 "Skills have various side-effects when used, which are removed after battle.",
 "Bows are not very accurate. You'll need to boost your dexterity to "+
 "compensate.",
 "Resistances are useful later in the game. Without them, enemies can easily "+
 "knock you out in one hit.",
 "Each defence point will reduce the damage you take by one.",
 "Every ten wisdom points nets you one percent to all resistances.",
 "Every point in dexterity will add one percent to your accuracy. You "+
 "will also get your base critical chance multiplied by one percent "+
 "and your block chance by five percent.",
 "Every point in strength will multiply your critical damage by an additional "+
 "one percent. This can really add up if you have a good critical damage base.",
 "If you are accompanied by other fighters, you can bring them into battle. "+
 "A man down will go unconscious until the end of the fight.",
 "I'm running out of tips--how about a drink? Try mixing one and a half "+
 "ounces of vodka with three-quarters of an ounce of coffee liquer. Add "+
 "some lemon juice and there you go, Black Magic."]
))
        elif selectionIndex == 1:
            if self.c.euros >= 5:
                self.c.euros -= 5
                self.text = (npc+": Enjoy.")
                if 'Adam Quest 1' not in self.c.flags:
                    self.text += ("..I do have a request for you, though. "+
                                  "You can kill orcs no problem, right? I "+
                                  "need a nice gift for my fiance and I think "+
                                  "a handcrafted orcskin jacket would do the "+
                                  "trick. Could you grab an orc skin for me?")
                    if 'Orc' in self.c.flags['Kills']:
                        self.c.flags['Adam Quest 1'] = \
                                            self.c.flags['Kills']['Orc']
                    else:
                        self.c.flags['Adam Quest 1'] = 0
                elif ('Adam Quest 1 Complete' not in self.c.flags and
                      'Adam Quest 1' in self.c.flags and
                      'Orc' in self.c.flags['Kills'] and
                      self.c.flags['Kills']['Orc']-1 >=
                      self.c.flags['Adam Quest 1']):
                    self.text += (" And thanks for your help."+
                                  "\nAdam gives you 30 euros.")
                    self.c.euros += 30
                    self.c.flags['Adam Quest 1 Complete'] = True
                elif ('Adam Quest 1 Complete' in self.c.flags and
                      'Adam Quest 2' not in self.c.flags):
                    self.text += ("..I have another request, though. "+
                                  "My fiance didn't appreciate the orcskin "+
                                  "jacket I made. But I know what would do "+
                                  "nicely: a goblinhide coat. Get me 5 "+
                                  "goblin hides. Any kind will do. Thanks.")
                    self.c.flags['Adam Quest 2'] = 0
                    if 'Goblin' in self.c.flags['Kills']:
                        self.c.flags['Adam Quest 2'] += \
                                             self.c.flags['Kills']['Goblin']
                    if 'Mountain Goblin' in self.c.flags['Kills']:
                        self.c.flags['Adam Quest 2'] += \
                                    self.c.flags['Kills']['Mountain Goblin']
                    if 'Goblin Ranger' in self.c.flags['Kills']:
                        self.c.flags['Adam Quest 2'] += \
                                    self.c.flags['Kills']['Goblin Ranger']
                    if 'Goblin Thug' in self.c.flags['Kills']:
                        self.c.flags['Adam Quest 2'] += \
                                    self.c.flags['Kills']['Goblin Thug']
                elif ('Adam Quest 2 Complete' not in self.c.flags and
                      'Adam Quest 2' in self.c.flags):
                    goblinKills = 0
                    if 'Goblin' in self.c.flags['Kills']:
                        goblinKills += self.c.flags['Kills']['Goblin']
                    if 'Mountain Goblin' in self.c.flags['Kills']:
                        goblinKills += self.c.flags['Kills']['Mountain Goblin']
                    if 'Goblin Ranger' in self.c.flags['Kills']:
                        goblinKills += self.c.flags['Kills']['Goblin Ranger']
                    if 'Goblin Thug' in self.c.flags['Kills']:
                        goblinKills += self.c.flags['Kills']['Goblin Thug']
                        
                    if goblinKills-5 >= self.c.flags['Adam Quest 2']:
                        self.text += (" You've done well."+
                                      "\nAdam gives you 60 euros.")
                        self.c.euros += 60
                        self.c.flags['Adam Quest 2 Complete'] = True
                elif ('Adam Quest 2 Complete' in self.c.flags and
                      'Adam Quest 3' not in self.c.flags):
                    self.text += ("..however I have one final request. "+
                                  "My fiance didn't like the coat as much as "+
                                  "I expected she would, so I've decided to "+
                                  "go with a plain seal coat. After all, "+
                                  "she does love animals. Fetch me 5 seal "+
                                  "furs.")
                    if 'Giant Seal1' in self.c.flags['Kills']:
                        self.c.flags['Adam Quest 3'] = \
                                            self.c.flags['Kills']['Giant Seal1']
                    else:
                        self.c.flags['Adam Quest 3'] = 0
                elif ('Adam Quest 3 Complete' not in self.c.flags and
                      'Adam Quest 3' in self.c.flags and
                      'Giant Seal1' in self.c.flags['Kills'] and
                      self.c.flags['Kills']['Giant Seal1']-5 >=
                      self.c.flags['Adam Quest 3']):
                    self.text += (" At last. I appreciate all your help."+
                                  "\nAdam gives you 200 euros.")
                    self.c.euros += 200
                    self.c.flags['Adam Quest 3 Complete'] = True
                elif 'Adam Quest 3 Complete' in self.c.flags:
                    self.text += (" As it turns out, my fiance broke up "+
                                  "with me. Not sure why. If you're looking "+
                                  "for more tasks, Dragan said he needed "+
                                  "assistance earlier. He should be in "+
                                  "the next house over.")
            else:
                self.text = (npc+": Doesn't look like you have enough there.")
        elif selectionIndex == 2:
            if (self.c.euros >= 15 or
                'Mojkovac Valley Room Level' in self.c.flags):
                X = 8
                Y = 3
                return self.actions({'area': "Mojkovac Valley",
                                     'coordinates': (X, Y)})
            else:
                self.text = (npc+": You need 15 euros for a room.")
        elif selectionIndex == 3:
            X = 3
            Y = 2
            return self.actions({'area': "Mojkovac Valley",
                                 'coordinates': (X, Y)})
        else:
            if 'Rested' in self.c.flags:
                self.text = ("You fall asleep."+
                             "\nWhen you wake up, you return to the front "+
                             "to give Adam your key."+
                             "\nBartender Adam: Feeling better?")
                del self.c.flags['Rested']
                del self.c.flags['Mojkovac Valley Room Level']
            elif ('Mojkovac Valley Room Level' in self.c.flags and
                  self.c.flags['Mojkovac Valley Room Level'] < self.c.level):
                self.text = (npc+": Where'd you go?"+
                             " I thought you ran off!"+
                             " Someone else took your room, so you'll need"+
                             " to pay again if you need a place to rest."+
                             " Sorry about that.")
                del self.c.flags['Mojkovac Valley Room Level']
            elif npc not in self.c.flags:
                self.text = (npc+": Welcome to Mojkovac! "+
                             "What would you like today?")
                self.c.flags[npc] = True
            else:
                self.text = (npc+": "+
                             choice(["Pretty dark in here, huh?",
                                     "Beautiful day out.",
                                     "I prefer my bowtie just slightly "+
                                     "off-center.",
                                     "For the last time, Ryfil isn't "+
                                     "allowed in here!",
                                     "Lots of goblins over the mountain today.",
                                     "We just got new pillows."]
                                    )
                             )
                self.text += (" What would you like today?")

        if 'Mojkovac Valley Room Level' in self.c.flags:
            self.menu = ["Ask for advice.",
                         "Buy a drink (5 euros).",
                         "Return to your room.",
                         "Leave."]
        else:
            self.menu = ["Ask for advice.",
                         "Buy a drink (5 euros).",
                         "Get a room (15 euros).",
                         "Leave."]
        return self.actions()
    
    def bedroom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Bartender Adam"
        if selectionIndex == 0:
            self.c.flags['Rested'] = True
            self.c.hp = self.c.maxHp
            self.c.ep = self.c.maxEp
            X = 6
            Y = 1
            return self.actions({'area': "Mojkovac Valley",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 6
            Y = 1
            return self.actions({'area': "Mojkovac Valley",
                                 'coordinates': (X, Y)})
        if 'Mojkovac Valley Room Level' not in self.c.flags:
            self.c.euros -= 15
            self.text = ("Adam takes you to a room. "+
                         "You give him 15 euros and he hands you a key.")
            self.c.flags['Mojkovac Valley Room Level'] = self.c.level
        else:
            self.text = ("You walk inside your room and lock the door.")
        self.menu = ["Sleep.",
                     "Leave your room."]
        return self.actions()

    def smith(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Blacksmith"
        if selectionIndex == 0:
            X = 4
            Y = 2
            return self.actions({'area': "Mojkovac Valley",
                                 'coordinates': (X, Y)})
        if 'Mojkovac Valley Blacksmith' not in self.c.flags:
            self.text = (npc+": Ah, a fresh face! My wife is in the back "+
                         "knitting if you need clothes.")
            self.c.flags['Mojkovac Valley Blacksmith'] = True
        elif ("Key Hunting" in self.c.flags and
              "Macedonian Gate Opened" not in self.c.flags):
            self.text = (npc+": A key, you say? I make weapons and" +
                         " armour, no keys.")
        else:
            self.text = npc+": "+choice(
                ["My steel won't let you down!",
                 "If it's metal, I can make it.",
                 "My quality is impeccable."])
        self.menu = ["Leave."]
        return self.actions({'items for sale': ["Flail",
                                                "Alder Bow",
                                                "Long Sword",
                                                "Flanged Mace",
                                                "Spear",
                                                "Espadon",
                                                "Great Axe",
                                                "Defender",
                                                "Enchanted Gauntlets"]})

    def clothier(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Granny Smith"
        if selectionIndex == 0:
            X = 4
            Y = 2
            return self.actions({'area': "Mojkovac Valley",
                                 'coordinates': (X, Y)})
        if 'Granny Smith' not in self.c.flags:
            self.text = (npc+": Hello, young man.")
            self.c.flags['Granny Smith'] = True
        else:
            self.text = npc+": "+choice(
                ["Oh, it's getting late.",
                 "Try this one on.",
                 "These colours would match perfectly.",
                 "Have a look at what I've made.",
                 "This gambeson is taking ages!",
                 "Nobody beats my embroidery work."])
        self.menu = ["Leave."]
        return self.actions({'items for sale': ["Canvas Gambeson",
                                                "Canvas Doublet",
                                                "Magerobe",
                                                "Brigandine",
                                                "Embroidered Cloths",
                                                "Dark Robe",
                                                "Velvet Doublet",
                                                "Leather Brigandine",
                                                "White Robe"]})

    def mercenary(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Dragan"
        self.menu = ["Leave."]
        if selectionIndex == 0 and 'Dragan' in self.c.flags:
            X = 2
            Y = 2
            return self.actions({'area': "Mojkovac Valley",
                                 'coordinates': (X, Y)})
        
        if 'Dragan' not in self.c.flags and selectionIndex == None:
            self.text = (npc+": Ah, a visitor. I am Dragan. "+
                         "What is your name?"+
                         "\nToshe: Toshe."+
                         "\n"+npc+": Toshe, I need your help. My father owns "+
                         "the abandoned watchmaking facility and swore to "+
                         "work until the day he died. This morning, the "+
                         "facility was set ablaze, and he is trapped in the "+
                         "flames. We do not have much time. You are the only "+
                         "other capable warrior in Mojkovac. We must go "+
                         "north and save my father.")
            self.menu = ["\"Ok.\"",
                         "\"No.\""]
        elif 'Dragan' not in self.c.flags and selectionIndex == 0:
            self.text = ("Toshe: Well, that doesn't give me much choice."+
                         "\n"+npc+" joins your team.")
            self.helpText = ("Your new party member will follow you on your "+
                             "journey and fight alongside you in battle.")
            self.c.flags['Dragan'] = True
            return self.actions({'mercenary': "Dragan"})
        elif 'Dragan' not in self.c.flags and selectionIndex == 1:
            self.text = ("Toshe: I'm not doing shit."+
                         "\n%s: Toshe, please think about this." % npc+
                         " My father is dying.")
            self.menu = ["\"Fine.\"",
                         "\"No.\""]
        elif "The Watchmaking Facility Complete" not in self.c.flags:
            self.text = (npc+": There is no time to waste.")
        elif "Ghost of Tomas" not in self.c.flags:
            self.imageIndex = 10
            self.text = ("You enter Dragan's house.")
        elif "Ghost of Tomas" in self.c.flags:
            self.imageIndex = 10
            self.text = ("You enter Dragan's house. "+
                         "It feels a little emptier now.")
        return self.actions()
