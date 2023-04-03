"""
File: TUAShield.py
Author: Ben Gardner
Created: January 14, 2013
Revised: April 2, 2023
"""

from TUAStatics import EquipUtils

class Shield:

    def __init__(self, name, price, element, requirementValue, defence,
                 reduction, bRate):
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
        self.CATEGORY = "Shield"
        self.B_RATE = int(bRate)
        self.upgradeCount = 0

    @property
    def displayName(self):
        return EquipUtils.getDisplayName(self)

    def upgrade(self):
        self.upgradeCount += 1
        self.DEFENCE += 2 + 1 * EquipUtils.getAscensionLevel(self)
