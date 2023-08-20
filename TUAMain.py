"""
File: TUAMain.py
Author: Ben Gardner
Created: January 14, 2013
Revised: August 20, 2023
"""


import pickle
import random
from copy import deepcopy, copy
from collections import Counter
from datetime import date
from threading import Thread

from TUAWeapon import Weapon
from TUAArmour import Armour
from TUAShield import Shield
from TUAMiscellaneousItem import MiscellaneousItem
from TUASkill import Skill
from TUAEnemy import Enemy
from TUACharacter import Character
from TUABattle import Battle
from TUAQuest import Quest
from TUAForge import Forge
from TUAModifiers import Modifiers

from TUASound import Sound
from TUAPreferences import Preferences

from TUAAdriaticSea import AdriaticSea
from TUABoat import Boat
from TUAKismet import Kismet
from TUABayOfKotor import BayOfKotor
from TUAHercegNovi import HercegNovi
from TUAHercegBluffs import HercegBluffs
from TUAIgalo import Igalo
from TUAHercegFields import HercegFields
from TUABlackMountain import BlackMountain
from TUAMojkovacSummit import MojkovacSummit
from TUAMojkovacValley import MojkovacValley
from TUATheWatchmakingFacility import TheWatchmakingFacility
from TUACemetery import Cemetery
from TUAScutariPeninsula import ScutariPeninsula
from TUAWesternKosovo import WesternKosovo
from TUATheSecretLaboratory import TheSecretLaboratory
from TUAPec import Pec
from TUAAlbanianDesert import AlbanianDesert
from TUAEasternKosovo import EasternKosovo
from TUAPristina import Pristina
from TUATrafCafe import TrafCafe
from TUAPresidentialPath import PresidentialPath
from TUAOldRuins import OldRuins
from TUARomadanVillage import RomadanVillage
from TUARomadanHideout import RomadanHideout
from TUAGambinoCastle import GambinoCastle
from TUAHiddenPassage import HiddenPassage
from TUAGreece import Greece
from TUAAthens import Athens
from TUAColiseum import Coliseum
from TUAThessaloniki import Thessaloniki
from TUAGreekFortress import GreekFortress
from TUAMacedonia import Macedonia
from TUACredits import Credits
from TUAGolemCavern1 import GolemCavern1
from TUAGolemCavern2 import GolemCavern2
from TUAGolemCavern3 import GolemCavern3
from TUASimelliermPit import SimelliermPit
from TUAGalijula import Galijula
from TUAFartooqHold import FartooqHold
from TUAYaouwVolcano import YaouwVolcano
from TUADuneHotsPeak import DuneHotsPeak
from TUALairOfTheMagi import LairOfTheMagi
from TUAIgaloCathedral import IgaloCathedral
from TUALitochoro import Litochoro
from TUAMountOlympus import MountOlympus
from TUALabyrinthOfDaedalus import LabyrinthOfDaedalus


