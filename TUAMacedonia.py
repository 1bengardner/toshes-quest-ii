# -*- coding: utf-8 -*-
"""
File: TUAMacedonia.py
Author: Ben Gardner
Created: December 4, 2015
Revised: August 26, 2023
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
            "Diggler Unfleeable",
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
             "Giacomo Slain" not in self.c.flags):
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
                self.text = ("%s: I'm finally here, in this...desolate" % self.c.NAME +
                             " wasteland?" +
                             "\nA Voice: Indeed!" +
                             "\nThe voice booms all through the mountain" +
                             " range." +
                             "\n%s: Who's that?" % self.c.NAME +
                             "\nYou look around but there's nobody in sight." +
                             "\nA Voice: It is I, your arch nemesis!" +
                             "\n%s: ...Tomas!" % self.c.NAME +
                             "\nTomas Tam: Yes, it is I, Tomas Tam!")
                self.menu = ["Ask Tomas how he is still alive.",
                             "Challenge Tomas to a fight."]
                
            elif "Tomas Talk 2" not in self.c.flags and selectionIndex == 0:
                self.tempFlag = "Tomas Talk 2"
                if self.c.isPolite:
                    htfLine = "%s: How the fudge are you alive?" % self.c.NAME
                else:
                    htfLine = "%s: How the fuck are you alive?" % self.c.NAME
                self.text = (htfLine +
                             "\nYou hear an explosion of rock from a nearby" +
                             " pillar. The rubble clears and you make out" +
                             " Tomas's tubby frame through the dust. He" +
                             " appears to be glowing." +
                             "\nTomas Tam: I have reincarnated!" +
                             "\n%s: But how? You have no soul!" % self.c.NAME +
                             "\nTomas Tam: Yes, that is precisely why I have" +
                             " complete control over my mortal entity!" +
                             " Ha ha ha! I am limitless without a soul!")
                self.menu = ["Ask Tomas why he is here."]
                
            elif "Tomas Talk 2" not in self.c.flags and selectionIndex == 1:
                self.tempFlag = "Tomas Talk 2"
                if self.c.isPolite:
                    owLine = "\n%s: Ow. Frick." % self.c.NAME
                else:
                    owLine = "\n%s: Ow. Fuck." % self.c.NAME
                self.text = ("%s: Show yourself! Come out and fight!" % self.c.NAME +
                             "\nA powerful blast knocks you forward and you" +
                             " fall on your face." +
                             owLine +
                             "\nTomas Tam: Ha! You'd be foolish to face me" +
                             " in my current form!" +
                             "\nYou get up and turn around to be greeted by" +
                             " a fiery, satanic Tomas Tam." +
                             "\nTomas Tam: Don't look so bewildered. It's" +
                             " the same old brother you know and love," +
                             " here to save the day." +
                             "\n%s: Save the day? I bet you couldn't even" % self.c.NAME +
                             " save the game right now!" +
                             " You're not my real brother!")
                self.c.hp -= 20
                self.menu = ["Ask Tomas why he is here."]
                
            else:
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Macedonia Monster Spawn"
                if self.c.isPolite:
                    wtfLine = "%s: What the frick are you still doing here," % self.c.NAME
                else:
                    wtfLine = "%s: What the fuck are you still doing here," % self.c.NAME
                self.text = (wtfLine +
                             " anyway?" +
                             "\nTomas Tam: Well, %s, I've decided to give" % self.c.NAME +
                             " you one final chance at saving your beloved" +
                             " homeland. A warning, if you will." +
                             "\n%s: I don't need help!" % self.c.NAME +
                             "\nTomas Tam: Hear me out. The stone you see" +
                             " here--" +
                             "\n%s: The Stone of Macedonia. A source of" % self.c.NAME +
                             " power and a symbol of hope." +
                             "\nTomas Tam: Its power has been" +
                             " re-programmed to generate monsters." +
                             "\n%s: I figured as much. So what?" % self.c.NAME +
                             "\nTomas Tam: Well, I hate to say it, but your" +
                             " only hope for saving Macedonia before it's" +
                             " completely overtaken is in destroying the" +
                             " stone." +
                             "\n%s: No way! I'll kill the monsters and" % self.c.NAME +
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
                if self.c.isPolite:
                    labLine = " science lab and crap. Fix the Stone!"
                    damnLine = "\n%s: You're goshdarn useless." % self.c.NAME
                else:
                    labLine = " science lab and shit. Fix the Stone!"
                    damnLine = "\n%s: You're goddamn useless." % self.c.NAME
                self.text = ("%s: These monsters won't stop me!" % self.c.NAME +
                             "\nTomas Tam: These monsters won't stop, that's" +
                             " for sure." +
                             "\n%s: You started this mess with your secret" % self.c.NAME +
                             labLine +
                             "\nTomas Tam: I'd really like to help, but my" +
                             " hands are tied at the moment." +
                             "\nTomas holds out two fiery appendages held" +
                             " together by a flow of lava." +
                             damnLine +
                             "\nA blinding ray of blue and white light from" +
                             " high above shoots" +
                             " through the fog down to Earth." +
                             "\n%s: What's this?" % self.c.NAME)
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
                self.text = ("%s: I've never seen anything like that" % self.c.NAME +
                             " one before." +
                             "\nTomas Tam: Yeah, the trouble with the stone is" +
                             " that it's ever-changing. It's constantly" +
                             " evolving, and it's even capable of learning." +
                             "\n%s: What are you saying?" % self.c.NAME +
                             "\nTomas Tam: Legend has it that the beast you" +
                             " just killed once roamed ancient Greece." +
                             " It appears that the stone retains knowledge of" +
                             " old, once-extinct species and infuses them with" +
                             " power to form a bolstered version." +
                             "\n%s: Why now, all of a sudden?" % self.c.NAME +
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
                self.text = ("%s: There's more?" % self.c.NAME +
                             "\nTomas Tam: Ancient Greece was known for" +
                             " its mythical beasts. And you came at just" +
                             " the right time. Only now is the wisdom of" +
                             " ancient times finally being compiled into" +
                             " the Stone's knowledge base." +
                             "\n%s: What are the chances?" % self.c.NAME +
                             "\nTomas Tam: Pretty high. All it takes is the" +
                             " presence of one patriotic Macedonian to" +
                             " assemble the" +
                             " Stone's knowledge of ancient history." +
                             "\n%s: So this is my fault?" % self.c.NAME +
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
                if self.c.isPolite:
                    bsLine = "\n%s: Lies! This is part of your messed" % self.c.NAME
                else:
                    bsLine = "\n%s: Bullshit! This is part of your fucked" % self.c.NAME
                self.text = ("%s: These monsters are pretty tough!" % self.c.NAME +
                             "\nTomas Tam: The most powerful to roam" +
                             " Europe yet! Ha ha ha, a former me would" +
                             " be quite proud. But, I'm a changed man." +
                             " I want to help you, %s." % self.c.NAME +
                             bsLine +
                             " up plan somehow." +
                             "\nTomas Tam: What could I possibly desire in" +
                             " this realm of mortals? I don't belong on this" +
                             " side of the earth anymore. I'm just a simple" +
                             " demon..." +
                             "\n%s: You're just an asshole." % self.c.NAME +
                             "\nTomas Tam: ...And you're just a simple %s." % ("woman" if self.c.isFemale else "man") +
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
                if self.c.isPolite:
                    fairLine = "\n%s: That's not fair, you ass!" % self.c.NAME
                else:
                    fairLine = "\n%s: That's not fair, you bastard!" % self.c.NAME
                self.text = ("%s: Ok..." % self.c.NAME +
                             "\nYou pause to catch your breath." +
                             "\n%s: ...How will destroying the Stone help me?" % self.c.NAME +
                             "\nTomas Tam: The monsters will stop being" +
                             " generated and Macedonia will be safe. Of" +
                             " course, you can repair the stone with cement" +
                             " from Mount Olympus after you have rid it of" +
                             " corruption." +
                             "\n%s: You just want me to smash the Stone" % self.c.NAME +
                             " so you can finally see Macedonia crumble." +
                             "\nTomas Tam: Yes, of course, that too, I" +
                             " suppose. But, that's what you call a" +
                             " win-win scenario, right?" +
                             fairLine +
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
                self.text = ("%s: I have to think of something fast" % self.c.NAME +
                             " before I run out of energy." +
                             "\nTomas Tam: Take it from me. I learned the" +
                             " hard way that you can't always get what you" +
                             " want. World domination is hard. Sometimes you" +
                             " just gotta take the side road." +
                             "\n%s: What was your side road?" % self.c.NAME +
                             "\nTomas Tam: Popping up as a ghost and" +
                             " attacking you in the cemetery." +
                             "\n%s: Enough! I've had it with your" % self.c.NAME +
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
                         "\n%s: That's the end for you, Tomas." % self.c.NAME +
                         "\nYou retrieve your thoroughly bloodied weapon." +
                         "\nYou scratch your head in deep thought." +
                         "\nSome white flakes drift down to Tomas's demon" +
                         " corpse." +
                         "\n%s: He was right, though. There's only one" % self.c.NAME +
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
                self.text = ("%s: Fuck! I never thought that thing" % self.c.NAME +
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
                                  % ("Qendresa" if
                                  self.c.hasMercenary("Qendresa") else
                                  "Barrie"))
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
                self.text = ("%s: Wow. I made a pretty big mess." % self.c.NAME +
                             "\nHigh up in the clear sky above, you see an" +
                             " unmistakably blue and white light coming" +
                             " from above the mountaintops." +
                             "\n%s: No..." % self.c.NAME +
                             "\nThe ray rapidly approaches, momentarily" +
                             " blinding you." +
                             "\n%s: ...That's impossible!" % self.c.NAME)
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
                if self.c.isPolite:
                    damn = "Darn"
                else:
                    damn = "Damn"
                self.text = ("%s: How is this possible? How are there" % self.c.NAME +
                             " still monsters being created? %s it!" % damn +
                             "\nYou kick the rubble pile." +
                             "\nPebbles and dust fly into your face." +
                             "\n%s: Ptoo! Ptoo! Did I just destroy you" % self.c.NAME +
                             " for nothing? The great Stone of Macedonia," +
                             " now just a crumbling rock. What have I done? What" +
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
                if self.c.isPolite:
                    self.text = "%s: Now I don't even have Tomas to tell me how silly I am. That guy really got me. I actually believed him! I knew that ancient Greek mythology crap wasn't real." % self.c.NAME
                else:
                    self.text = ("%s: Now I don't even have Tomas" % self.c.NAME +
                             " to tell me what" +
                             " a dumbass I am. That fucker tricked me! I" +
                             " actually believed him. I actually thought" +
                             " helping him would be a good idea. I ate up" +
                             " his stupid bullshit about ancient Greece." +
                             " Fuck Greece.")
                self.text += ("\nYou stand unfazed as another beam of" +
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
                if self.c.isPolite:
                    fLine = "%s: Drat. Rats. Crap." % self.c.NAME
                else:
                    fLine = "%s: Fuck. Fuck me." % self.c.NAME
                self.text = (fLine +
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
                self.text = ("%s: Alright. I have to stop these monsters" % self.c.NAME +
                             " from being created. Where are they coming" +
                             " from?" +
                             "\nYou look around you and see nothing but" +
                             " mountains and the rubble of the Stone of" +
                             " Macedonia." +
                             "\n%s: What's creating these pests?" % self.c.NAME +
                             "\nAs you turn your head left, you see a glow in" +
                             " the distance that turns into a bright light." +
                             " The light speeds towards you, becoming blue" +
                             " and white." +
                             "\n%s: So that's where it's coming from!" % self.c.NAME +
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

        elif ("Giacomo Slain" not in self.c.flags and
              "Left Summoner Complete" in self.c.flags and
              "Right Summoner Complete" in self.c.flags):
            
            if ( "Giacomo Macedonia Complete" in self.c.flags and
                 "Giacomo Slain" not in self.c.flags):
                self.c.flags['Giacomo Slain'] = True
                self.view = "battle"
                return self.actions({'enemy': "Giacomo Gambino4"})
            
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
                             " pompous gait of none other than Giacomo" +
                             " Gambino." +
                             "\n%s: The Italian president?" % self.c.NAME +
                             "\nGiacomo: The secret is out.")
                self.menu = ["Ask Giacomo what he is doing here.",
                             "Fight Giacomo."]
                
            elif ("Giacomo Macedonia 1" not in self.c.flags and
                  (selectionIndex == 0 or
                   "Giacomo Macedonia 1-0" in self.c.flags)):
                self.tempFlag = "Giacomo Macedonia 1"
                self.c.flags['Giacomo Macedonia 1-0'] = True
                if self.c.isPolite:
                    marcianoLine = "\n%s: Marciano, that butthole!" % self.c.NAME
                else:
                    marcianoLine = "\n%s: Marciano, that rat bastard!" % self.c.NAME
                self.text = ("%s: What...what are you doing here?" % self.c.NAME +
                             "\nGiacomo: One of my henchmen informed me of" +
                             " your imminent arrival, so I thought I would" +
                             " treat you to a personal visit. One on" +
                             " one. I charge by the hour." +
                             "\n%s: One of your henchmen?" % self.c.NAME +
                             "\nGiacomo: What was his name...ah, yes!" +
                             " Martian...Marciano!" +
                             marcianoLine +
                             "\nGiacomo: Kind of a nuisance, is he not?" +
                             "\n%s: You're the real nuisance here." % self.c.NAME +
                             "\nGiacomo: Being the important man I am," +
                             " my time isn't free. If you'd like" +
                             " to cut our talk short, please say so." +
                             "\nGiacomo turns his nose up at you.")
                self.menu = ["Ask Giacomo why he is doing this.",
                             "Fight Giacomo."]

            elif ("Giacomo Macedonia 1" not in self.c.flags and
                  (selectionIndex == 1 or
                   "Giacomo Macedonia 1-1" in self.c.flags)):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Giacomo Macedonia Complete"
                self.c.flags['Giacomo Macedonia 1-1'] = True
                self.text = ("%s: I'm going to dispose of you like I" % self.c.NAME +
                             " did your mages." +
                             "\nGiacomo: You ruined my plans once. Now" +
                             " I will ruin you.")
                self.menu = ["Brace yourself."]

            elif ("Giacomo Macedonia 2" not in self.c.flags and
                  (selectionIndex == 0 or
                   "Giacomo Macedonia 2-0" in self.c.flags)):
                self.tempFlag = "Giacomo Macedonia 2"
                self.c.flags['Giacomo Macedonia 2-0'] = True
                if self.c.isPolite:
                    bastardLine = "\n%s: You freaking lout...you were behind all of" % self.c.NAME
                else:
                    bastardLine = "\n%s: You bastard...you were behind all of" % self.c.NAME
                self.text = ("%s: Why have you brought such destruction" % self.c.NAME +
                             " to my country?" +
                             "\nGiacomo: Conquering Greater Albania has been a" +
                             " long and arduous process. As you know, I took" +
                             " Albania with ease. I then infiltrated" +
                             " Greece and imprisoned the president," +
                             " making him my puppet and gaining supremacy" +
                             " over the phalanxes, which I used to start a" +
                             " war against Macedonia. I caught wind of one" +
                             " stubborn Macedonian who attempted to get the" +
                             " key from the captive Macedonian president, but" +
                             " ended up killing him! Hahaha!" +
                             bastardLine +
                             " this!")
                self.menu = ["Continue."]

            elif ("Giacomo Macedonia 2" not in self.c.flags and
                  (selectionIndex == 1 or
                   "Giacomo Macedonia 2-1" in self.c.flags)):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Giacomo Macedonia Complete"
                self.c.flags['Giacomo Macedonia 2-1'] = True
                self.text = ("%s: I'm going to destroy you, you prick." % self.c.NAME +
                             "\nGiacomo: You will be paying dearly for" +
                             " this visit.")
                self.menu = ["Brace yourself."]

            elif ("Giacomo Macedonia 3" not in self.c.flags and
                  (selectionIndex == 0 or
                   "Giacomo Macedonia 3-0" in self.c.flags)):
                self.c.flags['New Song'] = "Drat"
                self.tempFlag = "Giacomo Macedonia Complete"
                self.c.flags['Giacomo Macedonia 3-0'] = True
                self.text = ("Giacomo: Hahaha! Yes, and to make matters worse" +
                             " for this Macedonian, I made a deal with a" +
                             " soulless ghost, granting him a demonic" +
                             " reincarnation in exchange for the recipe to" +
                             " summon destructive monsters that will do my" +
                             " bidding. Now all of my mages can summon at" +
                             " will!" +
                             "\n%s: Tomas?" % self.c.NAME +
                             "\nGiacomo: Your brother, if I'm not mistaken." +
                             " If you weren't such a simpleton, you could" +
                             " have figured all of this out already. But now" +
                             " it's" +
                             " too late. Greater Albania is mine, and soon," +
                             " the world." +
                             " All that's left of Macedonia is you. You" +
                             " are the only" +
                             " scrap left that has resisted my" +
                             " control." +
                             "\n%s: Македонците се борат," % self.c.NAME +
                             " за своите правдини!")
                self.menu = ["Fight Giacomo."]

        elif ("Giacomo Slain" in self.c.flags and
              "Conclusion" not in self.c.flags):
            self.audio = "Daring Feat"
            self.tempFlag = "Conclusion"
            self.text = ("%s: It's over. He's dead." % self.c.NAME +
                         "\nYou look at Giacomo's corpse. You scan" +
                         " the rocky Macedonian terrain," +
                         " destroyed." +
                         "\n%s: What have I done?...I have failed" % self.c.NAME +
                         " my country." +
                         "\nYou kick some rubble." +
                         "\n%s: Macedonia can never be restored to its" % self.c.NAME +
                         " former glory after this." +
                         "\nYou sit for a moment and listen, but you hear" +
                         " nothing." +
                         "\nYou are overcome by the serenity of a" +
                         " land without monsters." +
                         "\n%s: Macedonia is liberated...Macedonia is" % self.c.NAME +
                         " free. Free to live!" +
                         "\nYou rise with fists tightly clenched." +
                         "\nA tear rolls down your face, landing in Giacomo's" +
                         " blood pool. You look once more at the wreckage" +
                         " that was once your country." +
                         "\n%s: If this is the price of freedom...then I" % self.c.NAME +
                         " am willing to pay it.")
            self.menu = ["Continue."]

        elif ("Conclusion" in self.c.flags and "Credits" not in self.c.flags):
            X = 1
            Y = 1
            return self.actions({'area': "Credits",
                                 'coordinates': (X, Y)})

        elif ("Conclusion" in self.c.flags):
            if selectionIndex == 0:
                if "Macedonia Ointment" in self.c.flags:
                    self.view = "battle"
                    self.imageIndex = 14
                    del self.c.flags['Macedonia Ointment']
                    self.text = "You enter the sanctum and encounter a Will-o'-Wisp!"
                    return self.actions({'enemy': "Will o Wisp",
                                         'mercenaries': self.c.mercenaries,})
                else:
                    X = 1
                    Y = 1
                    return self.actions({'area': "Credits",
                                         'coordinates': (X, Y)})
            elif selectionIndex == 1 or "Macedonia Ointment" in self.c.flags:
                if selectionIndex == 1:
                    self.c.flags['Macedonia Ointment'] = True
                    self.c.removeItem(self.c.indexOfItem("Olympian Ointment"))
                    self.text = "You apply a jar of Olympian Ointment to the Stone of Macedonia."
                    self.text += "\nIt returns to its original vibrant hue. It begins to shake, pulling itself apart to reveal what appears to be an inner sanctum."
                    if "Inner Sanctum" not in self.c.flags:
                        self.c.flags['Inner Sanctum'] = True
                        if self.c.isPolite:
                            fLine = "\n%s: Mother of poo." % self.c.NAME
                        else:
                            fLine = "\n%s: Holy fuck." % self.c.NAME
                        self.text += fLine
                else:
                    self.text = "You approach the Stone of Macedonia, now with a door leading to its inner sanctum."
                self.imageIndex = 14
                self.menu = ["Enter the sanctum."]
            else:
                self.text = ("%s: This tired stone is all that's left." % self.c.NAME)
                if self.c.hasMercenary("Barrie"):
                    self.text += ("\nBarrie: %s, you alright, bud? That sounded way too poetic for you." % self.c.NAME)
                    if self.c.hasMercenary("Qendresa"):
                        self.text += ("\nQendresa: There is no greater love than for one's homeland.")
                    else:
                        if self.c.isPolite:
                            hushLine = "\n%s: You be quiet. I love Macedonia." % self.c.NAME
                        else:
                            hushLine = "\n%s: Shut the fuck up. I love Macedonia." % self.c.NAME
                        self.text += (hushLine)
                self.menu = ["Proceed to Credits."]
                if self.c.hasItem("Olympian Ointment"):
                    self.menu.append("Apply Olympian Ointment.")

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
                         "\n%s: Where's that maniacal laughter coming" % self.c.NAME +
                         " from? I need to get to the bottom of this." +
                         "\nTo your left and right are two stone paths" +
                         " that spiral up to two massive pillars.")
        elif ("Dark Voice 2" not in self.c.flags and
              ("Left Summoner Complete" in self.c.flags or
               "Right Summoner Complete" in self.c.flags)):
            self.c.flags['Dark Voice 2'] = True
            self.text = ("You hear a crash of rocks far in the distance." +
                         "\n%s: What was that?" % self.c.NAME)
            
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
            self.text += ("%s: Who would want" % self.c.NAME +
                          " to sabotage the great nation of Macedonia?\n")
        if "Macedonia Left" not in self.c.flags:
            self.c.flags['Macedonia Left'] = True
            self.text += ("The immensity of the western pillar becomes more" +
                          " evident as it comes into view.")
        if ( "Second Summoner" not in self.c.flags and
             "Left Summoner Complete" in self.c.flags):
            self.c.flags['Second Summoner'] = True
            self.text = ("%s: These monsters keep coming. There must" % self.c.NAME +
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
            self.text += ("%s: Who would want" % self.c.NAME +
                          " to sabotage the great nation of Macedonia?\n")
        if "Macedonia Right" not in self.c.flags:
            self.c.flags['Macedonia Right'] = True
            self.text += ("You approach the eastern pillar and see the" +
                          " faint silhouette of a white-armoured figure" +
                          " in the fog.")
        if ( "Second Summoner" not in self.c.flags and
             "Right Summoner Complete" in self.c.flags):
            self.c.flags['Second Summoner'] = True
            self.text = ("%s: These monsters keep coming. There must" % self.c.NAME +
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
            if self.c.isPolite:
                hugeLine = "%s: This pillar is really huge!" % self.c.NAME
            else:
                hugeLine = "%s: This pillar is fucking huge!" % self.c.NAME
            self.text = (hugeLine +
                         "\n"+npc+": It provides me with the perfect" +
                         " vantage point from which" +
                         " I can summon vile beasts." +
                         "\nYou look up and notice a summoner speaking to you" +
                         " from the top of the stone column." +
                         "\n%s: Why are you doing this?" % self.c.NAME +
                         "\n"+npc+": I do not ask questions. I simply do as" +
                         " I am told by my master." +
                         "\n%s: You've made my homeland uninhabitable!" % self.c.NAME +
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
            if self.c.isPolite:
                damnLine = "\n%s: Drat. He knows there's no way I can get up" % self.c.NAME
            else:
                damnLine = "\n%s: Damn. He knows there's no way I can get up" % self.c.NAME
            self.text = ("As you get closer, you plainly spot" +
                         " a second summoner atop the" +
                         " pillar, preparing a ray of magic." +
                         "\n%s: Hey!" % self.c.NAME +
                         "\nThe summoner pauses, then after three seconds of" +
                         " contemplation returns to concentrating his" +
                         " energy beam." +
                         damnLine +
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
            self.text = ("%s: I have to break this pillar to get at" % self.c.NAME +
                         " the summoner.")
            self.menu = ["Strike the pillar."]
        # If no summoner has been encountered yet
        elif (flagNames[3] not in self.c.flags and
              flagNames[4] not in self.c.flags):
            self.tempFlag = flagNames[4]
            if self.c.isPolite:
                bitchLine = " stupid punk."
            else:
                bitchLine = " annoying little bitch."
            self.text = ("The summoner falls to the ground as the base" +
                         " of the pillar crumbles." +
                         "\n%s: It's curtains for you, you" % self.c.NAME +
                         bitchLine +
                         "\n"+npc+": You have made a very grave mistake," +
                         " coming here." +
                         "\n%s: I'll make you pay for the damage you've" % self.c.NAME +
                         " done to Macedonia!" +
                         "\n"+npc+": You cannot stop us.")
            self.menu = ["Attack the summoner."]
        # If first summoner was killed already
        elif (flagNames[3] in self.c.flags and
              flagNames[4] not in self.c.flags):
            self.tempFlag = flagNames[4]
            if self.c.isPolite:
                miseryLine = " you out of your misery, you sorry sack of poo."
            else:
                miseryLine = " you out of your misery, you sorry piece of shit."
            self.text = ("The summoner falls to the ground as the base" +
                         " of the pillar crumbles." +
                         "\n"+npc+": You have interrupted a very important" +
                         " ritual." +
                         "\n%s: I'm putting" % self.c.NAME +
                         miseryLine +
                         "\n"+npc+": It is you who will be sorry." +
                         "\n%s: Save your breath for when I've got you" % self.c.NAME +
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
            self.text = ("%s: Time to face the music." % self.c.NAME)
            self.menu = ["Attack the summoner."]
        elif (flagNames[6] not in self.c.flags and
              flagNames[7] not in self.c.flags):
            self.c.flags[flagNames[7]] = True
            if self.c.isPolite:
                shitLine = "\n%s: Dagnabbit." % self.c.NAME
            else:
                shitLine = "\n%s: Shit!" % self.c.NAME
            self.text = ("You walk up to the summoner's near" +
                         "-lifeless body." +
                         "\n%s: Who's your master?" % self.c.NAME +
                         "\n"+npc+": G-Gia..." +
                         "\nThe summoner's eyelids shut as he lets out" +
                         " his last, frail breath." +
                         shitLine)
        elif (flagNames[6] in self.c.flags and
              flagNames[7] not in self.c.flags):
            self.tempFlag = flagNames[7]
            self.text = ("You approach the last summoner lying on" +
                         " the ground, his wounds gaping." +
                         "\n%s: Ok, answer one question and I'll" % self.c.NAME +
                         " spare you." +
                         " Who is behind all this?" +
                         "\n"+npc+": ..." +
                         "\n%s: Who!" % self.c.NAME +
                         "\n"+npc+": Three can keep a secret..." +
                         "\nThe summoner goes silent.")
            self.menu = ["Let the summoner finish.",
                         "Kill the summoner."]
        elif selectionIndex == 0:
            if self.c.isPolite:
                damnLine = "\n%s: Darn it..." % self.c.NAME
            else:
                damnLine = "\n%s: Damn it..." % self.c.NAME
            self.text = (npc+": ...If two of them are dead." +
                         "\nThe summoner goes still as the last ounce" +
                         " of blood leaks from his chest wound." +
                         damnLine)
            self.text += ("\nYou collect a hearty vial of life fluid.")
            self.c.potions += 1
        elif selectionIndex == 1:
            self.text = ("%s: Don't want to talk?" % self.c.NAME)
            if self.c.equippedWeapon.CATEGORY == "Wand":
                self.text += ("\nYou blast the summoner with a fusillade" +
                              " of magic.")
            elif self.c.equippedWeapon.CATEGORY == "Bow":
                self.text += ("\nYou shoot one final arrow into the" +
                              " summoner, piercing his neck.")
            else:
                self.text += ("\nYou plunge your weapon into the summoner's" +
                              " heart.")
            self.text += ("\n%s: Don't have to talk." % self.c.NAME +
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
