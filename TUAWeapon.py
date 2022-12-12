"""
File: TUAWeapon.py
Author: Ben Gardner
Created: January 14, 2013
Revised: December 11, 2022
"""


class Weapon:

    def __init__(self, name, price, element, requirementValue, power,
                 requirementType, category, cRate, cDamage):
        self.BASE_NAME = str(name)
        self.IMAGE_NAME = self.BASE_NAME
        self.PRICE = int(price)
        self.SELL_PRICE = int(price)/4
        self.ELEMENT = str(element)
        self.REQUIREMENT_VALUE = int(requirementValue)
        self.POWER = int(power)
        self.REQUIREMENT_TYPE = str(requirementType)
        self.CATEGORY = str(category)
        self.C_RATE = float(cRate)
        self.C_DAMAGE = int(cDamage)
        if category == "Sword":
            self.ACCURACY = 90
        elif category == "Club":
            self.ACCURACY = 80
        elif category == "Axe":
            self.ACCURACY = 70
        elif category == "Spear":
            self.ACCURACY = 60
        elif category == "Bow":
            self.ACCURACY = 50
        elif category == "Wand":
            self.ACCURACY = 999     # always hits
        elif category == "Gun":
            self.ACCURACY = 10
        else:
            self.ACCURACY = 0

    @property
    def NAME(self):
        return "%s +%s" % (self.BASE_NAME, self.upgradeCount) if hasattr(self, "upgradeCount") else self.BASE_NAME

    def upgrade(self):
        if not hasattr(self, "upgradeCount"):
            self.upgradeCount = 0
        self.POWER += 2
        self.upgradeCount += 1
