"""
File: TUACredits.py
Author: Ben Gardner
Created: December 30, 2015
Revised: June 3, 2023
"""


class Credits:

    name = "Congratulations"
    audio = "Just Jolly"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        cred = self.credits        
        
        self.spots = [
            [None, None, None],
            [None, cred, None],
            [None, None, None]]
             
        self.encounters = None
    
    def movementActions(self):
        pass

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def credits(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        self.c.flags['Credits'] = True
        if selectionIndex == 0:
            X = 5
            Y = 3
            return self.actions({'area': "Herceg Novi",
                                 'coordinates': (X, Y)})
        self.text = ("Toshe's Quest II: A game by Ben Gardner\n" +
                     "\nSean Anderson as Sean" +
                     "\nAbdalla Khafagy as Jazidhu" +
                     "\nBayezin Selim as Bayezin" +
                     "\nEric Han as Mushroom Man" +
                     "\nUduak Umoeka as Big Nigel" +
                     "\nLina as Lina\n" +
                     "\nSpecial thanks to Alvin Yang, Jeff Buscarino and" +
                     " Zain Zia for their support, and to Tyler" +
                     " Perris for the original game idea." +
                     "\nThank you for playing!")
        self.menu = ["Continue."]
        return self.actions()