class Main:
    """This object acts as an interface between the GUI and the Character and
    Area objects, passing user input to make changes to the character and return
    character and area information back to the GUI.

    currentArea should always be associated with an object.
    currentSpot should always be associated with a method.
    """

    def __init__(self):
        self.view = None
        self.character = None
        self.weapons = {}
        self.armour = {}
        self.shields = {}
        self.miscellaneousItems = {}
        self.skills = {}
        self.enemies = {}
        self.mercenaries = {}
        self.allQuests = []
        self.populateWeapons()
        self.populateArmour()
        self.populateShields()
        self.populateMiscellaneousItems()
        self.items = dict(self.weapons.items() +
                          self.armour.items() +
                          self.shields.items() +
                          self.miscellaneousItems.items())
        self.evasiveItems = set([
            "Moon Armour",
            "Ugly Disguise",
        ])
        self.populateSkills()
        self.populateEnemies()
        self.populateMercenaries()
        self.populateQuests()
        self.populateAreas()
        self.buyback = False
        self.sound = Sound()
        self.towns = set([
            "Herceg Novi",
            "Igalo",
            "Mojkovac Valley",
            "Pec",
            "Pristina",
            "Romadan Village",
            "Athens",
            "Litochoro",
        ])
        self.resetForge()

    def markMap(self, xy = None):
        marked = self.character.flags['Marked Areas'][self.currentArea.name]
        if xy is not None:
            if (xy[0], xy[1]) in marked:
                marked.remove((xy[0], xy[1]))
                return False
            else:
                marked.add((xy[0], xy[1]))
                return True
        if (self.x, self.y) in marked:
            marked.remove((self.x, self.y))
            return False
        else:
            marked.add((self.x, self.y))
            return True

    def loadGame(self, fileName):
        """Load a game from a savefile."""
        self.fileName = fileName
        with open("saves/"+self.fileName+".tq", "r") as gameFile:
            self.character = pickle.load(gameFile)
        self.character.NAME = fileName
        self.initGame()
        self.sound.playSound(self.sound.sounds['Load'])
        Thread(target=self.writeGameToPreferences).start()

    def loadFromCheckpoint(self):
        self.character.checkpoint.flags['Discovered Areas'] = self.character.flags['Discovered Areas']
        self.character.checkpoint.flags['Marked Areas'] = self.character.flags['Marked Areas']
        self.character.checkpoint.flags['Config'] = self.character.flags['Config']
        self.character = self.character.checkpoint
        self.character.checkpoint = None
        self.character.checkpoint = deepcopy(self.character)
        self.initGame()
        self.sound.playSound(self.sound.sounds['Load'])

    def startNewGame(self, fileName, portrait, mode):
        """Create a new character and record it in a savefile."""
        STARTING_X = 3
        STARTING_Y = 17
        self.fileName = fileName
        self.character = Character(fileName, 1, 0, 100, 100, 100, 100, 100,
                                   10, 10, 10, [], 0, [], [None]*9,
                                   {'Weapon': None, 'Armour': None,
                                    'Shield': None},
                                   self.weapons['Fists'],
                                   self.armour['Cotton Shirt'],
                                   self.shields['Nothing'],
                                   self.weapons['Fists'],
                                   self.armour['Cotton Shirt'],
                                   self.shields['Nothing'],
                                   0,
                                   {'Kills': {},
                                    'Discovered Areas': {},
                                    'Marked Areas': {},
                                    'Config': {
                                        'Automap On': 1,
                                        'Mission Log Open': 0,
                                   }},
                                   self.areas['Adriatic Sea'],
                                   STARTING_X, STARTING_Y,
                                   0, portrait, mode)
        self.character.hp = self.character.maxHp - 50
        self.character.ep = self.character.maxEp    # Chris
        self.initGame()
        self.saveGame()

    def initGame(self):
        self.currentArea = self.character.area(self.character)
        self.x = self.character.x
        self.y = self.character.y
        self.initializeDefaultBattle()
        self.readyQuests = set()
        self.initializeQuests()
        self.initializeUnlocks()

    def saveLocation(self):
        self.character.area = self.currentArea.__class__
        self.character.x = self.x
        self.character.y = self.y

    def saveGame(self, sync=False):
        self.saveLocation()
        with open("saves/"+self.fileName+".tq", "w") as gameFile:
            pickle.dump(self.character, gameFile)
        self.sound.playSound(self.sound.sounds['Save'])
        if sync:
            self.writeGameToPreferences()
        else:
            Thread(target=self.writeGameToPreferences).start()

    def writeGameToPreferences(self):
        try:
            with open("settings/recent_games.tqp", "r") as existingPreferences:
                preferences = pickle.load(existingPreferences)
        except IOError:
            preferences = Preferences()
        paredDownChar = copy(self.character)
        paredDownChar.flags = {}
        if "Legend" in self.character.flags:
            paredDownChar.flags['Legend'] = True
        paredDownChar.checkpoint = None
        preferences.recentCharacters[self.fileName] = paredDownChar
        with open("settings/recent_games.tqp", "w") as preferencesFile:
            pickle.dump(preferences, preferencesFile)

    def writeUnlocksToPreferences(self):
        preferences = Preferences()
        preferences.unlocks = self.unlocks
        with open("settings/unlocks.tqp", "w") as preferencesFile:
            pickle.dump(preferences, preferencesFile)

    def updateUnlocks(self):
        unlockCriteria = {
            "Apoc": lambda c:
                all(flag in c.flags for flag in [
                    "Daniel Quest 3 Complete",
                    "Adam Quest 3 Complete",
                    "Bartender Igor Quest 3 Complete",
                    "Bartender Zhang Quest 3 Complete",
                ]),
            "M. Wizzard": lambda c:
                all(flag in c.flags for flag in [
                    "Mudslide",
                    "Floodtide",
                    "Hot Coals",
                ]),
            "Gumball Machine": lambda c:
                "Gigantic Crayons" in c.flags['Kills'],
            "Lily": lambda c:
                "Queen Bee" in c.flags['Kills'] or "Pot Apparition" in c.flags['Kills'],
            "Ultimate Mode": lambda c:
                "Conclusion" in c.flags,
        }
        for unlockable in unlockCriteria:
            if unlockable not in self.unlocks and unlockCriteria[unlockable](self.character):
                self.unlocks[unlockable] = True
                self.writeUnlocksToPreferences()
                if unlockable == "Ultimate Mode":
                    continue
                return True
        return False

    def populateAreas(self):
        self.areas = {'Adriatic Sea': AdriaticSea,
                      'Boat at Sea': Boat,
                      'Kismet II': Kismet,
                      'Bay of Kotor': BayOfKotor,
                      'Herceg Novi': HercegNovi,
                      'Herceg Bluffs': HercegBluffs,
                      'Igalo': Igalo,
                      'Herceg Fields': HercegFields,
                      'Black Mountain': BlackMountain,
                      'Mojkovac Summit': MojkovacSummit,
                      'Mojkovac Valley': MojkovacValley,
                      'The Watchmaking Facility': TheWatchmakingFacility,
                      'Cemetery': Cemetery,
                      'Scutari Peninsula': ScutariPeninsula,
                      'Western Kosovo': WesternKosovo,
                      'The Secret Laboratory': TheSecretLaboratory,
                      'Pec': Pec,
                      'Albanian Desert': AlbanianDesert,
                      'Eastern Kosovo': EasternKosovo,
                      'Pristina': Pristina,
                      'Traf Cafe': TrafCafe,
                      'Presidential Path': PresidentialPath,
                      'Old Ruins': OldRuins,
                      'Romadan Village': RomadanVillage,
                      'Romadan Hideout': RomadanHideout,
                      'Gambino Castle': GambinoCastle,
                      'Hidden Passage': HiddenPassage,
                      'Greece': Greece,
                      'Athens': Athens,
                      'Coliseum': Coliseum,
                      'Thessaloniki': Thessaloniki,
                      'Greek Fortress': GreekFortress,
                      'Macedonia': Macedonia,
                      'Credits': Credits,
                      'Golem Cavern: Floor 1': GolemCavern1,
                      'Golem Cavern: Floor 2': GolemCavern2,
                      'Golem Cavern: Floor 3': GolemCavern3,
                      'Simellierm Pit': SimelliermPit,
                      'Galijula': Galijula,
                      'Fartooq Hold': FartooqHold,
                      'Yaouw Volcano': YaouwVolcano,
                      'Dune Hots Peak': DuneHotsPeak,
                      'Lair of the Magi': LairOfTheMagi,
                      'Igalo Cathedral': IgaloCathedral,
                      'Litochoro': Litochoro,
                      'Mount Olympus': MountOlympus,
                      'Labyrinth of Daedalus': LabyrinthOfDaedalus,
                      }

    def populateWeapons(self):
        with open("data/weapondata.txt", "r") as weaponFile:
            weaponFile.readline()
            for line in weaponFile:
                tokens = line.strip().split("\t")
                name = tokens[0]
                price = tokens[1]
                element = tokens[2]
                requirementValue = tokens[3]
                power = tokens[4]
                requirementType = tokens[5]
                category = tokens[6]
                cRate = tokens[7]
                cDamage = tokens[8]
                self.weapons[name] = (Weapon(name, price, element,
                                             requirementValue, power,
                                             requirementType, category, cRate,
                                             cDamage))
    
    def populateArmour(self):
        with open("data/armourdata.txt", "r") as armourFile:
            armourFile.readline()
            for line in armourFile:
                tokens = line.strip().split("\t")
                name = tokens[0]
                price = tokens[1]
                element = tokens[2]
                requirementValue = tokens[3]
                defence = tokens[4]
                reduction = tokens[5]
                self.armour[name] = (Armour(name, price, element,
                                            requirementValue, defence,
                                            reduction))

    def populateShields(self):
        with open("data/shielddata.txt", "r") as shieldFile:
            shieldFile.readline()
            for line in shieldFile:
                tokens = line.strip().split("\t")
                name = tokens[0]
                price = tokens[1]
                element = tokens[2]
                requirementValue = tokens[3]
                defence = tokens[4]
                reduction = tokens[5]
                bRate = tokens[6]
                self.shields[name] = (Shield(name, price, element,
                                             requirementValue, defence,
                                             reduction, bRate))

    def populateMiscellaneousItems(self):
        with open("data/miscellaneousitemdata.txt", "r") as rFile:
            rFile.readline()
            for line in rFile:
                tokens = line.strip().split("\t")
                name = tokens[0]
                price = tokens[1]
                info = tokens[2]
                self.miscellaneousItems[name] = MiscellaneousItem(name,
                                                                  price,
                                                                  info)

    def populateSkills(self):
        with open("data/skilldata.txt", "r") as skillFile:
            skillFile.readline()
            for line in skillFile:
                tokens = line.strip().split("\t")
                name = tokens[0]
                category = tokens[1]
                permittedWeapons = eval(tokens[2])
                epUsed = tokens[3]
                multiplier = tokens[4]
                element = tokens[5]
                userEffects = eval(tokens[6])
                targetEffects = eval(tokens[7])
                text = tokens[8]
                flag = tokens[9]
                self.skills[name] = Skill(name, category, permittedWeapons,
                                          epUsed, multiplier, element,
                                          userEffects, targetEffects, text,
                                          flag)

    def populateEnemies(self):
        with open("data/enemydata.txt", "r") as enemyFile:
            enemyFile.readline()
            for line in enemyFile:
                tokens = line.strip().split("\t")
                identifier = tokens[0]
                name = tokens[1]
                image = tokens[2]
                level = tokens[3]
                hp = tokens[4]
                maxHp = tokens[5]
                damage = tokens[6]
                accuracy = tokens[7]
                cRate = tokens[8]
                cDamage = tokens[9]
                bRate = tokens[10]
                defence = tokens[11]
                earthReduction = tokens[12]
                waterReduction = tokens[13]
                fireReduction = tokens[14]
                physicalReduction = tokens[15]
                tempSkills = eval(tokens[16])
                skills = {}
                totalProbability = 0
                for s in tempSkills:
                    totalProbability += tempSkills[s]
                    skills[self.skills[s]] = tempSkills[s]
                skills[self.skills['Attack']] = 100-totalProbability
                items = eval(tokens[17])
                xp = tokens[18]
                euros = tokens[19]
                fleeable = tokens[20]
                deathHp = tokens[21]
                music = tokens[22]
                unique = tokens[23]
                living = tokens[24]
                rarity = tokens[25]
                self.enemies[identifier] = Enemy(identifier, name, image,
                                           level, hp, maxHp, damage, accuracy,
                                           cRate, cDamage, bRate, defence,
                                           earthReduction, waterReduction,
                                           fireReduction, physicalReduction,
                                           skills, items, xp, euros, fleeable,
                                           unique, living, rarity, deathHp,
                                           music)

    def populateMercenaries(self):
        with open("data/mercenarydata.txt", "r") as mercenaryFile:
            mercenaryFile.readline()
            for line in mercenaryFile:
                tokens = line.strip().split("\t")
                name = tokens[0]
                level = tokens[1]
                xp = tokens[2]
                xpTnl = tokens[3]
                maxHp = tokens[4]
                hp = maxHp
                maxEp = tokens[5]
                ep = maxEp
                strength = tokens[6]
                dexterity = tokens[7]
                wisdom = tokens[8]
                tempSkills = eval(tokens[9])
                skills = {}
                totalProbability = 0
                for s in tempSkills:
                    totalProbability += tempSkills[s]
                    skills[self.skills[s]] = tempSkills[s]
                skills[self.skills['Attack']] = 100-totalProbability
                euros = 0
                items = [None]*9
                equippedItemIndices = {'Weapon': None, 'Armour': None,
                                       'Shield': None}
                equippedWeapon = self.weapons[tokens[10]]
                equippedArmour = self.armour[tokens[11]]
                equippedShield = self.shields[tokens[12]]
                blankWeapon = Weapon("Fists", 0, "Physical", 0, 5,
                                     "Strength", "Bludgeon", 1, 250),
                blankArmour = Armour("Cotton Shirt", 30, "Physical",
                                     0, 0, 0),
                blankShield = Shield("Nothing", 0, "Physical", 0, 0,
                                     0, 0)
                statPoints = 0
                flags = {}
                area = None
                x = 0
                y = 0
                self.mercenaries[name] = Character(name, level, xp, xpTnl,
                 hp, maxHp, ep, maxEp, strength, dexterity, wisdom,
                 skills, euros, [], items, equippedItemIndices,
                 equippedWeapon, equippedArmour, equippedShield,
                 blankWeapon, blankArmour, blankShield,
                 statPoints, flags, area, x, y, 0)

    def populateQuests(self):
        with open("data/questdata.txt", "r") as file:
            file.readline()
            for line in file:
                tokens = line.strip().split("\t")
                title = tokens[0]
                description = tokens[1]
                completionCriteria = eval(tokens[2])
                startFlag = tokens[3]
                endFlag = tokens[4]
                optional = tokens[5]
                repeatable = tokens[6]
                self.allQuests.append(Quest(title, description,
                 completionCriteria, startFlag, endFlag, optional, repeatable))

    def stepPlants(self):
        wiltText = ""
        plantsExpiryVerbs = {
            "Boulderwort": "crumbled",
            "Snowdrops": "wilted",
            "Prickly Pear": "dried up"
        }
        for i, item in enumerate(self.character.items):
            if item is not None and item.NAME in plantsExpiryVerbs:
                if hasattr(item, "steps"):
                    item.steps += 1
                else:
                    item.steps = 0
                if item.steps >= 200:
                    self.character.removeItem(i)
                    wiltText += "\nYour %s has %s." % (
                        item.NAME, plantsExpiryVerbs[item.NAME])
        return wiltText.strip() if wiltText else None

    def move(self, direction):
        """Move character in the specified direction in the area.

        Add temporary flags to the character."""
        if direction == "up":
            self.y -= 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        elif direction == "down":
            self.y += 1
        self.saveLocation() # Added to check Mount Olympus enemy locations
        self.character.ep += self.character.maxEp / 100
        self.currentArea.movementActions()
        self.addFlags()
        wiltText = self.stepPlants()
        if wiltText:
            return self.getInterfaceActions(extraText=wiltText)
        return self.getInterfaceActions()

    def select(self, selectionIndex):
        """Make changes based on the item in the menu that the user selected.

        Add temporary flags to the character."""
        self.addFlags()
        self.sound.playSound(self.sound.sounds['Select Option'])
        return self.getInterfaceActions(selectionIndex)

    def getLoginEvents(self):
        def getDailyChallenge():
            def randomChallenge():
                enemies = []
                with open("data/dailychallenge.txt", "r") as enemyFile:
                    for line in enemyFile:
                        enemies.append(line.strip())
                enemy = None
                state = random.getstate()
                random.seed(self.fileName.lower() + str(date.today()))
                while enemy is None or enemy.LEVEL - 1 > self.character.level:
                    i = random.randint(0, len(enemies) - 1)
                    enemy = self.enemies[enemies[i]]
                    del enemies[i]
                random.setstate(state)
                killCount = min(10, 2 + self.character.level - enemy.LEVEL)
                description = "Hunt: %s. Defeat %s of them." % (enemy.NAME, killCount)
                criteria = {'Kills': (enemy.IDENTIFIER, killCount)}
                return description, criteria

            interfaceActions = {}
            if "Conclusion" in self.character.flags:
                title = "Daily Challenge"
                startFlag = "%s %s" % (title, date.today())
                description, criteria = randomChallenge()
                todaysQuest = Quest(title, description, criteria, startFlag, "%s Complete" % startFlag, True, True)
                if todaysQuest in self.character.quests or todaysQuest.END_FLAG in self.character.flags:
                    return interfaceActions
                existingDailies = filter(lambda q: title in q.START_FLAG, self.character.quests)
                for quest in existingDailies:
                    self.character.quests.remove(quest)
                self.character.quests.insert(0, todaysQuest)
                self.character.flags[startFlag] = self.character.flags['Kills'][criteria['Kills'][0]] if criteria['Kills'][0] in self.character.flags['Kills'] else 0
                interfaceActions['new quest'] = todaysQuest
                self.sound.playSound(self.sound.sounds['New Quest'])
            return interfaceActions

        def getHolidayActions():
            interfaceActions = {}
            isHalloweenSeason = (
                date.today().month == 10 and
                date.today().day > 24 or
                date.today().month == 11 and
                date.today().day < 4)
            isChristmasSeason = (
                date.today().month == 12 and
                date.today().day > 10 or
                date.today().month == 1 and
                date.today().day < 9)
            year = date.today().year
            if date.today().month == 1:
                year -= 1
            if ( isHalloweenSeason and
                 self.character.hasRoom() and
                 "Halloween %i" % year not in self.character.flags):
                differentItems = 5
                rewardText = "Happy Halloween!"
                roll = (year + hash(self.fileName.lower())) % differentItems
                if roll == 0:
                    itemText = "A phantasm throws you an Aluminum Bat before vanishing in a puff of smoke."
                    item = "Aluminum Bat"
                elif roll == 1:
                    itemText = "A phantasm thrusts a Brittle Cuirass upon you before vanishing in a puff of smoke."
                    item = "Brittle Cuirass"
                elif roll == 2:
                    itemText = "A phantasm offers you a Pumpkin Crossbow before vanishing in a puff of smoke."
                    item = "Pumpkin Crossbow"
                elif roll == 3:
                    itemText = "A phantasm rests a Night Cloak over your shoulder before vanishing in a puff of smoke."
                    item = "Night Cloak"
                elif roll == 4:
                    itemText = "A phantasm stuffs a Witch's Wand in your pack before vanishing in a puff of smoke."
                    item = "Witch's Wand"
                self.character.flags["Halloween %i" % year] = True
                interfaceActions.update({
                    'text': itemText,
                    'italic text': rewardText,
                    'item': item,
                    'flash': True,
                    'halloween': True,})
                self.sound.playSound(self.sound.sounds['Halloween'])
                self.collectItem(interfaceActions)
            elif (isChristmasSeason and
                  self.character.hasRoom() and
                  "Christmas %i" % year not in self.character.flags):
                differentItems = 5
                rewardText = "Thank you for playing during this holiday season!"
                roll = (year + hash(self.fileName.lower())) % differentItems
                if roll == 0:
                    itemText = "The King of Elves appears and tosses you an Ugly Disguise."
                    item = "Ugly Disguise"
                elif roll == 1:
                    itemText = "The King of Elves appears and gives you a pair of Hopalong Boots."
                    item = "Hopalong Boots"
                elif roll == 2:
                    itemText = "The King of Elves appears and bestows upon you the Debonairiest Nowell Gambeson."
                    item = "Debonairiest Nowell Gambeson"
                elif roll == 3:
                    itemText = "The King of Elves appears and hands you a rifle that shoots."
                    item = "A rifle that shoots"
                elif roll == 4:
                    itemText = "The King of Elves appears and presents you with a Festive Tunic."
                    item = "Festive Tunic"
                self.character.flags["Christmas %i" % year] = True
                interfaceActions.update({
                    'text': itemText,
                    'italic text': rewardText,
                    'item': item})
                self.sound.playSound(self.sound.sounds['Christmas'])
                self.collectItem(interfaceActions)
            return interfaceActions

        interfaceActions = getDailyChallenge()
        interfaceActions.update(getHolidayActions())
        return interfaceActions if interfaceActions else None
        
    def getInterfaceActions(self, selectionIndex=None, justFought=False, extraText=None):
        """Retrieve the interface actions from the current spot.

        The spot is updated, then a check for an enemy encounter is made.
        If an encounter is not made, the interface actions from the spot are
        returned. A check is then made for Toshe's death.

        If a battle action is returned, an enemy is assigned.
        If a store action is returned, a store is assigned.
        If an area change is returned, the new location is assigned.
        """
        self.updateSpot()

        if self.currentArea.name not in self.character.flags['Discovered Areas']:
            self.character.flags['Discovered Areas'][self.currentArea.name] = set()
            self.character.flags['Marked Areas'][self.currentArea.name] = set()
        self.character.flags['Discovered Areas'][self.currentArea.name].add(
            (self.x, self.y))
        
        if ( justFought or
             (selectionIndex is not None)):
            enemyIdentifier = None
        else:
            enemyIdentifier = self.encounterEnemy()

        if ( enemyIdentifier and not
             (self.character.equippedArmour.NAME in self.evasiveItems and
              self.enemies[enemyIdentifier].LEVEL <= self.character.level)):
            interfaceActions = {'view': "battle",
                                'enemy': enemyIdentifier,
                                'text': "",
                                'mercenaries': self.character.mercenaries,
                                'image index': -999,}
            if self.currentArea.name == "Macedonia":
                del interfaceActions['mercenaries']
        else:
            if selectionIndex is None:
                interfaceActions = self.currentSpot()
            else:
                interfaceActions = self.currentSpot(selectionIndex)
                
        if self.character.isDead():
            interfaceActions['view'] = "game over"

        self.collectItem(interfaceActions)

        if 'sound' in interfaceActions:
            self.sound.playSound(self.sound.sounds[interfaceActions['sound']])

        if ('skill' in interfaceActions and
            interfaceActions['skill'] in
            [skill.NAME for skill in self.character.skills]):
            if 'text' not in interfaceActions or not interfaceActions['text']:
                interfaceActions['text'] = ("You already know this skill.")
            else:
                interfaceActions['text'] += ("\nYou already know this skill.")
        elif ('skill' in interfaceActions and
              interfaceActions['cost'] > self.character.euros):
            if 'text' not in interfaceActions or not interfaceActions['text']:
                interfaceActions['text'] = ("You do not have enough euros.")
            else:
                interfaceActions['text'] += ("\nYou do not have enough euros.")
        elif ('skill' in interfaceActions and not self.character.canLearn()):
            self.tempSkill = self.skills[interfaceActions['skill']]
            self.tempCost = interfaceActions['cost']
            interfaceActions['overloaded'] = "skills"
            if 'text' not in interfaceActions or not interfaceActions['text']:
                interfaceActions['text'] = ("You are learning "+
                                         self.tempSkill.NAME+
                                         ", but you cannot remember more than "+
                                         "four skills. Which skill should "+
                                         "be forgotten?")
            else:
                interfaceActions['text'] += ("\nYou are learning "+
                                             self.tempSkill.NAME+
                                             ", but you cannot remember more than "+
                                             "four skills. Which skill should "+
                                             "be forgotten?")
        elif ('skill' in interfaceActions):
            skill = self.skills[interfaceActions['skill']]
            self.character.learnSkill(skill)
            if 'text' not in interfaceActions or not interfaceActions['text']:
                interfaceActions['text'] = ("You learned "+skill.NAME+"!")
            else:
                interfaceActions['text'] += ("\nYou learned "+skill.NAME+"!")
            self.character.euros -= interfaceActions['cost']
            interfaceActions['new skill'] = True
            self.sound.playSound(self.sound.sounds['New Skill'])
        elif ('fusion skill' in interfaceActions):
            interfaceActions['skill'] = interfaceActions['fusion skill']
            if 'text' not in interfaceActions or not interfaceActions['text']:
                interfaceActions['text'] = ("You learned "+interfaceActions['skill']+"!")
            else:
                interfaceActions['text'] += ("\nYou learned "+interfaceActions['skill']+"!")
            interfaceActions['new skill'] = True
            self.sound.playSound(self.sound.sounds['New Skill'])

        if 'enemies' in interfaceActions:
            enemyIdentifier = self.selectRandomElement(
                interfaceActions['enemies'])
            interfaceActions['enemy'] = enemyIdentifier

        if 'area' in interfaceActions:
            self.currentArea = self.areas[interfaceActions['area']](
                self.character)
            self.x, self.y = interfaceActions['coordinates']
            self.sound.playSound(self.sound.sounds['Warp'])
            self.updateCheckpoint(interfaceActions['area'])
            if "Rested" in self.character.flags:
                self.sound.playSound(self.sound.sounds['Sleep'])
            return self.getInterfaceActions()
        elif interfaceActions['view'] == "battle":
            self.sound.playSound(self.sound.sounds['Encounter'])
            if interfaceActions['enemy'] == "Will o Wisp":
                enemyIdentifier = "Will o Wisp"
                enemy = random.choice(filter(lambda enemy: enemy.FLEEABLE and not enemy.UNIQUE and enemy.MUSIC is None, self.enemies.itervalues()))
                factor = float(self.character.level) / enemy.LEVEL
                interfaceActions['enemy'] = enemy.IDENTIFIER
                interfaceActions['flash'] = True
                interfaceActions['enemy modifiers'] = {
                    'Multiplicative': True,
                    'Stats': {
                        'LEVEL': self.character.level,
                        'XP': factor ** 1.5 * 8,
                        'maxHp': factor ** 2.2 * 5,
                        'damage': factor * 1.2,
                        'defence': factor,
                    },
                }
            elif interfaceActions['enemy'] == "Gigantic Crayons":
                interfaceActions['flash'] = True
            interfaceActions['menu'] = None
            mercenaries = []
            # Mercenaries must explicitly be added to interfaceActions
            # even if they are in your party
            if 'mercenaries' in interfaceActions:
                for mercenary in interfaceActions['mercenaries']:
                    if type(mercenary) == str:
                        mercenary = deepcopy(self.mercenaries[mercenary])
                    mercenaries.append(mercenary)
            if ("Giant" in interfaceActions['enemy'] and self.roll() == 1 and
                interfaceActions['enemy'].replace("1", "2") not in
                self.character.flags['Kills']):
                interfaceActions['enemy'] = interfaceActions['enemy'].replace(
                    "1", "2")
                interfaceActions['flash'] = True
            enemy = deepcopy(self.enemies[interfaceActions['enemy']])
            if "enemy modifiers" in interfaceActions:
                for stat in interfaceActions['enemy modifiers']['Stats']:
                    if stat == "SKILLS":
                        newSkills = dict()
                        for skillName in interfaceActions[
                             'enemy modifiers']['Stats'][stat]:
                            newSkills[self.skills[skillName]] =\
