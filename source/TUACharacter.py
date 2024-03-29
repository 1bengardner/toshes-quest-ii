"""
File: TUACharacter.py
Author: Ben Gardner
Created: January 25, 2013
Revised: September 3, 2023
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
                 statPoints, flags, area, x, y, potions, portrait=None, mode=None):
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
        self._euros = int(euros)
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
        self.portrait = portrait
        self.mode = mode
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
        if self.specialization in ("Son of Centaur", "Daughter of Centaur"):
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

        if self.portrait == "Pyroshe":
            self.fireReduction += 12
        elif self.portrait == "Toady":
            self.earthReduction += 7
            self.waterReduction += 7
        elif self.portrait == "Foxy":
            self.physicalReduction += 7
        elif self.portrait == "Lily":
            self.earthReduction += 15
            self.waterReduction += 5
            self.fireReduction -= 5
        elif self.portrait == "Apoc":
            self.defence += 10
        elif self.portrait == "M. Wizzard":
            self.earthReduction += 5
            self.waterReduction += 5
            self.fireReduction += 5

        if self.specialization == "Flame Knight":
            self.fireReduction += 2 * (self.mastery - 1)
        if self.specialization == "Reckless Lancer":
            self.damage += 2 * (self.mastery - 1)
            self.accuracy //= 2
            if self.equippedWeapon.CATEGORY == "Spear":
                self.damage *= 2
        if self.specialization == "Stalwart Slayer":
            self.damage *= 3
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
        if self.specialization in ("Sandman", "Sphinxkin"):
            self.earthReduction += 3 * (self.mastery - 1)
        if self.specialization == "Hermit":
            self.defence *= 2

        self.addOrbStats()

    def addOrbStats(self):
        wizardlyOrbReduction = 5 * self.countItem("Wizardly Orb")
        self.waterReduction += wizardlyOrbReduction + 10 * self.countItem("Ranine Orb")
        self.earthReduction += wizardlyOrbReduction + 10 * self.countItem("Bulbous Orb")
        self.fireReduction += wizardlyOrbReduction + 10 * self.countItem("Fiery Orb")
        self.bRate += 5 * self.countItem("Knightly Orb")
        self.physicalReduction += 5 * self.countItem("Feline Orb")

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
        value = self._strength
        if self.portrait == "Toshe":
            value += 5
        elif self.portrait == "Gumball Machine":
            value += 3
        if self.specialization == "Stalwart Slayer":
            value += 2 * (self.mastery - 1)
        elif self.specialization == "Squad Leader":
            value += 1 * (self.mastery - 1)
        value += 5 * self.countItem("Gumball of Power")
        return value 

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
        value = self._dexterity
        if self.portrait == "Toshette":
            value += 5
        elif self.portrait == "Gumball Machine":
            value += 3
        if self.specialization == "Executioner":
            value += 2 * (self.mastery - 1)
        elif self.specialization == "Squad Leader":
            value += 1 * (self.mastery - 1)
        value += 5 * self.countItem("Gumball of Power")
        return value

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
        value = self._wisdom
        if self.portrait == "Nome":
            value += 5
        elif self.portrait == "Gumball Machine":
            value += 3
        if self.specialization == "Snow Sorcerer":
            value += 2 * (self.mastery - 1)
        elif self.specialization == "Squad Leader":
            value += 1 * (self.mastery - 1)
        value += 5 * self.countItem("Gumball of Power")
        return value

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
        value = self._maxHp
        if self.portrait == "Reese":
            value += 50
        if self.specialization == "Paladin":
            return value + 20 * (self.mastery - 1)
        return value

    @maxHp.setter
    def maxHp(self, value):
        self._maxHp += value - self.maxHp

    @property
    def maxEp(self):
        value = self._maxEp
        if self.portrait == "Chris":
            value += 50
        if self.specialization == "Hermit":
            return value + 20 * (self.mastery - 1)
        return value

    @maxEp.setter
    def maxEp(self, value):
        self._maxEp += value - self.maxEp

    @property
    def euros(self):
        return 0 if self.mode == "Ultimate" else self._euros

    @euros.setter
    def euros(self, value):
        self._euros = value

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
        if not hasattr(self, "pastSpecializations"):
            self.pastSpecializations = {}
        self.pastSpecializations[self._specialization] = self.mastery
        if value in self.pastSpecializations:
            self.mastery = self.pastSpecializations[value]
        else:
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
            if self.NAME == "Dragan":
                self.dexterity += 5
            elif self.NAME == "Qendresa":
                self.strength += 5
            elif self.NAME == "Barrie":
                self.wisdom += 5
            else:
                self.statPoints += 5
                if self.specialization == "Paladin":
                    self.statPoints += 1
            self.maxHp += hpGainedOnLevelUp
            self.maxEp += epGainedOnLevelUp
            if not self.isDead():
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

    def countItem(self, itemName):
        return [itemName in item.NAME
                for item in self.items if item].count(True)

    def hasItem(self, itemName, quantity = 1):
        return self.countItem(itemName) >= quantity

    def itemIsEquipped(self, itemName):
        return True in [itemName in item.NAME for item in [
            self.items[index] for index in self.equippedItemIndices.values()
            if index is not None]]

    def indexOfItem(self, itemName):
        return [(item != None and itemName in item.NAME and i not in self.equippedItemIndices.values())
                for i, item in enumerate(self.items)].index(True)

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

    @property
    def isFemale(self):
        girls = [
            "Foxy",
            "Toshette",
            "Lily",
        ]
        return self.portrait in girls

    @property
    def isPolite(self):
        politeFolks = [
            "Foxy",
            "Toady",
            "Lily",
        ]
        return self.portrait in politeFolks

    @property
    def isHumanoid(self):
        nonHumans = [
            "Gumball Machine",
            "Lily",
        ]
        return self.portrait not in nonHumans
