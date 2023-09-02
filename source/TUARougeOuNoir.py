"""
File: TUARougeOuNoir.py
Author: Ben Gardner
Created: June 24, 2015
Revised: June 24, 2015
"""


from TUADeckOfCards import Deck


class Game:
    def __init__(self):
        self.deck = Deck()
        self.rouge = None
    def play(self):
        card = self.deck.popCard()
        text = ("The dealer draws the %s of %ss." % (card.number, card.suit))
        if card.suit in ("Spade", "Club"):
            self.rouge = False
            text += ("\nNoir!")
        elif card.suit in ("Heart", "Diamond"):
            self.rouge = True
            text += ("\nRouge!")
        return text
    def restart(self):
        self.deck.shuffle()
        return ("The dealer shuffles the deck." +
                "\nDealer: Rouge ou noir?")
