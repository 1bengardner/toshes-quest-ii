"""
File: TUAEnemy.py
Author: Ben Gardner
Created: March 13, 2013
Revised: May 19, 2023
"""


class Enemy(object):
    """Contains an enemy's stats.

    identifier: The unique name by which the enemy is identified.
    name: The enemy's name.
    level: Experience level.
    hp: Health points.
    maxHp: Maximum health points.
    damage: The enemy's base damage.
    accuracy: The enemy's chance to hit you.
    cRate: The enemy's chance to land a critical strike.
    cDamage: The enemy's critical damage multiplier (in %).
    bRate: The enemy's chance to block an attack.
    defence: The amount by which damage will be reduced when enemy is attacked.
    earthReduction: The amount by which damage will be reduced when enemy is
    damaged by Earth (in %).
    waterReduction: The amount by which damage will be reduced when enemy is
    damaged by Water (in %).
    fireReduction: The amount by which damage will be reduced when enemy is
    damaged by Fire (in %).
    physicalReduction: The amount by which damage will be reduced when enemy
    is attacked (in %).
    skills: Skills the enemy can use, along with the chance for enemy to use it.
    items: Potential items dropped, along with the chance for enemy to drop it.
    xp: XP awarded to the murderer upon enemy's death.
    euros: Number of euros the enemy drops when killed.
    fleeable: States whether you can escape from this enemy in battle (1 or 0).
    unique: Whether the enemy is unique (1 or 0).
    deathHp: The HP value the enemy must reach before dying.
    music: Name of the song playing during battle (no music = None)
    """

    def __init__(self, identifier, name, image, level, hp, maxHp, damage,
                 accuracy, cRate, cDamage, bRate, defence, earthReduction,
                 waterReduction, fireReduction, physicalReduction, skills,
                 items, xp, euros, fleeable, unique, living, rarity, deathHp=0,
                 music=None):
        self.IDENTIFIER = str(identifier)
        self.NAME = str(name)
        self.IMAGE = str(image)
        self.LEVEL = int(level)
        self._hp = int(hp)
        self.maxHp = int(maxHp)
        self.ep = 0
        self.maxEp = 0
        self.damage = int(damage)
        self.accuracy = int(accuracy)
        self.cRate = round(float(cRate), 1)
        self.cDamage = int(cDamage)
        self.bRate = int(bRate)
        self.defence = int(defence)
        self.earthReduction = int(earthReduction)
        self.waterReduction = int(waterReduction)
        self.fireReduction = int(fireReduction)
        self.physicalReduction = int(physicalReduction)
        self.SKILLS = dict(skills)
        self.ITEMS = dict(items)
        self.XP = int(xp)
        self.EUROS = int(euros)
        self.FLEEABLE = int(fleeable)
        self.DEATH_HP = int(deathHp)
        self.MUSIC = music if music != "None" else None
        self.UNIQUE = int(unique)
        self.LIVING = int(living)
        self.RARITY = rarity

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if self._hp > self.maxHp:
            self._hp = self.maxHp

    def isDead(self):
        return self.hp <= self.DEATH_HP
