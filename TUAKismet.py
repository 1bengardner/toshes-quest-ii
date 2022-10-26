"""
File: TUAKismet.py
Author: Ben Gardner
Created: May 5, 2013
Revised: October 26, 2022
"""

from random import choice


class Kismet:
    
    name = "Kismet II"
    audio = "Last Journey"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        outs = self.outside
        loby = self.lobby
        entr = self.entrance
        fbar = self.foodBar
        fbr2 = self.foodBar2
        barr = self.bar
        upst = self.upstairs
        dnst = self.downstairs
        bedr = self.bedroom
        abov = self.aboveFoodBar
        wrp1 = self.warp1
        wrp2 = self.warp2
        
        self.spots = [[None, None, None, None, None, None, None, None],
                      [None, loby, None, upst, bedr, abov, None, None],
                      [None, None, None, wrp2, None, None, None, None],
                      [None, outs, None, wrp1, None, fbr2, None, None],
                      [None, None, None, dnst, barr, fbar, entr, None],
                      [None, None, None, None, None, None, None, None]]

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

    def outside(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Kismet II",
                                 'coordinates': (X, Y)})
        self.text = ("You arrive at the side of a massive ship."+
                     "\nBert: Here we are."+
                     "\nHeinz: Hey! Hey!"+
                     "\nA man on deck turns around."+
                     "\nMan: Hello down there."+
                     "\nHeinz: Think you could help us out here?"+
                     "\nMan: Captain, sir, these men need our assistance."+
                     "\nCaptain: Let them on.")
        self.menu = ["Board the ship."]
        return self.actions()

    def lobby(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []

        if 'Kismet Chat 1' not in self.c.flags:
            self.text = ("Bert and Heinz follow you up a rope along the side "+
                         "of the ship. You set foot on the deck and the man leads "+
                         "you down two flights of stairs into the lobby."+
                         "\nMan: Welcome to the Kismet II! From which vessel do "+
                         "you hail?"+
                         "\nBert and Heinz look confused.")
            self.menu = ["\"I'm from the vessel that exploded.\""]
            self.tempFlag = "Kismet Chat 1"
            
        elif 'Kismet Chat 2' not in self.c.flags:
            self.text = ("Toshe: I'm from the ship that blew up."+
                         "\nMan: Oh, my! It's a wonder you all lived. Captain's "+
                         "orders state that all survivors are entitled to a free "+
                         "buffet at the food bar--"+
                         "\nBert and Heinz rush to the food bar."+
                         "\nMan: We have another passenger from your ship just "+
                         "in the next room. You might know him. Mat! Mat!"+
                         "\nMatsamot and a well-dressed Italian walk in.")
            self.menu = ["Greet Matsamot."]
            self.tempFlag = "Kismet Chat 2"
            
        elif 'Kismet Chat 3' not in self.c.flags:
            self.text = ("You wave at Matsamot."+
                         "\nMatsamot: Toshe, you're alive and well! Well, almost."+
                         "\nMan: Yes, good point. Let me get you a change of "+
                         "clothes."
                         "\nMatsamot: I go to take a nap and the next thing I "+
                         "know, there's this tremendous rumbling and the ship "+
                         "just explodes! I barely made it out in time. "+
                         "Luckily, Marciano here has connections with the Captain "+
                         "and was able to get me on the Kismet."
                         "\nMarciano: You were on Matsamot's ship?")
            self.menu = ["\"Yes.\"",
                         "\"No.\""]
            self.tempFlag = "Kismet Chat 3"
            
        elif 'Kismet Chat 4' not in self.c.flags:
            self.text = ""
            if selectionIndex == 0:
                self.text = ("Toshe: Yeah, I was.\n")
            elif selectionIndex == 1:
                self.text = ("Toshe: No, what happened?\n")
            self.text += ("Marciano: Bastards blew that thing up. "+
                          "I am done with these goddamn terrorists. "+
                          "I am trying to get as far away "+
                          "from Italy as possible. It is just horrible. It is "+
                          "nothing like it was five years ago. No monsters or "+
                          "beasts. I remember I could still go get a slice of "+
                          "pizza without being mugged by goblins. I would just get "+
                          "mugged by Rumadans."+
                          "\nMarciano seems to be on edge.")
            self.menu = ["Admit that it was all your brother's fault.",
                         "Laugh."]
            self.tempFlag = "Kismet Chat 4"

        elif 'Kismet Chat 5' not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            self.text = ""
            self.menu = ["Brace yourself."]
            self.tempFlag = "Kismet Chat 5"
            if selectionIndex == 0:
                self.text = ("Toshe: Actually, that was my brother. He blew "+
                             "up the ship and he made all those evil things."+
                             "\nMarciano: I am sorry? I beg...I beg your "+
                             "pardon? It was y-your brother?"+
                             "\nMarciano is trembling with rage.\n")
            elif selectionIndex == 1:
                self.text = ("Toshe: Hahaha, that's pretty funny."+
                             "\nMarciano: You think this is funny? You think "+
                             "I am joking? You think this is a funny joke.\n")
            self.text += ("Toshe: Calm down, man."+
                          "\nMarciano: You are the dead meat."+
                          "\nMarciano draws his sword."+
                          "\nToshe: What the fuck?")
            if ( not self.c.hasItem("Stick") and
                 not self.c.hasItem("Small Dagger")):
                self.text += ("\nHeinz: Catch!" +
                              "\nHeinz tosses a Small Dagger to you!")
                return self.actions({'item': "Small Dagger"})

        elif 'Kismet Battle' not in self.c.flags:
            self.view = "battle"
            self.c.flags['Kismet Battle'] = True
            return self.actions({'enemy': "Marciano1"})

        else:
            X = 6
            Y = 4
            return self.actions({'area': "Kismet II",
                                 'coordinates': (X, Y)})
        return self.actions()

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Kismet Chat 6' not in self.c.flags:
            self.text = ("Marciano: Watch your back."+
                         "\nMarciano storms off."+
                         "\nMatsamot: Toshe, what was that about?!"+
                         "\nToshe: I don't know."+
                         "\nMatsamot: Weird. Marciano is a very calm person."+
                         "\nThe man returns with clean garments for you, but "+
                         "promptly drops them and runs away upon seeing your "+
                         "now blood-stained clothing."+
                         "\nMatsamot: Well, we're going to be hitting port "+
                         "in a few hours. You might want to look around the "+
                         "ship or get some rest. Bedrooms are upstairs."+
                         "\nToshe: Alright.")
            self.c.flags['Kismet Chat 6'] = True
        else:
            if not all(flags in self.c.flags for flags in
                       ('Kismet Nap', 'Gan')):
                self.text = "Matsamot: We haven't docked quite yet."
            else:
                if selectionIndex == 0:
                    X = 3
                    Y = 2
                    return self.actions({'area': "Bay of Kotor",
                                         'coordinates': (X, Y)})
                elif selectionIndex == 1:
                    self.text = ("Toshe: Not yet."+
                                 "\nMatsamot: Take your time. We're staying "+
                                 "anchored up for a while here.")
                else:
                    self.text = "Matsamot: Ready to leave?"
                    self.menu = ["\"Yes.\"",
                                 "\"No.\""]
        return self.actions()

    def foodBar(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.hp += 10
            self.text = choice(["Toshe: That's pretty good!",
                                "Toshe: That hit the spot.",
                                "Toshe: Wow. I wish my mom could make turkey "+
                                "like that.",
                                "Toshe: Delicious.",
                                "Toshe: That is what I call food!"])
        elif selectionIndex == 1:
            self.text = choice(["Toshe: Hey."+
                                "\nBusinessman: How do you do?"+
                                "\nToshe: What do you do for a living?"+
                                "\nBusinessman: Unfortunately, I cannot "+
                                "divulge that information."+
                                "\nThe businessman walks away."+
                                "\nToshe: That's some good banter.",
                                "Toshe: Yo."+
                                "\nKid: Hey! Are you Toshe? Toshe from "+
                                "Toshe's Quest?!"+
                                "\nToshe: What the hell is that?",
                                "Gentleman: Sir, I must ask, from where "+
                                "did you obtain such a fine cotton shirt?"+
                                "\nToshe: Oh, this? Haha, my friend Chris "+
                                "lent it to me. I should probably give it "+
                                "back. He's from Canada."+
                                "\nGentleman: Oh, Canada! How is it?"+
                                "\nToshe: It sucks.",
                                "Young Lady: Hey, what's that scar from?"+
                                "\nToshe: Probably a spider."+
                                "\nYoung Lady: Oh..."+
                                "\nToshe: Uh, wait!",
                                "Man: Ay, man, you got any euros?"+
                                "\nToshe: Nope."+
                                "\nMan: Ay, tough luck, buddy.",
                                "Toshe: Hey. How's the ride?"+
                                "\nDrunk man: Uhgug. Pretty damn goo--"+
                                "\nThe man falls over."+
                                "\nToshe: Oh, shit.",
                                "Toshe: Hello."+
                                "\nElderly Lady: Hello, dear."+
                                "\nToshe: How's the food?"+
                                "\nElderly Lady: Quite tasty."+
                                "\nThe lady smiles crookedly."+
                                "\nToshe: That's good. Bye.",
                                "Dog: Woof!"+
                                "\nToshe: Fuck. I should get going."])
        else:
            self.text = ("The food bar is bustling. You see Bart and Heinz "+
                         "chowing down in a corner.")
        self.menu = ["Eat.",
                     "Chit-chat."]
        return self.actions()
        
    def foodBar2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("Security: I'm sorry, this seating area is reserved "+
                     "for our first-class customers.")
        return self.actions()

    def bar(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.text = choice(
["Bartender Jim: If you're stuck in a rut, look back in your text log to see "+
 "if you missed something.",
 "Bartender Jim: Keep an eye on the bottom-right-hand menu. When that box "+
 "fills with options, it's probably good to check 'em out.",
 "Bartender Jim: Click the center picture, of me, to save. You can't save "+
 "when it's greyed out.",
 "Bartender Jim: Click the button wedged in the middle of the navigation "+
 "arrows to see your inventory. When you're there, click an item in the top-"+
 "left where your inventory is displayed. That'll show you information about "+
 "it. Finally, you can click \"Equip\" to wear it.",
 "Bartender Jim: When you level up, you get five stat points. Click on the "+
 "numbers beside your three main stats: Strength, Dexterity, and Wisdom, "+
 "to raise them. That number is how much you have of that stat. Put some "+
 "thought into it, because there's no going back.",
 "Bartender Jim: Keep an eye on your HP in battle. Sometimes it jumps "
 "unexpectedly when the enemy gets a streak of good luck!",
 "Bartender Jim: If you're losing a fight, remember there's no shame in "+
 "running. Sometimes there's no escape path. In that case you'll have to "+
 "tough it out.",
 "Bartender Jim: Want to make a mojito? Start with some mint leaves and add "+
 "crushed ice, an ounce or so of rum, a tablespoon of sugar, half an ounce "+
 "of lime juice, and muddle it all up. Add some soda water and garnish."])
        else:
            self.text = ("Bartender Jim: Ahoy.")
        self.menu = ["Ask for advice."]
        return self.actions()

    def downstairs(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = "There's a flight of stairs going up."
        return self.actions()

    def upstairs(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = "There's a flight of stairs going down."
        return self.actions()

    def bedroom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.hp = self.c.maxHp
            self.text = "You take a quick nap."
            self.c.flags['Kismet Nap'] = True
        else:
            self.text = "Here's your room."
        self.menu = ["Nap."]
        return self.actions()

    def aboveFoodBar(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.text = ("Toshe: Ok."+
                         "\nGan: This move has been taught and passed down "+
                         "for generations. You will be the first Macedonian "+
                         "to know this technique."+
                         "\nYou're not sure how he knows you're Macedonian."+
                         "\nGan: First--"+
                         "\nGan draws a long pole from under his cloak."+
                         "\nGan: --you must place your foot like so..."+
                         "\nGan demonstrates how to perform the move "+
                         "step-by-step. You repeat the steps back to him."+
                         "\nGan vanishes.")
            self.c.flags['Gan'] = True
            return self.actions({'skill': "Deep Thrust",
                                 'cost': 0})
        elif 'Gan' not in self.c.flags:
            self.text = ("You see the back of an old man perched over the "+
                         "railing, observing the the people eating below."+
                         "\nGan: Hello, I am Gan."+
                         "\nToshe: Oh, hi."+
                         "\nYou're not sure whether he's talking to you."+
                         "\nGan turns around."+
                         "\nGan: A fighter! Rare to find on such a luxury "+
                         "voyage. I will show you something.")
            self.menu = ["\"Ok.\""]
        return self.actions()

    def warp1(self, selectionIndex=None):
        X = 3
        Y = 1
        return self.actions({'area': "Kismet II",
                                     'coordinates': (X, Y)})

    def warp2(self, selectionIndex=None):
        X = 3
        Y = 4
        return self.actions({'area': "Kismet II",
                                     'coordinates': (X, Y)})
