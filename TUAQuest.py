# -*- coding: utf-8 -*-
"""
File: TUAQuest.py
Author: Ben Gardner
Created: November 17, 2022
Revised: November 25, 2022
"""

class Quest:
    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.START_FLAG, self.END_FLAG))

    def __init__(self, title=None, description=None, completionCriteria={}, startFlag=None, endFlag=None, optional=False, repeatable=False):
        self.TITLE = title
        self.DESCRIPTION = description
        self.COMPLETION_CRITERIA = completionCriteria
        self.START_FLAG = startFlag
        self.END_FLAG = endFlag
        self.OPTIONAL = True if optional and int(optional) else False
        self.REPEATABLE = True if repeatable and int(repeatable) else False
        
    def getDetailsFor(self, character):
        details = []
        
        if 'Multiple Kills' in self.COMPLETION_CRITERIA:
            targets = self.COMPLETION_CRITERIA['Multiple Kills']
            details += filter(lambda detail: detail, ["%s: %s" % (target[1] if len(target) > 1 else target[0], "✗" * character.flags['Kills'][target[0]]) if target[0] in character.flags['Kills'] else "" for target in targets])
        
        if 'Wildcard Kills' in self.COMPLETION_CRITERIA:
            targetNames = self.COMPLETION_CRITERIA['Wildcard Kills'][0]
            generalName = self.COMPLETION_CRITERIA['Wildcard Kills'][2]
            startingKills = character.flags[self.START_FLAG] if isinstance(character.flags[self.START_FLAG], int) else 0
            currentKills = sum(character.flags['Kills'][targetName] if targetName in character.flags['Kills'] else 0 for targetName in targetNames)
            if currentKills > startingKills:
                details.append("%s: %s" % (generalName, "✗" * min(currentKills - startingKills, 10)))
            
        if 'Kills' in self.COMPLETION_CRITERIA:
            targetName = self.COMPLETION_CRITERIA['Kills'][0]
            startingKills = character.flags[self.START_FLAG] if isinstance(character.flags[self.START_FLAG], int) else 0
            currentKills = character.flags['Kills'][targetName] if targetName in character.flags['Kills'] else 0
            if currentKills > startingKills:
                details.append("%s: %s" % (targetName.strip("123456789"), "✗" * min(currentKills - startingKills, 10)))
            
        if 'Items' in self.COMPLETION_CRITERIA:
            items = self.COMPLETION_CRITERIA['Items']
            details += filter(lambda detail: detail, ["%s: %s" % (itemName, "✗" * len(filter(lambda item: item and itemName in item.NAME, character.items))) if character.hasItem(itemName) else "" for itemName in items])
            
        return "\n".join(details)
        
    def isCompletedBy(self, character):
        completed = True
        
        if 'No Criteria' in self.COMPLETION_CRITERIA:
            return False
        
        if 'Multiple Kills' in self.COMPLETION_CRITERIA:
            targets = self.COMPLETION_CRITERIA['Multiple Kills']
            completed = completed and len(filter(lambda target: target[0] in character.flags['Kills'], targets)) == len(targets)
        
        if 'Wildcard Kills' in self.COMPLETION_CRITERIA:
            targetNames = self.COMPLETION_CRITERIA['Wildcard Kills'][0]
            targetKills = self.COMPLETION_CRITERIA['Wildcard Kills'][1]
            startingKills = character.flags[self.START_FLAG] if isinstance(character.flags[self.START_FLAG], int) else 0
            currentKills = sum(character.flags['Kills'][targetName] if targetName in character.flags['Kills'] else 0 for targetName in targetNames)
            completed = completed and currentKills - startingKills >= targetKills
        
        if 'Kills' in self.COMPLETION_CRITERIA:
            targetName = self.COMPLETION_CRITERIA['Kills'][0]
            targetKills = self.COMPLETION_CRITERIA['Kills'][1]
            startingKills = character.flags[self.START_FLAG] if isinstance(character.flags[self.START_FLAG], int) else 0
            currentKills = character.flags['Kills'][targetName] if targetName in character.flags['Kills'] else 0
            completed = completed and currentKills - startingKills >= targetKills
            
        if 'Items' in self.COMPLETION_CRITERIA:
            items = self.COMPLETION_CRITERIA['Items']
            completed = completed and len(filter(lambda itemName: character.hasItem(itemName, items[itemName]), items)) == len(items)
            
        return completed
