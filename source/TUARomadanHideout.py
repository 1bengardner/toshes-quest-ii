"""
File: TUARomadanHideout.py
Author: Ben Gardner
Created: July 12, 2015
Revised: June 11, 2023
"""


import random


class RomadanHideout:

    name = "Romadan Hideout"
    audio = "Magic Lamp"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        self.skillArrangementPhase = None

        entr = self.entrance

        self.spots = [
            [None, None, None],
            [None, entr, None],
            [None, None, None]]

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

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        if ("Qendresa Crest" in self.c.flags or
            self.c.hasItem("Oseku Shield")) and self.c.hasMercenary("Barrie"):
            self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Jazidhu"

        if "Hideout Kills" not in self.c.flags:
            self.c.flags['Hideout Kills'] = 0

        if self.skillArrangementPhase == 1:
            self.skillArrangementPhase = 2
            self.skillArrangementIndex = selectionIndex
            self.text = ("Goldum: Choose the second skill to be swapped.")
            self.menu = [skill.NAME for skill in self.c.skills]
        elif self.skillArrangementPhase == 2:
            self.skillArrangementPhase = None
            self.c.skills[self.skillArrangementIndex]\
            , self.c.skills[selectionIndex]\
            = self.c.skills[selectionIndex]\
            , self.c.skills[self.skillArrangementIndex]
            self.text = ("Goldum: Um...again?")
            self.menu = ["Leave.",
                         "Rearrange your skills."]
        elif selectionIndex == 0:
            X = 2
            Y = 3
            return self.actions({'area': "Romadan Village",
                                 'coordinates': (X, Y)})
        elif (selectionIndex == 1 and
              "Qendresa Crest" not in self.c.flags and
               not self.c.hasItem("Oseku Shield")):
            self.text = ("You take the Oseku Shield!")
            self.c.flags['Oseku Shield'] = True
            self.menu = ["Leave."]
            return self.actions({'item': "Oseku Shield"})
        elif (npc not in self.c.flags['Kills'] and
              self.c.flags['Hideout Kills'] < 3):
            self.view = "battle"
            enemy = random.choice([
                "Romadan Man Unfleeable",
                "Romadan Warrior Unfleeable",
                "Romadan Assassin Unfleeable",
                "Romadan Ruffian Unfleeable",
                "Romadan Disciple Unfleeable",
                "Romadan Guru Unfleeable"])
            self.c.flags['Hideout Kills'] += 1
            self.text = ("%s: %s" % (npc, random.choice([
                "Attack, my %s!" % enemy.replace(" Unfleeable", "").lower() +
                " Destroy %s!" % ("her" if self.c.isFemale else "him"),
                "It's time to end this nonsense. Get %s!" % ("her" if self.c.isFemale else "him"),
                "Remove that %s at once!" % ("woman" if self.c.isFemale else "man"),
                "Kill the intruder!"])))
            return self.actions({'enemy': enemy,
                                 'mercenaries': self.c.mercenaries})
        elif (npc not in self.c.flags['Kills'] and
              self.c.flags['Hideout Kills'] == 3):
            self.view = "battle"
            self.text = "%s: No! Stop! Stay back! The shield is mine!" % npc
            return self.actions({'enemy': npc,
                                 'mercenaries': self.c.mercenaries})
        elif "Oseku Shield" not in self.c.flags:
            self.text = ("Beside Jazidhu's corpse lies a large shield.")
            self.menu = ["Leave.",
                         "Pick up the shield."]
        elif ("Qendresa Crest" not in self.c.flags and
              not self.c.hasItem("Oseku Shield")):
            self.text = ("You see the Oseku Shield on the ground.")
            self.menu = ["Leave.",
                         "Pick up the shield."]            
        elif (selectionIndex == 1 and
              "Goldum Gold" not in self.c.flags):
            self.c.removeItem(self.c.indexOfItem("Gold Ore"))
            self.c.flags['Goldum Gold'] = True
            self.text = ("You place a piece of gold ore in Goldum's" +
                         " frail demon hands." +
                         "\nGoldum: Yes...please, leave me with" +
                         " gold...return later. Yes...")
            self.menu = ["Leave."]
        elif (selectionIndex == 1 and 
              "Goldum Gold" in self.c.flags):
            self.skillArrangementPhase = 1
            self.text = "Goldum: Choose a skill to swap with another."
            self.menu = [skill.NAME for skill in self.c.skills]
        elif "Goldum Gold" in self.c.flags:
            self.text = ""
            if "Goldum" not in self.c.flags:
                self.c.flags['Goldum'] = True
                self.text = ("Goldum: Yes...um...thank you.\n")
            self.text += ("Goldum: Let Goldum...um...change your perspective.")
            self.menu = ["Leave.",
                         "Rearrange your skills."]
        else:
            self.menu = ["Leave."]
            if "Met Goldum" not in self.c.flags:
                self.text = "%s: I sure made a mess of this place." % self.c.NAME
                if self.c.hasMercenary("Qendresa"):
                    self.text += ("\nQendresa: There was no place in Albania" +
                                  " for these vile men.")
            if self.c.hasMercenary("Barrie"):
                if "Met Goldum" in self.c.flags:
                    self.text = "You see Goldum cowering in the corner."
                else:
                    self.c.flags['Met Goldum'] = True
                    self.text += ("\nBarrie: Wait...who's that?" +
                                  "\nBarrie shines his staff on a cloaked" +
                                  " demon cowering in the corner. It" +
                                  " gasps and curls into a ball."
                                  "\n%s: Yeah, who are you?" % self.c.NAME)
                self.text += ("\nGoldum: Um...I am gold-um...please..." +
                              " give gold...um...ore...")
                if self.c.hasItem("Gold Ore"):
                    self.menu.append("Give Goldum gold ore.")
                else:
                    self.text += ("\n%s: Let me find some first." % self.c.NAME)
        return self.actions()