interfaceActions['enemy modifiers']['Stats'][stat][skillName]
                        enemy.SKILLS.update(newSkills)
                    elif stat in ("NAME", "SUBNAME", "LEVEL"):
                        setattr(enemy, stat,
                            interfaceActions['enemy modifiers']['Stats'][stat])
                    elif interfaceActions['enemy modifiers']['Multiplicative']:
                        setattr(enemy, stat, int(getattr(enemy, stat) *
                                interfaceActions[
                                    'enemy modifiers']['Stats'][stat]
                                ))
                        # If the stat to be adjusted is max hp, set hp as well
                        if stat == "maxHp":
                            enemy.hp *= interfaceActions[
                                'enemy modifiers']['Stats'][stat]
                    else:
                        setattr(enemy, stat, getattr(enemy, stat) +
                                interfaceActions[
                                    'enemy modifiers']['Stats'][stat]
                                )
            if enemyIdentifier == "Will o Wisp":
                for item, chance in self.enemies['Will o Wisp'].ITEMS.items():
                    if item not in enemy.ITEMS:
                        enemy.ITEMS[item] = 0
                    enemy.ITEMS[item] += chance
                enemy.IDENTIFIER = self.enemies['Will o Wisp'].IDENTIFIER
                enemy.NAME = self.enemies['Will o Wisp'].NAME
                enemy.IMAGE = self.enemies['Will o Wisp'].IMAGE
                enemy.MUSIC = self.enemies['Will o Wisp'].MUSIC
                enemy.RARITY = self.enemies['Will o Wisp'].RARITY
            self.battle = Battle(self.character, enemy, mercenaries, "coliseum" in interfaceActions)
            if 'text' not in interfaceActions or not interfaceActions['text']:
                interfaceActions['text'] = ""
            interfaceActions['text'] += ("\nEncounter! "+enemy.NAME+
                                         ": Level "+str(enemy.LEVEL)+".")
            for mercenary in mercenaries:
                if mercenary.isDead():
                    if mercenary.NAME == "Dragan":
                        randomDialogue = random.choice([
                            "I am injured. You must fight without me.",
                            "I am injured. I will stay back.",
                        ])
                        interfaceActions['text'] += "\n%s: %s" % (mercenary.NAME, randomDialogue)
                    elif mercenary.NAME == "Qendresa":
                        randomDialogue = random.choice([
                            "My wounds are too great to engage.",
                            "I must rest before I continue.",
                            "I am not fit to fight. I have sustained an injury.",
                        ])
                        interfaceActions['text'] += "\n%s: %s" % (mercenary.NAME, randomDialogue)
                    elif mercenary.NAME == "Barrie":
                        randomDialogue = random.choice([
                            "No more battles until I've had a good sleep.",
                            "Sorry, I'm gonna have to sit this one out.",
                            "Go on without me. I'm not in fighting form.",
                        ])
                        interfaceActions['text'] += "\n%s: %s" % (mercenary.NAME, randomDialogue)
                    else:
                        interfaceActions['text'] += "\n%s is not healthy enough to fight!" % mercenary.NAME

        else:
            interfaceActions.update({
                'enabled directions': self.enabledDirections})

        if self.character.level == 2 and 'Level 2' not in self.character.flags:
            interfaceActions['italic text'] = (
                "You leveled up! Allocate points by clicking the stat buttons "+
                "at top right beside Strength, Dexterity or Wisdom.")
            self.character.flags['Level 2'] = True
        elif ('Potions' not in self.character.flags
              and self.character.potions > 0
              and interfaceActions['view'] == "travel"):
            interfaceActions['italic text'] = (
                "You found a potion. Click the potion button to consume it "+
                "to heal HP.")
            self.character.flags['Potions'] = True
            
        if interfaceActions['view'] == "store":
            if "buyback" in interfaceActions:
                self.buyback = True
            else:
                self.buyback = False
            self.store = []
            for item in interfaceActions['items for sale']:
                if type(item) == str:
                    self.store.append(self.items[item])
                elif item:
                    self.store.append(item)
                else:
                    self.store.append(None)

        self.addMercenary(interfaceActions)

        existingDailies = filter(lambda q: "Daily Challenge" in q.START_FLAG, self.character.quests)
        for quest in existingDailies:
            if quest.isCompletedBy(self.character):
                self.character.flags[quest.END_FLAG] = True
                def getDailyChallengeReward(interfaceActions):
                    equipmentTypes = ["Weapon", "Armour", "Shield"]
                    u = 40
                    equipToUpgrade = None
                    for equipmentType in equipmentTypes:
                        i = self.character.equippedItemIndices[equipmentType]
                        if i is None:
                            continue
                        else:
                            upgradeCandidate = self.character.items[i]
                            if upgradeCandidate.upgradeCount < u:
                                u = upgradeCandidate.upgradeCount
                                equipToUpgrade = upgradeCandidate
                    if 'text' not in interfaceActions or not interfaceActions['text']:
                        interfaceActions['text'] = "\nDaily Challenge complete!"
                    if equipToUpgrade is None or self.roll(u+1) > 10:
                        if self.roll(2) == 1:
                            reward = 5 + self.roll(45)
                            interfaceActions['text'] += ("\nYou got %s potions!" % reward)
                            self.character.potions += reward
                        else:
                            reward = 500 + self.roll(24500)
                            interfaceActions['text'] += ("\nYou got %s euros!" % reward)
                            self.character.euros += reward
                    else:
                        interfaceActions['text'] += ("\n%s got upgraded!" % equipToUpgrade.NAME)
                        equipToUpgrade.upgrade()
                        
                getDailyChallengeReward(interfaceActions)

        oldQuest = self.removeFinishedQuests(self.character.quests, self.character.flags, returnOne=True)
        if oldQuest:
            interfaceActions['remove quest'] = oldQuest
            self.sound.playSound(self.sound.sounds['Quest Complete'])
        else:
            newQuest = self.checkForNewQuest(self.character.quests, self.character.flags)
            if newQuest:
                interfaceActions['new quest'] = newQuest
                self.sound.playSound(self.sound.sounds['New Quest'])
        completedQuest = self.checkForReadyQuests(self.character.quests, self.character, returnOne=True)
        if completedQuest:
            interfaceActions['completed quest'] = completedQuest
            self.sound.playSound(self.sound.sounds['Quest Ready'])
        uncompletedQuests = self.checkForUnreadyQuests(self.character.quests, self.character)
        if uncompletedQuests:
            interfaceActions['uncompleted quests'] = uncompletedQuests

        if self.updateUnlocks():
            interfaceActions['italic text'] = "You have unlocked a secret character!"
            self.sound.playSound(self.sound.sounds['Unlock Secret'])

        self.view = interfaceActions['view']

        self.updateMusic(interfaceActions['view'])

        if extraText:
            if 'text' not in interfaceActions or not interfaceActions['text']:
                interfaceActions['text'] = "%s" % extraText.strip()
            else:
                interfaceActions['text'] += "\n%s" % extraText.strip()

        return interfaceActions

    def updateSpot(self):
        """Change the character's current location based on x and y coordinates.
        """
        self.currentSpot = self.currentArea.spots[self.y][self.x]
        self.updateDirections()

    def updateDirections(self):
        """Update enabled directions to represent which directions are
        accessible from the current spot.
        """
        self.enabledDirections = set()
        if self.currentArea.spots[self.y - 1][self.x]:
            self.enabledDirections.add("up")
        if self.currentArea.spots[self.y][self.x - 1]:
            self.enabledDirections.add("left")
        if self.currentArea.spots[self.y][self.x + 1]:
            self.enabledDirections.add("right")
        if self.currentArea.spots[self.y + 1][self.x]:
            self.enabledDirections.add("down")

    def updateCheckpoint(self, areaName):
        if areaName in self.towns:
            self.saveLocation()
            self.character.checkpoint = None
            self.character.checkpoint = deepcopy(self.character)

    def updateMusic(self, currentView):
        """Update the current song playing to match area music appropriately."""
        # Dead
        if currentView == "game over":
            self.sound.stopMusic()
            self.sound.playMusic(self.sound.songs['Game Over Theme'])
        # New battle with sound (no fade)
        elif (currentView == "battle" and
              self.battle.enemy.MUSIC is not None and
              self.sound.isNewSong(self.sound.songs[self.battle.enemy.MUSIC])):
            newSong = self.sound.songs[self.battle.enemy.MUSIC]
            self.sound.stopMusic()
            self.sound.playMusic(newSong)
        # No fade
        elif (self.sound.isInstantPlay(self.currentArea.audio) or
              "New Song" in self.character.flags):
            if "New Song" in self.character.flags:
                newSong = self.character.flags['New Song']
            else:
                newSong = self.currentArea.audio
            self.sound.playMusic(newSong)
        # New area
        elif (currentView != "battle" and
              currentView != "battle over" and
              self.sound.isNewSong(self.currentArea.audio)):
            newSong = self.currentArea.audio
            self.sound.fadeoutMusic(2000)
            self.sound.queueMusic(newSong)

        if "New Song" in self.character.flags:
            del self.character.flags['New Song']

    def encounterEnemy(self):
        """Check the spot to see if enemy encounter conditions have been
        fulfilled, and if so, return the enemy's identifier.
        """
        if self.currentArea.encounters:
            enemyProbabilities = self.currentArea.encounters[self.currentSpot]
            if enemyProbabilities:
                if self.roll(10000) == 1:
                    return "Gigantic Crayons"
                if "Conclusion" in self.character.flags and self.roll(1000) == 1:
                    return "Will o Wisp"
                return self.selectRandomElement(enemyProbabilities)
        return None

    def selectRandomElement(self, probabilities):
        """Select a random element from a dictionary of element: probability
        pairs.

        The probability value is out of 100 and is independent of the other
        probabilities.

        (copied from Battle)
        """
        randomNumber = self.roll()
        chanceCounter = 0
        for element in probabilities:
            chanceCounter += probabilities[element]
            if chanceCounter >= randomNumber:
                return element
        return None

    def roll(self, numberOfSides=100):
        """Return a random number given a range (defaults 1-100).

        (copied from Battle)
        """
        return random.randint(1, numberOfSides)

    def attack(self):
        if self.character.equippedWeapon.CATEGORY == "Gun":
            skill = self.skills['Shoot']
            interfaceActions = self.battle.attack(skill)
        elif self.character.specialization == "Weird Warlock" and self.character.equippedWeapon.CATEGORY in set(["Bow", "Wand"]) and self.roll(10) == 1:
            skill = random.choice([skill for skill in self.skills.itervalues() if set([self.character.equippedWeapon.CATEGORY]) == skill.PERMITTED_WEAPONS])
            interfaceActions = self.battle.attack(skill, useEp=False)
        else:
            skill = self.skills['Attack']
            interfaceActions = self.battle.attack(skill)
        self.updateBattleVariables(interfaceActions)
        return interfaceActions
    
    def defend(self):
        if self.character.specialization == "Mystic":
            interfaceActions = self.battle.attack(self.skills['Re-energize'])
        else:
            interfaceActions = self.battle.attack(self.skills['Defend'])
        self.updateBattleVariables(interfaceActions)
        return interfaceActions

    def flee(self):
        interfaceActions = self.battle.flee()
        self.updateBattleVariables(interfaceActions)
        return interfaceActions

    def useSkill(self, skill):
        interfaceActions = self.battle.attack(skill)
        self.updateBattleVariables(interfaceActions)
        return interfaceActions

    def equipItem(self, itemIndex):
        interfaceActions = self.battle.attack(
            self.skills['Equip Item'],
            lambda _: self.character.equip(itemIndex))
        self.updateBattleVariables(interfaceActions)
        return interfaceActions

    def drinkPotion(self):
        interfaceActions = self.battle.attack(
            self.skills['Drink Potion'],
            lambda battle: self.usePotion(battle))
        self.updateBattleVariables(interfaceActions)
        return interfaceActions

    def usePotion(self, battle=None):
        self.character.potions -= 1
        healAmount = int(50 + 10 * self.character.level ** 0.5 - 10)
        if self.character.specialization == "Alchemist":
            healAmount *= 10
        self.character.hp += healAmount
        self.sound.playSound(self.sound.sounds['Drink'])
        if battle:
            battle.text += "{0} heals {1} HP.\n".format(self.character.NAME, healAmount)
            battle.hits.append({
                "Target": self.character.NAME,
                "Kind": "Heal",
                "Number": int(healAmount),
                "Skill": False,
                "Critical": False,
                "Aux": False,
            })
        else:
            return "You consume a vial full of life fluid, healing %s HP." % healAmount

    def updateBattleVariables(self, interfaceActions):
        self.collectItem(interfaceActions, True)
        self.view = interfaceActions['view']
        self.updateMusic(interfaceActions['view'])
        if 'sounds' in interfaceActions:
            soundCount = Counter()
            for sound in interfaceActions['sounds']:
                if type(sound) is dict:
                    sound = tuple(sound.items())
                if "Critical" in sound: # Don't stack critical sounds
                    soundCount[sound] = 1
                else:
                    soundCount[sound] += 1
            for sound in soundCount:
                if type(sound) is tuple:
                    sound = dict(sound)
                    self.sound.playSound(self.sound.sounds[sound['Name']], count=soundCount[tuple(sound.items())], pan=sound['Panning'])
                else:
                    self.sound.playSound(self.sound.sounds[sound], count=soundCount[sound])

    def addMercenary(self, interfaceActions):
        if 'mercenary' in interfaceActions:
            self.character.mercenaries.append(
                self.mercenaries[interfaceActions['mercenary']])
            self.sound.playSound(self.sound.sounds['New Mercenary'])

    def buy(self, itemIndex):
        self.character.euros -= self.store[itemIndex].PRICE
        if self.store[itemIndex].NAME == "Chasmic Rucksack":
            self.character.flags['Chasmic Rucksack'] = True
            while len(self.character.items) < 16:
                self.character.items.append(None)
        elif "Enchantment" in self.store[itemIndex].NAME:
            if self.store[itemIndex].NAME == "Heroic Weapon Enchantment":
                upgradeIndex = self.character.equippedItemIndices['Weapon']
            elif self.store[itemIndex].NAME == "Heroic Armour Enchantment":
                upgradeIndex = self.character.equippedItemIndices['Armour']
            elif self.store[itemIndex].NAME == "Heroic Shield Enchantment":
                upgradeIndex = self.character.equippedItemIndices['Shield']
            if upgradeIndex is None or self.character.items[itemIndex] >= 10:
                self.character.euros += self.store[itemIndex].PRICE
                self.sound.playSound(self.sound.sounds['Error'])
                return
            while self.character.items[upgradeIndex].upgradeCount < 10:
                self.character.items[upgradeIndex].upgrade()
                self.sound.playSound(self.sound.sounds['Forge Upgrade'])
            self.character.updateStats()
        else:
            self.character.addItem(self.store[itemIndex])
        if self.buyback:
            self.character.flags['Buyback Items'][itemIndex] = None
            self.store[itemIndex].PRICE = self.store[itemIndex].PRICE * 2
            self.store[itemIndex] = None
        self.sound.playSound(self.sound.sounds['Buy'])

    def sell(self, itemIndex):
        if self.buyback:
            self.character.items[itemIndex].PRICE /= 2
            if self.character.mode == "Ultimate":
                self.character.items[itemIndex].PRICE = 0
            if None in self.character.flags['Buyback Items']:
                self.character.flags['Buyback Items'].remove(None)
                self.store.remove(None)
            else:
                del self.character.flags['Buyback Items'][-1]
                del self.store[-1]
            self.character.flags['Buyback Items'].insert(
                0,
                self.character.items[itemIndex])
            self.store.insert(
                0,
                self.character.items[itemIndex])
        self.character.euros += self.character.items[itemIndex].SELL_PRICE
        self.character.removeItem(itemIndex)
        self.character.updateStats()
        self.sound.playSound(self.sound.sounds['Sell'])

    def collectItem(self, interfaceActions, randomize=False):
        if ( 'item' in interfaceActions and
             self.items[interfaceActions['item']].CATEGORY == "Miscellaneous"):
            randomize = False
            
        if 'item' in interfaceActions:
            item = deepcopy(self.items[interfaceActions['item']])
            if randomize:
                item, modifier = self.randomizeItem(item)
                if modifier is not None:
                    if interfaceActions['text'] == None:
                        interfaceActions['text'] = ""
                    interfaceActions['text'] += ("\n%s: It looks %s!" % (self.character.NAME, modifier.lower()))
            if self.character.hasRoom():
                self.character.addItem(item)
            else:
                self.tempItem = item
                interfaceActions['overloaded'] = "items"
                if interfaceActions['text'] == None:
                    interfaceActions['text'] = ""
                interfaceActions['text'] += ("\nYou are carrying too much! "+
                                             "Choose an item to drop.")
            self.character.updateStats()

    def randomizeItem(self, item):
        successChance = 25
        if self.character.ring is not None:
            successChance += self.character.ring.level
        if self.roll(100) > successChance:
            return item, None
        level = 1
        levelRoll = self.roll(10000)
        if levelRoll < item.PRICE:
            level = 2
        modifier = random.choice(Modifiers.getByCategoryAndLevel(item.CATEGORY, level))
        value = (self.roll(3) + 1) * level
        Modifiers.modifyItem(item, modifier, value)
        item.NAME = "%s %s" % (modifier, item.NAME)
        return item, modifier

    def initializeDefaultBattle(self):
        """Initialize the battle attribute to prevent glitches that occur
        when killed by natural causes."""
        defaultBattle = Battle(self.character,
                               deepcopy(self.enemies['Gigantic Crayons']),
                               [])
        self.battle = defaultBattle

    def initializeQuests(self):
        def syncWithCharacter(quests, character):
            for questInProgress in character.quests:
                if questInProgress in quests:
                    quests.remove(questInProgress)
            self.checkForReadyQuests(character.quests, character)
            self.removeFinishedQuests(quests, character.flags)

        self.availableQuests = [quest for quest in self.allQuests]
        syncWithCharacter(self.availableQuests, self.character)

    def addFlags(self):
        if self.currentArea.tempFlag is not None:
            if type(self.currentArea.tempFlag) == str:
                self.character.flags[self.currentArea.tempFlag] = True
            elif type(self.currentArea.tempFlag) == dict:
                for element in self.currentArea.tempFlag:
                    self.character.flags[element] = self.currentArea.tempFlag[element]

            self.currentArea.tempFlag = None

    def checkForNewQuest(self, quests, flags):
        for quest in self.availableQuests:
            if quest.START_FLAG in flags:
                self.availableQuests.remove(quest)
                if quest.END_FLAG in flags:
                    return None
                quests.insert(0, quest)
                return quest

    def checkForReadyQuests(self, quests, character, returnOne=False):
        for quest in quests:
            if quest.isCompletedBy(character) and quest not in self.readyQuests:
                self.readyQuests.add(quest)
                quests.remove(quest)
                quests.insert(0, quest)
                if returnOne:
                    return quest

    def checkForUnreadyQuests(self, quests, character):
        uncompletedQuests = []
        for quest in self.readyQuests:
            if not quest.isCompletedBy(character):
                uncompletedQuests.append(quest)
        for quest in uncompletedQuests:
            self.readyQuests.remove(quest)
        return uncompletedQuests

    def removeFinishedQuests(self, quests, flags, returnOne=False):
        questsToRemove = []
        for quest in quests:
            if quest.END_FLAG in flags:
                questsToRemove.append(quest)
                if returnOne:
                    break
        for quest in questsToRemove:
            quests.remove(quest)
            if quest in self.readyQuests:
                self.readyQuests.remove(quest)
        return questsToRemove[0] if returnOne and len(questsToRemove) == 1 else questsToRemove

    def resetForge(self):
        self.forge = Forge()
        self.forge.sacrificeIndexes = [None, None]

    def setHorn(self):
        self.forge.horn = None   # Required to get correct successChance calculation
        
        if self.character.hasItem("Green Horn") and (self.forge.getSuccessChance() > 1000 / 3.0 or self.forge.getSuccessChance() > 95 / 3.0 and not self.character.hasItem("Purple Horn") or not self.character.hasItem("Purple Horn") and not self.character.hasItem("Golden Horn")):
            self.forge.horn = "Green Horn"
        elif self.character.hasItem("Purple Horn"):
            self.forge.horn = "Purple Horn"
        elif self.character.hasItem("Golden Horn") and self.forge.getSuccessChance() < 95:
            self.forge.horn = "Golden Horn"

    def setForgeItem(self, itemIndex):
        replacementIndex = self.forge.setForgeItem(self.character.items[itemIndex])
        self.setHorn()
        return replacementIndex

    def setSacrificeItem(self, key, itemIndex):
        self.forge.sacrificeIndexes[key-1] = itemIndex
        replacementIndex = self.forge.setSacrificeItem(key, self.character.items[itemIndex])
        self.setHorn()
        return replacementIndex

    def smith(self):
        def getOrdinal(number):
            ordinals = {
                1: "first",
                2: "second",
                3: "third",
                4: "fourth",
                5: "fifth",
                6: "sixth",
                7: "seventh",
                8: "eighth",
                9: "ninth",
                11: "eleventh",
                12: "twelfth",
                13: "thirteenth",
                14: "fourteenth",
                15: "fifteenth",
                16: "sixteenth",
                17: "seventeenth",
                18: "eighteenth",
                19: "nineteenth",
                10: "tenth",
                20: "twentieth",
                30: "thirtieth",
                40: "fortieth",
                50: "fiftieth",
                60: "sixtieth",
                70: "seventieth",
                80: "eightieth",
                90: "ninetieth",
            }
            cardinals = {
                20: "twenty",
                30: "thirty",
                40: "forty",
                50: "fifty",
                60: "sixty",
                70: "seventy",
                80: "eighty",
                90: "ninety",
            }

            if number > 99:
                raise ValueError("Can only get ordinal up to 99")
            elif number in ordinals:
                return ordinals[number]
            return "%s-%s" % (cardinals[int(str(number)[0] + "0")], ordinals[int(str(number)[1])])
        def collectReward(ascension, c):
            def getSpecialReward(c):
                for candidate in ["Moon Armour", "Macedonian Protector", "Scintillous Ring"]:
                    if not c.hasItem(candidate) and ("Buyback Items" not in c.flags or all(item.NAME != candidate for item in c.flags['Buyback Items'] if item is not None)):
                        return candidate
                return "Platinum Ball"
            if ascension == 10:
                return
            rewards = {
                0: "Purple Horn",
                10: getSpecialReward(c),
                20: "Ranine Orb",
                30: "Bulbous Orb",
                40: "Fiery Orb",
                50: "Platinum Ball",
                60: "Wizardly Orb",
                70: "Knightly Orb",
                80: "Feline Orb",
                90: "Gumball of Power",
            }
            if ascension % 100 in rewards:
                interfaceActions.update({
                    'item': rewards[ascension % 100]
                })
                self.collectItem(interfaceActions)

        if self.forge.horn is not None:
            self.character.removeItem(self.character.indexOfItem(self.forge.horn))
        for i in self.forge.sacrificeIndexes:
            if i in self.character.equippedItemIndices.values():
                self.character.equip(i)
            self.character.removeItem(i)
        previousName = self.forge.forgeItem.displayName
        upgradedCategory = self.forge.forgeItem.CATEGORY
        success = False
        for _ in self.forge.do():
            if not success:
                text = ("The anvil cools and you retrieve your bolstered %s."
                    % (upgradedCategory.lower()))
                success = True
            newName = self.forge.forgeItem.displayName
            text += "\n%s is now %s!" % (previousName, newName)
            previousName = newName
            self.sound.playSound(self.sound.sounds['Forge Upgrade'])
        if not success:
            text = ("The crucible was not hot enough. "+
                "You fail to upgrade your %s." % (upgradedCategory.lower()))
            self.sound.playSound(self.sound.sounds['Failed Upgrade'])
        self.character.updateStats()
        text += "\nA seismic surge of energy emanates from the anvil, shifting the mountain and beckoning back the horde of mythological monsters."
        self.character.flags['Just Forged'] = True
        interfaceActions = self.getInterfaceActions()
        interfaceActions.update({'text': text,})
        self.character.flags['Mount Olympus Ascensions'] += 1
        if "Mount Olympus Complete" not in self.character.flags:
            interfaceActions.update({
                'italic text': "You may now reascend Mount Olympus for another trial.",
            })
            self.character.flags['Mount Olympus Complete'] = True
        elif self.character.flags['Mount Olympus Ascensions'] < 100:
            interfaceActions.update({
                'italic text': "You have completed your %s ascension of Mount Olympus." % getOrdinal(self.character.flags['Mount Olympus Ascensions']),
            })
        else:
            interfaceActions.update({
                'italic text': "You have completed ascension %s of Mount Olympus." % (self.character.flags['Mount Olympus Ascensions']),
            })
        if (self.character.flags['Mount Olympus Ascensions']) % 10 == 0:
            interfaceActions['italic text'] = interfaceActions['italic text'][:-1] + "!"
            collectReward(self.character.flags['Mount Olympus Ascensions'], self.character)
        self.saveGame()
        return success, interfaceActions

    def initializeUnlocks(self):
        self.unlocks = {}
        try:
            with open("settings/unlocks.tqp", "r") as unlocksFile:
                self.unlocks = pickle.load(unlocksFile).unlocks
        except IOError:
            return
