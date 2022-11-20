"""
File: TUAHercegNovi.py
Author: Ben Gardner
Created: May 19, 2013
Revised: November 19, 2022
"""


from random import choice


class HercegNovi:

    name = "Herceg Novi"
    audio = "July Sky"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        bay0 = self.bay0
        entr = self.entrance
        sqre = self.square
        bay1 = self.bay1
        bay2 = self.bay2
        bay3 = self.bay3
        bay4 = self.bay4
        aly1 = self.alley1
        aptm = self.apartments
        splt = self.split
        cltE = self.clothierEntrance
        dPth = self.dirtPath
        aly2 = self.alley2
        arch = self.archway
        lSHs = self.leftStoneHouse
        rSHs = self.rightStoneHouse
        str1 = self.stairs1
        cstl = self.castle
        fork = self.fork
        corr = self.corridor
        cstl = self.castle
        tvrE = self.tavernEntrance
        lBrg = self.leftBridge
        ctyd = self.courtyard
        smtE = self.smithEntrance
        str2 = self.stairs2
        tvrn = self.tavern
        bedr = self.bedroom
        smth = self.smith
        clth = self.clothier
        blfs = self.bluffs
        flds = self.fields
        mayr = self.mayorsOffice
        self.spots = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, blfs, None, smth, None, clth, None, None, None, None],
            [None, str2, None, None, None, None, None, flds, None, None],
            [None, str1, cstl, fork, corr, tvrE, lBrg, ctyd, smtE, None],
            [None, None, None, aly2, None, arch, None, lSHs, rSHs, None],
            [None, tvrn, None, aly1, None, aptm, splt, cltE, dPth, None],
            [None, None, None, sqre, None, bay1, bay2, bay3, bay4, None],
            [None, bedr, None, entr, None, None, None, None, None, None],
            [None, None, None, bay0, None, mayr, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None]]

        self.encounters = None

    def movementActions(self):
        if "About to Leave" in self.c.flags:
            del self.c.flags['About to Leave']

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def bay0(self, selectionIndex=None):
        X = 1
        Y = 2
        return self.actions({'area': "Bay of Kotor",
                             'coordinates': (X, Y)})

    def bay1(self, selectionIndex=None):
        X = 3
        Y = 2
        return self.actions({'area': "Bay of Kotor",
                             'coordinates': (X, Y)})

    def bay2(self, selectionIndex=None):
        X = 4
        Y = 2
        return self.actions({'area': "Bay of Kotor",
                             'coordinates': (X, Y)})

    def bay3(self, selectionIndex=None):
        X = 5
        Y = 2
        return self.actions({'area': "Bay of Kotor",
                             'coordinates': (X, Y)})

    def bay4(self, selectionIndex=None):
        X = 6
        Y = 2
        return self.actions({'area': "Bay of Kotor",
                             'coordinates': (X, Y)})

    def bluffs(self, selectionIndex=None):
        X = 8
        Y = 3
        return self.actions({'area': "Herceg Bluffs",
                             'coordinates': (X, Y)})

    def fields(self, selectionIndex=None):
        X = 4
        Y = 12
        return self.actions({'area': "Herceg Fields",
                             'coordinates': (X, Y)})

    def apartments(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if self.c.level < 3:
            self.text = ("You unfortunately spot a naked man lounging on "+
                         "the balcony."+
                         "\nNaked Man: Welcome to Montenegro! Woo!"+
                         "\nToshe: Thanks...")
        return self.actions()

    def split(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def clothierEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 5
            Y = 1
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        if "Tipsy Tuesday" not in self.c.flags:
            self.text = ("You read a sign:"+
                         "\n\"Welcome to Lina's!\"")
        elif "Tipsy Tuesday" in self.c.flags:
            self.text = ("You read a sign:"+
                         "\n\"Velcome to Pina's Colada!\"")
        self.menu = ["Enter the store."]
        return self.actions()

    def dirtPath(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def archway(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Herceg Novi Archway' not in self.c.flags:
            self.text = ("The town square has quite a few shoppers today.")
            self.c.flags['Herceg Novi Archway'] = True
        elif "Tipsy Tuesday" in self.c.flags:
            self.text = ("The town square has quite a few drunkards today.")
        return self.actions()

    def leftStoneHouse(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Petar' not in self.c.flags:
            self.text = ("Petar: Hi, I'm Petar. Use my house, if you want. "+
                         "Everyone does.")
            self.c.flags['Petar'] = True
        elif "Tipsy Tuesday" in self.c.flags:
            self.text = ("Petar: Hooooowdy!!")
        else:
            randomInteger = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            generatedText = {
                0: "Petar: Do you like my house? Everyone does.",
                1: "Petar: While visiting Herceg Novi, make sure you see "+
                "The Bluffs. Everyone does.",
                2: "Petar: If you are going swimming, take a weapon with "+
                "you. Everyone does. Just in case. You never know.",
                3: "Petar: You want to be my friend? Everyone does.",
                4: "Petar: You wonder what the mayor is doing? Everyone does.",
                5: "Petar: My wife will kill me if she finds out I've been at "+
                "home all day.",
                6: None,
                7: None,
                8: None,
                9: None}
            self.text = generatedText[randomInteger]
            if randomInteger == 1:
                self.c.flags['Petar Bluffs'] = True
        return self.actions()

    def rightStoneHouse(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Petar' not in self.c.flags:
            self.text = ("Petar: Hi, I'm Petar. Use my house, if you want. "+
                         "Everyone does.")
            self.c.flags['Petar'] = True
        elif "Tipsy Tuesday" in self.c.flags:
            self.text = ("Petar: Wahooooo!!")
        else:
            randomInteger = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            generatedText = {
                0: "Petar: Do you like my house? Everyone does.",
                1: "Petar: While visiting Herceg Novi, make sure you see "+
                "The Bluffs. Everyone does.",
                2: "Petar: If you are going swimming, take a weapon with "+
                "you. Everyone does. Just in case. You never know.",
                3: "Petar: You want to be my friend? Everyone does.",
                4: "Petar: You wonder what the mayor is doing? Everyone does.",
                5: "Petar: My wife will kill me if she finds out I've been at "+
                "home all day.",
                6: None,
                7: None,
                8: None,
                9: None}
            self.text = generatedText[randomInteger]
            if randomInteger == 1:
                self.c.flags['Petar Bluffs'] = True
        return self.actions()

    def tavernEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = ""
        self.helpText = None
        self.menu = []
        if "Hot Air Balloon Price" in self.c.flags:
            self.c.euros -= self.c.flags['Hot Air Balloon Price']
            self.text = ("You pay the Hot Air Balloon Mafia "+
                         "%s " % (self.c.flags['Hot Air Balloon Price'])+
                         "euros and they fly you to Herceg Novi.")
            del self.c.flags['Hot Air Balloon Price']
        if selectionIndex == 0:
            X = 1
            Y = 5
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        if self.c.level % 5 == 0:
            special = "Crab Soup"
        elif self.c.level % 3 == 0:
            special = "Serbian Eel-Basted Pork Loin"
        elif self.c.level % 2 == 0:
            special = "Grilled Aubergine Musaka"
        else:
            special = "Mystery Goulash"
        if "Tipsy Tuesday" not in self.c.flags:
            self.text += ("You read a sign:"+
                          "\n\"Vojo's Inn and Tavern"+
                          "\nToday's Special: "+special+"\"")
        elif "Tipsy Tuesday" in self.c.flags:
            self.text += ("You read a sign:"+
                          "\n\"Vojo's Inn and Tavern"+
                          "\nToday is Tipsy Tuesday!\"")
        if 'Bartender Daniel' not in self.c.flags:
            self.text += ("\nToshe: I think this is the place Matsamot mentioned.")
        self.menu = ["Enter the inn."]
        return self.actions()

    def courtyard(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        npc = choice(["Ivana",
                      "Boris",
                      "Dado"])
        if npc == "Ivana":
            if 'Ivana' not in self.c.flags:
                self.text = ("Ivana: Hello! I'm Ivana!"+
                             "\nToshe: Toshe.")
                self.c.flags['Ivana'] = True
            elif "Tipsy Tuesday" in self.c.flags:
                self.text = ("Ivana: Hi, Toshe..."+
                             "\nIvana winks at you.")
            elif ('Ivana Talk 3' in self.c.flags and
                  'Necklace Fixed' not in self.c.flags and
                  self.c.hasItem("Aquamarine Shard") and
                  not self.c.itemIsEquipped("Aquamarine Shard")):
                self.c.removeItem(self.c.indexOfItem("Aquamarine Shard"))
                self.text = ("Ivana: Oh, thank you so much! Please, take "+
                             "this. It's all I have."+
                             "\nIvana gives you 10000 euros!")
                self.c.euros += 10000
                self.c.flags['Necklace Fixed'] = True
            elif 'Ivana Talk 3' in self.c.flags:
                self.text = ("Ivana: Could you get me a shard of aquamarine? I "+
                             "can reward you handsomely.")
            elif ('Ivana Talk 2' in self.c.flags and
                  self.c.flags['Ivana Level'] != self.c.level):
                self.text = ("Ivana: Wow Toshe! You look taller than "+
                             "last time! Where have you been? "+
                             "Anyway, I don't normally do this, but I have a "+
                             "small favour to ask of you. My necklace is broken "+
                             "but Petar is too lazy to find the Shield Man to fix "+
                             "it for me. I honestly don't know where the Shield "+
                             "Man is either. Long story short, I have another "+
                             "necklace, but it's not the same. It's missing a "+
                             "gem and that happens to be aquamarine. If I had "+
                             "one it would be like brand-new. So, basically, "+
                             "could you get me a shard of aquamarine? I can "+
                             "reward you handsomely.")
                self.c.flags['Ivana Talk 3'] = True
            elif 'Ivana Talk 1' in self.c.flags:
                self.text = ("Ivana: Hello, Toshe! Have you gone to The Bluffs "+
                             "against my word? Well, it's inevitable. Nobody "+
                             "listens to me. But, if you manage to get past "+
                             "The Bluffs, you will end up in Igalo. It's a "+
                             "small town close to the peninsula. Not much to "+
                             "do there, but it's a nice change in scenery from "+
                             "Herceg Novi.")
                self.c.flags['Ivana Talk 2'] = True
                self.c.flags['Ivana Level'] = self.c.level
            elif ('Ivana Talk 1' not in self.c.flags and
                  'Petar Bluffs' in self.c.flags):
                self.text = ("Ivana: Hi there, stranger! Don't listen to "+
                             "everything my husband Petar says. He knows all "+
                             "about Herceg Novi, but The Bluffs are a dangerous "+
                             "place to go sightseeing! Only go out there if you "+
                             "are really prepared.")
                self.c.flags['Ivana Talk 1'] = True
            else:
                self.text = choice(
                    ["Ivana: I want to be forever young.",
                     "Ivana: I wanna be the very best.",
                     "Ivana: I want to break free.",
                     "Ivana: I wanna rock!"])
        elif npc == "Boris":
            if 'Boris' not in self.c.flags:
                self.text = ("Boris: Hello. I am Boris.")
                self.c.flags['Boris'] = True
            elif "Tipsy Tuesday" in self.c.flags:
                self.text = ("Boris: Hello. I am drunk.")
            else:
                self.text = choice(["Boris: Igalo is a magic town that is "+
                                    "west. Go there to learn magic. I do "+
                                    "not know magic.",
                                    "Boris: Mountains are north. Go "+
                                    "there for training.",
                                    "Boris: I do not know much. What I know "+
                                    "I am certain of.",
                                    "Boris: If you need to go to Macedonia, "+
                                    "it is southeast. Very far southeast.",
                                    "Boris: Deep in the mountain there is "+
                                    "great treasure. I am sure of this.",
                                    "Boris: There is a knights' post north "+
                                    "of this city where you can learn combat."])
        elif npc == "Dado":
            token = choice(["Euros",
                            "No Coin",
                            "No Coin",
                            "No Coin"])
            if 'Dado' not in self.c.flags:
                self.text = ("Dado: Hoho, how do you do? The name's Dado!")
                self.c.flags['Dado'] = True
            elif "Tipsy Tuesday" in self.c.flags:
                self.text = ("Dado: Fuckin' fuck! Let's do something crazy!")
            elif (token == "Euros" and
                  'Dado Chat 1' in self.c.flags and
                  'Dado Euros' not in self.c.flags):
                self.text = ("Dado: Ho ho! Pay day! Yippee! Sharing is caring!"+
                             "\nDado hands you 4 euros."+
                             "\nDado: Ok, thank me later you ungrateful pig!")
                self.c.euros += 4
                self.c.flags['Dado Euros'] = True
            else:
                if 'Ivana' in self.c.flags:
                    generatedText = ("Ivana: Hi, Dado!"+
                             "\nDado: Oh, hello, Ivana! What a lovely "+
                             "dress!"+
                             "\nIvana: Thank you!")
                else:
                    generatedText = ("Dado: Achoo! See? Nobody reads the "+
                                     "dialogue.")
                self.text = choice([
                    "Dado: Ho! I heard that Ivana's cheating! Not "+
                    "in cards, either!",
                    "Dado: Ho, ho, ho! What a fine day out!",
                    "Dado: Ho, take it from me, the Shield Man isn't "+
                    "coming back. Sorry.",
                    "Dado: Hoho, I wonder what today's special is.",
                    "Dado: That blacksmith in the corner is "+
                    "definitely going out of business soon, hoho!",
                    "Dado: Why can't we all just get along?",
                    "Dado: I heard Boris tried stealing clothes from "+
                    "that dog. Apparently, the mutt bit him right on "+
                    "the ass!",
                    "Dado: That bartender sure seems a "+
                    "little queer, hoho!",
                    generatedText])
                self.c.flags['Dado Chat 1'] = True
        return self.actions()

    def leftBridge(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if 'Sad Man' not in self.c.flags:
            self.text = ("Sad Man: I'm disappointed. I traveled all the way from "+
                         "Moldova to get a world famous shield from the Shield "+
                         "Man, but he's gone. I wonder where he would go. He "+
                         "just abandoned his shop like that.")
            self.c.flags['Sad Man'] = True
        elif ("Tipsy Tuesday" in self.c.flags and
              "Sad Man Dead" not in self.c.flags):
            self.text = ("Happy Man: I found him! I found the Shield Man!")
        elif "Sad Man Dead" not in self.c.flags:
            self.text = ("Sad Man: Did you find the Shield Man?")
            if ( "Shield Man" in self.c.flags and
                 "Sad Man Dead" not in self.c.flags):
                self.text += ("\nToshe: Yes, he's in Igalo." +
                              "\nSad Man: But that's too far! You're lying!")
                if self.c.hasMercenary("Barrie"):
                    outcome = choice([1, 2, 3])
                    if outcome == 1:
                        self.text += ("\nBarrie: Who ya callin' a liar? He's" +
                                      " not lying!" +
                                      "\nBarrie draws his wand." +
                                      "\nSad Man: Help!" +
                                      "\nToshe: Calm down, it's ok.")
                    elif outcome == 2:
                        self.text += ("\nBarrie: Look here, nobody's lying." +
                                      " You don't" +
                                      " want to start with these sorts" +
                                      " of accusations." +
                                      "\nSad Man: I just want the Shield" +
                                      " Man back..." +
                                      "\nToshe: So do we, so do we.")
                    elif outcome == 3:
                        self.text += ("\nBarrie: Who ya callin' a liar? He's" +
                                      " not lying!" +
                                      "\nBarrie draws his wand." +
                                      "\nSad Man: Help!" +
                                      "\nToshe: Calm down, it's ok." +
                                      "\nAs the sad man tries to escape," +
                                      " Barrie blows him" +
                                      " to smithereens." +
                                      "\nToshe: Maybe it's not ok.")
                        self.c.flags['Sad Man Dead'] = True
        return self.actions()

    def smithEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 3
            Y = 1
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        self.text = ("Blacksmith: Why, hello there!"+
                     "\nYou hear the blacksmith calling you from the window.")
        self.menu = ["Enter the blacksmith's."]
        return self.actions()

    def corridor(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("You read a sign:"+
                     "\n\"Left: Mayor's District"+
                     "\nRight: Town Square\"")
        return self.actions()

    def fork(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def castle(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def alley2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def alley1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = choice(
            ["You hear someone playing the lute."+
             "\nToshe: Damn it! I hate that sound!",
             "You hear very clearly, with almost one hundred percent "+
             "certainty, the mayor "+
             "arguing about the price of "+choice(["onions",
                                                   "rice",
                                                   "cabbage",
                                                   "carp",
                                                   "hummus"])+".",
             None,
             None,
             None,
             None,
             None])
        return self.actions()

    def square(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and "About to Leave" in self.c.flags:
            del self.c.flags['About to Leave']
            X = 5
            Y = 8
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0 and "Tipsy Tuesday" not in self.c.flags:
            self.text = ("Guard: The mayor is currently engaged in other "+
                         "business. Please come back later.")
            self.menu = ["Approach the guards."]
        elif selectionIndex == 0 and "Tipsy Tuesday" in self.c.flags:
            self.text = ("Guard: Ah! A visitor! Come in! Mirko loves company!")
            self.menu = ["Enter the Mayor's Residence."]
            self.tempFlag = "About to Leave"
        elif ("Tipsy Tuesday" in self.c.flags and
              self.c.hasItem("Letter from the Mayor")):
            self.text = ("Guard: Have a funtastic day!")
        else:
            self.text = ("There are two guards by a door.")
            self.menu = ["Approach the guards."]
        return self.actions()

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("It looks like you can hop over the wall to get to the "+
                     "docks, but you won't be able to jump over from the "+
                     "other side.")
        return self.actions()

    def stairs1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = ("There is a set of stairs leading to the bluffs.")
        return self.actions()

    def stairs2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = choice(["You almost jump as a kid pops out of the bushes."+
                            "\nKid: Be careful man! Monsters up there!"+
                            "\nThe kid points up the stairs as though you've "+
                            "never killed anything in your life.",
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None])
        return self.actions()

    def tavern(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.text = ("Bartender Daniel: "+choice(
["Strength makes you stronger. Hand weapons will do more "+
 "damage and you will do more critical damage. Dexterity makes you nimbler. "+
 "Bows will hit harder and you will land more hits, more critical hits, and "+
 "more blocks if you are using a shield. Wisdom makes you smarter. Wands "+
 "will shoot more powerful blasts and your resistance to the elements will "+
 "rise.",
 "You may be tempted to learn every skill, but don't waste your money--"+
 "you can only remember four at a time.",
 "Try to keep most of your stat points in one area. A few dexterity points "+
 "wouldn't hurt a warrior. However, giving a bowman wisdom isn't the wisest "+
 "idea.",
 "If you are lost, just find me! Then, I'll tell you this: talk to everyone "+
 "in town. They'll give you direction. Or at least a few chores.",
 "You can't use two weapons. It just doesn't work. Trust me on this.",
 "You can't use two shields. Why would you?",
 "Each time you level up you get five stat points to spend and your health "+
 "and energy increase by twenty.",
 "Walking around outside of battle will restore energy. You get 1% of your "+
 "energy back every step you take.",
 "Buy a drink and we can talk about what's going on in the city.",
 "Here's how you can make your own pina colada: blend three ounces of rum, "+
 "three tablespoons of coconut cream and three tablespoons of pineapple with "+
 "a lotta crushed ice. You can substitute coconut milk if it's not too "+
 "thin for you."]
)
                         )
        elif selectionIndex == 1:
            if self.c.euros >= 2 and "Tipsy Tuesday" not in self.c.flags:
                self.c.euros -= 2
                self.text = ("Bartender Daniel: Here you are.")
                if 'Daniel Quest 1' not in self.c.flags:
                    self.text += (" Hey, let me let you in on something. "+
                                  "The Rumadan men roaming the fields outside "+
                                  "have been pillaging the gin and Vojo is "+
                                  "getting upset. You're a mercenary, right? "+
                                  "Take care of 2 Rumadan men for me to teach "+
                                  "them a lesson.")
                    if 'Rumadan Man' in self.c.flags['Kills']:
                        self.c.flags['Daniel Quest 1'] = \
                                            self.c.flags['Kills']['Rumadan Man']
                    else:
                        self.c.flags['Daniel Quest 1'] = 0
                elif ('Daniel Quest 1 Complete' not in self.c.flags and
                      'Daniel Quest 1' in self.c.flags and
                      'Rumadan Man' in self.c.flags['Kills'] and
                      self.c.flags['Kills']['Rumadan Man']-2 >=
                      self.c.flags['Daniel Quest 1']):
                    self.text += (" Oh, you did it? You killed them? Nice! "+
                                  "Here, take this. No need to thank me."+
                                  "\nDaniel gives you 20 euros.")
                    self.c.euros += 20
                    self.c.flags['Daniel Quest 1 Complete'] = True
                elif ('Daniel Quest 1 Complete' in self.c.flags and
                      'Daniel Quest 2' not in self.c.flags):
                    self.text += (" Ok, here's the scoop. We need more crab "+
                                  "for the crab soup we're going to serve. "+
                                  "Get me a nice Kotor crab. Make sure it's "+
                                  "dead though; I don't like dealing with "+
                                  "those things.")
                    if 'Kotor Crab' in self.c.flags['Kills']:
                        self.c.flags['Daniel Quest 2'] = \
                                             self.c.flags['Kills']['Kotor Crab']
                    else:
                        self.c.flags['Daniel Quest 2'] = 0
                elif ('Daniel Quest 2 Complete' not in self.c.flags and
                      'Daniel Quest 2' in self.c.flags and
                      'Kotor Crab' in self.c.flags['Kills'] and
                      self.c.flags['Kills']['Kotor Crab']-1 >=
                      self.c.flags['Daniel Quest 2']):
                    self.text += (" Thanks for the crab. Take this."+
                                  "\nDaniel gives you 30 euros.")
                    self.c.euros += 30
                    self.c.flags['Daniel Quest 2 Complete'] = True
                elif ('Daniel Quest 2 Complete' in self.c.flags and
                      'Daniel Quest 3' not in self.c.flags):
                    self.text += (" Hey. There's a wanted man in Herceg Novi "+
                                  "known only as \"Dr. Grabh.\" Do what you "+
                                  "will with that information.")
                    self.c.flags['Daniel Quest 3'] = True
                elif ('Daniel Quest 3 Complete' not in self.c.flags and
                      'Daniel Quest 3' in self.c.flags and
                      'Dr. Grabh' in self.c.flags['Kills']):
                    self.text += (" I heard you finished off Dr. Grabh. "+
                                  "Here's the bounty."+
                                  "\nDaniel gives you 100 euros.")
                    self.c.euros += 100
                    self.c.flags['Daniel Quest 3 Complete'] = True
                elif 'Daniel Quest 3 Complete' in self.c.flags:
                    self.text += ("\nToshe: How do I get to Macedonia?"+
                                  "\nBartender Daniel: You want to go to "+
                                  "Macedonia? You'll have to go through the "+
                                  "Black Mountain up north.")
            elif "Tipsy Tuesday" in self.c.flags:
                self.text = ("Bartender Daniel: On the house!")
            else:
                self.text = ("Bartender Daniel: Sorry, that's not the right "+
                             "number of euros.")
        elif selectionIndex == 2:
            X = 1
            Y = 7
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 3:
            X = 5
            Y = 3
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        else:
            if 'Rested' in self.c.flags:
                self.text = ("You fall asleep."+
                             "\nWhen you wake up, you return to the front "+
                             "to give Daniel your key."+
                             "\nBartender Daniel: Did you enjoy your stay?")
                del self.c.flags['Rested']
                del self.c.flags['Herceg Novi Room Level']
            elif ('Herceg Novi Room Level' in self.c.flags and
                  self.c.flags['Herceg Novi Room Level'] < self.c.level):
                self.text = ("Bartender Daniel: Your room time has expired. "+
                             "I'll have to take your key now.")
                del self.c.flags['Herceg Novi Room Level']
            elif 'Bartender Daniel' not in self.c.flags:
                self.text = ("Bartender Daniel: Welcome to Vojo's Inn and "+
                             "Tavern. How may I be of service?")
                self.c.flags['Bartender Daniel'] = True
            elif "Tipsy Tuesday" in self.c.flags:
                self.text = ("Bartender Daniel: "+
                             "It's Tipsy Tuesday! Time to drink, my friend!")
            else:
                self.text = ("Bartender Daniel: "+
                             choice(["This drink is taking forever to pour!",
                                     "Good afternoon!",
                                     "It's a pleasure to see you once again!",
                                     "Well, if it isn't my favourite customer!",
                                     "I swear, this is the longest day of the "+
                                     "year, and I decide to put on suspenders.",
                                     "I'll keep grinning as long as I'm "+
                                     "ginning!"]
                                    )
                             )
                self.text += (" How may I be of service?")
        if  ('Herceg Novi Room Level' in self.c.flags and
             "Tipsy Tuesday" not in self.c.flags):
            self.menu = ["Ask for advice.",
                         "Buy a drink (2 euros).",
                         "Return to your room.",
                         "Leave."]
        elif ('Herceg Novi Room Level' in self.c.flags and
              "Tipsy Tuesday" in self.c.flags):
            self.menu = ["Ask for advice.",
                         "Get a drink.",
                         "Return to your room.",
                         "Leave."]
        elif (self.c.euros < 5 and
              "Tipsy Tuesday" not in self.c.flags):
            self.menu = ["Ask for advice.",
                         "Buy a drink (2 euros).",
                         "Get a room.",
                         "Leave."]
        elif (self.c.euros < 5 and
              "Tipsy Tuesday" in self.c.flags):
            self.menu = ["Ask for advice.",
                         "Get a drink.",
                         "Get a room.",
                         "Leave."]
        elif "Tipsy Tuesday" not in self.c.flags:
            self.menu = ["Ask for advice.",
                         "Buy a drink (2 euros).",
                         "Get a room (5 euros).",
                         "Leave."]
        elif "Tipsy Tuesday" in self.c.flags:
            self.menu = ["Ask for advice.",
                         "Get a drink.",
                         "Get a room (5 euros).",
                         "Leave."]
        return self.actions()

    def bedroom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 21
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.flags['Rested'] = True
            self.c.hp = self.c.maxHp
            self.c.ep = self.c.maxEp
            X = 1
            Y = 5
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            X = 1
            Y = 5
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        if 'Herceg Novi Room Level' not in self.c.flags:
            if self.c.euros >= 5:
                self.c.euros -= 5
                self.text = ("Daniel takes you to a room. "+
                             "You give him 5 euros and he hands you a key.")
            else:
                self.text = ("Bartender Daniel: You need a place to stay? "+
                             "Don't worry about the money."+
                             "\nDaniel takes you to a room and gives you a "+
                             "key.")
            self.c.flags['Herceg Novi Room Level'] = self.c.level
        else:
            self.text = ("You walk inside your room and lock the door.")
        self.menu = ["Sleep.",
                     "Leave your room."]
        return self.actions()

    def smith(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 22
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 8
            Y = 3
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        if 'Herceg Novi Blacksmith' not in self.c.flags:
            self.text = ("Blacksmith: Hi. This is my workshop. Not your "+
                         "typical blacksmith, eh?")
            self.c.flags['Herceg Novi Blacksmith'] = True
        elif ("Key Hunting" in self.c.flags and
              "Macedonian Gate Opened" not in self.c.flags):
            self.text = ("Blacksmith: It's a key you're looking to make?" +
                         " Why not" +
                         " try the Shield Man? He's good with all sorts of" +
                         " fine metal pieces.")
        else:
            self.text = choice(["Blacksmith: I can't smith shields. The Shield"+
                                " Man is a much better bet for that.",
                                "Blacksmith: These are the best weapons "+
                                "you can find in Herceg Novi!",
                                "Blacksmith: I would make armour, but Lina "+
                                "has you covered.",
                                "Blacksmith: Hot off the anvil!"])
        self.menu = ["Leave."]
        return self.actions({'items for sale': ["Small Dagger",
                                                "Emerald Dagger",
                                                "Pine Bow",
                                                "Rapier",
                                                "Cleaver",
                                                "Cudgel",
                                                "Battle Axe",
                                                "Mace",
                                                "Double Axe"]})

    def clothier(self, selectionIndex=None):
        self.view = "store"
        self.imageIndex = 23
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 7
            Y = 5
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 1:
            self.imageIndex = 24
            self.view = "battle"
            if "Silvio Slain" in self.c.flags:
                enemy = "Lina3"
            else:
                enemy = choice(["Lina1", "Lina2"])
            return self.actions({'enemy': enemy,
                                 'mercenaries': self.c.mercenaries})            
        if 'Juliana' not in self.c.flags:
            self.text = ("Juliana: Hey! You must be new in town. I'm Juliana."+
                         " If you need anything, just ask my dog, Lina, to"+
                         " grab it for you.")
            self.c.flags['Juliana'] = True
            self.menu = ["Leave."]
        elif ("Key Hunting" in self.c.flags and
              "Macedonian Gate Opened" not in self.c.flags):
            self.text = ("Toshe: Juliana, can you help me find a goldsmith?" +
                         " I'm trying to forge a key to save my homeland." +
                         "\nJuliana: Oh, you're on a quest!" +
                         " That sounds exciting. I think there might be" +
                         " someone that could help you in Igalo. Good luck!")
            self.menu = ["Leave."]
        else:
            self.imageIndex = 24
            self.text = "Lina: " + choice(["Woof!",
                                           "Arf arf!",
                                           "Yip yip yaouuuw!!"])
            self.menu = ["Leave.",
                         "Attempt to steal from Lina."]
        return self.actions({'items for sale': ["Cassock",
                                                "Wool Gambeson",
                                                "Wool Doublet",
                                                "Leather Gambeson",
                                                "Leather Doublet",
                                                "Canvas Gambeson",
                                                "Canvas Doublet",
                                                "Magerobe",
                                                "Velvet Doublet"]})

    def mayorsOffice(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 25
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Mayor Mirko"
        if (selectionIndex == 0 and
            "About to Leave" in self.c.flags):
            del self.c.flags['About to Leave']
            X = 3
            Y = 6
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        elif (selectionIndex == 0 and
              "Mirko Intro" in self.c.flags and
              "Mirko Talk 1" not in self.c.flags):
            del self.c.flags['Mirko Intro']
            self.text = ("Toshe: I need your signature." +
                         "\n%s: NO! Leave NOW!" % npc +
                         "\nThe mayor kicks you out of his office.")
            self.menu = ["Get kicked out."]
            self.tempFlag = "About to Leave"
        elif (selectionIndex == 0 and
             "Mirko Talk 1" in self.c.flags and
              "Mirko Talk 2" not in self.c.flags):
            del self.c.flags['Mirko Talk 1']
            self.text = ("Toshe: So can you sign a letter for me?" +
                         "\n%s: What does it say?" % npc +
                         "\nToshe: Basically that I'm important enough to" +
                         " talk to the Macedonian president." +
                         "\n%s: NO! Leave NOW!" % npc +
                         "\nThe mayor kicks you out of his office.")
            self.menu = ["Get kicked out."]
            self.tempFlag = "About to Leave"
        elif (selectionIndex == 0 and
             "Mirko Talk 2" in self.c.flags and
              "Mirko Talk 3" not in self.c.flags):
            del self.c.flags['Mirko Talk 2']
            self.text = ("Toshe: Could you sign a letter for me?" +
                         "\n%s: Sure, son. Let me just find some ink." % npc +
                         "\n%s grabs a jar of ink, but it slips," % npc +
                         " spilling everywhere." +
                         "\n%s is furious." % npc +
                         "\n%s: Leave NOW!" % npc +
                         "\nThe mayor kicks you out of his office.")
            self.menu = ["Get kicked out."]
            self.tempFlag = "About to Leave"
        elif (selectionIndex == 0 and
             "Mirko Talk 3" in self.c.flags):
            del self.c.flags['Mirko Talk 3']
            self.text = ("You grab the parchment from the table." +
                         "\nThe mayor is too drunk to notice, or care." +
                         "\nToshe: See ya later, Mirko!" +
                         "\n%s: Farewell, Yoshi!" % npc)
            self.menu = ["Leave."]
            self.tempFlag = "About to Leave"
            self.c.flags['Got Letter'] = True
            return self.actions({'item': "Letter from the Mayor"})
        elif (selectionIndex == 1 and
              "Mirko Intro" in self.c.flags and
              "Mirko Talk 1" not in self.c.flags):
            del self.c.flags['Mirko Intro']
            self.text = ("Toshe: Toshe." +
                         "\n%s: TouCHE!! HAhahahAha!" % npc +
                         "\nToshe: Toshe. That's my name." +
                         "\n%s: I like that, son." % npc)
            self.menu = ["Ask for the signature.",
                         "Talk about the weather.",
                         "Talk about sports."]
            self.tempFlag = "Mirko Talk 1"
        elif (selectionIndex == 1 and
              "Mirko Talk 1" in self.c.flags and
              "Mirko Talk 2" not in self.c.flags):
            del self.c.flags['Mirko Talk 1']
            self.text = ("Toshe: So how are you enjoying this nice weather?" +
                         "\n%s: Hoh, I love it." % npc +
                         "\nToshe: Who's a ho?" +
                         "\n%s: I like that, son." % npc)
            self.menu = ["Ask for the signature.",
                         "Discuss politics.",
                         "Discuss food."]
            self.tempFlag = "Mirko Talk 2"
        elif (selectionIndex == 1 and
              "Mirko Talk 2" in self.c.flags and
              "Mirko Talk 3" not in self.c.flags):
            del self.c.flags['Mirko Talk 2']
            self.text = ("Toshe: What new laws are being passed these days?" +
                         "\n%s: Are you saying I don't work hard" % npc +
                         " enough? Begone!" +
                         "\nToshe: No, no, just making conversation." +
                         "\n%s: BeGONE!" % npc +
                         "\nThe mayor kicks you out of his office.")
            self.menu = ["Get kicked out."]
            self.tempFlag = "About to Leave"
        elif (selectionIndex == 1 and
              "Mirko Talk 3" in self.c.flags):
            del self.c.flags['Mirko Talk 3']
            self.text = ("Toshe: Hey, what's that?" +
                         "\n%s: What's what? Ouch!" % npc +
                         "\nThe mayor twists his body out of his chair." +
                         "\nToshe: Oops, sorry." +
                         "\n%s: Guards!!" % npc +
                         "\nThe mayor's guards come in and" +
                         " stab you, then drag you out.")
            self.c.hp -= 150
            self.menu = ["Get dragged out."]
            self.tempFlag = "About to Leave"
        elif (selectionIndex == 2 and
              "Mirko Talk 1" in self.c.flags and
              "Mirko Talk 2" not in self.c.flags):
            del self.c.flags['Mirko Talk 1']
            self.text = ("Toshe: So what do you think about jousting?" +
                         "\n%s: What's that, son?" % npc +
                         "\nToshe: Jousting, like horses and stuff." +
                         "\n%s: I hate horses! Leave NOW!" % npc +
                         "\nThe mayor kicks you out of his office.")
            self.menu = ["Get kicked out."]
            self.tempFlag = "About to Leave"
        elif (selectionIndex == 2 and
              "Mirko Talk 2" in self.c.flags and
              "Mirko Talk 3" not in self.c.flags):
            del self.c.flags['Mirko Talk 2']
            self.text = ("Toshe: What's some good food around here?" +
                         "\n%s: Well." % npc +
                         "\nSuddenly %s becomes very attentive." % npc +
                         "\n%s: Well...there is one thing. This new" % npc +
                         " fruit, the Mirkoberry, that I discovered in a" +
                         " bush outside. It leaves a permanent mark on" +
                         " anything it touches!" +
                         "\n%s writes his name onto a piece of" % npc +
                         " parchment." +
                         "\n%s: This won't fade!" % npc)
            self.menu = ["Grab the parchment.",
                         "Distract the mayor."]
            self.tempFlag = "Mirko Talk 3"
        else:
            self.text = ("You encounter a drunk mayor." +
                         "\nToshe: Hi." +
                         "\n%s: Hmm and how--who are you?" % npc +
                         "\nThe mayor lets out a subtle yet noticeable belch.")
            self.menu = ["\"I need your signature.\"",
                         "\"Toshe.\""]
            self.tempFlag = "Mirko Intro"
        return self.actions()
