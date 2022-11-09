"""
File: TUAColiseum.py
Author: Ben Gardner
Created: August 10, 2015
Revised: November 9, 2022
"""


import random


class Coliseum:

    name = "Coliseum"
    audio = "The Price of Glory"

    def __init__(self, character):
        self.foes = [
            "Greek Duelist",
            "Greek Swordsman",
            "Greek Fighter",
            "Greek Gladiator",
            "Greek Knight"
            ]
        self.heroBodies = [
            "Greek Hero1",
            "Greek Hero2",
            "Greek Hero3",
            "Greek Hero4",
            "Greek Hero5",
            "Greek Hero6",
            "Greek Hero7",
            "Greek Hero8",
            "Greek Hero9"
            ]
        self.heroSouls = []
        self.champions = [
            "The Bladedriver",
            "The Gashmaster",
            "The Impaler",
            "The Pummeler"
            ]
        self.championSkills = {
            'The Bladedriver': "Bladedriver's Barbarity",
            'The Gashmaster': "Gashmaster's Grace",
            'The Impaler': "Impaler's Impulse",
            'The Pummeler': "Pummeler's Precision"
            }
        self.foeText = []
        self.heroText = []
        self.championText = []
        with open("data\\coliseumdata.txt", "r") as fileIn:
            # Strip header
            fileIn.readline()
            for line in fileIn:
                tokens = line.strip().split("\t")
                name = tokens[0]
                multiplicative = int(tokens[1])
                stats = eval(tokens[2])
                stats['NAME'] = name
                self.heroSouls.append({'Multiplicative': multiplicative,
                                       'Stats': stats})
        with open("data\\coliseumtext.txt", "r") as fileIn:
            fileIn.readline()
            for line in fileIn:
                tokens = line.strip().split("\t")
                self.foeText.append(tokens[0])
                self.heroText.append(tokens[1])            
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"
        self.winnings = 0
        self.heroesDefeated = 0
        self.CHARACTER_DEATH_HP = 100
        self.championDefeated = False

        coli = self.coliseum
        duel = self.duelArena
        
        self.spots = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, coli, None, None, None, duel, None],
            [None, None, None, None, None, None, None, None],
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

    def coliseum(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []

        entryFee = 1000

        if ( selectionIndex == 0 and self.c.hp <= self.CHARACTER_DEATH_HP):
            self.text = ("Guard: Sir, you are not fit to fight. Take a" +
                         " rest and come back.")
        elif (selectionIndex == 0 and self.c.euros < entryFee):
            self.text = "Guard: One thousand euros to enter, sir."
        elif selectionIndex == 0:
            self.c.euros -= entryFee
            X = 6
            Y = 2
            return self.actions({'area': "Coliseum",
                                 'coordinates': (X, Y)})            
        elif "Coliseum" not in self.c.flags or selectionIndex == 1:
            self.text = ("Champion: My fellow warrior, have you come to" +
                         " do battle? Have you come to win the hearts of" +
                         " fans and the gold of foes? Well, good!" +
                         "\nYou shall duel, one by one, an array of" +
                         " fighters until you have demonstrated your might," +
                         " after which you shall face a formidable hero." +
                         " With each victory you shall accumulate more coin." +
                         " If you lose, you shall walk away with nothing but" +
                         " shame!" +
                         " Those who" +
                         " prove their worth against the most valiant" +
                         " of knights shall be honoured with a visit to the" +
                         " Fortress of Greece! Are you ready, warrior?")
            self.c.flags['Coliseum'] = True
        elif selectionIndex == 2:
            X = 3
            Y = 3
            return self.actions({'area': "Athens",
                                 'coordinates': (X, Y)})
        elif "Lost the Battle" in self.c.flags:
            del self.c.flags['Lost the Battle']
            self.text = ("Champion: How dishonourable! Rise and" +
                         " fight again, warrior!")
        elif "Kicked Out" in self.c.flags:
            del self.c.flags['Kicked Out']
            self.text = ("Guard: Please do not save while in the pit.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: The hell's he talkin' about?")
            elif self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: It seems as though progress" +
                              " shall not be recorded whilst one is dueling.")
        elif "Coliseum Winnings" in self.c.flags:
            if ( "Champion Defeated" in self.c.flags and
                 "Coliseum Complete" not in self.c.flags):
                self.text = ("You receive " +
                             str(self.c.flags['Coliseum Winnings']) +
                             " euros." +
                             "\nChampion: What an incredible feat!" +
                             " Warrior, it has become clear to" +
                             " me that your skill in combat is superior to" +
                             " mine. I have not had a duel of that caliber" +
                             " in over a decade. You have earned the" +
                             " privilege of a grand tour!" +
                             " Guards, lead this man to the fortress!" +
                             "\nThree escorts assemble around you and" +
                             " point you westward in the direction of the" +
                             " fortress.")
                self.c.euros += self.c.flags['Coliseum Winnings']
                self.c.flags['Coliseum Complete'] = True
                del self.c.flags['Champion Skill']
                del self.c.flags['Champion Defeated']
                del self.c.flags['Coliseum Winnings']
            elif "Champion Defeated" in self.c.flags:
                self.text = ("You receive " +
                             str(self.c.flags['Coliseum Winnings']) +
                             " euros." +
                             "\nChampion: A heroic display of proficiency," +
                             " champion. I shall bestow upon you a gift to" +
                             " bolster your might in future trials.")
                self.c.euros += self.c.flags['Coliseum Winnings']
                skillName = self.c.flags['Champion Skill']
                del self.c.flags['Champion Skill']
                del self.c.flags['Champion Defeated']
                del self.c.flags['Coliseum Winnings']
                self.menu = ["Enter the pit (%s euros)." % entryFee,
                             "Ask for the rules.",
                             "Leave."]
                return self.actions({'skill': skillName,
                                     'cost': 0})
            else:
                self.text = ("Champion: Warrior, you've earned " +
                             str(self.c.flags['Coliseum Winnings']) +
                             " euros. Well done.")
                self.c.euros += self.c.flags['Coliseum Winnings']
                del self.c.flags['Coliseum Winnings']
        else:
            self.text = ("Champion: Welcome, warrior.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: Good luck, Toshe!")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Go kick butt in there, chap.")
        self.menu = ["Enter the pit (%s euros)." % entryFee,
                     "Ask for the rules.",
                     "Leave."]
        return self.actions()

    def duelArena(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if self.c.hp <= self.CHARACTER_DEATH_HP:
            del self.c.flags['Coliseum Opponents']
            self.c.flags['Lost the Battle'] = True
            X = 2
            Y = 2
            return self.actions({'area': "Coliseum",
                                 'coordinates': (X, Y)})          
        elif self.winnings == 0 and "Coliseum Opponents" in self.c.flags:
            del self.c.flags['Coliseum Opponents']
            self.c.flags['Kicked Out'] = True
            X = 2
            Y = 2
            return self.actions({'area': "Coliseum",
                                 'coordinates': (X, Y)})
        elif self.championDefeated:
            del self.c.flags['Coliseum Opponents']
            self.c.flags['Coliseum Winnings'] = self.winnings
            self.c.flags['Champion Defeated'] = True
            self.c.flags['Champion Skill'] = self.championSkill
            X = 2
            Y = 2
            return self.actions({'area': "Coliseum",
                                 'coordinates': (X, Y)})            
        elif selectionIndex == 0 or self.winnings == 0:
            numberOfOpponents = random.randint(2 * (self.heroesDefeated + 1),
                                               3 * (self.heroesDefeated + 1)
                                               + 1)
            opponents = []
            for i in range(0, numberOfOpponents):
                opponents.append(random.choice(self.foes))
            if self.heroesDefeated < 3:
                opponents.append(random.choice(self.heroBodies))
            elif self.heroesDefeated == 3:
                opponents.append(random.choice(self.champions))
            self.c.flags['Coliseum Opponents'] = opponents
        elif selectionIndex == 1:
            del self.c.flags['Coliseum Opponents']
            self.c.flags['Coliseum Winnings'] = self.winnings
            X = 2
            Y = 2
            return self.actions({'area': "Coliseum",
                                 'coordinates': (X, Y)})
        if self.c.flags['Coliseum Opponents']:
            self.view = "battle"
            enemy = self.c.flags['Coliseum Opponents'].pop(0)
            if enemy in self.foes:
                self.winnings += (self.foes.index(enemy) *
                                  10 *
                                  self.heroesDefeated ** 2 +
                                  110)
                self.text = enemy + ": " + random.choice(self.foeText)
                if random.randint(1, 13) == 1:
                    self.text = ("Heinz: Go Toshe!" +
                                 "\nBert: Kick his ass!" +
                                 "\nYou can see Bert and Heinz waving their" +
                                 " fists in the crowd.")
                return self.actions({'enemy': enemy,
                                     'coliseum': True})
            elif enemy in self.heroBodies:
                self.winnings += 1000 * (self.heroesDefeated + 1)
                self.heroesDefeated += 1
                soul = random.choice(self.heroSouls)
                text = random.choice(self.heroText)
                self.text = soul['Stats']['NAME'] + ": " + text
                if "*" in text:
                    self.text = (soul['Stats']['NAME'] + " " + text.strip("*"))
                return self.actions({'enemy': enemy,
                                     'coliseum': True,
                                     'enemy modifiers': soul})
            elif enemy in self.champions:
                self.winnings += 5000
                self.championDefeated = True
                self.championSkill = self.championSkills[enemy]
                if enemy == self.champions[0]:
                    self.text = ("Champion: Warrior, that was a spectacle" +
                                 " to behold. Now it is my turn to paint" +
                                 " a picture for the ages. The canvas, this" +
                                 " arena; the brush, my weapon. The" +
                                 " paint...")
                elif enemy == self.champions[1]:
                    self.text = ("Champion: You've come far, warrior." +
                                 " Very far. You are a formidable fighter." +
                                 " Is it possible that you can" +
                                 " hold up even against the greatest?")
                elif enemy == self.champions[2]:
                    self.text = ("Champion: What a display of talent!" +
                                 " Warrior! You are, so far," +
                                 " unstoppable! There is, however, a" +
                                 " way to combat this.")
                elif enemy == self.champions[3]:
                    self.text = ("Champion: I can see that you are a" +
                                 " masterful fighter. You have proven" +
                                 " your worth, warrior. I usually need" +
                                 " not prove mine, but I will make an" +
                                 " exception on this day.")
                return self.actions({'enemy': enemy,
                                     'coliseum': True})
        else:
            self.view = "store"
            self.text = ("Champion: Congratulations on your victory." +
                         " You may continue to battle more warriors or" +
                         " leave now with what you have earned." +
                         "\nColiseum Vendor: Or purchase this lovely item!")
            self.menu = ["Challenge the next opponent.",
                         "Leave and collect your winnings."]
            return self.actions({'items for sale': [random.choice(
                [
                    "Rusty Tower Shield",
                    "Rusty Titanium Shield",
                    "Wimpwood Wand",
                    "Moaning Star",
                    "Asp Bow"]),
                                                    None,
                                                    None,
                                                    None,
                                                    None,
                                                    None,
                                                    None,
                                                    None,
                                                    None]})
        return self.actions()
