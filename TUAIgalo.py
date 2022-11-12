# -*- coding: utf-8 -*-
"""
File: TUAIgalo.py
Author: Ben Gardner
Created: May 21, 2013
Revised: November 12, 2022
"""


from random import choice
from random import randint


class Igalo:

    name = "Igalo"
    audio = "Green Lawn"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"
        self.creaturePage = 1

        dimC = self.dimCorner
        nrw1 = self.narrowStreet1
        dimF = self.dimFork
        crnr = self.corner
        arc1 = self.archway1
        hall = self.townHall
        nrw2 = self.narrowStreet2
        arc2 = self.archway2
        cthd = self.cathedral
        arc3 = self.archway3
        tHC1 = self.townHallCorridor1
        tHC2 = self.townHallCorridor2
        tHC3 = self.townHallCorridor3
        lady = self.creatureLady
        mayr = self.mayorsOffice
        tHC4 = self.townHallCorridor4
        tHC5 = self.townHallCorridor5
        army = self.armyGrounds
        shld = self.shieldMan
        blfs = self.bluffs
        
        self.spots = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, lady, None, None, None, None],
            [None, mayr, None, tHC3, None, tHC5, army, None],
            [None, None, None, tHC2, tHC1, tHC4, None, None],
            [None, blfs, None, None, None, None, None, None],
            [None, dimC, dimF, crnr, hall, None, None, None],
            [None, nrw1, None, arc1, None, None, None, None],
            [None, nrw2, None, arc3, None, shld, None, None],
            [None, arc2, cthd, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]

        self.encounters = None

        self.populateCreatureList()

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

    def populateCreatureList(self):
        creatures = [
            {'Name': "Goblin",
             'Identifiers': ["Sea Goblin", "Goblin", "Mountain Goblin",
                             "Goblin Ranger", "Goblin Thug", "Ancient Goblin"],
             'Description': ("Ah, yes, goblins. Those pesky monsters "+
                         "are everywhere. There are a variety of types, but "+
                         "they all share some common characteristics--pointy "+
                         "ears, large noses and the like. They started "+
                         "appearing only recently and have since inhabited "+
                         "almost every kind of environment. They are thought "+
                         "to have originated in Macedonia. They vary greatly "+
                         "in size and shape and are very protective of "+
                         "their territory. They have an odd obsession with "+
                         "human trinkets.")
             },
            {'Name': "Moghi",
             'Identifiers': ["Moghi"],
             'Description': ("The moghi is a large and peaceful beast. "+
                         "It will protect "+
                         "its young by any means. It inhabits dry and "+
                         "mountainous regions. It is thought to have "+
                         "originated in Ethiopia. In recent times, moghis "+
                         "have become much more aggressive, sometimes "+
                         "attacking anything in sight.")
             },
            {'Name': "Divelk",
             'Identifiers': ["Divelk"],
             'Description': ("Divelks. They are strange beings. Though "+
                         "similar in appearance to goblins, they are not to "+
                         "be trifled with. Research dictates that they are an "+
                         "ancient race with great magical knowledge. Oddly, "+
                         "they have only been spotted in Europe within the "+
                         "last year, and natively in Montenegro! For whatever "+
                         "reason, they have decided to settle in the bluffs.")
             },
            {'Name': "Golem",
             'Identifiers': ["Golem", "Gold Golem", "Crystal Golem Green",
                             "Crystal Golem Blue", "Crystal Golem Red"],
             'Description': ("Hmm, golems. Those are massive things "+
                         "that cause destruction wherever they roam, and "+
                         "where they roam nobody knows. All that is known "+
                         "is that where there are rocks, there may be golems.")
             },
            {'Name': "Ent",
             'Identifiers': ["Ent"],
             'Description': ("Ents are tree spirits that are in eternal" +
                             " conflict with man. Most people agree the war" +
                             " started and continues with lumberjacks" +
                             " taking wood from forests, but at this point" +
                             " we have no reason to stop, as ents provide" +
                             " new recruits with good combat training.")
             },
            {'Name': "Vampire Bat",
             'Identifiers': ["Vampire Bat"],
             'Description': ("Vampire bats are a carnivorous, hostile bat" +
                             " that you can only find in the Black Mountain." +
                             " Stay away if you can, as they will suck your" +
                             " blood as means of rejuvenation.")
             },
            {'Name': "Skeleton",
             'Identifiers': ["Skeleton", "Skeleton Mage1", "Skeleton Mage2",
                             "Skeleton Soldier", "Skeleton Archer",
                             "Flaming Skeleton", "Skeleton Arcanist"],
             'Description': ("Similar to goblins, skeletons come in assorted" +
                             " flavours--flaming, magical and more. They tend" +
                             " to adapt to their environment and take on" +
                             " attributes that reflect their surroundings." +
                             " Mostly harmless for experienced adventurers," +
                             " but they may surprise you" +
                             " with a powerful blow if you're not expecting" +
                             " it.")
             },
            {'Name': "Asp",
             'Identifiers': ["Arcane Asp", "Dark Asp"],
             'Description': ("Snakes are usually not hostile toward" +
                             " humans, however, in recent times, new breeds" +
                             " have shown up: the arcane asps and dark asps." +
                             " Arcane asps take refuge in the lush forest" +
                             " of Herceg Novi where they prey on strangers" +
                             " who happen to cross their path. Dark asps" +
                             " reside in damp regions closer to Greece." +
                             " What you want to watch out for with these asps" +
                             " is their magical blasts. They have evolved" +
                             " from common snakes and developed an affinity" +
                             " for magic--and jade--in the process.")
             },
            {'Name': "Orc",
             'Identifiers': ["Orc", "Cave Orc", "Shorc", "Florc"],
             'Description': ("Mean and vicious, but fairly unintelligent." +
                             "\nToshe: Hey!" +
                             "\nMarija: Not you--orcs. Be prepared for their" +
                             " worst strikes, but don't expect them all to" +
                             " connect. They're basically giant goblins" +
                             " with bloodlust instead of an eye for gold." +
                             " Little research has been conducted, but the" +
                             " general consensus is that they come from" +
                             " Macedonia, though some sources hypothesize" +
                             " that they may actually have originated in" +
                             " Kosovo, where an ancient species was recently" +
                             " discovered.")
             },
            {'Name': "Giant Animal",
             'Identifiers': ["Giant Seal1", "Giant Shark1", "Giant Salamander1",
                             "Giant Scorpion1", "Giant Scarab1"],
             'Description': ("The various giant animals roaming across Europe" +
                             " are a central topic of monstology. Legend says" +
                             " that these beasts have a sacred power that" +
                             " can be unleashed and absorbed into the body" +
                             " through the blood of their fallen leader." +
                             " They are aggressive and will attack if" +
                             " approached." +
                             " Their numbers are scarce, so not much" +
                             " factual information has been gathered.")
             },
            {'Name': "Unholy Crow",
             'Identifiers': ["Unholy Crow"],
             'Description': ("Unholy crows began to settle in western Kosovo" +
                             " recently. They'd been spotted for centuries" +
                             " but only in small numbers. Flocks can now be" +
                             " seen preying on pedestrians below from high up" +
                             " in tall trees. Be careful if you wish to" +
                             " explore the forests west of Kosovo, but know" +
                             " that they have a penchant for collecting" +
                             " garnet gems.")
             },
            {'Name': "Digger",
             'Identifiers': ["Sand Digger"],
             'Description': ("The digger is an ancient ancestor of the common" +
                             " mole. Diggers have lived for millennia," +
                             " relying on burrowing deep in the Earth when" +
                             " catastrophe strikes. The only species of" +
                             " digger remaining is the sand digger, who" +
                             " has stood the test of time and can be found" +
                             " scattered throughout desertous regions." +
                             " Over time, they have adapted to harsh climate" +
                             " changes and developed an aggressive nature." +
                             " Don't upset them or they will lash out. They" +
                             " have a nasty bite!")
             },
            {'Name': "Imp",
             'Identifiers': ["Pestering Imp", "Fire Imp"],
             'Description': ("Those pesky imps. When will they stop" +
                             " bothering us?" +
                             "\nToshe: I don't know." +
                             "\nMarija laughs." +
                             "\nMarija: They enjoy playing games with humans" +
                             " and abusing arcane wisdom for their own" +
                             " pleasure. They're like small children, only" +
                             " more dangerous." +
                             "\nToshe: Small children are dangerous enough." +
                             "\nMarija: Imps can often be found carrying" +
                             " small magical objects, just like goblins" +
                             " love shiny things. Imps don't come out often," +
                             " but if you see one, you're bound to see more.")
             },
            {'Name': "Adurbid",
             'Identifiers': ["Adurbid"],
             'Description': ("The adurbids are the result of an" +
                             " old magical ritual performed on Albanian" +
                             " fighters when the storm came. The storm killed" +
                             " many, but those who had an incantantion spoken" +
                             " upon them were able to resist it. They" +
                             " became known as the adurbids." +
                             " Their bodies miraculously persisted." +
                             " Unfortunately, their minds began to decay." +
                             " They have one strange characteristic;" +
                             " even with a severed body, an adurbid will" +
                             " rise at the end of the waxing" +
                             " crescent, also known as the bloodmoon by" +
                             " Albanians. It's a moon phase that signifies" +
                             " resurrection in many old rituals." +
                             " So, basically, adurbids are zombie mummies" +
                             " living forever in the desert." +
                             "\nToshe: That really sucks.")
             },
            {'Name': "Dust Dweller",
             'Identifiers': ["Dust Dweller"],
             'Description': ("My, my. You want to know about the dwellers?" +
                             " Stay away from those vicious worms!" +
                             " They have baffled scientists as to how they" +
                             " manage to sustain themselves in the harsh" +
                             " desert climate. They are massive carnivores," +
                             " so they need to eat a lot of meat to survive." +
                             " If you get within 100 metres of one, it will" +
                             " make a meal out of you.")
             },
            {'Name': "Manticore",
             'Identifiers': ["Manticore"],
             'Description': ("The manticore is a majestic beast of myth." +
                             " It is still unknown whether they really exist" +
                             " or they are just a mirage seen by exhausted" +
                             " travellers. From the tales about them, I can" +
                             " tell you that they are not to be trifled with." +
                             " Their physical appearance is daunting, but" +
                             " what's most striking is their magical" +
                             " affinity. They have been said to breathe" +
                             " fire and poison at those who provoke them." +
                             " The caveat is that they only" +
                             " rise to those who they deem worthy of" +
                             " a fight. Do you consider yourself worthy?")
             },
            ]

        self.knownCreatures = [creature for creature in creatures
                               if True in [creatureId in self.c.flags['Kills']
                                           for creatureId in
                                           creature['Identifiers']]]

    def bluffs(self, selectionIndex=None):
        X = 3
        Y = 12
        return self.actions({'area': "Herceg Bluffs",
                             'coordinates': (X, Y)})

    def dimCorner(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Niplin" in self.c.flags['Kills']:
            self.text = ("Pavle: Look, the cathedral gates have opened up!"+
                         "\nVuk: I wonder why.")
        else:
            self.text = choice([
                            "Pavle: That cathedral down the road there has "+
                            "been closed off for quite a while."+
                            "\nVuk: It's going to take some real magic to "+
                            "get that place open again.",
                            "Pavle: You give the people weapons and they "+
                            "want magic. There's just no pleasing them."+
                            "\nVuk: It's just fashion. Next October it's "+
                            "gonna be bows again. Remember those?",
                            "Pavle: Whoever started that magic riot must not "+
                            "have been too bright. Have you seen how "+
                            "mighty Igalo's army is?"+
                            "\nVuk: Well, whoever it is must have a lot "+
                            "of wisdom to cause that much destruction."])
        return self.actions()

    def narrowStreet1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            if self.c.euros >= 1400 and self.c.hasRoom():
                self.text = ("Toshe: Sure."+
                             "\nShady Man: Done. Thanks!"+
                             "\nThe man walks away.")
                self.c.euros -= 1400
                self.c.flags['Shady Purchase'] = True
                return self.actions({'item': "Yew Wand"})
            elif self.c.euros < 1400:
                self.text = ("Toshe: I can't afford that.")
            elif not self.c.hasRoom():
                self.text = ("You have no room.")
        elif selectionIndex == 1:
            self.text = ("Toshe: Hey, wands are outlawed here."+
                         "\nShady Man: What's your problem?")
        elif 'Shady Purchase' not in self.c.flags:
            self.text = ("Shady Man: Psst. You want a wand? 1400 euros and "+
                         "it's yours.")
            self.menu = ["\"Yes.\"",
                         "\"That's illegal.\""]
        elif 'Shady Purchase' in self.c.flags and self.c.hp < self.c.maxHp:
            self.text = ("Shady Man: You're a good guy. Keep this on the "+
                         "down-low."+
                         "\nThe man casts a healing spell on you.")
            self.c.hp = self.c.maxHp
        return self.actions()

    def dimFork(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def corner(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You read a sign:"+
                     "\n\"Left: Cathedral of Magic"+
                     "\nRight: Town Hall\"")
        return self.actions()

    def archway1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 5
            Y = 7
            return self.actions({'area': "Igalo",
                                 'coordinates': (X, Y)})
        self.text = ("You hear hammering coming from inside a building.")
        self.menu = ["Enter the building."]
        return self.actions() 

    def townHall(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 4
            Y = 3
            return self.actions({'area': "Igalo",
                            'coordinates': (X, Y)})
        self.text = ("You read a banner:"+
                     "\n\"Town Hall\"")
        self.menu = ["Enter the building."]
        return self.actions()

    def narrowStreet2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def archway2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def cathedral(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 2
            Y = 3
            return self.actions({'area': "Igalo Cathedral",
                                 'coordinates': (X, Y)})
        if "Niplin" in self.c.flags['Kills']:
            self.imageIndex = 19
            self.menu = ["Enter the cathedral."]
        else:
            self.text = ("The entrance to the cathedral is fenced off.")
        return self.actions()

    def archway3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.text = "You break a pot.\n"
            if randint(0, 333) == 333:
                self.view = "battle"
                self.text += ("Toshe: Uh oh. That sounded bad.")               
                return self.actions({'enemy': "Pot Apparition",
                                     'flash': True})
            else:
                self.text += choice([
                    "Toshe: That was fun.",
                    "Toshe: I feel more heroic.",
                    "Toshe: I wonder how many of these there are.",
                    "Toshe: Broken pots are better than un-broken pots.",
                    "Toshe: My mom is proud of me right now.",
                    "Toshe: I hope I don't get in trouble.",
                    "Toshe: Who do these pots belong to?",
                    "Toshe: Only 99 left.",
                    "Toshe: That one looked expensive.",
                    "Toshe: Денес над Македонија!"])
        else:
            self.text = ("You reach a dead end with a lot of pots.")
        self.menu = ["Break a pot."]
        return self.actions()

    def townHallCorridor1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 4
            Y = 5
            return self.actions({'area': "Igalo",
                            'coordinates': (X, Y)})
        self.text = ("You enter the main chamber of the Town Hall.")
        self.menu = ["Leave."]
        return self.actions()

    def townHallCorridor2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You see building plans erected in various places.")
        return self.actions()

    def townHallCorridor3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 2
            return self.actions({'area': "Igalo",
                            'coordinates': (X, Y)})
        self.text = ("This corridor looks unfinished. There are stairs going "+
                     "up to the mayor's office.")
        self.menu = ["Take the stairs."]
        return self.actions()

    def creatureLady(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex is not None:
            # If you hit next page
            if ((selectionIndex == 3 and len(self.knownCreatures) > 4) or
                 (len(self.knownCreatures) - (self.creaturePage-1) * 3
                 == selectionIndex)):
                # If you hit the end
                if self.creaturePage * 3 >= len(self.knownCreatures):
                    self.creaturePage = 1
                else:
                    self.creaturePage += 1
            # If you wanted creature info
            else:
                self.text = ("Toshe: Tell me about %ss." +
                             "\nMarija: %s") % (
                                 self.knownCreatures[
                                     (self.creaturePage-1) * 3
                                     + selectionIndex]['Name'].lower(),
                                 self.knownCreatures[
                                     (self.creaturePage-1) * 3
                                     + selectionIndex]['Description'])
        elif 'Marija' not in self.c.flags:
            self.creaturePage = 1
            self.text = ("Marija: Hello. I'm Marija. I'm the town historian. "+
                         "I like to do landscape paintings on the side, so I "+
                         "have accumulated a good amount of information about "+
                         "the local area. Ask me about any species and I will "+
                         "tell you all there is to know.")
            self.c.flags['Marija'] = True
        else:
            self.creaturePage = 1
            self.text = ("Marija: Is there a particular creature you would "+
                         "like to know about?")
        menuItem1 = menuItem2 = menuItem3 = menuItem4 = None
        # Exactly 4 or fewer creatures to display
        if len(self.knownCreatures) < 5:
            self.menu = ["Ask about %ss." % creature['Name']
                         for creature in self.knownCreatures]
        else:
            if len(self.knownCreatures) - (self.creaturePage-1) * 3 > 2:
                menuItem4 = "Next page."
            # More than 2 creatures remaining
            if len(self.knownCreatures) - (self.creaturePage-1) * 3 > 2:
                menuItem3 = ("Ask about %ss." %
                             self.knownCreatures[
                                 (self.creaturePage-1) * 3 + 2]['Name'])
            # Exactly 2 creatures remaining
            elif len(self.knownCreatures) - (self.creaturePage-1) * 3 == 2:
                menuItem3 = "Next page."
            if len(self.knownCreatures) - (self.creaturePage-1) * 3 > 1:
                menuItem2 = ("Ask about %ss." %
                             self.knownCreatures[
                                 (self.creaturePage-1) * 3 + 1]['Name'])
            elif len(self.knownCreatures) - (self.creaturePage-1) * 3 == 1:
                menuItem2 = "Next page."
            if len(self.knownCreatures) - (self.creaturePage-1) * 3 > 0:
                menuItem1 = ("Ask about %ss." %
                             self.knownCreatures[
                                 (self.creaturePage-1) * 3]['Name'])
            self.menu = [item for item in [
                menuItem1, menuItem2, menuItem3, menuItem4] if item is not None]
        return self.actions()

    def mayorsOffice(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 2
            return self.actions({'area': "Igalo",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            self.text = ("Toshe: I have a question."+
                         "\nMayor Radoman: No time for questions.")
            self.menu = ["Leave."]
            
        elif (selectionIndex == 2 and
              "Radoman Information 1" not in self.c.flags):
            self.text = ("Toshe: I have information."+
                         "\nMayor Radoman: Oh, good. Always time for"+
                         " information."+
                         "\nToshe: It turns out that the archmages left Igalo"+
                         " to go help some evil dude named Niplin."+
                         "\nMayor Radoman: Niplin? Hahaha, oh, my..."+
                         "he must be the one behind all this. I want you to"+
                         " scout out his base for me.")
            self.tempFlag = "Radoman Information 1"
            self.menu = ["Leave.",
                         "Ask a question."]
                         
        elif 'Radoman' not in self.c.flags:
            if self.c.hasNoItems():
                self.text = ("Mayor: Greetings. Who might you be?"+
                             "\nToshe: Toshe."+
                             "\nMayor Radoman: Toshe. Radoman. It's good to "+
                             "see fresh fighters in times of need. Do you "+
                             "have a weapon?"+
                             "\nToshe: Uh, no."+
                             "\nMayor Radoman: Don't worry. The knights will "+
                             "supply you with one. They're "+
                             "outside. Go join them for your debriefing."+
                             "\nToshe: What?"+
                             "\nMayor Radoman: No time for questions. Get "+
                             "moving.")
            else:
                self.text = ("Mayor: Greetings. Who might you be?"+
                             "\nToshe: Toshe."+
                             "\nMayor Radoman: Toshe. Radoman. It's good to "+
                             "see fresh fighters in times of need. Do you "+
                             "have a weapon?"+
                             "\nToshe: Uh, yeah."+
                             "\nMayor Radoman: Good, good. The knights are "+
                             "outside. Go join them for your debriefing."+
                             "\nToshe: What?"+
                             "\nMayor Radoman: No time for questions. Get "+
                             "moving.")
            self.tempFlag = "Radoman"
            self.menu = ["Leave."]
                         
        elif ("The Watchmaking Facility Complete" in self.c.flags and
            "Radoman Information 1" not in self.c.flags):
            self.text = ("Mayor Radoman: Greetings, Toshe.")
            self.menu = ["Leave.",
                         "Ask a question.",
                         "Tell Radoman the news."]
                         
        else:
            self.text = ("Mayor Radoman: Greetings, Toshe.")
            self.menu = ["Leave.",
                         "Ask a question."]
                         
        return self.actions()

    def townHallCorridor4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def townHallCorridor5(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def armyGrounds(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and "Niplin" in self.c.flags['Kills']:
            self.text = ("Toshe: What happened to the Cathedral of Magic?"+
                         "\nKnight: The archmages have returned to the cathedral. They are welcoming all those apprentices who seek to enrich their knowledge of the arcane.")
        elif selectionIndex == 1 and "Niplin" in self.c.flags['Kills']:
            self.text = ("Toshe: Why was magic outlawed?"+
                         "\nKnight: When people began casting spells with "+
                         "iniquity, the fate of Igalo was in jeopardy "+
                         "without the wisdom of the archmages. "+
                         "The mayor was forced to pass a law making "+
                         "all forms of magic illegal. However, with the return of the archmages, the law has been abolished.")
        elif selectionIndex == 0:
            self.text = ("Toshe: What happened to the Cathedral of Magic?"+
                         "\nKnight: Igalo was once a thriving magic town. "+
                         "Magicians then began using magic with malicious "+
                         "intent. Soon our own walls were being "+
                         "destroyed by magic. As a result, the Cathedral "+
                         "of Magic, run by the highest archmages in the "+
                         "world, was abandoned. They were ashamed of the "+
                         "gross abuse of their art.")
        elif selectionIndex == 1:
            self.text = ("Toshe: Why was magic outlawed?"+
                         "\nKnight: When people began casting spells with "+
                         "iniquity, the fate of Igalo was in jeopardy "+
                         "without the wisdom of the archmages. "+
                         "The mayor was forced to pass a law making "+
                         "all forms of magic illegal. Our citizens cannot "+
                         "be given the privilege of such a great power.")
        elif selectionIndex == 2 and "Niplin" in self.c.flags['Kills']:
            self.text = ("Toshe: What's our current mission?"+
                         "\nKnight: Now that Niplin is dead, we can focus on building our defences. For such a mighty warrior as yourself, you may find virtuosity in Mount Olympus.")
        elif selectionIndex == 2 and "Radoman Information 1" in self.c.flags:
            self.text = ("Toshe: What's our current mission?"+
                         "\nKnight: You must be Toshe. We are to"+
                         " seek out the base of Niplin. He initiated"+
                         " this magic fiasco and now he must pay."+
                         " The mayor wants"+
                         " him dead or alive.")
        elif selectionIndex == 2:
            self.text = ("Toshe: What's our current mission?"+
                         "\nKnight: Ah, you must be one of us. We are to "+
                         "seek out a mastermind evildoer who is at the root "+
                         "of this magic fiasco. We heard that he "+
                         "started the black magic riots and the mayor wants "+
                         "him dead or alive.")
        elif selectionIndex == 3:
            self.text = ("Toshe: What's going on with the Town Hall?"+
                         "\nKnight: It is still being rebuilt after the "+
                         "magic incident, so some rooms may look unkempt.")
        else:
            self.text = ("Knight: Good day. We are the Knights of Igalo, the "+
                         "elite of Igalo's army.")
            if self.c.hp <= 50:
                self.text += (" You do not look like you are in good "+
                              "condition. Take this."+
                              "\nThe knight hands you some rations. You "+
                              "feel better after consuming them.")
                self.c.hp += 70
        if 'Radoman' not in self.c.flags:
            self.menu = ["Ask about the cathedral.",
                         "Ask about the ban on magic."]
        else:
            self.menu = ["Ask about the cathedral.",
                         "Ask about the ban on magic.",
                         "Ask about the current mission.",
                         "Ask about the Town Hall construction."]
        return self.actions()

    def shieldMan(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Shield Man"
        smithed = False
        if selectionIndex == 0:
            X = 3
            Y = 6
            return self.actions({'area': "Igalo",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            rawMaterial = "Gold Bar"
            product = "Gold Hauberk"
            price = 2000
            numberOfMaterials = 2
            if  (self.c.hasItem(rawMaterial, numberOfMaterials) and
                 self.c.euros >= price and
                 not self.c.itemIsEquipped(rawMaterial)):
                for i in range(0, numberOfMaterials):
                    self.c.removeItem(self.c.indexOfItem(rawMaterial))
                self.c.euros -= price
                self.text = ("After you pay %s euros," % price +
                             " the %s smiths your bars into" % npc +
                             " a %s." % product)
                smithed = True
            elif price > self.c.euros:
                self.text = (
                    npc+": Sorry, my service is too expensive for you.")
            elif not self.c.hasItem(rawMaterial, numberOfMaterials):
                self.text = (npc+": I can't make it for you without the bars.")
        elif selectionIndex == 2:
            rawMaterial = "Gold Bar"
            product = "Gold Cuirass"
            price = 2000
            numberOfMaterials = 2
            if  (self.c.hasItem(rawMaterial, numberOfMaterials) and
                 self.c.euros >= price and
                 not self.c.itemIsEquipped(rawMaterial)):
                for i in range(0, numberOfMaterials):
                    self.c.removeItem(self.c.indexOfItem(rawMaterial))
                self.c.euros -= price
                self.text = ("After you pay %s euros," % price +
                             " the %s smiths your bars into" % npc +
                             " a %s." % product)
                smithed = True
            elif price > self.c.euros:
                self.text = (
                    npc+": Sorry, my service is too expensive for you.")
            elif not self.c.hasItem(rawMaterial, numberOfMaterials):
                self.text = (npc+": I can't make it for you without the bars.")
        elif selectionIndex == 3:
            rawMaterial = "Gold Bar"
            product = "Gold Shield"
            price = 4000
            numberOfMaterials = 3
            if  (self.c.hasItem(rawMaterial, numberOfMaterials) and
                 self.c.euros >= price and
                 not self.c.itemIsEquipped(rawMaterial)):
                for i in range(0, numberOfMaterials):
                    self.c.removeItem(self.c.indexOfItem(rawMaterial))
                self.c.euros -= price
                self.text = ("After you pay %s euros," % price +
                             " the %s smiths your bars into" % npc +
                             " a %s." % product)
                smithed = True
            elif price > self.c.euros:
                self.text = (
                    npc+": Sorry, my service is too expensive for you.")
            elif not self.c.hasItem(rawMaterial, numberOfMaterials):
                self.text = (npc+": I can't make it for you without the bars.")
                
        elif self.c.hasItem("Key Mold") and self.c.hasItem("Gold Bar"):
            self.c.flags['Got Key'] = True
            rawMaterial = "Gold Bar"
            product = "The Key to Macedonia"
            self.c.removeItem(self.c.indexOfItem(rawMaterial))
            self.text = ("Toshe: %s. Make this key for me." % npc +
                         "\nYou hand the Shield Man your mold and gold bar."+
                         "\n%s: Excellent! Let me tinker for a moment." % npc +
                         "\nThe Shield Man returns with a key."+
                         "\nYou receive The Key to Macedonia!")
            smithed = True
        elif self.c.hasItem("Key Mold") and not self.c.hasItem("Gold Bar"):
            self.text = ("Toshe: %s, make this key for me." % npc+
                         "\n%s: I most certainly can do that as soon" % npc+
                         " as you get me a bar of metal to smith it with.")
        elif self.c.hasItem("Gold Bar") and "Gold Man" not in self.c.flags:
            self.text = (npc+": Wowee! Is that gold? I'm a goldsmith "+
                         "don'cha know? It's just that nobody ever brings "+
                         "me a hunk of gold to hammer away at! Let me make "+
                         "you something special!")
            self.c.flags['Gold Man'] = True
        elif npc not in self.c.flags:
            self.text = (npc+": Sorry for all the loudness. "+
                         "I'm probably disturbing the neighbourhood. They "+
                         "call me %s. I'm sort of a traveling " % npc+
                         "merchant, because shields are a bit of a "+
                         "fad, you see.")
            self.c.flags[npc] = True
        else:
            self.text = choice([npc+": Get your designer shields here.",
                                npc+": I just got up and left my old shop "+
                                "to keep people on their toes.",
                                npc+": I came here thinking I could make a "+
                                "few euros since people are looking for "+
                                "the next exciting thing after magic."])

        if "Gold Man" in self.c.flags:
            self.menu = ["Leave.",
                         "Smith Gold Hauberk (2000 euros, 2 bars).",
                         "Smith Gold Cuirass (2000 euros, 2 bars).",
                         "Smith Gold Shield (4000 euros, 3 bars)."]
        else:
            self.menu = ["Leave."]

        if smithed:
            return self.actions({'item': product,
                                 'items for sale': ["Earthen Buckler",
                                                    "Waterproof Buckler",
                                                    "Tempered Buckler",
                                                    "Defender",
                                                    "Tower Shield",
                                                    "Kite Shield",
                                                    None,
                                                    None,
                                                    None]})
        else:
            return self.actions({'items for sale': ["Earthen Buckler",
                                                    "Waterproof Buckler",
                                                    "Tempered Buckler",
                                                    "Defender",
                                                    "Tower Shield",
                                                    "Kite Shield",
                                                    None,
                                                    None,
                                                    None]})    
