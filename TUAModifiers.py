"""
File: TUAModifiers.py
Author: Ben Gardner
Created: April 2, 2023
Revised: April 2, 2023
"""

class Modifiers:
    BIG = "Big"
    KEEN = "Keen"
    EXOTIC = "Exotic"
    GIANT = "Giant"
    DEADLY = "Deadly"
    STONY = "Stony"
    ICY = "Icy"
    FIERY = "Fiery"
    STURDY = "Sturdy"
    GAIAN = "Gaian"
    GLACIAL = "Glacial"
    MOLTEN = "Molten"
    ROBUST = "Robust"
    HEAVY = "Heavy"
    MASSIVE = "Massive"

    ALL = [
        BIG,
        KEEN,
        EXOTIC,
        GIANT,
        DEADLY,
        STONY,
        ICY,
        FIERY,
        STURDY,
        GAIAN,
        GLACIAL,
        MOLTEN,
        ROBUST,
        HEAVY,
        MASSIVE,
    ]

    @classmethod
    def extractFromItem(self, item):
        firstWord = item.NAME.split(" ")[0]
        return next((mod for mod in self.ALL if firstWord == mod), None)

    @classmethod
    def modifyItem(self, item, modifier, value):
        if modifier in (self.BIG, self.GIANT):
            item.POWER += value
        elif modifier in (self.KEEN, self.DEADLY):
            item.C_RATE += value / 2.0
        elif modifier == self.EXOTIC:
            item.SELL_PRICE *= value
        elif modifier in (self.STONY, self.GAIAN):
            item.EARTH_REDUCTION += value
        elif modifier in (self.ICY, self.GLACIAL):
            item.WATER_REDUCTION += value
        elif modifier in (self.FIERY, self.MOLTEN):
            item.FIRE_REDUCTION += value
        elif modifier in (self.STURDY, self.ROBUST):
            item.DEFENCE += value
        elif modifier in (self.HEAVY, self.MASSIVE):
            item.B_RATE += value // 2

    @classmethod
    def getByCategoryAndLevel(self, category, level):
        weaponModifiers = {
            1: [
                self.BIG,
                self.KEEN,
                self.EXOTIC],
            2: [
                self.GIANT,
                self.DEADLY],}
        armourModifiers = {
            1: [
                self.STONY,
                self.ICY,
                self.FIERY,
                self.STURDY,
                self.EXOTIC],
            2: [
                self.GAIAN,
                self.GLACIAL,
                self.MOLTEN,
                self.ROBUST],}
        shieldModifiers = {
            1: [
                self.STONY,
                self.ICY,
                self.FIERY,
                self.STURDY,
                self.EXOTIC,
                self.HEAVY],
            2: [
                self.GAIAN,
                self.GLACIAL,
                self.MOLTEN,
                self.ROBUST,
                self.MASSIVE],}
        return {
            'Sword': weaponModifiers,
            'Club': weaponModifiers,
            'Axe': weaponModifiers,
            'Spear': weaponModifiers,
            'Bow': weaponModifiers,
            'Wand': weaponModifiers,
            'Armour': armourModifiers,
            'Shield': shieldModifiers,
        }[category][level]

    @classmethod
    def getByCategory(self, category):
        return self.getByCategoryAndLevel(category, 1) + self.getByCategoryAndLevel(category, 2)

    @classmethod
    def levelOf(self, modifier):
        return {
            self.BIG: 1,
            self.KEEN: 1,
            self.EXOTIC: 1,
            self.GIANT: 2,
            self.DEADLY: 2,
            self.STONY: 1,
            self.ICY: 1,
            self.FIERY: 1,
            self.STURDY: 1,
            self.GAIAN: 2,
            self.GLACIAL: 2,
            self.MOLTEN: 2,
            self.ROBUST: 2,
            self.HEAVY: 1,
            self.MASSIVE: 2,
        }[modifier]
