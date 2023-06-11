"""
File: TUAForge.py
Author: Ben Gardner
Created: March 31, 2023
Revised: June 10, 2023
"""

import random
from TUAModifiers import Modifiers

class Forge:

    def __init__(self):
        self.forgeItem = None
        self.sacrificeItems = [None, None]
        self.maxDecimals = 5
        self.fiddle = 0
        self.horn = None

    # Returns index where item was placed elsewhere
    def setForgeItem(self, item):
        self.forgeItem = item
        if item == self.sacrificeItems[0]:
            self.sacrificeItems[0] = None
            return 1
        elif item == self.sacrificeItems[1]:
            self.sacrificeItems[1] = None
            return 2

    # Returns index where item was placed elsewhere
    def setSacrificeItem(self, which, item):
        self.sacrificeItems[which-1] = item
        if item == self.forgeItem:
            self.forgeItem = None
            return 0
        elif which == 2 and item == self.sacrificeItems[0]:
            self.sacrificeItems[0] = None
            return 1
        elif which == 1 and item == self.sacrificeItems[1]:
            self.sacrificeItems[1] = None
            return 2

    def hasAllSacrifices(self):
        return all(self.sacrificeItems)

    def isReady(self):
        return all([self.forgeItem] + self.sacrificeItems)

    def getSuccessChance(self):
        if self.horn == "Golden Horn":
            return 95 + self.fiddle
        u = self.forgeItem
        a = self.sacrificeItems[0]
        b = self.sacrificeItems[1]
        if not all([u, a, b]) or u.SELL_PRICE < 5:
            return 0
        chance = 100 * (
                 (a.SELL_PRICE * (1 + 0.5 * a.upgradeCount * 1.2 ** min(4, a.upgradeCount // 10)) +
                  b.SELL_PRICE * (1 + 0.5 * b.upgradeCount * 1.2 ** min(4, a.upgradeCount // 10))) / 2.0 /
                 (u.SELL_PRICE * (1 + 0.1 * u.upgradeCount))) + self.fiddle
        if chance < 0:
            return 0
        elif str(chance)[0] == "0":
            # Stop one short of maxDecimals to use last decimal for precision
            for i in range(2, min(self.maxDecimals, len(str(chance)))):
                if str(chance)[i] != "0":
                    # Give extra decimal place after first significant decimal
                    return round(chance, i)
        if self.horn == "Purple Horn":
            return 1000 + int(chance)
        elif self.horn == "Green Horn":
            return 3 * int(chance)
        return int(chance)

    def fiddleWithSuccess(self):
        self.fiddle = random.randint(-5, 5)
        return self.fiddle

    def do(self):
        if not all([self.forgeItem] + self.sacrificeItems):
            raise ValueError("Cannot forge without base and two sacrifices")
        successChance = self.getSuccessChance()
        while successChance > 100:
            self.upgradeItem()
            yield True
            successChance -= 100
        chance = successChance * 10 ** self.maxDecimals
        failureThreshold = random.randint(1, 100 * 10 ** self.maxDecimals) - 1
        if chance > failureThreshold:
            self.upgradeItem()
            yield True
        self.fiddle = 0

    def upgradeItem(self):
        self.forgeItem.upgrade()
        for item in self.sacrificeItems:
            mod = Modifiers.extractFromItem(item)
            if mod in Modifiers.getByCategory(self.forgeItem.CATEGORY):
                value = Modifiers.levelOf(mod) * (1 + random.randint(1, 3)) // 2
                Modifiers.modifyItem(self.forgeItem, mod, value)
