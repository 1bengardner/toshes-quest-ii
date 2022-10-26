"""
File: TUATheWatchmakingFacility.py
Author: Ben Gardner
Created: August 24, 2013
Revised: October 26, 2022
"""


from random import randint


class TheWatchmakingFacility:

    name = "The Watchmaking Facility"
    audio = "Burning"

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
        sdeL = self.sideLeft
        sdeR = self.sideRight
        frkL = self.forkLeft
        frkR = self.forkRight
        left = self.left
        rght = self.right
        smkL = self.smokeLeft
        smkR = self.smokeRight
        endL = self.endLeft
        endR = self.endRight
        boss = self.boss
        
        self.spots = [[None, None, None, None, None, None, None, None],
                      [None, None, endL, None, endR, None, boss, None],
                      [None, None, smkL, None, smkR, None, None, None],
                      [None, left, frkL, None, frkR, rght, None, None],
                      [None, None, sdeL, entr, sdeR, None, None, None],
                      [None, None, None, None, None, None, None, None]]

        e = {'Flaming Skeleton': 20,
             'Fire Sorceress': 15,
             'Fire Enchantress': 15}

        self.encounters = {entr: {},
                           sdeL: e,
                           sdeR: e,
                           frkL: e,
                           frkR: e,
                           left: e,
                           rght: e,
                           smkL: e,
                           smkR: e,
                           endL: e,
                           endR: e,
                           boss: {}}

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
        self.text = None
        self.helpText = None
        if selectionIndex == 0:
            X = 6
            Y = 1
            return self.actions({'area': "Mojkovac Summit",
                                 'coordinates': (X, Y)})
        if "The Watchmaking Facility" not in self.c.flags:
            self.text = ("Toshe: Looks like the way forward is blocked."+
                         "\nDragan: Go another way. I can take the heat.")
        self.menu = ["Leave."]
        return self.actions()

    def sideLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if "The Watchmaking Facility" not in self.c.flags:
            self.text = ("Toshe: It really is hot in here!")
            self.c.flags['The Watchmaking Facility'] = True
        return self.actions()

    def sideRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if "The Watchmaking Facility" not in self.c.flags:
            self.text = ("Toshe: It really is hot in here!")
            self.c.flags['The Watchmaking Facility'] = True
        return self.actions()

    def forkLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if ("The Watchmaking Facility Complete" not in self.c.flags and
            "The Watchmaking Facility Wrong Way" not in self.c.flags):
            self.text = ("Dragan: I feel like this is the wrong way.")
            self.c.flags['The Watchmaking Facility Wrong Way'] = True
        return self.actions()

    def forkRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def left(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        if "The Watchmaking Facility Complete" not in self.c.flags:
            self.text = ("Toshe: Dead end.")
        return self.actions()

    def right(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if "The Watchmaking Facility Complete" not in self.c.flags:
            self.text = ("Toshe: Dead end.")
        return self.actions()

    def smokeLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def smokeRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        if "The Watchmaking Facility Complete" not in self.c.flags:
            self.text = ("You feel the heat intensifying.")
        return self.actions()

    def endLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if "The Watchmaking Facility Complete" not in self.c.flags:
            self.text = ("Dragan: He is not here! We must try another route!")
        return self.actions()

    def endRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if "The Watchmaking Facility Complete" not in self.c.flags:
            X = 6
            Y = 1
            return self.actions({'area': "The Watchmaking Facility",
                                 'coordinates': (X, Y)})
        elif "Ghost of Tomas" not in self.c.flags and 'Radoman' in self.c.flags:
            self.text = ("Toshe: That was weird, what Maximilian said about the "+
                         "archmages. Maybe I should talk to the mayor of "+
                         "Igalo about it.")
        return self.actions()

    def boss(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if "Pespozeor 1" not in self.c.flags:
            self.text = ("Dragan: Toshe...what is that?"+
                         "\nYou see a gigantic beast lying in the corner of "+
                         "the room. It looks heavily wounded."+
                         "\nToshe: I don't know. But it's in the way. We "+
                         "need to get rid of that."+
                         "\nYou prepare to strike."+
                         "\nDragan: Toshe, wait."+
                         "\nA man who looks to be a conjurer emerges "+
                         "from the flames."+
                         "\nMan: Intruders?")
            self.menu = ["\"Intruders?!\"",
                         "\"Yes?\""]
            self.tempFlag = "Pespozeor 1"

        elif "Pespozeor 2" not in self.c.flags:
            self.text = ""
            if selectionIndex == 0:
                self.text = ("Toshe: Intruders?! Who are you? What do you "+
                             "think you're doing here?\n")
            elif selectionIndex == 1:
                self.text = ("Toshe: Yes?\n")
            self.text += ("Man: You're not supposed to be here.")
            self.menu = ["\"Says who?\"",
                         "\"Why not?\"",
                         "\"I'm sorry.\""]
            self.tempFlag = "Pespozeor 2"

        elif "Pespozeor 3" not in self.c.flags:
            self.text = ""
            self.menu = []
            if selectionIndex == 0:
                self.text = ("Toshe: Says who?"+
                             "\nMaximilian: Says I, Maximilian. This "+
                             "is now my domain. You are my slaves. And "+
                             "things are going quite smoothly. In fact, "+
                             "I could stand to--fire...a few of you "+
                             "right now.")
                self.menu = ["\"Yeah? Try me.\""]
            elif selectionIndex == 1:
                self.text = ("Toshe: Why not?"+
                             "\nMaximilian: Oh, are you not aware that "+
                             "this building is currently on fire? That "+
                             "fact aside, I, Maximilian, maintain "+
                             "the right to blow you both to smithereens "+
                             "before you have the chance to say another "+
                             "word.")
                self.menu = ["\"Yeah? Here's one.\""]
            elif selectionIndex == 2:
                self.text = ("Toshe: I'm sorry."+
                             "\nMaximilian: No need to apologize. Let "+
                             "Maximilian "+
                             "help you forget about this entire "+
                             "instance by burning the two of you to ashes.")
                self.menu = ["\"Yeah, right.\""]
            self.menu += ["\"You sound like a pretentious asswipe.\"",
                          "\"Not in a Maximilian years.\"",
                          "\"Can't we talk this out?\""]
            self.tempFlag = "Pespozeor 3"

        elif "Pespozeor 4" not in self.c.flags:
            self.text = ""
            if selectionIndex in (0, 1):
                self.text = ("Toshe: Y--")
            elif selectionIndex == 2:
                self.text = ("Toshe: N--")
            if selectionIndex in (0, 1, 2):
                self.text += ("\nMaximilian: Listen, you cheeky "+
                              "curmudgeon. Before I give you the chance to "+
                              "embarrass yourself again, I should have you "+
                              "know that there isn't one chance in hell "+
                              "that you, or any of your knightly friends, "+
                              "could possibly \"rescue\" the archmages "+
                              "of Igalo now. They all work for Niplin now "+
                              "and they love it. "+
                              "And, now, all four of his guardian beasts "+
                              "are summoned--one of them in the corner of "+
                              "this room. There's nothing you can do.")
            if selectionIndex == 3:
                self.text = ("Toshe: Can't we talk this out?"+
                             "\nMaximilian: There's nothing that can be "+
                             "done now. The archmages of Igalo are a lost "+
                             "cause. Now that I have summoned all four "+
                             "guardian beasts, Niplin will begin his "+
                             "reign. The archmages have converted to "+
                             "darkness and there's no going back.")
            self.menu = ["\"What?\"",
                         "\"I think you've got the wrong guy.\""]
            self.tempFlag = "Pespozeor 4"

        elif "Pespozeor 5" not in self.c.flags:
            self.text = ""
            if selectionIndex == 0:
                self.text = ("Toshe: What? I don't care about your sick "+
                             "satanic ritual. I just want to find the "+
                             "owner of this facility, dammit!"+
                             "\nDragan: Yes, my father was left here and "+
                             "we must save him!\n")
            elif selectionIndex == 1:
                self.text = ("Toshe: Um, I think you have the wrong guy.\n")
            self.text += ("Maximilian: Hmm...you mean to say you weren't "+
                          "sent here on a mission to rescue the archmages "+
                          "from impending doom?")
            self.menu = ["\"Nope.\"",
                         "\"Actually, yes, we were.\""]
            self.tempFlag = "Pespozeor 5"

        elif "Pespozeor 6" not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            self.text = ""
            if selectionIndex == 0:
                self.text = ("Toshe: Nope.\n")
            elif selectionIndex == 1:
                self.text = ("Toshe: Wait...yeah, actually, that was us."+
                             "\nDragan: Is this true?\n")
            self.text += ("Maximilian: Why should I believe you? Either "+
                         "way, the course of action is congruent. "+
                         "Pespozeor!"+
                         "\nPespozeor: Graaagh!!"+
                         "\nDragan: Have at thee!"+
                         "\nToshe: Oh fuck.")
            self.menu = ["Face Pespozeor."]
            self.tempFlag = "Pespozeor 6"

        elif "Pespozeor Encounter" not in self.c.flags:
            self.view = "battle"
            self.c.flags['Pespozeor Encounter'] = True
            return self.actions({'enemy': "Pespozeor",
                                 'mercenaries': self.c.mercenaries})

        elif "Maximilian" not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            self.text = ("Toshe: We're unstoppable!"+
                         "\nDragan: Now leave us!"+
                         "\nMaximilian: I suppose you leave me no other "+
                         "option."+
                         "\nMaximilian reveals a flaming wand and shield."+
                         "\nMaximilian: I must kill you, myself. How quaint."+
                         "\nToshe: No water break?")
            self.menu = ["Brace yourself."]
            self.tempFlag = "Maximilian"

        elif "Maximilian Encounter" not in self.c.flags:
            self.view = "battle"
            self.c.flags['Maximilian Encounter'] = True
            return self.actions({'enemy': "Maximilian",
                                 'mercenaries': self.c.mercenaries})

        elif "Dragan's Dad 1" not in self.c.flags:
            self.text = ("Toshe: Don't fuck with me."+
                         "\nYou notice Dragan is looking off into the "+
                         "distance."+
                         "\nDragan: Is...it's not true. N-no!"+
                         "\nDragan's eyes begin to well up.")
            self.menu = ["Find out what Dragan is looking at."]
            self.tempFlag = "Dragan's Dad 1"

        elif "Dragan's Dad 2" not in self.c.flags:
            self.text = ("You peer beyond Pespozeor's corpse to spot the "+
                         "body of an old man."+
                         "\nToshe: Oh, no. That's..."+
                         "\nDragan: My father is--my father...is..."+
                         "\nYou both stand silently with only the "+
                         "crackling of the flames entering your ears."+
                         "\nDragan: This menace...this monster..."+
                         "\nDragan swings his blade toward the head of "+
                         "Maximilian's corpse.")
            self.menu = ["Suggest leaving.",
                         "Wait for Dragan."]
            self.tempFlag = "Dragan's Dad 2"

        elif "Dragan's Dad 3" not in self.c.flags:
            self.menu = ["Suggest leaving.",
                         "Wait for Dragan."]
            if selectionIndex == 0:
                self.text = ("Toshe: We should get out of here, man. This place "+
                             "is burning down. We can take your dad, too."+
                             "\nDragan: I cannot bear to see him in this state. "+
                             "Please, take him to the cemetery. Give him a proper "+
                             "burial.")
                self.menu = ["Agree.",
                             "Disagree."]
                self.tempFlag = "Dragan's Dad 3"
            elif selectionIndex == 1:
                self.text = ("You wait while Dragan lets out his anger. ")
                if randint(0, 1) == 0:
                    self.c.hp -= 10
                    self.text += ("Debris from the collapsing building hits "+
                                  "you, dealing 10 damage.")
                else:
                    self.c.hp += 10
                    self.text += ("You regain 10 HP.")

        elif "The Watchmaking Facility Complete" not in self.c.flags:
            if selectionIndex == 0:
                self.text = ("Toshe: Ok.")
            if selectionIndex == 1:
                self.text = ("Toshe: I can't."+
                             "\nDragan: No, you must. Please go.")
            self.menu = ["Take the body."]
            self.tempFlag = "The Watchmaking Facility Complete"
            del self.c.mercenaries[0]

        else:
            X = 4
            Y = 1
            return self.actions({'area': "The Watchmaking Facility",
                                 'coordinates': (X, Y)})
        
        return self.actions()
