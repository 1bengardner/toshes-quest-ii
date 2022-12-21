"""
File: TUAArmour.py
Author: Ben Gardner
Created: January 14, 2013
Revised: December 20, 2022
"""


class Armour:

    def __init__(self, name, price, element, requirementValue, defence,
                 reduction):
        self.NAME = str(name)
        self.IMAGE_NAME = self.NAME
        self.PRICE = int(price)
        self.SELL_PRICE = int(price)/4
        self.ELEMENT = str(element)
        self.REQUIREMENT_VALUE = int(requirementValue)
        self.DEFENCE = int(defence)
        self.REDUCTION = int(reduction)
        if element == "Elemental":
            self.EARTH_REDUCTION = int(reduction)
            self.WATER_REDUCTION = int(reduction)
            self.FIRE_REDUCTION = int(reduction)
            self.PHYSICAL_REDUCTION = 0
        elif element == "Earth":
            self.EARTH_REDUCTION = int(reduction)
            self.WATER_REDUCTION = 0
            self.FIRE_REDUCTION = 0
            self.PHYSICAL_REDUCTION = 0
        elif element == "Water":
            self.EARTH_REDUCTION = 0
            self.WATER_REDUCTION = int(reduction)
            self.FIRE_REDUCTION = 0
            self.PHYSICAL_REDUCTION = 0
        elif element == "Fire":
            self.EARTH_REDUCTION = 0
            self.WATER_REDUCTION = 0
            self.FIRE_REDUCTION = int(reduction)
            self.PHYSICAL_REDUCTION = 0
        elif element == "Physical":
            self.EARTH_REDUCTION = 0
            self.WATER_REDUCTION = 0
            self.FIRE_REDUCTION = 0
            self.PHYSICAL_REDUCTION = int(reduction)
        self.REQUIREMENT_TYPE = "Strength"
        self.CATEGORY = "Armour"
        self.upgradeCount = 0

    @property
    def displayName(self):
        return "%s +%s" % (self.NAME, self.upgradeCount) if self.upgradeCount > 0 else self.NAME

    def upgrade(self):
        self.DEFENCE += 2
        self.upgradeCount += 1
