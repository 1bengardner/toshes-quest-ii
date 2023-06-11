"""
File: TUALabyrinthOfDaedalus.py
Author: Ben Gardner
Created: May 19, 2023
Revised: July 11, 2023
"""

import random

class LabyrinthOfDaedalus:

    name = "Labyrinth of Daedalus"
    audio = "Suken"

    @staticmethod
    def getSizeFor(character):
        if "Labyrinth Size" not in character.flags or character.flags['Labyrinth Size'] < 1:
            character.flags['Labyrinth Size'] = 1
        return 9 + 2 * character.flags['Labyrinth Size']

    @staticmethod
    def getOriginFor(character):
        size = LabyrinthOfDaedalus.getSizeFor(character)
        return (size / 2, size - 2)

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "step"

        self.encounters = None

        size = LabyrinthOfDaedalus.getSizeFor(self.c)
        if "In Labyrinth" in self.c.flags:
            self.c.flags['Kicked Out'] = True
            self.spots = [[self.room] * size for i in range(size)]
        else:
            self.spots = self.getMap(size, size)

    def getMap(self, rows, columns):
        start = self.entrance
        live = self.room
        final = self.minotaur
        grid = [[None] * columns for i in range(rows)]
        startX, startY = LabyrinthOfDaedalus.getOriginFor(self.c)
        grid[startY][startX] = start

        def isValid():
            def outOfBounds(X, Y):
                return X < 1 or Y < 1 or X >= columns - 1 or Y >= rows - 1

            def hasOneLiveConnection():
                liveConnectionCount = 0
                for cX, cY in getConnectedCells():
                    if not outOfBounds(cX, cY) and grid[cY][cX] is not None:
                        liveConnectionCount += 1
                        if liveConnectionCount > 1:
                            return False
                return liveConnectionCount == 1

            return not outOfBounds(X, Y) and grid[Y][X] is None and hasOneLiveConnection()

        def checkSurroundingCells():
            neighbours = getConnectedCells()
            random.shuffle(neighbours)
            for cell in neighbours:
                cellsToCheck.append(cell)

        def getConnectedCells():
            cells = []
            cells.append((X+1, Y))
            cells.append((X-1, Y))
            cells.append((X, Y+1))
            cells.append((X, Y-1))
            return cells

        cellsToCheck = [(startX, startY - 1)]
        invalidInARow = 0
        lastCell = None
        lastValid = None

        while (cellsToCheck):
            X, Y = cellsToCheck.pop()
            if not isValid():
                invalidInARow += 1
                if invalidInARow == 4 and lastCell is None:
                    lastCell = lastValid
                continue
            invalidInARow = 0
            lastValid = (X, Y)
            grid[Y][X] = live
            checkSurroundingCells()

        if lastCell is None:
            lastCell = (X, Y)
        X, Y = lastCell
        grid[Y][X] = final
        return grid

    def movementActions(self):
        self.c.hp -= 20
        
    def actions(self, newActions=None):
        if "Kicked Out" in self.c.flags:
            del self.c.flags['Kicked Out']
            del self.c.flags['Marked Areas'][self.name]
            del self.c.flags['Discovered Areas'][self.name]
            X = 1
            Y = 3
            return self.actions({'area': "Litochoro",
                                 'coordinates': (X, Y)})
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = -1
        self.text = None
        self.helpText = None
        self.menu = []

        self.text = "You descend the town cellar, climbing down a ladder and a series of murky stone steps before stepping into an elaborate labyrinth. The one-way door shuts loudly behind you."
        if "Labyrinth Door" not in self.c.flags:
            self.c.flags['Labyrinth Door'] = True
            self.text += "\n%s: Oh, shit. What do we do?" % "Toshe"
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\n%s: We must find the exit. Swiftly, before we go mad." % "Qendresa")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\n%s: I kinda like it down here. Suits me." % "Barrie")
        elif random.randint(1, 2) == 1:
            self.text += "\n%s: Here we go again." % "Toshe"
            if random.randint(1, 4) == 1 and self.c.hasMercenary("Barrie"):
                    self.text += ("\n%s: I hope you brought potions." % "Barrie")
            if random.randint(1, 4) == 1 and self.c.hasMercenary("Qendresa"):
                self.text += ("\n%s: Why must we torture ourselves down here?" % "Qendresa")

        self.c.flags['In Labyrinth'] = True

        return self.actions()

    def room(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = -1
        self.text = None
        self.helpText = None
        self.menu = []

        return self.actions()

    def minotaur(self, selectionIndex=None):
        self.view = "battle"
        self.imageIndex = -1
        self.text = None
        self.helpText = None
        self.menu = []

        if "In Labyrinth" not in self.c.flags:
            self.c.flags['Labyrinth Complete'] = True
            self.c.flags['Labyrinth Size'] += 1
            del self.c.flags['Marked Areas'][self.name]
            del self.c.flags['Discovered Areas'][self.name]
            X = 1
            Y = 5
            return self.actions({'area': "Litochoro",
                                 'coordinates': (X, Y)})

        multiplier = (LabyrinthOfDaedalus.getSizeFor(self.c) - 1) / 10.0
        modifiers = {
            'Multiplicative': True,
            'Stats': {
                'LEVEL': 10 * LabyrinthOfDaedalus.getSizeFor(self.c),
                'XP': multiplier,
                'maxHp': multiplier,
                'damage': multiplier,
                'defence': multiplier,
            },
        }

        del self.c.flags['In Labyrinth']

        return self.actions({'enemy': random.choice([
                                 "Gold Minotaur",
                                 "Green Minotaur",]),
                             'mercenaries': self.c.mercenaries,
                             'enemy modifiers': modifiers,})
