"""
File: TUADeckOfCards.py
Author: Ben Gardner
Created: June 24, 2015
Revised: June 24, 2015
"""


import random

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Deck:
    def __init__(self):
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        suits = ["Spade", "Club", "Diamond", "Heart"]

        self.cards = []
        for number in range(13):
            for suit in range(4):
                self.cards.append(Card(suits[suit], numbers[number]))
    def popCard(self):
        return self.cards.pop()
    def shuffle(self):
        random.shuffle(self.cards)
    def pushCard(self, card):
        self.cards.insert(0, card)
