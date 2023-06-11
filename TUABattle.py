"""
File: TUABattle.py
Author: Ben Gardner
Created: March 24, 2013
Revised: June 11, 2023
"""


import random
from copy import copy


class Battle(object):
    """This class contains methods to execute a battle and is instantiated each
    time a new battle begins. The object can be deleted after the battle ends.
    """

    def __init__(self,
                 character,
                 enemy,
                 auxiliaryCharacters=[],
                 coliseum=False):
        self.DEFEND_BLOCK_VALUE = 25
        self.PROTECTOR_BLOCK_VALUE = 5
        self.view = "battle"
        self.text = ""
        self.sounds = []
        self.hits = []
        self.mainCharacter = character
        self.auxiliaryCharacters = [
            c for c in auxiliaryCharacters if not c.isDead()]
        self.charactersFlags = {}
        self.enemy = enemy
        if self.mainCharacter.mode == "Easy":
            self.enemy.cRate /= 2
            self.enemy.defence /= 2
        self.enemyFlags = set()
        for character in self.auxiliaryCharacters+[self.mainCharacter]:
            self.charactersFlags[character.NAME] = set()

        # HP Alerts to indicate when low HP text should be displayed
        self.hpAlert1 = False
        self.hpAlert2 = False
        self.hpAlert3 = False
        # Don't display message if HP meets alert condition before battle
        self.tosheAlertMessages()

        # 50/50 chance for each combatant to go first
        if ( self.mainCharacter.equippedWeapon.CATEGORY == "Bow" and
             self.mainCharacter.equippedShield.NAME != "Nothing"):
            self.characterFirst = False
        elif (self.mainCharacter.equippedWeapon.CATEGORY == "Bow" or
              self.mainCharacter.specialization == "Squad Leader" or
              self.roll() >= 50 and not self.enemy.UNIQUE):
            self.characterFirst = True
        elif self.enemy.UNIQUE:
            self.characterFirst = random.seed(self.mainCharacter.rareSeed + self.enemy.IDENTIFIER)
        else:
            self.characterFirst = False

        # Set coliseum mode if specified so main character does not die
        self.coliseumMode = False
        self.CHARACTER_DEATH_HP = 0
        if coliseum:
            self.coliseumMode = True
            self.CHARACTER_DEATH_HP = 100

        # Strings for variable name-to-English interpretation
        self.statStrings = {'hp': ["HP", "."],
                            'maxHp': ["max HP", "."],
                            'ep': ["EP", "."],
                            'maxEp': ["max EP", "."],
                            'damage': ["damage", "."],
                            'cDamage': ["critical damage", "%."],
                            'accuracy': ["accuracy", "%."],
                            'cRate': ["critical chance", "%."],
                            'bRate': ["block chance", "%."],
                            'earthReduction': ["earth reduction", "%."],
                            'waterReduction': ["water reduction", "%."],
                            'fireReduction': ["fire reduction", "%."],
                            'physicalReduction': ["physical damage reduction", "%."],
                            'defence': ["defence", "."]}

        self.consumableEffects = {
            'Nutritious Mushroom': [{
                'stat': "hp",
                'type': "Multiply",
                'value': 1,
                'multiplicand': "maxHp"}],
            'Delicious Mushroom': [{
                'stat': "ep",
                'type': "Multiply",
                'value': 1,
                'multiplicand': "maxEp"}],
            'Big Mushroom': [{
                'stat': "damage",
                'type': "Multiply",
                'value': 2,
                'multiplicand': "damage"}],
            'Thick Mushroom': [{
                'stat': "defence",
                'type': "Multiply",
                'value': 2,
                'multiplicand': "defence"}],
            'Jagged Mushroom': [{
                'stat': "cRate",
                'type': "Add",
                'value': 25,
                'multiplicand': None}],
            'Magical Mushroom': [{
                'stat': "earthReduction",
                'type': "Add",
                'value': 25,
                'multiplicand': None},
                                 {
                'stat': "waterReduction",
                'type': "Add",
                'value': 25,
                'multiplicand': None},
                                 {
                'stat': "fireReduction",
                'type': "Add",
                'value': 25,
                'multiplicand': None}]
            }

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'text': "\n"+self.text.strip(),
                   'sounds': self.sounds,
                   'hits': self.hits,}
        if newActions:
            actions.update(newActions)
        return actions

    def attack(self, skill, successfulTurnCallback=lambda: None):
        """Make Toshe attack the enemy with a specified skill."""
        self.text = ""
        self.sounds = []
        self.hits = []
        if self.mainCharacter.equippedWeapon.CATEGORY not in\
           skill.PERMITTED_WEAPONS:
            self.text += "You cannot use this skill with your equipped weapon!"
        elif self.mainCharacter.ep < skill.EP_USED:
            self.text += "You do not have enough EP!"
        else:
            turns = [
                lambda: self.takeCharacterTurn(skill, successfulTurnCallback),
                self.takeEnemyTurn]
            if not self.characterFirst:
                turns.reverse()
            for turn in turns:
                turn()
                if self.checkDeath():
                    droppedItem = self.checkDroppedItem()
                    if droppedItem and not self.mainCharacter.isDead():
                        return self.actions({'item': droppedItem})
                    return self.actions()
            self.tosheAlertMessages()

        return self.actions()

    def flee(self):
        """Allow Toshe to attempt to flee from battle.

        If he is unsuccessful at fleeing, the battle will continue and the enemy
        will attack."""
        self.text = ""
        self.sounds = []
        self.hits = []
        if not self.enemy.FLEEABLE:
            self.text += "There's nowhere to run."

        elif self.isStunned(self.mainCharacter,
                            self.charactersFlags[self.mainCharacter.NAME]):
            self.text += "You cannot flee right now."

        else:
            divisor = (self.enemy.LEVEL - self.mainCharacter.level + 2)
            
            if divisor <= 0:
                chance = 99
            else:
                chance = 100/divisor
            
            if self.roll() <= chance:
                self.endBattle()

            else:
                if divisor <= 0:
                    self.text = ("Bad luck! ")
                self.text += ("Toshe tried to run away, but "+self.enemy.NAME+
                              " caught up!\n")
                
                self.doFlagActions(self.mainCharacter,
                    self.charactersFlags[self.mainCharacter.NAME])
                if self.checkDeath():
                    return self.actions()
                self.takeEnemyTurn()
                if self.checkDeath():
                    return self.actions()
                self.tosheAlertMessages()

        return self.actions()

    def takeCharacterTurn(self, skill, successfulTurnCallback=lambda: None):
        """Allow Toshe and his party to attack the enemy."""
        if not self.isStunned(self.mainCharacter,
                              self.charactersFlags[self.mainCharacter.NAME]):
            self.checkConsumables(skill)
            self.mainCharacter.ep -= skill.EP_USED
        self.takeTurn(skill, self.mainCharacter, self.enemy,
                      self.charactersFlags[self.mainCharacter.NAME],
                      self.enemyFlags, successfulTurnCallback)
        for character in self.auxiliaryCharacters:
            skill = self.selectRandomElement(character.skills)
            self.takeTurn(skill, character, self.enemy,
                          self.charactersFlags[character.NAME],
                          self.enemyFlags)

    def takeEnemyTurn(self):
        """Allow the enemy to attack Toshe."""
        skill = self.selectRandomElement(self.enemy.SKILLS)
        if hasattr(self.enemy, "homingTarget"):
            defender = self.enemy.homingTarget
        else:
            defenders = self.auxiliaryCharacters+[self.mainCharacter]
            defenderIndex = random.randint(0, len(self.auxiliaryCharacters))
            defender = defenders[defenderIndex]
        self.takeTurn(skill, self.enemy, defender, self.enemyFlags,
                      self.charactersFlags[defender.NAME])
                      
    def getPanning(self, affectedCombatant):
        return {
            self.mainCharacter: (1, 0.25),
            self.enemy: (0.25, 1)
        }[affectedCombatant]

    def takeTurn(self, skill, attacker, defender, attackerFlags, defenderFlags,
        successfulTurnCallback=lambda: None):
        """Run through one turn of the battle.

        The specified attacker will attack the defender with its chosen skill
        and any additional actions and effects that correspond will be executed.
        """
        basicSkills = set([
            "Attack",
            "Venom Strike",
            "Strong Attack",
            "Defend",
            "Recover"
        ])

        if not self.isStunned(attacker, attackerFlags):
            # Initialize values
            damage = None
            healing = None
            miss = False
            blocked = False
            critical = False
            parried = False
            
            damageElement = "Physical"

            # Set damage and healing based on skill category
            if skill.CATEGORY == "Accurate Damage":
                attacker.accuracy *= 2
            elif skill.CATEGORY == "Reduced Accuracy Damage":
                attacker.accuracy /= 2.
            if "Damage" in skill.CATEGORY:
                miss = self.miss(attacker) or "Auto Avoid" in defenderFlags
                if not self.isStunned(defender, defenderFlags):
                    blocked = self.gotBlockedBy(defender)
                    if not blocked and skill.ELEMENT == "Physical":
                        parried = self.gotParriedBy(defender)
            if skill.CATEGORY == "Accurate Damage":
                attacker.accuracy /= 2
            elif skill.CATEGORY == "Reduced Accuracy Damage":
                attacker.accuracy = int(2 * attacker.accuracy + 0.1)

            if skill.CATEGORY == "Multi-Hit Damage":
                damage = (attacker.damage * self.randomChance())
                if skill.MULTIPLIER > 1:
                    skill = copy(skill)
                    skill.MULTIPLIER -= 1
                    self.takeTurn(skill, attacker, defender, attackerFlags,
                                  defenderFlags, successfulTurnCallback)
            elif skill.CATEGORY == "Life Steal Damage":
                damage = (attacker.damage * self.randomChance())
            elif "Damage" in skill.CATEGORY:
                damage = (skill.MULTIPLIER * attacker.damage / 100. *
                      self.randomChance())

            if skill.CATEGORY == "Heal":
                healing = (skill.MULTIPLIER * self.randomChance())
            elif skill.CATEGORY == "Percent Heal":
                healing = (skill.MULTIPLIER * attacker.maxHp / 100. *
                           self.randomChance())
            elif skill.CATEGORY == "Magic Heal":
                healing = (skill.MULTIPLIER * attacker.damage / 100. *
                           self.randomChance())

            if skill.CATEGORY == "Critical Damage":
                attacker.cRate *= 4
                
            critical = self.critical(attacker)
            if damage and critical:
                damage *= attacker.cDamage / 100.
            if healing and critical:
                healing *= attacker.cDamage / 100.

            if skill.CATEGORY == "Critical Damage":
                attacker.cRate /= 4
                
            if (skill.ELEMENT == "Physical" and
                skill.CATEGORY != "No Defence Damage" and
                damage):
                damage -= defender.defence
            elif (skill.CATEGORY != "No Defence Damage" and
                  damage):
                damage -= defender.defence / 3

            if ( hasattr(attacker, "specialization") and
                 attacker.specialization == "Adrenal Avenger" and
                 attacker.hp <= attacker.maxHp / 2 and
                 damage):
                damage *= 2

            damage = self.adjustedDamage(damage)

            if ( hasattr(attacker, "specialization") and
                 attacker.specialization == "Astral Assailant" and
                 hasattr(attacker, "equippedWeapon")):
                if attacker.equippedWeapon.ELEMENT in ("Earth", "Lightning"):
                    defender.earthReduction /= 2.0
                elif attacker.equippedWeapon.ELEMENT == "Water":
                    defender.waterReduction /= 2.0
                elif attacker.equippedWeapon.ELEMENT == "Fire":
                    defender.fireReduction /= 2.0
                elif attacker.equippedWeapon.ELEMENT == "Frostfire":
                    defender.waterReduction /= 1.5
                    defender.fireReduction /= 1.5

            # Modify damage based on defender's reduction values
            if damage:
                if (skill.ELEMENT == "Earth" or
                    skill.ELEMENT == "Poison" or
                    skill.ELEMENT == "Lightning" or
                    (hasattr(attacker, "equippedWeapon") and
                     attacker.equippedWeapon.ELEMENT in ("Earth", "Lightning") and
                     skill.ELEMENT == "Physical")):
                    damage *= (100-defender.earthReduction) / 100.
                    damageElement = "Earth"
                    if ( hasattr(attacker, "specialization") and
                         attacker.specialization == "Stone Sage"):
                        damage *= 1.5
                elif (skill.ELEMENT == "Water" or
                      skill.ELEMENT == "Ice" or
                      skill.ELEMENT == "Freezing" or
                      (hasattr(attacker, "equippedWeapon") and
                       attacker.equippedWeapon.ELEMENT == "Water" and
                       skill.ELEMENT == "Physical")):
                    damage *= (100-defender.waterReduction) / 100.
                    damageElement = "Water"
                    if ( hasattr(attacker, "specialization") and
                         attacker.specialization == "Snow Sorcerer"):
                        damage *= 1.5
                elif (skill.ELEMENT == "Fire" or
                      (hasattr(attacker, "equippedWeapon") and
                       attacker.equippedWeapon.ELEMENT == "Fire" and
                       skill.ELEMENT == "Physical") or
                      (hasattr(attacker, "specialization") and
                       attacker.specialization == "Flame Knight" and
                       skill.NAME == "Attack")):
                    damage *= (100-defender.fireReduction) / 100.
                    damageElement = "Fire"
                    if ( hasattr(attacker, "specialization") and
                         attacker.specialization == "Blaze Mage"):
                        damage *= 1.5
                elif (skill.ELEMENT == "Frostfire" or
                      (hasattr(attacker, "equippedWeapon") and
                       attacker.equippedWeapon.ELEMENT == "Frostfire" and
                       skill.ELEMENT == "Physical")):
                    damage = (max(0, damage/2. * (100-defender.fireReduction)
                        / 100.)
                        + max(0, damage/2. * (100-defender.waterReduction)
                        / 100.))
                    damageElement = "Frostfire"
                    if ( hasattr(attacker, "specialization") and
                         (attacker.specialization == "Blaze Mage" or
                          attacker.specialization == "Snow Sorcerer")):
                        damage *= 1.25
                elif not (hasattr(attacker, "equippedWeapon") and
                          attacker.equippedWeapon.CATEGORY == "Wand"):
                    damage *= (100-defender.physicalReduction) / 100.

            if ( hasattr(attacker, "specialization") and
                 attacker.specialization == "Astral Assailant" and
                 hasattr(attacker, "equippedWeapon")):
                if attacker.equippedWeapon.ELEMENT in ("Earth", "Lightning"):
                    defender.earthReduction *= 2.0
                elif attacker.equippedWeapon.ELEMENT == "Water":
                    defender.waterReduction *= 2.0
                elif attacker.equippedWeapon.ELEMENT == "Fire":
                    defender.fireReduction *= 2.0
                elif attacker.equippedWeapon.ELEMENT == "Frostfire":
                    defender.waterReduction *= 1.5
                    defender.fireReduction *= 1.5

            if "Bloody Socket Active" in attackerFlags and damage is not None:
                damage = defender.hp - 1
                if not (miss or blocked or parried):
                    self.hits.append({
                        "Kind": "Bloody Attack",
                        "Target": None,
                    })

            damage = self.adjustedDamage(damage)

            if skill.CATEGORY == "Life Steal Damage":
                healing = damage * skill.MULTIPLIER / 100.
            elif "Damage" in skill.CATEGORY and hasattr(skill, "VAMPIRIC"):
                healing = damage * 0.025

            bruhMoment = False
            if ( self.mainCharacter.hasItem("Brummo Mint") and
                 attacker == self.mainCharacter and
                 critical and
                 damage and
                 skill.NAME == "Attack" and
                 not self.enemy.UNIQUE):
                bruhMoment = True
                damage = defender.hp
                self.mainCharacter.removeItem(
                    self.mainCharacter.indexOfItem("Brummo Mint"))

            if ( hasattr(attacker, "specialization") and
                 attacker.specialization == "Headshot Hunter" and
                 not (miss or blocked or parried) and damage):
                if 5 * damage >= defender.hp:
                    damage *= 5
                    self.text += "Headshot! "
                else:
                    oldAccuracy = attacker.accuracy
                    attacker.accuracy *= 0.1
                    miss = self.miss(attacker)
                    attacker.accuracy = oldAccuracy

            # Apply damage to defender and add flags
            if not (miss or blocked or parried) and damage is not None:
                if skill.CATEGORY == "XP Damage":
                    defender.xp -= int(damage)
                else:
                    defender.hp -= int(damage)
                    self.hits.append({
                        "Target": "Enemy" if defender is self.enemy else defender.NAME,
                        "Kind": damageElement,
                        "Number": int(damage),
                        "Skill": False if skill.NAME in basicSkills else True,
                        "Critical": critical,
                        "Aux": attacker in self.auxiliaryCharacters,
                    })
            if not (miss or blocked or parried) and healing is not None:
                attacker.hp += int(healing)
                self.hits.append({
                    "Target": "Enemy" if attacker is self.enemy else attacker.NAME,
                    "Kind": "Heal",
                    "Number": int(healing),
                    "Skill": False if skill.NAME in basicSkills else True,
                    "Critical": critical,
                    "Aux": attacker in self.auxiliaryCharacters,
                })
            if not (miss or blocked or parried):
                attackerFlags.add(skill.FLAG)

            # Add text corresponding to attack
            if miss:
                self.text += attacker.NAME+" missed!\n"
                self.hits.append({
                    "Target": "Enemy" if defender is self.enemy else defender.NAME,
                    "Kind": "Miss",
                    "Skill": False if skill.NAME in basicSkills else True,
                    "Aux": attacker in self.auxiliaryCharacters,
                })
                if self.mainCharacter in (attacker, defender):
                    self.sounds.append({
                        "Name": "Miss",
                        "Panning": self.getPanning(defender)})
            elif blocked or parried:
                self.text += ("%s was %s by %s!\n" % (
                    attacker.NAME,
                    "parried" if parried else "blocked",
                    defender.NAME))
                if "Defending Active" in defenderFlags and defender == self.mainCharacter:
                    self.hits.append({
                        "Target": "Enemy" if defender is self.enemy else defender.NAME,
                        "Kind": "Boost",
                        "Aux": attacker in self.auxiliaryCharacters,
                    })
                    boost = 1 + int(damage ** 0.5 * 9)
                    if ( hasattr(defender, "specialization") and
                         defender.specialization == "Guardian"):
                        defender.hp += boost
                        defender.ep += boost
                        self.text += ("Guardian rush! %s gained a %s HP/EP" +
                                      " boost from blocking.\n") % (
                                      defender.NAME, boost)
                    else:
                        defender.ep += boost
                        self.text += ("Adrenaline rush! %s gained a %s EP" +
                                      " boost from blocking.\n") % (
                                      defender.NAME, boost)
                    self.sounds.append("Boost")
                else:
                    self.hits.append({
                        "Target": "Enemy" if defender is self.enemy else defender.NAME,
                        "Kind": "Parry" if parried else "Block",
                        "Aux": attacker in self.auxiliaryCharacters,
                    })
                if self.mainCharacter in (attacker, defender):
                    self.sounds.append({
                        "Name": "Block",
                        "Panning": self.getPanning(defender)})
            else:
                if critical:
                    if damage:
                        self.text += "Critical strike! "
                    elif healing:
                        self.text += "Critical heal! "
                    if attacker == self.mainCharacter and (damage is not None and int(damage) > 0 or healing is not None and int(healing) > 0):
                        self.sounds.append("Critical Strike")
                    elif defender == self.mainCharacter and damage is not None and int(damage) > 0:
                        self.sounds.append("Critical Injury")

                if damage is not None and healing is not None:
                    self.text += (attacker.NAME+" "+skill.TEXT+" "+
                                  defender.NAME+
                                  ", dealing "+str(int(damage))+
                                  " damage and healing "+
                                  str(int(healing))+" HP.\n")
                elif damage is not None:
                    if skill.CATEGORY == "XP Damage":
                        self.text += (attacker.NAME+" "+skill.TEXT+" "+
                                      defender.NAME+
                                      ", removing "+
                                      str(int(damage))+" XP!\n")
                    else:
                        self.text += (attacker.NAME+" "+skill.TEXT+" "+
                                      defender.NAME+
                                      ", dealing "+
                                      str(int(damage))+" damage.\n")
                elif healing is not None:
                    self.text += (attacker.NAME+" "+skill.TEXT+
                                  ", healing "+str(int(healing))+" HP.\n")
                    if attacker in (self.mainCharacter, self.enemy):
                        self.sounds.append({
                            "Name": "Heal",
                            "Panning": self.getPanning(attacker)})
                elif skill.CATEGORY == "Lock On":
                        self.text += (attacker.NAME+" "+skill.TEXT+" "+
                                      defender.NAME+".\n")
                else:
                    self.text += (attacker.NAME+" "+skill.TEXT+".\n")

                if ( hasattr(attacker, "specialization") and
                     attacker.specialization == "Soul Sniper" and
                     damage and
                     int(damage) > 0 and
                     critical):
                    attacker.ep += 50
                    self.text += ("Snipe! %s restored 50 EP by scoring a critical hit.\n"
                                  % attacker.NAME)
                if ( hasattr(attacker, "specialization") and
                     attacker.specialization == "Skulker" and
                     self.roll() <= 10):
                    attacker.physicalReduction += 100
                    attackerFlags.add("Hiding")
                    self.text += ("Skulking! %s hid in the shadows.\n"
                                  % attacker.NAME)
                if ( hasattr(defender, "specialization") and
                     defender.specialization == "Son of Centaur" and
                     damage and
                     int(damage) > 0 and
                     (self.roll() <= 5 or critical and self.roll() <= 5)):
                    defender.damage += 5
                    defender.cRate += 10
                    defender.cDamage += 25
                    self.text += ("Centaur blood! %s became enraged.\n"
                                  % defender.NAME)
                if ( hasattr(attacker, "specialization") and
                     attacker.specialization == "Sandman" and
                     skill.NAME == "Attack" and
                     self.roll() <= 50):
                    defender.accuracy *= 0.9
                    self.text += ("%s got sand in %s's eye.\n"
                                  % (attacker.NAME, defender.NAME))
                if ( hasattr(attacker, "specialization") and
                     attacker.specialization == "Spirit Seer" and
                     self.roll() <= 20):
                    attacker.ep += 20
                    self.text += ("Spiritual strike! %s restored 20 EP.\n"
                                  % attacker.NAME)

                if bruhMoment:
                    self.text += ("Toshe: That was a Brummo Mint.\n")

                for stat, value in skill.USER_EFFECTS.items():
                    if value >= 0:
                        self.text += (attacker.NAME+"'s "+self.mapStat(stat)[0]+
                                      " increased by "+str(value)+
                                      self.mapStat(stat)[1]+"\n")
                    elif value < 0:
                        self.text += (attacker.NAME+"'s "+self.mapStat(stat)[0]+
                                      " decreased by "+str(-value)+
                                      self.mapStat(stat)[1]+"\n")
                    # Set both HP and max HP if max HP and HP are altered
                    # since HP can't exceed max HP and dict order is random.
                    # Discard both after so they don't get double counted.
                    if stat == "hp" and "maxHp" in skill.USER_EFFECTS:
                        continue
                    setattr(attacker, stat, getattr(attacker, stat)+value)
                    if stat == "maxHp" and "hp" in skill.USER_EFFECTS:
                        setattr(attacker, "hp", getattr(
                            attacker, "hp")+skill.USER_EFFECTS['hp'])
                for stat, value in skill.TARGET_EFFECTS.iteritems():
                    if value >= 0:
                        self.text += (defender.NAME+"'s "+self.mapStat(stat)[0]+
                                      " increased by "+str(value)+
                                      self.mapStat(stat)[1]+"\n")
                    elif value < 0:
                        self.text += (defender.NAME+"'s "+self.mapStat(stat)[0]+
                                      " decreased by "+str(-value)+
                                      self.mapStat(stat)[1]+"\n")
                    if stat == "hp" and "maxHp" in skill.TARGET_EFFECTS:
                        continue
                    setattr(defender, stat, getattr(defender, stat)+value)
                    if stat == "maxHp" and "hp" in skill.TARGET_EFFECTS:
                        setattr(defender, "hp", getattr(
                            defender, "hp")+skill.TARGET_EFFECTS['hp'])
                        
            # Add potential status ailments along with corresponding text
            if ( damage is not None and int(damage) > 0 or
                 skill.CATEGORY == "Miscellaneous") and not (miss or blocked):
                if skill.ELEMENT == "Earth" and ("Grounded" not in
                                                 defenderFlags):
                    if self.roll() <= 30:
                        self.text += defender.NAME+" was grounded!\n"
                        defenderFlags.add("Grounded")
                        if self.mainCharacter in (attacker, defender):
                            self.sounds.append({
                                "Name": "Grounded",
                                "Panning": self.getPanning(defender)})
                        if defender in (self.mainCharacter, self.enemy):
                            self.hits.append({
                                "Target": "Enemy" if defender is self.enemy else defender.NAME,
                                "Kind": "Grounded",
                                "Skill": False if skill.NAME in basicSkills else True,
                                "Aux": attacker in self.auxiliaryCharacters,})
                elif (skill.ELEMENT == "Poison" and
                      "Poisoned" not in defenderFlags and
                      defender.LIVING):
                    self.text += defender.NAME+" was poisoned!\n"
                    defenderFlags.add("Poisoned")
                    if self.mainCharacter in (attacker, defender):
                        self.sounds.append({
                            "Name": "Poisoned",
                            "Panning": self.getPanning(defender)})
                    if defender in (self.mainCharacter, self.enemy):
                        self.hits.append({
                            "Target": "Enemy" if defender is self.enemy else defender.NAME,
                            "Kind": "Poisoned",
                            "Skill": False if skill.NAME in basicSkills else True,
                            "Aux": attacker in self.auxiliaryCharacters,})
                elif ((skill.ELEMENT == "Lightning" or
                       hasattr(attacker, "equippedWeapon") and
                       attacker.equippedWeapon.ELEMENT == "Lightning" and
                       skill.ELEMENT == "Physical" and
                       "Damage" in skill.CATEGORY) and
                      "Paralyzed" not in defenderFlags):
                    if self.roll() <= 20:
                        self.text += defender.NAME+" was paralyzed!\n"
                        defenderFlags.add("Paralyzed")
                        if self.mainCharacter in (attacker, defender):
                            self.sounds.append({
                                "Name": "Paralyzed",
                                "Panning": self.getPanning(defender)})
                        if defender in (self.mainCharacter, self.enemy):
                            self.hits.append({
                                "Target": "Enemy" if defender is self.enemy else defender.NAME,
                                "Kind": "Paralyzed",
                                "Skill": False if skill.NAME in basicSkills else True,
                                "Aux": attacker in self.auxiliaryCharacters,})
                elif skill.ELEMENT == "Water":
                    if self.roll() <= 50 and damage >= defender.maxHp/2:
                        self.text += defender.NAME+" drowned!\n"
                        defender.hp = 0
                        if self.mainCharacter in (attacker, defender):
                            self.sounds.append({
                                "Name": "Drowned",
                                "Panning": self.getPanning(defender)})
                        if defender in (self.mainCharacter, self.enemy):
                            self.hits.append({
                                "Target": "Enemy" if defender is self.enemy else defender.NAME,
                                "Kind": "Drowned",
                                "Skill": False if skill.NAME in basicSkills else True,
                                "Aux": attacker in self.auxiliaryCharacters,})
                elif skill.ELEMENT == "Freezing" or (
                     (skill.ELEMENT == "Ice" or skill.ELEMENT == "Frostfire")
                      and ("Frozen" not in defenderFlags)
                      and self.roll() <= 15):
                        self.text += defender.NAME+" was frozen!\n"
                        defenderFlags.add("Frozen")
                        defenderFlags.discard("Burning")
                        if self.mainCharacter in (attacker, defender):
                            self.sounds.append({
                                "Name": "Frozen",
                                "Panning": self.getPanning(defender)})
                        if defender in (self.mainCharacter, self.enemy):
                            self.hits.append({
                                "Target": "Enemy" if defender is self.enemy else defender.NAME,
                                "Kind": "Frozen",
                                "Skill": False if skill.NAME in basicSkills else True,
                                "Aux": attacker in self.auxiliaryCharacters,})
                elif skill.ELEMENT == "Petrification" and ("Petrified" not in
                                                           defenderFlags):
                    self.text += defender.NAME+" turned to stone!\n"
                    defenderFlags.add("Petrified")
                    defenderFlags.discard("Paralyzed")
                    defenderFlags.discard("Frozen")
                    if self.mainCharacter in (attacker, defender):
                        self.sounds.append({
                            "Name": "Petrified",
                            "Panning": self.getPanning(defender)})
                    if defender in (self.mainCharacter, self.enemy):
                        self.hits.append({
                            "Target": "Enemy" if defender is self.enemy else defender.NAME,
                            "Kind": "Petrified",
                            "Skill": False if skill.NAME in basicSkills else True,
                            "Aux": attacker in self.auxiliaryCharacters,})
                elif skill.ELEMENT == "Sunder" and ("Sundered" not in
                                                    defenderFlags):
                    defenderFlags.add("Sundered")
                    if self.mainCharacter in (attacker, defender):
                        self.sounds.append({
                            "Name": "Grounded",
                            "Panning": self.getPanning(defender)})
                    # I don't think I actually need this, but this check is everywhere now; might as well be consistent
                    if defender in (self.mainCharacter, self.enemy):
                        self.hits.append({
                            "Target": "Enemy" if defender is self.enemy else defender.NAME,
                            "Kind": "Sundered",
                            "Skill": False if skill.NAME in basicSkills else True,
                            "Aux": attacker in self.auxiliaryCharacters,})
                elif ((skill.ELEMENT == "Fire" or skill.ELEMENT == "Frostfire")
                      and ("Burning" not in defenderFlags)):
                    if self.roll() <= 25:
                        self.text += defender.NAME+" caught on fire!\n"
                        defenderFlags.add("Burning")
                        defenderFlags.discard("Frozen")
                        self.burnDamage = damage/4
                        if self.mainCharacter in (attacker, defender):
                            self.sounds.append({
                                "Name": "Burning",
                                "Panning": self.getPanning(defender)})
                        if defender in (self.mainCharacter, self.enemy):
                            self.hits.append({
                                "Target": "Enemy" if defender is self.enemy else defender.NAME,
                                "Kind": "Burning",
                                "Skill": False if skill.NAME in basicSkills else True,
                                "Aux": attacker in self.auxiliaryCharacters,})

            # Make sounds
            if skill.NAME == "Defend" and attacker == self.mainCharacter:
                self.sounds.append("Defend")
            if skill.NAME == "Equip Item" and attacker == self.mainCharacter:
                self.sounds.append("Equip")

            if not (miss or blocked):
                if damage is not None:
                    if int(damage) > 0:
                        if attacker == self.mainCharacter:
                            if attacker.equippedWeapon.CATEGORY == "Wand":
                                self.sounds.append("Wand Attack")
                            elif attacker.equippedWeapon.CATEGORY == "Bow":
                                self.sounds.append("Bow Attack")
                            elif attacker.equippedWeapon.CATEGORY == "Gun":
                                self.sounds.append("Gun Attack")
                            else:
                                self.sounds.append("Deal Damage")
                        elif defender == self.mainCharacter:
                            self.sounds.append("Take Damage")
                    elif self.mainCharacter in (attacker, defender):
                        self.sounds.append({
                            "Name": "No Damage",
                            "Panning": self.getPanning(defender)})

            if ( hasattr(attacker, "specialization") and
                 attacker.specialization == "Swift Sharpshooter" and
                 attacker.accuracy > 100 and
                 damage is not None and
                 attacker.ep >= skill.EP_USED):
                attacker.ep -= skill.EP_USED
                originalAccuracy = attacker.accuracy
                attacker.accuracy -= 100
                self.takeTurn(skill, attacker, defender, set(), set())
                attacker.accuracy = originalAccuracy
            if ( hasattr(self.mainCharacter, "specialization") and
                 self.mainCharacter.specialization == "Vengeful Vigilante" and
                 defender in self.auxiliaryCharacters and
                 not self.isStunned(self.mainCharacter, self.charactersFlags[self.mainCharacter.NAME]) and
                 not (miss or blocked or parried) and
                 self.roll() <= 50 and
                 len(self.mainCharacter.skills) > 0):
                self.text += "Vengeance! "
                self.takeTurn(self.mainCharacter.skills[0], self.mainCharacter, attacker, set(), set())

        self.doAdditionalActions(skill, attacker, defender)

        # Do actions associated with flags attached to the attacker
        self.doFlagActions(attacker, attackerFlags)

        if not self.isStunned(attacker, attackerFlags):
            successfulTurnCallback()

    def mapStat(self, stat):
        """Map a given stat name to its literal description and literal modifier
        type (percentage or flat value).
        """
        return self.statStrings[stat]

    def adjustedDamage(self, damage):
        """Return the adjusted damage if it is negative."""
        if damage and damage < 0:
            return 0.1
        return damage

    def roll(self, numberOfSides=100):
        """Return a random number given a range (defaults 1-100)."""
        return random.randint(1, numberOfSides)

    def randomChance(self):
        """Return a number between .875 and 1.125"""
        return self.roll() / 400. + .875

    def isStunned(self, target, flags):
        """Return whether the target is stunned."""
        stunFlags = {"Grounded",
                     "Frozen",
                     "Recovering Active",
                     "Sleeping Active",
                     "Paralyzed",
                     "Petrified",
                     "Sundered"}
        return bool(stunFlags & flags)

    def miss(self, attacker):
        """Return whether the attacker has missed."""
        # Gryphon Clan Check
        if ("Gryphon Clan Reward" in self.mainCharacter.flags and
            attacker == self.enemy and
            self.roll() <= 1):
            self.text += ("A gryphon swoops down and lifts Toshe to avoid"+
                          " the hit!\n")
            return True
        return self.roll() > attacker.accuracy

    def gotBlockedBy(self, defender):
        """Return whether the defender has blocked."""
        return self.roll() <= defender.bRate

    def gotParriedBy(self, defender):
        return (hasattr(defender, "specialization") and
                defender.specialization == "Defender" and
                self.roll() <= 20)

    def critical(self, attacker):
        """Return whether the attacker has scored a critical hit."""
        return self.roll(1000) <= attacker.cRate*10
        
    def doAdditionalActions(self, skill, attacker, defender):
        if skill.CATEGORY == "Lock On":
            attacker.homingTarget = defender
        elif defender.NAME == "Riplin" and defender.hp <= defender.maxHp/4 and not hasattr(defender, "finalForm"):
            defender.defence = 0
            defender.cRate *= 10
            defender.finalForm = True
            self.text += ("Riplin sheds his armour!\nRiplin's defence fell to %s.\nRiplin's critical chance rose to %i%%.\n" % (defender.defence, int(defender.cRate)))
            self.sounds.append({
                "Name": "Remove Armour",
                "Panning": self.getPanning(defender)})

    def doFlagActions(self, target, flags):
        """Perform any actions specified by current flags on the target."""
        if "Frozen" in flags:
            if self.roll() <= 25:
                flags.remove("Frozen")
                self.text += target.NAME+" thaws.\n"
                if target in (self.mainCharacter, self.enemy):
                    self.sounds.append({
                        "Name": "Break Free",
                        "Panning": self.getPanning(target)})
            else:
                self.text += target.NAME+" is frozen solid.\n"
        elif "Petrified" in flags:
            if self.roll() <= 25:
                flags.remove("Petrified")
                self.text += target.NAME+" is no longer a statue.\n"
                if target in (self.mainCharacter, self.enemy):
                    self.sounds.append({
                        "Name": "Break Free",
                        "Panning": self.getPanning(target)})
            else:
                self.text += target.NAME+" is a statue.\n"
        elif "Paralyzed" in flags:
            if self.roll() <= 50:
                flags.remove("Paralyzed")
                self.text += (target.NAME+" is no longer affected by "+
                              "paralysis.\n")
                if target in (self.mainCharacter, self.enemy):
                    self.sounds.append({
                        "Name": "Break Free",
                        "Panning": self.getPanning(target)})
            else:
                self.text += target.NAME+" is paralyzed.\n"
        elif "Sundered" in flags:
            flags.remove("Sundered")
            self.text += target.NAME+" is recovering.\n"
        elif "Grounded" in flags:
            flags.remove("Grounded")
            self.text += target.NAME+" is breaking free.\n"
            if target in (self.mainCharacter, self.enemy):
                self.sounds.append({
                    "Name": "Break Free",
                    "Panning": self.getPanning(target)})
        if "Poisoned" in flags:
            poisonDamage = int(target.maxHp/50*self.randomChance())
            target.hp -= poisonDamage
            self.text += ("Venom seeps into "+target.NAME+"'s blood, dealing "
                     +str(poisonDamage)+" damage.\n")
        elif "Burning" in flags:
            if self.roll() <= 25:
                flags.remove("Burning")
                self.text += target.NAME+" stopped burning.\n"
                if target in (self.mainCharacter, self.enemy):
                    self.sounds.append({
                        "Name": "Break Free",
                        "Panning": self.getPanning(target)})
            else:
                burnDamage = int(self.burnDamage*self.randomChance())
                target.hp -= burnDamage
                self.text += ("Fire continues to singe "+target.NAME+", dealing "
                              +str(burnDamage)+" damage.\n")
                
        if "Recovering Active" in flags:
            self.text += target.NAME+" is regaining composure.\n"
            if target in (self.mainCharacter, self.enemy):
                self.sounds.append({
                    "Name": "Break Free",
                    "Panning": self.getPanning(target)})
            flags.remove("Recovering Active")
        if "Recovering" in flags:
            flags.remove("Recovering")
            flags.add("Recovering Active")

        if any([flag in flags for flag in [
            "Re-energizing Active", "Re-energizing 2", "Re-energizing 3"]]):
            epGain = 5 + target.wisdom // 2 + target.maxEp // 20
            target.ep += epGain
            self.text += "%s re-energizes %s EP.\n" % (target.NAME, epGain)
        if "Re-energizing" in flags:
            flags.remove("Re-energizing")
            flags.add("Re-energizing Active")
        elif "Re-energizing Active" in flags:
            flags.add("Re-energizing 2")
            flags.remove("Re-energizing Active")
        elif "Re-energizing 2" in flags:
            flags.add("Re-energizing 3")
            flags.remove("Re-energizing 2")
        elif "Re-energizing 3" in flags:
            self.text += target.NAME+" has finished re-energizing.\n"
            flags.remove("Re-energizing 3")

        if "Golden Fur" in flags:
            pass
        elif "Golden Fur Active" in flags:
            self.text += target.NAME+"'s golden fur is shining brightly.\n"
        elif "Golden Fur 2" in flags:
            self.text += target.NAME+"'s golden fur is fading.\n"
        elif "Golden Fur 3" in flags:
            self.text += target.NAME+"'s fur returned to normal.\n"
        if "Golden Fur 3" in flags:
            target.bRate -= 75
            flags.remove("Golden Fur 3")
        if "Golden Fur 2" in flags:
            flags.add("Golden Fur 3")
            flags.remove("Golden Fur 2")
        if "Golden Fur Active" in flags:
            flags.add("Golden Fur 2")
            flags.remove("Golden Fur Active")
        if "Golden Fur" in flags:
            flags.remove("Golden Fur")
            flags.add("Golden Fur Active")
            self.sounds.append({
                "Name": "Bolster Defence",
                "Panning": self.getPanning(target)})

        if "Giacomo Defending" in flags:
            pass
        elif "Giacomo Defending Active" in flags:
            self.text += target.NAME+" resumes parrying.\n"
        elif "Giacomo Defending 2" in flags:
            self.text += target.NAME+"'s guard goes down.\n"
        if "Giacomo Defending 2" in flags:
            flags.remove("Giacomo Defending 2")
            target.defence -= 500
        if "Giacomo Defending Active" in flags:
            flags.add("Giacomo Defending 2")
            flags.remove("Giacomo Defending Active")
        if "Giacomo Defending" in flags:
            flags.remove("Giacomo Defending")
            flags.add("Giacomo Defending Active")
            self.sounds.append({
                "Name": "Bolster Defence",
                "Panning": self.getPanning(target)})
        
        if "Defending Active" in flags and "Defending" not in flags:
            self.text += target.NAME+"'s guard goes down.\n"
        if "Defending Active" in flags:
            target.bRate -= self.DEFEND_BLOCK_VALUE
            if ( hasattr(target, "equippedWeapon") and
                 target.hasItem("Macedonian Protector")):
                target.bRate -= int(self.PROTECTOR_BLOCK_VALUE *
                                    target.baseBRate)
            flags.remove("Defending Active")
        if "Defending" in flags:
            target.bRate += self.DEFEND_BLOCK_VALUE
            if hasattr(target, "equippedWeapon"):
                epBoost = int(5 + target.wisdom ** 0.75)
                target.ep += epBoost
                self.text += target.NAME+" restored "+str(epBoost)+" EP.\n"
                if target.hasItem("Macedonian Protector"):
                    target.bRate += int(self.PROTECTOR_BLOCK_VALUE *
                                        target.baseBRate)
            flags.remove("Defending")
            flags.add("Defending Active")

        if "Hiding Active" in flags and "Hiding" not in flags:
            self.text += target.NAME+" came out of hiding.\n"
        if "Hiding Active" in flags:
            target.physicalReduction -= 100
            flags.remove("Hiding Active")
        if "Hiding" in flags:
            flags.remove("Hiding")
            flags.add("Hiding Active")
            self.sounds.append({
                "Name": "Bolster Defence",
                "Panning": self.getPanning(target)})

        if "Aggression Active" in flags and "Aggression" not in flags:
            self.text += target.NAME+" returned to guarding position.\n"
        if "Aggression Active" in flags:
            target.damage -= 50
            flags.remove("Aggression Active")
        if "Aggression" in flags:
            flags.remove("Aggression")
            flags.add("Aggression Active")
            self.sounds.append({
                "Name": "Bolster Attack",
                "Panning": self.getPanning(target)})

        if "Homing Active" in flags and "Homing" not in flags:
            self.text += target.NAME+" stopped homing.\n"
            del target.homingTarget
        if "Homing Active" in flags:
            target.accuracy -= 90
            target.cRate -= 90
            flags.remove("Homing Active")
        if "Homing" in flags:
            flags.remove("Homing")
            flags.add("Homing Active")
            flags.add("Recovering")
            if "Recovering Active" in flags:
                flags.remove("Recovering Active")
            self.sounds.append({
                "Name": "Bolster Attack",
                "Panning": self.getPanning(target)})

        if "Escaping 2" in flags and False not in [
            flag not in flags for flag in [
                "Escaping",
                "Escaping Active"]]:
            self.text += target.NAME+" stopped running.\n"
        if "Escaping 2" in flags:
            flags.remove("Escaping 2")
            flags.discard("Auto Avoid")
        if "Escaping Active" in flags:
            self.text += target.NAME+" is moving too quickly to be hit.\n"
            flags.add("Escaping 2")
            flags.remove("Escaping Active")
            flags.add("Auto Avoid")
        if "Escaping" in flags:
            flags.remove("Escaping")
            flags.add("Escaping Active")
            flags.add("Auto Avoid")
            self.sounds.append({
                "Name": "Bolster Defence",
                "Panning": self.getPanning(target)})

        if "Regenerating 2" in flags:
            self.text += target.NAME+" is regenerating.\n"
            flags.remove("Regenerating 2")
            target.hp += 500
        if "Regenerating Active" in flags:
            self.text += target.NAME+" is regenerating.\n"
            flags.remove("Regenerating Active")
            flags.add("Regenerating 2")
            target.hp += 500
        if "Regenerating" in flags:
            self.text += target.NAME+" is regenerating.\n"
            flags.remove("Regenerating")
            flags.add("Regenerating Active")
            target.hp += 500

        if "Winding Up Active" in flags:
            target.defence += 1800
            target.damage -= 70
            target.cRate -= 100
            self.text += target.NAME+" is winding down.\n"
            flags.add("Regenerating")
            flags.remove("Winding Up Active")
        if "Winding Up" in flags:
            flags.remove("Winding Up")
            flags.add("Winding Up Active")
            self.sounds.append({
                "Name": "Bolster Attack",
                "Panning": self.getPanning(target)})

        if "Bloody Socket Active" in flags:
            flags.remove("Bloody Socket Active")
        if "Bloody Socket" in flags:
            flags.remove("Bloody Socket")
            flags.add("Bloody Socket Active")
            flags.add("Recovering")
            if "Recovering Active" in flags:
                flags.remove("Recovering Active")
            self.hits.append({
                "Kind": "Bloody Up",
                "Target": None,
            })

        if "Sleeping 3" in flags:
            self.text += target.NAME+" woke up.\n"
            flags.remove("Sleeping 3")
            flags.remove("Sleeping Active")
        if "Sleeping 2" in flags:
            flags.add("Sleeping 3")
            flags.remove("Sleeping 2")
        if "Sleeping Active" in flags and False not in [
            flag not in flags for flag in [
                "Sleeping 2",
                "Sleeping 3"]]:
            flags.add("Sleeping 2")
        if "Sleeping" in flags:
            flags.remove("Sleeping")
            flags.add("Sleeping Active")
            flags.add("Regenerating")

        # Affinity group
        if "Earth Affinity" in flags:
            pass
        elif "Earth Affinity Active" in flags:
            self.text += target.NAME+"'s earth affinity is strong.\n"
        elif "Earth Affinity 2" in flags:
            self.text += target.NAME+"'s earth affinity is losing strength.\n"
        elif "Earth Affinity 3" in flags:
            self.text += target.NAME+" no longer has earth affinity.\n"
        if "Earth Affinity 3" in flags:
            target.earthReduction -= 25
            flags.remove("Earth Affinity 3")
        if "Earth Affinity 2" in flags:
            target.earthReduction -= 25
            flags.add("Earth Affinity 3")
            flags.remove("Earth Affinity 2")
        if "Earth Affinity Active" in flags:
            flags.add("Earth Affinity 2")
            flags.remove("Earth Affinity Active")
        if "Earth Affinity" in flags:
            flags.remove("Earth Affinity")
            flags.add("Earth Affinity Active")

        if "Water Affinity" in flags:
            pass
        elif "Water Affinity Active" in flags:
            self.text += target.NAME+"'s water affinity is strong.\n"
        elif "Water Affinity 2" in flags:
            self.text += target.NAME+"'s water affinity is losing strength.\n"
        elif "Water Affinity 3" in flags:
            self.text += target.NAME+" no longer has water affinity.\n"
        if "Water Affinity 3" in flags:
            target.waterReduction -= 25
            flags.remove("Water Affinity 3")
        if "Water Affinity 2" in flags:
            target.waterReduction -= 25
            flags.add("Water Affinity 3")
            flags.remove("Water Affinity 2")
        if "Water Affinity Active" in flags:
            flags.add("Water Affinity 2")
            flags.remove("Water Affinity Active")
        if "Water Affinity" in flags:
            flags.remove("Water Affinity")
            flags.add("Water Affinity Active")

        if "Fire Affinity" in flags:
            pass
        elif "Fire Affinity Active" in flags:
            self.text += target.NAME+"'s fire affinity is strong.\n"
        elif "Fire Affinity 2" in flags:
            self.text += target.NAME+"'s fire affinity is losing strength.\n"
        elif "Fire Affinity 3" in flags:
            self.text += target.NAME+" no longer has fire affinity.\n"
        if "Fire Affinity 3" in flags:
            target.fireReduction -= 25
            flags.remove("Fire Affinity 3")
        if "Fire Affinity 2" in flags:
            target.fireReduction -= 25
            flags.add("Fire Affinity 3")
            flags.remove("Fire Affinity 2")
        if "Fire Affinity Active" in flags:
            flags.add("Fire Affinity 2")
            flags.remove("Fire Affinity Active")
        if "Fire Affinity" in flags:
            flags.remove("Fire Affinity")
            flags.add("Fire Affinity Active")

    def tosheAlertMessages(self):
        """Add any low HP alert messages concerning Toshe's HP to the running
        text.
        """
        if (self.mainCharacter.hp < self.mainCharacter.maxHp/20) and\
           not self.hpAlert3:
            self.text += "Toshe: I can't breathe."
            self.hpAlert3 = True
            self.hpAlert2 = True
            self.hpAlert1 = True
            self.sounds.append("Low HP")
            self.sounds.append("Low HP")
            self.sounds.append("Low HP")

        elif (self.mainCharacter.hp < self.mainCharacter.maxHp/10) and\
             not self.hpAlert2:
            self.text += "Toshe: My heart..."
            self.hpAlert2 = True
            self.hpAlert1 = True
            self.sounds.append("Low HP")
            self.sounds.append("Low HP")

        elif (self.mainCharacter.hp < self.mainCharacter.maxHp/4) and\
             not self.hpAlert1:
            self.text += "Toshe: I'm in pain!"
            self.hpAlert1 = True
            self.sounds.append("Low HP")

        elif (self.mainCharacter.hp >= self.mainCharacter.maxHp/4):
            self.hpAlert1 = False
            self.hpAlert2 = False
            self.hpAlert3 = False

    def checkDeath(self):
        """Check for any deaths and take appropriate action.

        Return true if battle ending death has occurred."""
        # Skeleton clan check
        if (self.mainCharacter.isDead() and
            "Skeleton Clan Reward" in self.mainCharacter.flags):
            if self.roll() <= 6:
                self.mainCharacter.hp = 1
                self.text += "Toshe rose from the dead!\n"
        # Coliseum mode check
        if ( self.coliseumMode and
             self.mainCharacter.hp <= self.CHARACTER_DEATH_HP):
            self.mainCharacter.hp = self.CHARACTER_DEATH_HP
            self.endBattle()
            return True
        # Syvre leaf check
        if ( self.mainCharacter.isDead() and
             self.mainCharacter.hasItem("Syvre Leaf")):
            self.mainCharacter.hp = self.mainCharacter.maxHp / random.randint(2, 8)
            self.text += ("Toshe uses his last ounce of energy to consume" +
                          " a syvre leaf. He breathes a sigh of relief and" +
                          " continues the fight!\n")
            self.mainCharacter.removeItem(
                self.mainCharacter.indexOfItem("Syvre Leaf"))
        if self.mainCharacter.isDead() or self.enemy.isDead():
            self.endBattle()
            return True
        elif self.auxiliaryCharacters:
            for character in self.auxiliaryCharacters:
                if character.isDead():
                    self.text += character.NAME+" retreats from combat!\n"
                    self.auxiliaryCharacters.remove(character)
                    self.sounds.append("Dead")
        return False

    def checkConsumables(self, skill):
        """Check if any consumables should be consumed and take action."""
        if skill.NAME == "Attack":
            for item in self.consumableEffects:
                while self.mainCharacter.hasItem(item):
                    for effects in self.consumableEffects[item]:
                        if effects['type'] == "Add":
                            setattr(self.mainCharacter,
                                    effects['stat'],
                                    getattr(self.mainCharacter,
                                            effects['stat'])
                                    + effects['value'])
                        elif effects['type'] == "Multiply":
                            setattr(self.mainCharacter,
                                    effects['stat'],
                                    effects['value']
                                    * getattr(self.mainCharacter,
                                              effects['multiplicand']))
                    aOrAn = "an" if item[0] in ("A", "E", "I", "O", "U")\
                    else "a"
                    self.text += ("Toshe consumes %s %s!\n" % (aOrAn, item))
                    self.mainCharacter.removeItem(
                        self.mainCharacter.indexOfItem(item))
        

    def endBattle(self):
        """End the battle.

        If Toshe dies, the death is handled by the main program. If the enemy
        dies, its XP and euros are added to Toshe's, and text is added
        ("defeated" or "surrendered", depending on whether the enemy dies. There
        is also a chance that an item will be added to Toshe's inventory if
        the enemy was carrying one.
        If Toshe flees, text is added.
        This method returns actions for the GUI.
        """
        self.view = "battle over"
        for character in self.auxiliaryCharacters+[self.mainCharacter]:
            character.updateStats()
        if self.mainCharacter.isDead():
            self.view = "game over"
            self.sounds.append("Dead")
        elif self.enemy.isDead():
            if self.enemy.DEATH_HP > 0:
                self.text += ("\n"+self.enemy.NAME+" surrenders!\n")
                self.enemy.hp = self.enemy.DEATH_HP
            else:
                self.text += ("\n"+self.enemy.NAME+" has been defeated!\n")
            jackpotRoll = self.roll()
            if jackpotRoll <= 4:
                self.text += "Jackpot!\n"
                xpGained = self.enemy.XP*2
                eurosGained = self.enemy.EUROS*2
                self.sounds.append("Jackpot")
            elif jackpotRoll <= 5:
                self.text += "Double Jackpot!\n"
                xpGained = self.enemy.XP*4
                eurosGained = self.enemy.EUROS*4
                self.sounds.append("Jackpot")
                self.sounds.append("Jackpot")
            # Pirate Clan Check
            elif ("Pirate Clan Reward" in self.mainCharacter.flags
                  and jackpotRoll <= 9):
                self.text += "Pirate Jackpot!\n"
                xpGained = self.enemy.XP*2
                eurosGained = self.enemy.EUROS*2
                self.sounds.append("Jackpot")
            elif ("Pirate Clan Reward" in self.mainCharacter.flags
                  and jackpotRoll <= 10):
                self.text += "Double Pirate Jackpot!\n"
                xpGained = self.enemy.XP*4
                eurosGained = self.enemy.EUROS*4
                self.sounds.append("Jackpot")
                self.sounds.append("Jackpot")
            else:
                xpGained = self.enemy.XP
                eurosGained = self.enemy.EUROS

            if self.mainCharacter.mode == "Easy":
                xpGained *= 2
            elif self.mainCharacter.mode == "Ultimate":
                xpGained *= 5

            divisor = (self.mainCharacter.level - self.enemy.LEVEL)
            if divisor <= 0:
                divisor = 1
            
            xpGained /= divisor

            if self.mainCharacter.specialization == "Spirit Seer":
                xpGained = int(xpGained * (1 + 0.1 * self.mainCharacter.mastery))
            if self.mainCharacter.specialization == "Alchemist":
                eurosGained = int(eurosGained * (1 + 0.2 * self.mainCharacter.mastery))

            if self.mainCharacter.hasItem("Psilocybin"):
                roll = self.roll(11) - 1
                xpGained *= roll
                if roll > 1:
                    self.text += "Psychedelic! "
                elif roll == 0:
                    self.text += "Bad vibes! "
                    self.mainCharacter.removeItem(
                        self.mainCharacter.indexOfItem("Psilocybin"))

            if self.mainCharacter.ring is not None:
                self.mainCharacter.ring.xp += xpGained
                xpGainString = "Scintillous Ring gains "+str(xpGained)+" XP.\n"
            else:
                self.mainCharacter.xp += xpGained
                xpGainString = "You gain "+str(xpGained)+" XP.\n"
            for character in self.auxiliaryCharacters:
                character.xp += xpGained
            self.mainCharacter.euros += eurosGained
            euroGainString = "You gain "+str(eurosGained)+" euros.\n"
            if self.mainCharacter.mode == "Ultimate":
                euroGainString = ""
            self.text += (xpGainString+euroGainString)
            if ( eurosGained == 0 and self.enemy.LIVING
                 and self.enemy.DEATH_HP <= 0
                 and self.roll() <= max(1, 20 - self.mainCharacter.level + self.enemy.LEVEL)):
                self.mainCharacter.potions += 1
                self.text += ("You collect a hearty vial of life fluid.\n")
            if self.enemy.IDENTIFIER not in self.mainCharacter.flags['Kills']:
                self.mainCharacter.flags['Kills'][self.enemy.IDENTIFIER] = 0
            self.mainCharacter.flags['Kills'][self.enemy.IDENTIFIER] += 1
            if self.mainCharacter.specialization is not None:
                self.mainCharacter.sp += 1
                if self.mainCharacter.hasItem("Sigil of Ascension"):
                    self.mainCharacter.sp += 4
            if self.enemy.IDENTIFIER == "Will o Wisp" and "Labyrinth Size" in self.mainCharacter.flags:
                self.mainCharacter.flags['Labyrinth Size'] -= 1
            if self.mainCharacter.hasItem("The good stuff!") and self.roll(15) == 1:
                event = random.choice([
                    "Your heart starts beating increasingly faster until it explodes.",
                    "You haven't drank water in over 72 hours.",
                    "You trip over a pebble and forget to catch yourself, landing head-first.",
                ])
                self.text += ("Unfortunately, %s\n" % event.lower())
                self.mainCharacter.hp = 0
                self.view = "game over"
                self.sounds.append("Dead")
                if self.mainCharacter.checkpoint.hasItem("The good stuff!"):
                    self.mainCharacter.checkpoint.removeItem(self.mainCharacter.checkpoint.indexOfItem("The good stuff!"))
            else:
                self.sounds.append("Kill")
        elif (self.coliseumMode and
              self.mainCharacter.hp <= self.CHARACTER_DEATH_HP):
            self.text += "Toshe surrenders!"
        else:
            self.text += "You flee from battle."
            self.sounds.append("Flee")

    def checkDroppedItem(self):
        """Checks if the enemy left behind an item upon death.

        Returns the item name if one was dropped, otherwise None."""
        if self.enemy.isDead():
            drop = self.selectRandomElement(self.enemy.ITEMS, self.enemy.UNIQUE)
            if drop and (drop != "Brummo Mint" or
                         not self.mainCharacter.hasItem(drop)):
                self.text += (self.enemy.NAME+" left behind an item: "+
                              drop+"!")
                return drop
            
    def selectRandomElement(self, probabilities, fixed=False):
        """Select a random element from a dictionary of element: probability
        pairs.

        The probability value is out of 100 and is independent of the other
        probabilities.
        """
        if fixed:
            random.seed(self.mainCharacter.rareSeed + self.enemy.IDENTIFIER)
        randomNumber = self.roll()
        chanceCounter = 0
        for element in probabilities:
            chanceCounter += probabilities[element]
            if self.mainCharacter.hasItem("The good stuff!"):
                chanceCounter += probabilities[element]
            if chanceCounter >= randomNumber:
                return element
        return None
