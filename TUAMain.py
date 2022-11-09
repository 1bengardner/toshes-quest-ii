"""
File: TUAMain.py
Author: Ben Gardner
Created: January 14, 2013
Revised: November 6, 2022
"""


import pickle
from copy import deepcopy
from random import randint
from random import choice
from collections import Counter
from datetime import date

from TUAWeapon import Weapon
from TUAArmour import Armour
from TUAShield import Shield
from TUAMiscellaneousItem import MiscellaneousItem
from TUASkill import Skill
from TUAEnemy import Enemy
from TUACharacter import Character
from TUABattle import Battle

from TUASound import Sound

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
from TUARumadanVillage import RumadanVillage
from TUARumadanHideout import RumadanHideout
from TUABerlusconiCastle import BerlusconiCastle
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
        weaponModifiers = {
                1: [
                    'Big',
                    'Keen',
                    'Exotic'],
                2: [
                    'Giant',
                    'Deadly'],}
        armourModifiers = {
                1: [
                    'Stony',
                    'Icy',
                    'Fiery',
                    'Sturdy',
                    'Exotic'],
                2: [
                    'Gaian',
                    'Glacial',
                    'Molten',
                    'Robust'],}
        shieldModifiers = {
                1: [
                    'Stony',
                    'Icy',
                    'Fiery',
                    'Sturdy',
                    'Exotic',
                    'Heavy'],
                2: [
                    'Gaian',
                    'Glacial',
                    'Molten',
                    'Robust',
                    'Massive'],}
        self.itemModifiers = {  # Category: Level: ModName
            'Sword': weaponModifiers,
            'Club': weaponModifiers,
            'Axe': weaponModifiers,
            'Spear': weaponModifiers,
            'Bow': weaponModifiers,
            'Wand': weaponModifiers,
            'Armour': armourModifiers,
            'Shield': shieldModifiers,}            
        self.populateWeapons()
        self.populateArmour()
        self.populateShields()
        self.populateMiscellaneousItems()
        self.items = dict(self.weapons.items() +
                          self.armour.items() +
                          self.shields.items() +
                          self.miscellaneousItems.items())
        self.populateSkills()
        self.populateEnemies()
        self.populateMercenaries()
        self.populateAreas()
        self.buyback = False
        self.sound = Sound()

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


    def modifyItemStat(self, item, modifier, value):
        if modifier in ('Big', 'Giant'):
            item.POWER += value
        elif modifier in ('Keen', 'Deadly'):
            item.C_RATE += value / 2.0
        elif modifier == 'Exotic':
            item.SELL_PRICE *= value
        elif modifier in ('Stony', 'Gaian'):
            item.EARTH_REDUCTION += value
        elif modifier in ('Icy', 'Glacial'):
            item.WATER_REDUCTION += value
        elif modifier in ('Fiery', 'Molten'):
            item.FIRE_REDUCTION += value
        elif modifier in ('Sturdy', 'Robust'):
            item.DEFENCE += value
        elif modifier in ('Heavy', 'Massive'):
            item.B_RATE += value / 2

    def loadGame(self, fileName):
        """Load a game from a savefile."""
        self.fileName = fileName
        with open("saves\\"+self.fileName+".tq", "r") as gameFile:
            self.character = pickle.load(gameFile)
            self.currentArea = self.character.area(self.character)
            self.x = self.character.x
            self.y = self.character.y
            self.initializeDefaultBattle()
        self.sound.playSound(self.sound.sounds['Load'])

    def startNewGame(self, fileName):
        """Create a new character and record it in a savefile."""
        STARTING_X = 3
        STARTING_Y = 17
        self.fileName = fileName
        self.character = Character("Toshe", 1, 0, 100, 50, 100, 100, 100,
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
                                    'Config': {'Automap On': 0}},
                                   self.areas['Adriatic Sea'],
                                   STARTING_X, STARTING_Y,
                                   0)
        self.currentArea = self.character.area(self.character)
        self.x = self.character.x
        self.y = self.character.y
        self.saveGame()
        self.initializeDefaultBattle()

    def saveGame(self):
        self.character.area = self.currentArea.__class__
        self.character.x = self.x
        self.character.y = self.y
        with open("saves\\"+self.fileName+".tq", "w") as gameFile:
            pickle.dump(self.character, gameFile)
        self.sound.playSound(self.sound.sounds['Save'])

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
                      'Rumadan Village': RumadanVillage,
                      'Rumadan Hideout': RumadanHideout,
                      'Berlusconi Castle': BerlusconiCastle,
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
                      'Lair of the Magi': LairOfTheMagi}

    def populateWeapons(self):
        with open("data\\weapondata.txt", "r") as weaponFile:
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
        with open("data\\armourdata.txt", "r") as armourFile:
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
        with open("data\\shielddata.txt", "r") as shieldFile:
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
        with open("data\\miscellaneousitemdata.txt", "r") as rFile:
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
        with open("data\\skilldata.txt", "r") as skillFile:
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
        with open("data\\enemydata.txt", "r") as enemyFile:
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
                self.enemies[identifier] = Enemy(identifier, name, image,
                                           level, hp, maxHp, damage, accuracy,
                                           cRate, cDamage, bRate, defence,
                                           earthReduction, waterReduction,
                                           fireReduction, physicalReduction,
                                           skills, items, xp, euros, fleeable,
                                           unique, living, deathHp, music)

    def populateMercenaries(self):
        with open("data\\mercenarydata.txt", "r") as mercenaryFile:
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
                                     "Strength", "Club", 1, 250),
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
        self.character.ep += self.character.maxEp / 100
        self.currentArea.movementActions()
        self.addFlags()
        return self.getInterfaceActions()

    def select(self, selectionIndex):
        """Make changes based on the item in the menu that the user selected.

        Add temporary flags to the character."""
        self.addFlags()
        self.sound.playSound(self.sound.sounds['Select Option'])
        return self.getInterfaceActions(selectionIndex)

    def getLoginEvents(self):
        isChristmasSeason = (
            date.today().month == 12 and
            date.today().day > 10 or
            date.today().month == 1 and
            date.today().day < 9)
        year = date.today().year
        if date.today().month == 1:
            year -= 1
        if ( isChristmasSeason and
             self.character.hasRoom() and
             "Christmas %i" % year not in self.character.flags):
            itemText = "You get an Ugly Disguise."
            rewardText = "Thank you for playing during this holiday season!"
            interfaceActions = {
                'view': "travel",
                'image index': 0,
                'menu': [],
                'text': itemText,
                'italic text': rewardText,
                'item': "Ugly Disguise"}
            self.collectItem(interfaceActions)
            self.character.flags["Christmas %i" % year] = True
            return interfaceActions
        
    def getInterfaceActions(self, selectionIndex=None, justFought=False):
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
            
        # The definition
        if ( enemyIdentifier and not
             (self.character.equippedArmour.NAME == "Moon Armour" and
              self.enemies[enemyIdentifier].LEVEL - 1 < self.character.level)):
            interfaceActions = {'view': "battle",
                                'enemy': enemyIdentifier,
                                'text': "",
                                'mercenaries': self.character.mercenaries}
        else:
            if selectionIndex is None:
                interfaceActions = self.currentSpot()
            else:
                interfaceActions = self.currentSpot(selectionIndex)
                
        if self.character.isDead():
            interfaceActions['view'] = "game over"

        self.collectItem(interfaceActions)

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

        if 'enemies' in interfaceActions:
            enemyIdentifier = self.selectRandomElement(
                interfaceActions['enemies'])
            interfaceActions['enemy'] = enemyIdentifier

        if 'area' in interfaceActions:
            self.currentArea = self.areas[interfaceActions['area']](
                self.character)
            self.x, self.y = interfaceActions['coordinates']
            self.sound.playSound(self.sound.sounds['Warp'])
            return self.getInterfaceActions()
        elif interfaceActions['view'] == "battle":
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
                    elif stat == "NAME":
                        enemy.NAME =\
                            interfaceActions['enemy modifiers']['Stats'][stat]
                    elif interfaceActions['enemy modifiers']['Multiplicative']:
                        setattr(enemy, stat, getattr(enemy, stat) *
                                interfaceActions[
                                    'enemy modifiers']['Stats'][stat]
                                )
                        # If the stat to be adjusted is max hp, set hp as well
                        if stat == "maxHp":
                            enemy.hp *= interfaceActions[
                                'enemy modifiers']['Stats'][stat]
                    else:
                        setattr(enemy, stat, getattr(enemy, stat) +
                                interfaceActions[
                                    'enemy modifiers']['Stats'][stat]
                                )
            coliseum = False
            if "coliseum" in interfaceActions:
                coliseum = True
            self.battle = Battle(self.character, enemy, mercenaries, coliseum)
            if 'text' not in interfaceActions or not interfaceActions['text']:
                interfaceActions['text'] = ""
            interfaceActions['text'] += ("\nEncounter! "+enemy.NAME+
                                         ": Level "+str(enemy.LEVEL)+".")
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

        self.view = interfaceActions['view']

        self.updateMusic(interfaceActions['view'])

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
                del self.character.flags['New Song']
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

    def encounterEnemy(self):
        """Check the spot to see if enemy encounter conditions have been
        fulfilled, and if so, return the enemy's identifier.
        """
        if self.currentArea.encounters:
            enemyProbabilities = self.currentArea.encounters[self.currentSpot]
            if enemyProbabilities:
                if self.roll(10000) == 1:
                    return "Gigantic Crayons"
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
        return randint(1, numberOfSides)

    def attack(self):
        interfaceActions = self.battle.attack(self.skills['Attack'])
        self.updateBattleVariables(interfaceActions)
        return interfaceActions
    
    def defend(self):
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

    def equipItem(self):
        interfaceActions = self.battle.attack(self.skills['Equip Item'])
        self.updateBattleVariables(interfaceActions)
        return interfaceActions
        
    def updateBattleVariables(self, interfaceActions):
        self.collectItem(interfaceActions, True)
        self.view = interfaceActions['view']
        self.updateMusic(interfaceActions['view'])
        if 'sounds' in interfaceActions:
            soundCount = Counter()
            for sound in interfaceActions['sounds']:
                if "Critical" in sound: # Don't stack critical sounds
                    soundCount[sound] = 1
                else:
                    soundCount[sound] += 1
            for sound in soundCount:
                self.sound.playSound(self.sound.sounds[sound], soundCount[sound])

    def addMercenary(self, interfaceActions):
        if 'mercenary' in interfaceActions:
            self.character.mercenaries.append(
                self.mercenaries[interfaceActions['mercenary']])

    def buy(self, itemIndex):
        self.character.euros -= self.store[itemIndex].PRICE
        self.character.addItem(self.store[itemIndex])
        if self.buyback:
            self.character.flags['Buyback Items'][itemIndex] = None
            self.store[itemIndex] = None
        self.sound.playSound(self.sound.sounds['Buy'])

    def sell(self, itemIndex):
        if self.buyback:
            if None in self.character.flags['Buyback Items']:
                self.character.flags['Buyback Items'].remove(None)
                self.store.remove(None)
            else:
                del self.character.flags['Buyback Items'][
                    len(self.character.flags['Buyback Items']) - 1]
                del self.store[len(self.store) - 1]
            self.character.flags['Buyback Items'].insert(
                0,
                self.character.items[itemIndex])
            self.store.insert(
                0,
                self.character.items[itemIndex])
        self.character.euros += self.character.items[itemIndex].SELL_PRICE
        self.character.removeItem(itemIndex)
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
                    interfaceActions['text'] += ("\nToshe: It looks %s!" % modifier.lower())
            if self.character.hasRoom():
                self.character.addItem(item)
            else:
                self.tempItem = item
                interfaceActions['overloaded'] = "items"
                interfaceActions['text'] += ("\nYou are carrying too much! "+
                                             "Choose an item to drop.")

    def randomizeItem(self, item):
        if self.roll(100) > 25:
            return item, None
        level = 1
        levelRoll = self.roll(10000)
        if levelRoll < item.PRICE:
            level = 2
        modifier = choice(self.itemModifiers[item.CATEGORY][level])
        value = (self.roll(3) + 1) * level
        self.modifyItemStat(item, modifier, value)
        item.NAME = "%s %s" % (modifier, item.NAME)
        return item, modifier

    def initializeDefaultBattle(self):
        """Initialize the battle attribute to prevent glitches that occur
        when killed by natural causes."""
        defaultBattle = Battle(self.character,
                               deepcopy(self.enemies['Gigantic Crayons']),
                               [])
        self.battle = defaultBattle

    def addFlags(self):
        if self.currentArea.tempFlag is not None:
            if type(self.currentArea.tempFlag) == str:
                self.character.flags[self.currentArea.tempFlag] = True
            elif type(self.currentArea.tempFlag) == dict:
                for element in self.currentArea.tempFlag:
                    self.character.flags[element] = self.currentArea.tempFlag[element]

            self.currentArea.tempFlag = None
