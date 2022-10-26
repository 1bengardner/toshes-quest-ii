# -*- coding: utf-8 -*-
"""
File: TUAMacedonia.py
Author: Ben Gardner
Created: December 4, 2015
Revised: October 25, 2022
"""


import random


class Macedonia(object):

    name = "Macedonia"
    audio = "Daring Feat"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        self.monsters = [
            "Vampire Bat Unfleeable",
            "Goblin Unfleeable",
            "Orc Unfleeable",
            "Moghi Unfleeable",
            "Unholy Crow Unfleeable",
            "Sand Digger Unfleeable",
            "Dust Dweller Unfleeable",
            "Dark Asp Unfleeable",
            "Manticore Unfleeable",
            "Ancient Goblin Unfleeable",
            "Skeleton Arcanist Unfleeable",
            "Skeleton Mage2 Unfleeable"
            ]
        random.shuffle(self.monsters)

        self._mythicalMonsters = [
            "Nemean Lion",
            "Teumessian Fox",
            "Stymphalian Bird",
            "Cerberus",
            "Chimera",
            "Hydra",
            "Cychreides",
            "Skolopendra",
            "Pterripus",
            "Gorgon",
            "Harpy",
            "Minotaur",
            "Centaur",
            "Satyr",
            "Siren"
            ]

        if ( "Dark Voice 3" in self.c.flags and
             "Silvio Slain" not in self.c.flags):
            self.audio = "Castle Stronghold"
        elif ("Demon Slayer" in self.c.flags):
            self.audio = "Wrathful Warrior"

        entr = self.entrance
        ston = self.stoneOfMacedonia
        left = self.left
        rght = self.right
        plrL = self.pillarLeft
        plrR = self.pillarRight

        self.spots = [
            [None, None, None, None, None, None, None],
            [None, plrL, left, ston, rght, plrR, None],
            [None, None, None, None, None, None, None],
            [None, None, None, entr, None, None, None],
            [None, None, None, None, None, None, None]
            ]

        self.encounters = self.getEncounters()

    @property
    def mythicalMonsters(self):
        for monster in self._mythicalMonsters:
            if monster in self.c.flags['Kills']:
                self._mythicalMonsters.remove(monster)
        return self._mythicalMonsters
    
    def movementActions(self):
        self.encounters = self.getEncounters()

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def getEncounters(self):
        return {self.entrance: {},
                self.stoneOfMacedonia: {},
                self.left: self.getRandomEncounter(),
                self.right: self.getRandomEncounter(),
                self.pillarLeft: {},
                self.pillarRight: {}}

    def getRandomEncounter(self):
        return {random.choice(self._mythicalMonsters)
                if not ("Left Summoner Complete" in self.c.flags and
                        "Right Summoner Complete" in self.c.flags)
                else "Death Commander"
                : 100}

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        if "Stone Destroyer" in self.c.flags:
            self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if "Macedonia Monster Spawn" not in self.c.flags:
            if "Macedonia Monster Kills" not in self.c.flags:
                self.c.flags['Macedonia Monster Kills'] = 0
            if "Tomas Talk 1" not in self.c.flags:
                self.tempFlag = "Tomas Talk 1"
                self.text = ("Toshe: I'm finally here, in this...desolate" +
                             " wasteland?" +
                             "\nA Voice: Indeed!" +
                             "\nThe voice booms all through the mountain" +
                             " range." +
                             "\nToshe: Who's that?" +
                             "\nYou look around but there's nobody in sight." +
                             "\nA Voice: It is I, your arch nemesis!" +
                             "\nToshe: ...Tomas!" +
                             "\nTomas Tam: Yes, it is I, Tomas Tam!")
                self.menu = ["Ask Tomas how he is still alive.",
                             "Challenge Tomas to a fight."]
                
            elif "Tomas Talk 2" not in self.c.flags and selectionIndex == 0:
                self.tempFlag = "Tomas Talk 2"
                self.text = ("Toshe: How the fuck are you alive?" +
                             "\nYou hear an explosion of rock from a nearby" +
                             " pillar. The rubble clears and you make out" +
                             " Tomas's tubby frame through the dust. He" +
                             " appears to be glowing." +
                             "\nTomas Tam: I have reincarnated!" +
                             "\nToshe: But how? You have no soul!" +
                             "\nTomas Tam: Yes, that is precisely why I have" +
                             " complete control over my mortal entity!" +
                             " Ha ha ha! I am limitless without a soul!")
                self.menu = ["Ask Tomas why he is here."]
                
            elif "Tomas Talk 2" not in self.c.flags and selectionIndex == 1:
                self.tempFlag = "Tomas Talk 2"
                self.text = ("Toshe: Show yourself! Come out and fight!" +
                             "\nA powerful blast knocks you forward and you" +
                             " fall on your face." +
                             "\nToshe: Ow. Fuck." +
                             "\nTomas Tam: Ha! You'd be foolish to face me" +
                             " in my current form!" +
                             "\nYou get up and turn around to be greeted by" +
                             " a fiery, satanic Tomas Tam." +
                             "\nTomas Tam: Don't look so bewildered. It's" +
                             " the same old brother you know and love," +
                             " here to save the day." +
                             "\nToshe: Save the day? I bet you couldn't even" +
                             " save the game right now!" +
                             " You're not my real brother!")
                self.c.hp -= 20
                self.menu = ["Ask Tomas why he is here."]
                
            else:
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Macedonia Monster Spawn"
                self.text = ("Toshe: What the fuck are you still doing here," +
                             " anyway?" +
                             "\nTomas Tam: Well, Toshe, I've decided to give" +
                             " you one final chance at saving your beloved" +
                             " homeland. A warning, if you will." +
                             "\nToshe: I don't need help!" +
                             "\nTomas Tam: Hear me out. The stone you see" +
                             " here--" +
                             "\nToshe: The Stone of Macedonia. A source of" +
                             " power and a symbol of hope." +
                             "\nTomas Tam: Its power has been" +
                             " re-programmed to generate monsters." +
                             "\nToshe: I figured as much. So what?" +
                             "\nTomas Tam: Well, I hate to say it, but your" +
                             " only hope for saving Macedonia before it's" +
                             " completely overtaken is in destroying the" +
                             " stone." +
                             "\nToshe: No way! I'll kill the monsters and" +
                             " you'll re-program the--" +
                             "\nAll of a sudden, a bright flash lights up" +
                             " the area and several monsters appear.")
                self.menu = ["Brace yourself."]

        elif "Mythical Monster Spawn" not in self.c.flags:
            if self.c.flags['Macedonia Monster Kills'] < 10:
                self.view = "battle"
                self.c.flags['Macedonia Monster Kills'] += 1
                return self.actions({'enemy': self.monsters.pop()})
            else:
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Mythical Monster Spawn"
                self.text = ("Toshe: These monsters won't stop me!" +
                             "\nTomas Tam: These monsters won't stop, that's" +
                             " for sure." +
                             "\nToshe: You started this mess with your secret" +
                             " science lab and shit. Fix the Stone!" +
                             "\nTomas Tam: I'd really like to help, but my" +
                             " hands are tied at the moment." +
                             "\nTomas holds out two fiery appendages held" +
                             " together by a flow of lava." +
                             "\nToshe: You're goddamn useless." +
                             "\nA blinding ray of blue and white light from" +
                             " high above shoots" +
                             " through the fog down to Earth." +
                             "\nToshe: What's this?")
                self.menu = ["Brace yourself."]

        elif "Demon Slayer" not in self.c.flags:
            if "Mythical Monster Kills" not in self.c.flags:
                self.c.flags['Mythical Monster Kills'] = 0
                    
            if self.c.flags['Mythical Monster Kills'] == 0:
                self.view = "battle"
                self.c.flags['Mythical Monster Kills'] += 1
                return self.actions(
                    {'enemy': random.choice(self.mythicalMonsters)})
            
            elif (self.c.flags['Mythical Monster Kills'] == 1 and
                  "Mythical Banter 1" not in self.c.flags):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Mythical Banter 1"
                self.text = ("Toshe: I've never seen anything like that" +
                             " one before." +
                             "\nTomas Tam: Yeah, the trouble with the stone is" +
                             " that it's ever-changing. It's constantly" +
                             " evolving, and it's even capable of learning." +
                             "\nToshe: What are you saying?" +
                             "\nTomas Tam: Legend has it that the beast you" +
                             " just killed once roamed ancient Greece." +
                             " It appears that the stone retains knowledge of" +
                             " old, once-extinct species and infuses them with" +
                             " power to form a bolstered version." +
                             "\nToshe: Why now, all of a sudden?" +
                             "\nA blast of blue-white light interrupts you.")
                self.menu = ["Brace yourself."]
            elif self.c.flags['Mythical Monster Kills'] == 1:
                self.view = "battle"
                self.c.flags['Mythical Monster Kills'] += 1
                return self.actions(
                    {'enemy': random.choice(self.mythicalMonsters)})
            
            elif (self.c.flags['Mythical Monster Kills'] == 2 and
                  "Mythical Banter 2" not in self.c.flags):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Mythical Banter 2"
                self.text = ("Toshe: There's more?" +
                             "\nTomas Tam: Ancient Greece was known for" +
                             " its mythical beasts. And you came at just" +
                             " the right time. Only now is the wisdom of" +
                             " ancient times finally being compiled into" +
                             " the Stone's knowledge base." +
                             "\nToshe: What are the chances?" +
                             "\nTomas Tam: Pretty high. All it takes is the" +
                             " presence of one patriotic Macedonian to" +
                             " assemble the" +
                             " Stone's knowledge of ancient history." +
                             "\nToshe: So this is my fault?" +
                             "\nTomas Tam: Hey, don't be so hard on--" +
                             "\nA blast of blue-white light interrupts Tomas.")
                self.menu = ["Brace yourself."]
            elif self.c.flags['Mythical Monster Kills'] == 2:
                self.view = "battle"
                self.c.flags['Mythical Monster Kills'] += 1
                return self.actions(
                    {'enemy': random.choice(self.mythicalMonsters)})

            elif (self.c.flags['Mythical Monster Kills'] == 3 and
                  "Mythical Banter 3" not in self.c.flags):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Mythical Banter 3"
                self.text = ("Toshe: These monsters are pretty tough!" +
                             "\nTomas Tam: The most powerful to roam" +
                             " Europe yet! Ha ha ha, a former me would" +
                             " be quite proud. But, I'm a changed man." +
                             " I want to help you, Toshe." +
                             "\nToshe: Bullshit! This is part of your fucked" +
                             " up plan somehow." +
                             "\nTomas Tam: What could I possibly desire in" +
                             " this realm of mortals? I don't belong on this" +
                             " side of the earth anymore. I'm just a simple" +
                             " demon..." +
                             "\nToshe: You're just an asshole." +
                             "\nTomas Tam: ...And you're just a simple man." +
                             " Why don't we cooperate? Let's stop wasting" +
                             " our time and destroy this stone already!" +
                             "\nAnother blinding beam of light appears before" +
                             " you.")
                self.menu = ["Brace yourself."]
            elif self.c.flags['Mythical Monster Kills'] == 3:
                self.view = "battle"
                self.c.flags['Mythical Monster Kills'] += 1
                return self.actions(
                    {'enemy': random.choice(self.mythicalMonsters)})
            
            elif (self.c.flags['Mythical Monster Kills'] == 4 and
                  "Mythical Banter 4" not in self.c.flags):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Mythical Banter 4"
                self.text = ("Toshe: Ok..." +
                             "\nYou pause to catch your breath." +
                             "\nToshe: ...How will destroying the Stone help me?" +
                             "\nTomas Tam: The monsters will stop being" +
                             " generated and Macedonia will be safe. Of" +
                             " course, you can repair the stone with cement" +
                             " from Mount Olympus after you have rid it of" +
                             " corruption." +
                             "\nToshe: You just want me to smash the Stone" +
                             " so you can finally see Macedonia crumble." +
                             "\nTomas Tam: Yes, of course, that too, I" +
                             " suppose. But, that's what you call a" +
                             " win-win scenario, right?" +
                             "\nToshe: That's not fair, you bastard!" +
                             "\nA flash illuminates the area and another" +
                             " beast emerges.")
                self.menu = ["Brace yourself."]
            elif self.c.flags['Mythical Monster Kills'] == 4:
                self.view = "battle"
                self.c.flags['Mythical Monster Kills'] += 1
                return self.actions(
                    {'enemy': random.choice(self.mythicalMonsters)})
            
            elif (self.c.flags['Mythical Monster Kills'] == 5 and
                  "Mythical Banter 5" not in self.c.flags):
                self.tempFlag = "Mythical Banter 5"
                self.text = ("Toshe: I have to think of something fast" +
                             " before I run out of energy." +
                             "\nTomas Tam: Take it from me. I learned the" +
                             " hard way that you can't always get what you" +
                             " want. World domination is hard. Sometimes you" +
                             " just gotta take the side road." +
                             "\nToshe: What was your side road?" +
                             "\nTomas Tam: Popping up as a ghost and" +
                             " attacking you in the cemetery." +
                             "\nToshe: Enough! I've had it with your" +
                             " egotistical nonsense!")
                self.menu = ["Fight Tomas Tam."]
            else:
                self.view = "battle"
                self.c.flags['Demon Slayer'] = True
                return self.actions({'enemy': "Demon Tomas"})

        elif "Stone Banter" not in self.c.flags:
            self.audio = "Wrathful Warrior"
            self.tempFlag = "Stone Banter"
            self.text = ("Tomas Tam: This isn't over yet!" +
                         "\nTomas turns to leave." +
                         "\nYou hurl your "+
                         self.c.equippedWeapon.CATEGORY.lower()+
                         " straight at" +
                         " him, impaling the back of his head." +
                         "\nHe falls to the ground, face first, dead." +
                         "\nToshe: That's the end for you, Tomas." +
                         "\nYou retrieve your thoroughly bloodied weapon." +
                         "\nYou scratch your head in deep thought." +
                         "\nSome white flakes drift down to Tomas's demon" +
                         " corpse." +
                         "\nToshe: He was right, though. There's only one" +
                         " thing I can do to save Macedonia.")
            self.menu = ["Approach the Stone."]

        elif "Stone Destroyer" not in self.c.flags:
            self.view = "battle"
            self.c.flags['Stone Destroyer'] = True
            return self.actions({'enemy': "Stone of Macedonia"})

        elif "Crushing Realization" not in self.c.flags:
            if ( self.c.flags['Mythical Monster Kills'] == 5 and
                 "Post Stone Banter 1" not in self.c.flags):
                self.tempFlag = "Post Stone Banter 1"
                self.text = ("Toshe: Fuck! I never thought that thing" +
                             " would put up that much of a fight." +
                             " I feel a little less bad for destroying" +
                             " it now. Well, looks like all that's left to do" +
                             " is appoint myself as the new President of" +
                             " Macedonia.")
                if ( self.c.hasMercenary("Qendresa") and
                     self.c.hasMercenary("Barrie")):
                    self.text += " I guess I should get my companions now."
                elif (self.c.hasMercenary("Qendresa") or
                      self.c.hasMercenary("Barrie")):
                    self.text += (" I should probably tell %s."
                                  % "Qendresa" if
                                  self.c.hasMercenary("Qendresa") else
                                  "Barrie")
                self.text += ("\nThe Stone of Macedonia almost appears to be" +
                              " crying in agony." +
                              "\nYou look up to see the fog clearing as the" +
                              " dust accumulates from the settling rubble" +
                              " resulting from the aftermath of destruction.")
                self.menu = ["Continue."]
            elif (self.c.flags['Mythical Monster Kills'] == 5 and
                  "Post Stone Banter 2" not in self.c.flags):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Post Stone Banter 2"
                self.text = ("Toshe: Wow. I made a pretty big mess." +
                             "\nHigh up in the clear sky above, you see an" +
                             " unmistakably blue and white light coming" +
                             " from above the mountaintops." +
                             "\nToshe: No..." +
                             "\nThe ray rapidly approaches, momentarily" +
                             " blinding you." +
                             "\nToshe: ...That's impossible!")
                self.menu = ["Brace yourself."]
            elif self.c.flags['Mythical Monster Kills'] == 5:
                self.view = "battle"
                self.c.flags['Mythical Monster Kills'] += 1
                return self.actions(
                    {'enemy': random.choice(self.mythicalMonsters)})
            
            elif (self.c.flags['Mythical Monster Kills'] == 6 and
                  "Post Stone Banter 3" not in self.c.flags):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Post Stone Banter 3"
                self.text = ("Toshe: How is this possible? How are there" +
                             " still monsters being created? Damn it!" +
                             "\nYou kick the rubble pile." +
                             "\nPebbles and dust fly into your face." +
                             "\nToshe: Ptoo! Ptoo! Did I just destroy you" +
                             " for nothing? The great Stone of Macedonia," +
                             " now a pile of rocks. What have I done? What" +
                             " would my mom think?" +
                             "\nA burst of light quickly fills the area," +
                             " signalling the presence of another beast.")
                self.menu = ["Brace yourself."]
            elif self.c.flags['Mythical Monster Kills'] == 6:
                self.view = "battle"
                self.c.flags['Mythical Monster Kills'] += 1
                return self.actions(
                    {'enemy': random.choice(self.mythicalMonsters)})
            
            elif (self.c.flags['Mythical Monster Kills'] == 7 and
                  "Post Stone Banter 4" not in self.c.flags):
                self.tempFlag = "Post Stone Banter 4"
                self.c.flags['New Song'] = "Drat"
                self.text = ("Toshe: Now I don't even have Tomas" +
                             " to tell me what" +
                             " a dumbass I am. That fucker tricked me! I" +
                             " actually believed him. I actually thought" +
                             " helping him would be a good idea. I ate up" +
                             " his stupid bullshit about ancient Greece." +
                             " Fuck Greece." +
                             "\nYou stand unfazed as another beam of" +
                             " blue and white hits your field of view.")
                self.menu = ["Brace yourself."]
            elif self.c.flags['Mythical Monster Kills'] == 7:
                self.view = "battle"
                self.c.flags['Mythical Monster Kills'] += 1
                return self.actions(
                    {'enemy': random.choice(self.mythicalMonsters)})
            
            elif (self.c.flags['Mythical Monster Kills'] == 8 and
                  "Post Stone Banter 5" not in self.c.flags):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Post Stone Banter 5"
                self.text = ("Toshe: Fuck. Fuck me." +
                             "\nYou hopelessly embrace the next approaching" +
                             " creature.")
                self.menu = ["Brace yourself."]
            elif self.c.flags['Mythical Monster Kills'] == 8:
                self.view = "battle"
                self.c.flags['Mythical Monster Kills'] += 1
                return self.actions(
                    {'enemy': random.choice(self.mythicalMonsters)})
            
            elif (self.c.flags['Mythical Monster Kills'] == 9 and
                  "Post Stone Banter 6" not in self.c.flags):
                self.tempFlag = "Post Stone Banter 6"
                self.c.flags['New Song'] = "Drat"
                self.text = ("Toshe: Alright. I have to stop these monsters" +
                             " from being created. Where are they coming" +
                             " from?" +
                             "\nYou look around you and see nothing but" +
                             " mountains and the rubble of the Stone of" +
                             " Macedonia." +
                             "\nToshe: What's creating these pests?" +
                             "\nAs you turn your head left, you see a glow in" +
                             " the distance that turns into a bright light." +
                             " The light speeds towards you, becoming blue" +
                             " and white." +
                             "\nToshe: So that's where it's coming from!" +
                             "\nThe summoned beast advances toward you.")
                self.menu = ["Brace yourself."]
            elif self.c.flags['Mythical Monster Kills'] == 9:
                self.view = "battle"
                self.c.flags['Mythical Monster Kills'] += 1
                return self.actions(
                    {'enemy': random.choice(self.mythicalMonsters)})

            else:
                self.c.flags['Crushing Realization'] = True
                X = 3
                Y = 1
                return self.actions({'area': "Macedonia",
                                     'coordinates': (X, Y)})

        elif ("Silvio Slain" not in self.c.flags and
              "Left Summoner Complete" in self.c.flags and
              "Right Summoner Complete" in self.c.flags):
            
            if ( "Silvio Macedonia Complete" in self.c.flags and
                 "Silvio Slain" not in self.c.flags):
                self.c.flags['Silvio Slain'] = True
                self.view = "battle"
                return self.actions({'enemy': "Silvio Berlusconi4"})
            
            elif ("Dark Voice 3" not in self.c.flags):
                self.tempFlag = "Dark Voice 3"
                self.text = ("A Dark Voice: Hahaha!" +
                             "\nAn Italian emerges from a stone tunnel." +
                             " You squint your eyes to try to make out who" +
                             " it could be." +
                             "\nItalian Man: I've been expecting you.")
                self.menu = ["Squint harder."]
                
            elif ("Dark Voice 4" not in self.c.flags):
                self.audio = "Castle Stronghold"
                self.tempFlag = "Dark Voice 4"
                self.text = ("As he emerges from the fog, you recognize the" +
                             " pompous gait of none other than Silvio" +
                             " Berlusconi." +
                             "\nToshe: The Italian president?" +
                             "\nSilvio: The secret is out.")
                self.menu = ["Ask Silvio what he is doing here.",
                             "Fight Silvio."]
                
            elif ("Silvio Macedonia 1" not in self.c.flags and
                  (selectionIndex == 0 or
                   "Silvio Macedonia 1-0" in self.c.flags)):
                self.tempFlag = "Silvio Macedonia 1"
                self.c.flags['Silvio Macedonia 1-0'] = True
                self.text = ("Toshe: What...what are you doing here?" +
                             "\nSilvio: One of my henchmen informed me of" +
                             " your imminent arrival, so I thought I would" +
                             " treat you to a personal visit. One on" +
                             " one. I charge by the hour." +
                             "\nToshe: One of your henchmen?" +
                             "\nSilvio: What was his name...ah, yes!" +
                             " Martian...Marciano!" +
                             "\nToshe: Marciano, that rat bastard!" +
                             "\nSilvio: Kind of a nuisance, is he not?" +
                             "\nToshe: You're the real nuisance here." +
                             "\nSilvio: Being the important man I am," +
                             " my time isn't free. If you'd like" +
                             " to cut our talk short, please say so." +
                             "\nSilvio turns his nose up at you.")
                self.menu = ["Ask Silvio why he is doing this.",
                             "Fight Silvio."]

            elif ("Silvio Macedonia 1" not in self.c.flags and
                  (selectionIndex == 1 or
                   "Silvio Macedonia 1-1" in self.c.flags)):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Silvio Macedonia Complete"
                self.c.flags['Silvio Macedonia 1-1'] = True
                self.text = ("Toshe: I'm going to dispose of you like I" +
                             " did your mages." +
                             "\nSilvio: You ruined my plans once. Now" +
                             " I will ruin you.")
                self.menu = ["Brace yourself."]

            elif ("Silvio Macedonia 2" not in self.c.flags and
                  (selectionIndex == 0 or
                   "Silvio Macedonia 2-0" in self.c.flags)):
                self.tempFlag = "Silvio Macedonia 2"
                self.c.flags['Silvio Macedonia 2-0'] = True
                self.text = ("Toshe: Why have you brought such destruction" +
                             " to my country?" +
                             "\nSilvio: Conquering Greater Albania has been a" +
                             " long and arduous process. As you know, I took" +
                             " Albania with ease. I then infiltrated" +
                             " Greece and imprisoned the president," +
                             " making him my puppet and gaining supremacy" +
                             " over the phalanxes, which I used to start a" +
                             " war against Macedonia. I caught wind of one" +
                             " stubborn Macedonian who attempted to get the" +
                             " key from the captive Macedonian president, but" +
                             " ended up killing him! Hahaha!" +
                             "\nToshe: You bastard...you were behind all of" +
                             " this!")
                self.menu = ["Continue."]

            elif ("Silvio Macedonia 2" not in self.c.flags and
                  (selectionIndex == 1 or
                   "Silvio Macedonia 2-1" in self.c.flags)):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Silvio Macedonia Complete"
                self.c.flags['Silvio Macedonia 2-1'] = True
                self.text = ("Toshe: I'm going to destroy you, you prick." +
                             "\nSilvio: You will be paying dearly for" +
                             " this visit.")
                self.menu = ["Brace yourself."]

            elif ("Silvio Macedonia 3" not in self.c.flags and
                  (selectionIndex == 0 or
                   "Silvio Macedonia 3-0" in self.c.flags)):
                self.tempFlag = "Silvio Macedonia Complete"
                self.c.flags['Silvio Macedonia 3-0'] = True
                self.text = ("Silvio: Hahaha! Yes, and to make matters worse" +
                             " for this Macedonian, I made a deal with a" +
                             " soulless ghost, granting him a demonic" +
                             " reincarnation in exchange for the recipe to" +
                             " summon destructive monsters that will do my" +
                             " bidding. Now all of my mages can summon at" +
                             " will!" +
                             "\nToshe: Tomas?" +
                             "\nSilvio: Your brother, if I'm not mistaken." +
                             " If you weren't such a simpleton, you could" +
                             " have figured all of this out already. But now" +
                             " it's" +
                             " too late. Greater Albania is mine, and soon," +
                             " the world." +
                             " All that's left of Macedonia is you. You" +
                             " are the only" +
                             " scrap left that has resisted my" +
                             " control." +
                             "\nToshe: Македонците се борат," +
                             " за своите правдини!")
                self.menu = ["Fight Silvio."]

        elif ("Silvio Slain" in self.c.flags and
              "Conclusion" not in self.c.flags):
            self.audio = "Daring Feat"
            self.tempFlag = "Conclusion"
            self.text = ("Toshe: It's over. He's dead." +
                         "\nYou look at Silvio's corpse. You scan" +
                         " the rocky Macedonian terrain," +
                         " destroyed." +
                         "\nToshe: What have I done?...I have failed" +
                         " my country." +
                         "\nYou kick some rubble." +
                         "\nToshe: Macedonia can never be restored to its" +
                         " former glory after this." +
                         "\nYou sit for a moment and listen, but you hear" +
                         " nothing." +
                         "\nYou are overcome by the serenity of a" +
                         " land without monsters." +
                         "\nToshe: Macedonia is liberated...Macedonia is" +
                         " free. Free to live!" +
                         "\nYou rise with fists tightly clenched." +
                         "\nA tear rolls down your face, landing in Silvio's" +
                         " blood pool. You look once more at the wreckage" +
                         " that was once your country." +
                         "\nToshe: If this is the price of freedom...then I" +
                         " am willing to pay it.")
            self.menu = ["Continue."]

        elif ("Conclusion" in self.c.flags):
            X = 1
            Y = 1
            return self.actions({'area': "Credits",
                                 'coordinates': (X, Y)})

        else:
            X = 3
            Y = 1
            return self.actions({'area': "Macedonia",
                                 'coordinates': (X, Y)})
                
        return self.actions()

    def stoneOfMacedonia(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if "Dark Voice 1" not in self.c.flags:
            self.c.flags['Dark Voice 1'] = True
            self.text = ("A Dark Voice: Ah hahaha!" +
                         "\nToshe: Where's that maniacal laughter coming" +
                         " from? I need to get to the bottom of this." +
                         "\nTo your left and right are two stone paths" +
                         " that spiral up to two massive pillars.")
        elif ("Dark Voice 2" not in self.c.flags and
              ("Left Summoner Complete" in self.c.flags or
               "Right Summoner Complete" in self.c.flags)):
            self.c.flags['Dark Voice 2'] = True
            self.text = ("You hear a crash of rocks far in the distance." +
                         "\nToshe: What was that?")
            
        elif ("Dark Voice 3" not in self.c.flags and
              "Left Summoner Complete" in self.c.flags and
              "Right Summoner Complete" in self.c.flags):
            X = 3
            Y = 3
            return self.actions({'area': "Macedonia",
                                 'coordinates': (X, Y)})
            
        return self.actions()

    def left(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = ""
        self.helpText = None
        self.menu = []
        if "Macedonia Sabotage" not in self.c.flags:
            self.c.flags['Macedonia Sabotage'] = True
            self.text += ("Toshe: Who would want" +
                          " to sabotage the great nation of Macedonia?\n")
        if "Macedonia Left" not in self.c.flags:
            self.c.flags['Macedonia Left'] = True
            self.text += ("The immensity of the western pillar becomes more" +
                          " evident as it comes into view.")
        if ( "Second Summoner" not in self.c.flags and
             "Left Summoner Complete" in self.c.flags):
            self.c.flags['Second Summoner'] = True
            self.text = ("Toshe: These monsters keep coming. There must" +
                         " be someone else summoning them.")
        if self.text == "":
            self.text = None
        return self.actions()

    def right(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = ""
        self.helpText = None
        self.menu = []
        if "Macedonia Sabotage" not in self.c.flags:
            self.c.flags['Macedonia Sabotage'] = True
            self.text += ("Toshe: Who would want" +
                          " to sabotage the great nation of Macedonia?\n")
        if "Macedonia Right" not in self.c.flags:
            self.c.flags['Macedonia Right'] = True
            self.text += ("You approach the eastern pillar and see the" +
                          " faint silhouette of a white-armoured figure" +
                          " in the fog.")
        if ( "Second Summoner" not in self.c.flags and
             "Right Summoner Complete" in self.c.flags):
            self.c.flags['Second Summoner'] = True
            self.text = ("Toshe: These monsters keep coming. There must" +
                         " be someone else summoning them.")
        if self.text == "":
            self.text = None
        return self.actions()

    # 8 flags
    def pillarTemplate(self,
                       selectionIndex,
                       npcName,
                       flagNames,
                       summonerIdentifier,
                       imageIndex1,
                       imageIndex2):
        self.imageIndex = imageIndex1
        if flagNames[2] in self.c.flags:
            self.imageIndex = imageIndex2
        npc = npcName
        # If this is the first pillar encountered
        if ( flagNames[0] not in self.c.flags and
             flagNames[1] not in self.c.flags):
            self.tempFlag = flagNames[1]
            self.text = ("Toshe: This pillar is fucking huge!" +
                         "\n"+npc+": It provides me with the perfect" +
                         " vantage point from which" +
                         " I can summon vile beasts." +
                         "\nYou look up and notice a summoner speaking to you" +
                         " from the top of the stone column." +
                         "\nToshe: Why are you doing this?" +
                         "\n"+npc+": I do not ask questions. I simply do as" +
                         " I am told by my master." +
                         "\nToshe: You've made my homeland uninhabitable!" +
                         "\n"+npc+": I am sorry. I suggest you go live in" +
                         " Montenegro. The monsters are much less harsh" +
                         " there." +
                         "\nYou scan the pillar up and down and see no easy" +
                         " way up. Your only hope is to destroy the pillar's" +
                         " foundation.")
            self.menu = ["Strike the pillar."]
        # If one pillar has already been destroyed
        elif (flagNames[0] in self.c.flags and
              flagNames[1] not in self.c.flags):
            self.tempFlag = flagNames[1]
            self.text = ("As you get closer, you plainly spot" +
                         " a second summoner atop the" +
                         " pillar, preparing a ray of magic." +
                         "\nToshe: Hey!" +
                         "\nThe summoner pauses, then after three seconds of" +
                         " contemplation returns to concentrating his" +
                         " energy beam." +
                         "\nToshe: Damn. He knows there's no way I can get up" +
                         " there. Guess I'll just have to do this the old" +
                         " fashioned way.")
            self.menu = ["Strike the pillar."]
        # Pillar Battle
        elif (flagNames[2] not in self.c.flags and
              selectionIndex == 0):
            self.view = "battle"
            self.c.flags[flagNames[2]] = True
            return self.actions({'enemy': "Pillar"})
        # Returned to tile after sequence one complete
        elif flagNames[2] not in self.c.flags:
            self.text = ("Toshe: I have to break this pillar to get at" +
                         " the summoner.")
            self.menu = ["Strike the pillar."]
        # If no summoner has been encountered yet
        elif (flagNames[3] not in self.c.flags and
              flagNames[4] not in self.c.flags):
            self.tempFlag = flagNames[4]
            self.text = ("The summoner falls to the ground as the base" +
                         " of the pillar crumbles." +
                         "\nToshe: It's curtains for you, you" +
                         " annoying little bitch." +
                         "\n"+npc+": You have made a very grave mistake," +
                         " coming here." +
                         "\nToshe: I'll make you pay for the damage you've" +
                         " done to Macedonia!" +
                         "\n"+npc+": You cannot stop us.")
            self.menu = ["Attack the summoner."]
        # If first summoner was killed already
        elif (flagNames[3] in self.c.flags and
              flagNames[4] not in self.c.flags):
            self.tempFlag = flagNames[4]
            self.text = ("The summoner falls to the ground as the base" +
                         " of the pillar crumbles." +
                         "\n"+npc+": You have interrupted a very important" +
                         " ritual." +
                         "\nToshe: I'm putting" +
                         " you out of your misery, you sorry piece of shit." +
                         "\n"+npc+": It is you who will be sorry." +
                         "\nToshe: Save your breath for when I've got you" +
                         " down to 2 HP.")
            self.menu = ["Attack the summoner."]
        # Summoner Battle
        elif (flagNames[5] not in self.c.flags and
              selectionIndex == 0):
            self.view = "battle"
            self.c.flags[flagNames[5]] = True
            return self.actions({'enemy': summonerIdentifier})
        # Returned to tile after sequence two complete
        elif flagNames[5] not in self.c.flags:
            self.text = ("Toshe: Time to face the music.")
            self.menu = ["Attack the summoner."]
        elif (flagNames[6] not in self.c.flags and
              flagNames[7] not in self.c.flags):
            self.c.flags[flagNames[7]] = True
            self.text = ("You walk up to the summoner's near" +
                         "-lifeless body." +
                         "\nToshe: Who's your master?" +
                         "\n"+npc+": S-Sil..." +
                         "\nThe summoner's eyelids shut as he lets out" +
                         " his last, frail breath." +
                         "\nToshe: Shit!")
        elif (flagNames[6] in self.c.flags and
              flagNames[7] not in self.c.flags):
            self.tempFlag = flagNames[7]
            self.text = ("You approach the last summoner lying on" +
                         " the ground, his wounds gaping." +
                         "\nToshe: Ok, answer one question and I'll" +
                         " spare you." +
                         " Who is behind all this?" +
                         "\n"+npc+": ..." +
                         "\nToshe: Who!" +
                         "\n"+npc+": Three can keep a secret..." +
                         "\nThe summoner goes silent.")
            self.menu = ["Let the summoner finish.",
                         "Kill the summoner."]
        elif selectionIndex == 0:
            self.text = (npc+": ...If two of them are dead." +
                         "\nThe summoner goes still as the last ounce" +
                         " of blood leaks from his chest wound." +
                         "\nToshe: Damn it!")
        elif selectionIndex == 1:
            self.text = ("Toshe: Don't want to talk?")
            if self.c.equippedWeapon.CATEGORY == "Wand":
                self.text += ("\nYou blast the summoner with a fusillade" +
                              " of magic.")
            elif self.c.equippedWeapon.CATEGORY == "Bow":
                self.text += ("\nYou shoot one final arrow into the" +
                              " summoner, piercing his neck.")
            else:
                self.text += ("\nYou plunge your weapon into the summoner's" +
                              " heart.")
            self.text += ("\nToshe: Don't have to talk." +
                          "\n"+npc+": Ugh...")
        return self.actions()

    def pillarLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.pillarTemplate(selectionIndex,
                                   "Black Summoner",
                                   ["Right Pillar Talk",
                                    "Left Pillar Talk",
                                    "Left Pillar Battle",
                                    "Right Summoner Talk",
                                    "Left Summoner Talk",
                                    "Left Summoner Battle",
                                    "Right Summoner Complete",
                                    "Left Summoner Complete"],
                                   "Mysterious Summoner1",
                                   4,
                                   6)

    def pillarRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.pillarTemplate(selectionIndex,
                                   "White Summoner",
                                   ["Left Pillar Talk",
                                    "Right Pillar Talk",
                                    "Right Pillar Battle",
                                    "Left Summoner Talk",
                                    "Right Summoner Talk",
                                    "Right Summoner Battle",
                                    "Left Summoner Complete",
                                    "Right Summoner Complete"],
                                   "Mysterious Summoner2",
                                   5,
                                   7)
