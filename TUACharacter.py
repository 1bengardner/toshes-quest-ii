"""
File: TUACharacter.py
Author: Ben Gardner
Created: January 25, 2013
Revised: June 3, 2023
"""


class Character(object):
    """Contains all information about the character.

    level: Experience level.
    xp: Current experience.
    xpTnl: Experience needed to get to the next level.
    hp: Health points.
    maxHp: Maximum health points.
    ep: Energy points.
    maxEp: Maximum energy points.
    strength: Strength (determines melee damage etc).
    dexterity: Dexterity (determines ranged damage etc).
    wisdom: Wisdom (determines magic damage etc).
    euros: Money (to buy things).
    mercenaries: Party members on your team.
    items: Items in inventory.
    equippedItemIndices: Indices of items that are equipped.
    equippedWeapon: Equipped weapon object.
    equippedArmour: Equipped armour object.
    equippedShield: Equipped shield object.
    blankWeapon: Placeholder weapon when none is equipped.
    blankArmour: Placeholder armour when none is equipped.
    blankShield: Placeholder shield when none is equipped.
    statPoints: Number of available stat points to spend.
    flags: Game completion markers that are used throughout the game to
        indicate when event triggers should occur (flag: state).
    area: The area object in which the character is situated. Used for game
        saves/loads.
    x: X coordinate of the character in the area. Used for game saves/loads.
    y: Y coordinate of the character in the area. Used for game saves/loads.
    potions: Available potion count.
    """

    def __init__(self, name, level, xp, xpTnl, hp, maxHp, ep, maxEp, strength,
                 dexterity, wisdom, skills, euros, mercenaries,
                 items, equippedItemIndices,
                 equippedWeapon, equippedArmour, equippedShield,
                 blankWeapon, blankArmour, blankShield,
                 statPoints, flags, area, x, y, potions):
        self.NAME = str(name)
        self.level = int(level)
        self.xp = int(xp)
        self.xpTnl = int(xpTnl)
        self._hp = int(hp)
        self._maxHp = int(maxHp)
        self._ep = int(ep)
        self._maxEp = int(maxEp)
        self._strength = int(strength)
        self._dexterity = int(dexterity)
        self._wisdom = int(wisdom)
        self.skills = skills
        self.euros = int(euros)
        self.mercenaries = list(mercenaries)
        self.items = list(items)
        self.equippedItemIndices = dict(equippedItemIndices)
        self.equippedWeapon = equippedWeapon
        self.equippedArmour = equippedArmour
        self.equippedShield = equippedShield
        self.blankWeapon = blankWeapon
        self.blankArmour = blankArmour
        self.blankShield = blankShield
        self.statPoints = int(statPoints)
        self.flags = dict(flags)
        self.area = area
        self.x = int(x)
        self.y = int(y)
        self.potions = int(potions)
        self.LIVING = 1
        self.checkpoint = None
        self.quests = []
        self._specialization = None
        self.mastery = 1
        self.sp = 0
        self.updateStats()

    def updateStats(self):
        """Update stats that are dependent on other stats."""
        power = self.equippedWeapon.POWER
        if ((self.specialization == "Blaze Mage" and
             self.equippedWeapon.CATEGORY == "Wand") or
            self.specialization == "Astral Assailant" or
            (self.specialization == "Weird Warlock" and
             self.equippedWeapon.CATEGORY not in
             set(["Sword", "Bludgeon", "Axe", "Spear"])) or
            (self.specialization == "Magic Marksman" and
             self.equippedWeapon.CATEGORY == "Bow")):
            power += 2 * (self.mastery - 1)
        if self.specialization == "Son of Centaur":
            power *= 1 + 0.01 * (self.mastery - 1)
        if self.specialization == "Vengeful Vigilante":
            power *= 1 + 0.02 * (self.mastery - 1)
        power = int(power)
        if self.specialization == "Magic Marksman":
            self.damage = (self.dexterity + self.wisdom) * power / 10
        elif self.equippedWeapon.CATEGORY == "Gun":
            self.damage = power
        elif self.equippedWeapon.REQUIREMENT_TYPE == "Strength":
            self.damage = self.strength * power / 10
        elif self.equippedWeapon.REQUIREMENT_TYPE == "Dexterity":
            self.damage = self.dexterity * power / 10
        elif self.equippedWeapon.REQUIREMENT_TYPE == "Wisdom":
            self.damage = self.wisdom * power / 10
        cRate = self.equippedWeapon.C_RATE
        cDamage = self.equippedWeapon.C_DAMAGE
        accuracy = self.equippedWeapon.ACCURACY
        if self.specialization == "Adrenal Avenger":
            cRate *= 1 + 0.03 * (self.mastery - 1)
        self.cRate = round(cRate * self.baseCRate, 1)
        if self.specialization == "Critical Caster":
            cDamage *= 1 + 0.03 * (self.mastery - 1)
            accuracy = 0
            self.cRate = 100
        self.cDamage = int(cDamage * self.baseCDamage)
        self.accuracy = int(accuracy + self.baseAccuracy)
        bRate = self.equippedShield.B_RATE
        if self.specialization == "Defender":
            bRate *= 1 + 0.03 * (self.mastery - 1)
        self.bRate = int(bRate * self.baseBRate)
        self.earthReduction = int(self.equippedArmour.EARTH_REDUCTION +
                                  self.equippedShield.EARTH_REDUCTION +
                                  self.baseReduction)
        self.waterReduction = int(self.equippedArmour.WATER_REDUCTION +
                                  self.equippedShield.WATER_REDUCTION +
                                  self.baseReduction)
        self.fireReduction = int(self.equippedArmour.FIRE_REDUCTION +
                                 self.equippedShield.FIRE_REDUCTION +
                                 self.baseReduction)
        self.physicalReduction = int(self.equippedArmour.PHYSICAL_REDUCTION +
                                     self.equippedShield.PHYSICAL_REDUCTION)
        self.defence = int(self.equippedArmour.DEFENCE +
                           self.equippedShield.DEFENCE)

        if self.specialization == "Flame Knight":
            self.fireReduction += 2 * (self.mastery - 1)
        if self.specialization == "Reckless Lancer":
            self.damage += 2 * (self.mastery - 1)
            if self.equippedWeapon.CATEGORY == "Spear":
                self.damage *= 2
                self.accuracy //= 2
        if self.specialization == "Stalwart Slayer":
            self.damage *= 4
            self.cRate = 0
        if (self.specialization == "Executioner" and
            self.equippedWeapon.CATEGORY == "Axe"):
            self.cDamage *= 3
        if self.specialization == "Swift Sharpshooter":
            self.accuracy += 2 * (self.mastery - 1)
        if self.specialization == "Soul Sniper":
            self.cRate += 0.5 * (self.mastery - 1)
        if self.specialization == "Headshot Hunter":
            self.cDamage += 5 * (self.mastery - 1)
        if self.specialization == "Skulker":
            self.earthReduction += 1 * (self.mastery - 1)
            self.waterReduction += 1 * (self.mastery - 1)
            self.fireReduction += 1 * (self.mastery - 1)
        if self.specialization == "Stone Sage":
            self.bRate += 1 * (self.mastery - 1)
        if self.specialization == "Mystic":
            self.physicalReduction += 1 * (self.mastery - 1)
        if self.specialization == "Guardian":
            self.defence += 2 * (self.mastery - 1)
        if self.specialization == "Scallywag":
            self.waterReduction += int(max(0, 0.5 * (self.mastery - 1) * (self.accuracy - 100)))
        if self.specialization == "Sandman":
            self.earthReduction += 3 * (self.mastery - 1)
        if self.specialization == "Hermit":
            self.defence *= 2

    @property
    def ep(self):
        return self._ep

    @ep.setter
    def ep(self, value):
        self._ep = value
        if self._ep > self.maxEp:
            self._ep = self.maxEp
        if self._ep < 0:
            self._ep = 0

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if self._hp > self.maxHp:
            self._hp = self.maxHp
        if "Rested" in self.flags:
            for mercenary in self.mercenaries:
                mercenary.hp = mercenary.maxHp
        
    @property
    def strength(self):
        if self.specialization == "Stalwart Slayer":
            return self._strength + 2 * (self.mastery - 1)
        elif self.specialization == "Squad Leader":
            return self._strength + 1 * (self.mastery - 1)
        return self._strength

    @strength.setter
    def strength(self, value):
        """Change strength and update its associated values.

        Values: damage*, cDamage
        Increases critical damage by 1% of base critical damage per point.
        """
        self._strength += value - self.strength
        self.updateStats()

    @property
    def dexterity(self):
        if self.specialization == "Executioner":
            return self._dexterity + 2 * (self.mastery - 1)
        elif self.specialization == "Squad Leader":
            return self._dexterity + 1 * (self.mastery - 1)
        return self._dexterity

    @dexterity.setter
    def dexterity(self, value):
        """Change dexterity and update its associated values.

        Values: damage*, accuracy, cRate, bRate
        Adds 0.5% accuracy per point.
        Increases critical chance by 1% of base critical chance per point.
        Increases block chance by 5% of base block chance per point.
        """
        self._dexterity += value - self.dexterity
        self.updateStats()

    @property
    def wisdom(self):
        if self.specialization == "Snow Sorcerer":
            return self._wisdom + 2 * (self.mastery - 1)
        elif self.specialization == "Squad Leader":
            return self._wisdom + 1 * (self.mastery - 1)
        return self._wisdom

    @wisdom.setter
    def wisdom(self, value):
        """Chance wisdom and update its associated values.

        Values: damage*, earthReduction, waterReduction, fireReduction
        Adds 0.1% to all element reductions per point.
        """
        self._wisdom += value - self.wisdom
        self.updateStats()

    @property
    def maxHp(self):
        if self.specialization == "Paladin":
            return self._maxHp + 20 * (self.mastery - 1)
        return self._maxHp

    @maxHp.setter
    def maxHp(self, value):
        self._maxHp += value - self.maxHp

    @property
    def maxEp(self):
        if self.specialization == "Hermit":
            return self._maxEp + 20 * (self.mastery - 1)
        return self._maxEp

    @maxEp.setter
    def maxEp(self, value):
        self._maxEp += value - self.maxEp

    @property
    def baseCDamage(self):
        return 0.01*(100+self.strength-10)

    @property
    def baseAccuracy(self):
        return self.dexterity-10

    @property
    def baseCRate(self):
        return 0.01*(100+self.dexterity-10)

    @property
    def baseBRate(self):
        return 0.01*(100+5*(self.dexterity-10))

    @property
    def baseReduction(self):
        if self.wisdom < 10:
            return -(abs(self.wisdom-10)**2)
        else:
            return 3*(self.wisdom-10)**0.5
            
    @property
    def spTnl(self):
        if self.mastery > 5:
            return self.mastery * 50 - 100
        return (self.mastery ** 2 - self.mastery + 10) // 2 * 10

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, value):
        self.mastery = 1
        self.sp = 0
        if self._specialization == "Paladin":
            extraPoints = self.level - 1
            while extraPoints > 0:
                if extraPoints % 3 == 0:
                    self.strength -= 1
                elif extraPoints % 3 == 1:
                    self.dexterity -= 1
                elif extraPoints % 3 == 2:
                    self.wisdom -= 1
                extraPoints -= 1
        if value == "Paladin":
            self.statPoints += self.level - 1
        self._specialization = value
        self.updateStats()

    def hasLeveledUp(self):
        """Check if the character has enough xp to level up."""
        if self.ring is not None:
            if self.ring.xp >= self.ring.xpTnl:
                self.ring.level += 1
                self.ring.xp = self.ring.xp - self.ring.xpTnl
                self.ring.xpTnl += 20*self.ring.level**2 - 20*self.ring.level + 100
                return True
            return False
        elif self.xp >= self.xpTnl:
            hpGainedOnLevelUp = 20
            epGainedOnLevelUp = 20
            
            self.level += 1
            self.xp = self.xp - self.xpTnl
            self.xpTnl += 20*self.level**2 - 20*self.level + 100
            if self.NAME == "Toshe":
                self.statPoints += 5
                if self.specialization == "Paladin":
                    self.statPoints += 1
            elif self.NAME == "Dragan":
                self.dexterity += 5
            elif self.NAME == "Qendresa":
                self.strength += 5
            elif self.NAME == "Barrie":
                self.wisdom += 5
            self.maxHp += hpGainedOnLevelUp
            self.maxEp += epGainedOnLevelUp
            self.hp = self.maxHp
            self.ep = self.maxEp
            return True
        return False
        
    def hasSpecializedUp(self):
        """Check if the character has enough kills to specialize up."""
        if self.sp >= self.spTnl:
            self.sp = self.sp - self.spTnl
            self.mastery += 1
            self.updateStats()
            return True
        return False

    def equip(self, itemIndex):
        """Equip an item to the character, or unequips it if it already on.

        Sets the item at the specified index as the equipped weapon, armour or
        shield depending on its category. The character's stats are adjusted
        according to the item properties. Invoking on an item that is equipped
        will cause it to be unassigned from the equippedX variable and its
        properties will no longer affect the character.

        Parameters:
        int itemIndex: The index in the inventory of the item to be
        equipped/unequipped.
        """
        item = self.items[itemIndex]
        if itemIndex not in self.equippedItemIndices.values(): # Equipping
            if item.NAME == "Scintillous Ring":
                self.equippedItemIndices['Ring'] = itemIndex
                item.level = 1
                item.xp = 0
                item.xpTnl = 100
            elif item.CATEGORY == "Armour":
                if self.equippedItemIndices['Armour'] is not None:
                    self.equip(self.equippedItemIndices['Armour'])
                self.equippedItemIndices['Armour'] = itemIndex
                self.equippedArmour = item
            elif item.CATEGORY == "Shield":
                if self.equippedItemIndices['Shield'] is not None:
                    self.equip(self.equippedItemIndices['Shield'])
                self.equippedItemIndices['Shield'] = itemIndex
                self.equippedShield = item
            else:
                if self.equippedItemIndices['Weapon'] is not None:
                    self.equip(self.equippedItemIndices['Weapon'])
                self.equippedItemIndices['Weapon'] = itemIndex
                self.equippedWeapon = item
        else:                                           # Unequipping
            if item.NAME == "Scintillous Ring":
                self.equippedItemIndices['Ring'] = None                
            elif item.CATEGORY == "Armour":
                self.equippedItemIndices['Armour'] = None
                self.equippedArmour = self.blankArmour
            elif item.CATEGORY == "Shield":
                self.equippedItemIndices['Shield'] = None
                self.equippedShield = self.blankShield
            else:
                self.equippedItemIndices['Weapon'] = None
                self.equippedWeapon = self.blankWeapon
        self.updateStats()

    def hasNoItems(self):
        return self.items == [None]*len(self.items)

    def hasRoom(self):
        return None in self.items

    def addItem(self, item):
        self.items[self.items.index(None)] = item

    def removeItem(self, index):
        self.items[index] = None

    def hasItem(self, itemName, quantity = 1):
        return [itemName in item.NAME
                for item in self.items if item].count(True) >= quantity

    def itemIsEquipped(self, itemName):
        return True in [itemName in item.NAME for item in [
            self.items[index] for index in self.equippedItemIndices.values()
            if index is not None]]

    def indexOfItem(self, itemName):
        return [(item != None and itemName in item.NAME)
                for item in self.items].index(True)

    def canLearn(self):
        return len(self.skills) < 4

    def learnSkill(self, skill):
        self.skills.append(skill)

    def forgetSkill(self, skill):
        self.skills.remove(skill)

    def isDead(self):
        return self.hp <= 0

    def hasMercenary(self, name):
        return True in [merc.NAME == name for merc in self.mercenaries]

    @property
    def ring(self):
        if "Ring" in self.equippedItemIndices and self.equippedItemIndices['Ring'] is not None:
            return self.items[self.equippedItemIndices['Ring']]
        return None

    @property
    def normalSeed(self):
        return self.level + self.level * len(
            [i for i in self.items if i is not None])

    @property
    def rareSeed(self):
        return "".join(skill.NAME for skill in self.skills)
