"""
File: TUATrafCafe.py
Author: Ben Gardner
Created: June 24, 2015
Revised: August 25, 2023
"""


import TUABlackjack
import TUARougeOuNoir


class TrafCafe:

    name = "Traf Cafe"
    audio = "Traf Cafe"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        entr = self.entrance
        roun = self.rougeOuNoir
        blkj = self.blackjack

        self.spots = [
            [None, None, None, None, None, None, None],
            [None, roun, None, entr, None, blkj, None],
            [None, None, None, None, None, None, None]
            ]

        self.encounters = None

        self.bets = ["5", "100", "2000"]

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

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if hasattr(self, "game"):
            del self.game
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Traf Cafe",
                                 'coordinates': (X, Y)})            
        elif selectionIndex == 1:
            X = 5
            Y = 1
            return self.actions({'area': "Traf Cafe",
                                 'coordinates': (X, Y)}) 
        elif selectionIndex == 2:
            X = 7
            Y = 4
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        
        if "Traf Cafe" not in self.c.flags:
            self.text = ("%s: ...It's a lot bigger and flashier" % self.c.NAME +
                         " on the inside.")
            self.c.flags['Traf Cafe'] = True
        else:
            self.text = ("%s: Well, here I am again, gambling my" % self.c.NAME +
                         " life's savings away.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: Gambling? My favourite!")
        self.menu = ["Play Rouge ou Noir.",
                     "Play Blackjack.",
                     "Leave."]
        return self.actions()

    def rougeOuNoir(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Dealer"
        hits = []

        if selectionIndex == 3:
            X = 3
            Y = 1
            return self.actions({'area': "Traf Cafe",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0 and "Kicked Out" in self.c.flags:
            X = 7
            Y = 4
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        elif selectionIndex is not None and not hasattr(self, "game"):
            self.c.euros -= int(self.bets[selectionIndex])
            self.bet = self.bets[selectionIndex]
            self.game = TUARougeOuNoir.Game()
            self.text = ("You bet %s euros." % self.bet +
                         "\n%s" % self.game.restart())
            self.menu = ["\"Rouge.\"",
                         "\"Noir.\""]
            return self.actions({'save': True})
        elif selectionIndex == 0:
            self.text = self.game.play()
            if self.game.rouge:
                winnings = int(self.bet) * 2
                self.c.euros += winnings
                hits.append({
                    "Target": self.c.NAME,
                    "Kind": "Money",
                    "Number": winnings,
                })
            elif not self.game.rouge:
                pass
        elif selectionIndex == 1:
            self.text = self.game.play()
            if self.game.rouge:
                pass
            elif not self.game.rouge:
                winnings = int(self.bet) * 2
                self.c.euros += winnings
                hits.append({
                    "Target": self.c.NAME,
                    "Kind": "Money",
                    "Number": winnings,
                })

        if not hasattr(self, "game"):
            if self.c.euros < 0:
                X = 7
                Y = 4
                return self.actions({'area': "Pristina",
                                     'coordinates': (X, Y)})                
            self.bet = 0
            if self.c.isFemale:
                sirText = "ma'am"
            else:
                sirText = "sir"
            self.text = ("%s: Hello, %s. How much would you like" % (npc, sirText) +
                         " to bet?")
            self.menu = ["Bet " + bet + "." for bet in self.bets] + ["Leave."]
        elif self.game.rouge is not None:
            self.bet = 0
            del self.game
            if self.c.euros < 0:
                self.c.flags['Kicked Out'] = True
                self.text += ("\nSecurity: You cannot have negative euros." +
                              " Please leave.")
                self.menu = ["Leave."]
            else:
                self.text += "\n%s: Bet again?" % npc
                self.menu = ["Bet " + bet + "." for bet in self.bets] + ["Leave."]

        if hits:
            return self.actions({'hits': hits})
        return self.actions()

    def blackjack(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        npc = "Dealer"
        hits = []

        if selectionIndex == 3:
            X = 3
            Y = 1
            return self.actions({'area': "Traf Cafe",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0 and "Kicked Out" in self.c.flags:
            X = 7
            Y = 4
            return self.actions({'area': "Pristina",
                                 'coordinates': (X, Y)})
        elif selectionIndex is not None and not hasattr(self, "game"):
            self.c.euros -= int(self.bets[selectionIndex])
            self.bet = self.bets[selectionIndex]
            self.game = TUABlackjack.Game(self.c.NAME)
            self.text = ("You bet %s euros." % self.bet +
                         "\n%s" % self.game.takeTurn("restart"))
            if self.game.outcome is None:
                self.menu = ["Hit.",
                             "Stand."]
            else:
                if self.game.outcome == "Natural":
                    winnings = int(int(self.bet) * 2.5)
                    self.c.euros += winnings
                    hits.append({
                        "Target": self.c.NAME,
                        "Kind": "Money",
                        "Number": winnings,
                        "Critical": True,
                    })
                elif self.game.outcome == "Win":
                    winnings = int(self.bet) * 2
                    self.c.euros += winnings
                    hits.append({
                        "Target": self.c.NAME,
                        "Kind": "Money",
                        "Number": winnings,
                    })
                elif self.game.outcome == "Lose":
                    pass
                elif self.game.outcome == "Push":
                    winnings = int(self.bet)
                    self.c.euros += winnings
                    hits.append({
                        "Target": self.c.NAME,
                        "Kind": "Money",
                        "Number": winnings,
                    })
                self.bet = 0
                del self.game
                if self.c.euros < 0:
                    self.c.flags['Kicked Out'] = True
                    self.text += ("\nSecurity: You cannot have negative euros." +
                                  " Please leave.")
                    self.menu = ["Leave."]
                else:
                    self.text += "\n%s: Bet again?" % npc
                    self.menu = ["Bet " + bet + "." for bet in self.bets] + ["Leave."]
            actions = {'save': True}
            if hits:
                actions.update({'hits': hits})
            return self.actions(actions)
        elif selectionIndex == 0:
            self.text = self.game.takeTurn("hit")
            self.menu = ["Hit.",
                         "Stand."]
        elif selectionIndex == 1:
            self.text = self.game.takeTurn("stand")
            self.menu = ["Hit.",
                         "Stand."]
            
        if not hasattr(self, "game"):
            if self.c.euros < 0:
                X = 7
                Y = 4
                return self.actions({'area': "Pristina",
                                     'coordinates': (X, Y)}) 
            self.bet = 0
            if self.c.isFemale:
                sirText = "miss"
            else:
                sirText = "sir"
            self.text = ("%s: Welcome, %s. How much would you like" % (npc, sirText) +
                         " to bet?")
            self.menu = ["Bet " + bet + "." for bet in self.bets] + ["Leave."]
        elif self.game.outcome is not None:
            if self.game.outcome == "Win":
                winnings = int(self.bet) * 2
                self.c.euros += winnings
                hits.append({
                    "Target": self.c.NAME,
                    "Kind": "Money",
                    "Number": winnings,
                })
            elif self.game.outcome == "Lose":
                pass
            elif self.game.outcome == "Push":
                winnings = int(self.bet)
                self.c.euros += winnings
                hits.append({
                    "Target": self.c.NAME,
                    "Kind": "Money",
                    "Number": winnings,
                })
            self.bet = 0
            del self.game
            if self.c.euros < 0:
                self.c.flags['Kicked Out'] = True
                self.text += ("\nSecurity: You cannot have negative euros." +
                              " Please leave.")
                self.menu = ["Leave."]
            else:
                self.text += "\n%s: Bet again?" % npc
                self.menu = ["Bet " + bet + "." for bet in self.bets] + ["Leave."]

        if hits:
            return self.actions({'hits': hits})
        return self.actions()
