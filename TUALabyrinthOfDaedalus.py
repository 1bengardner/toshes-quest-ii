"""
File: TUALabyrinthOfDaedalus.py
Author: Ben Gardner
Created: May 19, 2023
Revised: May 30, 2023
"""

class LabyrinthOfDaedalus:

    name = "Labyrinth of Daedalus"
    audio = "Suken"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "step"
        
        if "In Labyrinth" in self.c.flags:
            X = 1
            Y = 5
            return self.actions({'area': "Litochoro",
                                 'coordinates': (X, Y)})

        self.encounters = None
        
        if "Labyrinth Size" not in self.c.flags:
            self.c.flags['Labyrinth Size'] = 1
        size = 9 + 2 * self.c.flags['Labyrinth Size']
        self.spots = self.getMap(size, size)

    def getMap(self, rows, columns):
        grid = [[None] * columns] * rows
        startingCell = (
            columns / 2,
            rows - 2,
        )
        cellsToCheck = [startingCell]
        
        def isValid(cell):
            # TBD
        
        while (cellsToCheck):
            if isValid(cellsToCheck.pop()):
                # TBD

    def movementActions(self):
        self.c.hp -= 20
        
    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def complete(self):
        self.c.flags['Labyrinth Size'] += 1

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []

        self.c.flags['In Labyrinth'] = True