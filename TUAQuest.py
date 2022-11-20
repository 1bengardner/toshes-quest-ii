# -*- coding: utf-8 -*-
"""
File: TUAQuest.py
Author: Ben Gardner
Created: November 17, 2022
Revised: November 19, 2022
"""

class Quest:
    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.START_FLAG, self.END_FLAG))

    def __init__(self, title=None, description=None, completionCriteria={}, startFlag=None, endFlag=None):
        self.TITLE = title
        self.DESCRIPTION = description
        self.COMPLETION_CRITERIA = completionCriteria
        self.START_FLAG = startFlag
        self.END_FLAG = endFlag
        
    def getDetailsFor(self, character):
        details = []
        if 'Kills' in self.COMPLETION_CRITERIA:
            targetName = self.COMPLETION_CRITERIA['Kills'][0]
            startingKills = character.flags[self.START_FLAG] if character.flags[self.START_FLAG] is not True else 0
            currentKills = character.flags['Kills'][targetName] if targetName in character.flags['Kills'] else 0
            details.append("%s: %s" % (targetName, "✗" * min(currentKills - startingKills, 10)) if currentKills > startingKills else "")
        
        if 'Items' in self.COMPLETION_CRITERIA:
            items = self.COMPLETION_CRITERIA['Items']
            details += ["%s: %s" % (itemName, "✗" * len(filter(lambda itemName: itemName in item.NAME, character.items))) if character.hasItem(itemName) else "" for itemName in items]
            
        return "\n".join(details)
        
    def isCompletedBy(self, character):
        completed = True
        
        if 'Kills' in self.COMPLETION_CRITERIA:
            targetName = self.COMPLETION_CRITERIA['Kills'][0]
            targetKills = self.COMPLETION_CRITERIA['Kills'][1]
            startingKills = character.flags[self.START_FLAG] if character.flags[self.START_FLAG] is not True else 0
            currentKills = character.flags['Kills'][targetName] if targetName in character.flags['Kills'] else 0
            completed = completed and currentKills - startingKills >= targetKills
            
        if 'Items' in self.COMPLETION_CRITERIA:
            items = self.COMPLETION_CRITERIA['Items']
            completed = completed and len(filter(lambda itemName: character.hasItem(itemName, items[itemName]), items)) == len(items)
            
        return completed
