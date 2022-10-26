"""
File: TUABoat.py
Author: Ben Gardner
Created: March 2, 2013
Revised: October 25, 2022
"""


class Boat:
    
    name = "Boat at Sea"
    audio = "Across the River"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"
        
        nrl1 = self.normal1
        nml2 = self.normal2
        self.spots = [[None, None, None, None, None],
                      [None, nrl1, None, nml2, None],
                      [None, None, None, None, None]]

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

    def normal1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []        
        if "Boat Awakening" not in self.c.flags:
            self.imageIndex = 0
            if "Boat Recovery" not in self.c.flags:
                self.c.hp += self.c.flags['Swimming HP Loss']+50
                del self.c.flags['Swimming HP Loss']
                self.c.flags['Boat Recovery'] = True
            self.text = ("About to pass out, you feel a hand tugging on "+
                         "your arm. You are pulled upwards and air enters "+
                         "your nostrils. You land on something solid with a "+
                         "thud.\n")
            self.menu = ["Open your eyes."]
            self.tempFlag = "Boat Awakening"
            
        elif "Boat Chat 1" not in self.c.flags:
            self.text = ("As you come to your senses you realize there are "+
                         "two grungy faces staring down at you."+
                         "\nMan: He looks tired, Bert."+
                         "\nBert: Hey, guy, what were you doing down there?"+
                         "\nMan: Maybe he went fishing and fell in.")
            self.menu = ["\"I fell in.\"",
                         "\"My ship exploded.\""]
            self.tempFlag = "Boat Chat 1"
            
        elif "Boat Chat 2" not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            self.text = ""
            if selectionIndex == 0:
                self.text = ("Toshe: Yeah, I fucking fell in."+
                             "\nMan: Ah, he's a funny one. He has a sense of "+
                             "humour."+
                             "\nBert: Sounds kind of pissed to me, Heinz.\n")
            elif selectionIndex == 1:
                self.text = ("Toshe: My ship exploded."+
                             "\nMan: Seriously? That's a lot crazier than "+
                             "fishing and falling in."+
                             "\nBert: I don't know, Heinz. You'd have to be "+
                             "pretty crazy to go fishing in these waters.\n")
            self.text += ("Heinz: Speaking of which, it looks like we have an "+
                          "angry visitor crawling up the back."
                          "\nBert: Something must be crawling up my back "+
                          "because I'm just itching for a fight! Heads up!"+
                          "\nToshe: Wait, do I have time to take a shit?")
            self.menu = ["Brace yourself."]
            self.tempFlag = "Boat Chat 2"

        elif "Boat Encounter" not in self.c.flags:
            self.view = "battle"
            self.c.flags['Boat Encounter'] = True
            return self.actions({'enemy': "Venomvice the Blind",
                                 'mercenaries': ["Heinz", "Bert"]})

        elif "Boat Chat 3" not in self.c.flags:
            self.text = ("Bert: Heinz, are you alright?"+
                         "\nHeinz: Yeah, that spider knocked me around a "+
                         "bit but I'm feeling fine. You?"+
                         "\nBert: Ha ha, yes, I feel alive. That was the "+
                         "biggest one yet! How do you feel, guy?"+
                         "\nToshe: I feel, um, relieved."+
                         "\nHeinz: Here, this might help you. It removes "+
                         "venom."+
                         "\nYou receive an antidote kit!"+
                         "\nBert: I never asked, what's your name, guy?")
            self.menu = ["\"Toshe.\""]
            self.tempFlag = "Boat Chat 3"

        elif "Boat Chat 4" not in self.c.flags:
            self.text = ("Toshe: My name is Toshe."+
                         "\nHeinz: Hey, we could use a fighter like you, "+
                         "Toshe. You're pretty skilled with your fists."+
                         "\nBert: Yeah, I bet he's even better with a weapon! "+
                         "Heinz, pass him that little knife beside you."+
                         "\nHeinz: No!"+
                         "\nBert: Huh? Why not?"+
                         "\nHeinz: Th-then what will I use...?"+
                         "\nBert: Oh. It looks like we're in short supply."+
                         "\nBert bends down and rips something off the boat."+
                         "\nBert: Here, take this stick...!")
            self.menu = ["Take the stick.", "Decline offer."]
            self.tempFlag = "Boat Chat 4"

        elif "Boat Chat 5" not in self.c.flags:
            self.text = ""
            if selectionIndex == 0:
                self.text = ("You receive a stick!\n")
                self.helpText = ("Click on the armour to access your "+
                                 "inventory, where you can equip your stick."+
                                 "\nClick on the circular arrow to return to "+
                                 "the game.")
            if selectionIndex == 1:
                self.text = ("Bert: Suit yourself.\n")
            self.text += ("Heinz: Toshe, we kind of got lost out here "+
                          "and we don't know where we're going at all. So "+
                          "keep an eye out for help, because we won't last "+
                          "long with what little supplies we have left."+
                          "\nBert: Take a rest for now, though. You need the "+
                          "energy. We'll keep watch on the boat.")
            self.menu = ["Rest."]
            self.tempFlag = "Boat Chat 5"
            if selectionIndex == 0:
                if "Boat Stick" not in self.c.flags:
                    self.c.flags['Boat Stick'] = True
                    return self.actions({'item': "Stick"})

        elif "Boat Chat 6" not in self.c.flags:
            self.c.hp = self.c.maxHp
            self.text = ("You rest for a while, feeling refreshed "+
                         "afterwards."+
                         "\nHeinz: Hey, Toshe! Look over there!"+
                         "\nYou look far into the distance and see a "+
                         "ship."+
                         "\nHeinz: We need you to keep watch while we "+
                         "row. Any crazy monsters that try to come up--"+
                         "you just whack them back down, ok?"+
                         "\nBert: My guess is that we will be there in ten "+
                         "more hours."+
                         "\nHeinz: If you need a break from guarding the "+
                         "boat, take two quick rests, but no more than "+
                         "that. We can't afford to stop now. Got it?")
            self.menu = ["\"Yes.\"", "\"Repeat that.\""]
            self.tempFlag = "Boat Chat 6"
            
        elif selectionIndex == 1:
            self.text = ("Toshe: Say that again?"+
                         "\nHeinz: We're giving you guard duty. Ten hours "+
                         "and we'll reach that ship, but you can only "+
                         "rest twice, max."+
                         "\nBert: First-aid kit is over there if you need "+
                         "it.")
            self.menu = ["\"Ok.\"", "\"Repeat that.\""]
            del self.c.flags['Boat Chat 6']
            self.tempFlag = "Boat Chat 6"
                
        else:
            X = 3
            Y = 1
            return self.actions({'area': "Boat at Sea",
                                 'coordinates': (X, Y)})
        
        return self.actions()
            

    def normal2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Boat Rests' not in self.c.flags:
            self.c.flags['Boat Rests'] = 2
        if 'Boat Hours' not in self.c.flags:
            self.c.flags['Boat Hours'] = 10
        elif self.c.flags['Boat Hours'] <= 5:
            self.imageIndex = 2
        if 'Boat Chat Done' not in self.c.flags:
            self.text = ("Toshe: Got it.")
            self.c.flags['Boat Chat Done'] = True
        elif 'Boat Chat Done' in self.c.flags:
            if selectionIndex == 0:
                self.view = "battle"
                self.c.flags['Boat Hours'] -= 1
                self.text = ("You guard the boat while Heinz and Bert row."+
                             "\nThe boat begins to shake!")
                return self.actions({'enemies':
                                     {'Water Spider': 20,
                                      'Small Jellyfish': 20,
                                      'Sea Goblin': 20,
                                      'Crab': 20,
                                      'Blood Carp': 20
                                      }
                                     })
            elif selectionIndex == 1:
                self.c.hp = self.c.maxHp
                self.c.flags['Boat Rests'] -= 1
                self.text = ("You rest for a while, feeling refreshed "+
                             "afterwards.")
            else:
                if self.c.flags['Boat Hours'] == 1:
                    self.text = ("Bert: "+str(self.c.flags['Boat Hours'])+
                             " hour 'til we're there!")
                elif self.c.flags['Boat Hours'] == 0:
                    X = 1
                    Y = 3
                    return self.actions({'area': "Kismet II",
                                         'coordinates': (X, Y)})
                else:
                    self.text = ("Bert: "+str(self.c.flags['Boat Hours'])+
                             " hours 'til we're there!")
        if self.c.flags['Boat Rests'] > 0:
            self.menu = ["Protect the Boat.", "Rest."]
        else:
            self.menu = ["Protect the Boat."]
        return self.actions()
