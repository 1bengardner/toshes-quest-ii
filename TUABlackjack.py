"""
File: TUABlackjack.py
Author: Ben Gardner
Created: June 24, 2015
Revised: June 27, 2015
"""


from TUADeckOfCards import Deck

class Hand:
        
    def __init__(self):
        self.cards = []
        
    def drawCard(self, card):
        if len(str(card.number)) > 2:
            card.number = card.number[0]
        self.cards.append(card)
        
    def popCard(self):
        return self.cards.pop()

    def discardHand(self, deck):
        for card in self.cards:
            deck.pushCard(self.popCard())
            
    def getValue(self):
        value = 0
        hasAce = False
        for card in self.cards:
            if card.number == "A":
                value += 1
                hasAce = True
            elif card.number in ("J", "Q", "K"):
                value += 10
            else:
                value += card.number
        if hasAce and value < 12:
            value += 10
        return value

    def hasNatural(self):
        return self.getValue() == 21 and len(self.cards) == 2


class Game:
        
    def __init__(self):
        self.player = Hand()
        self.dealer = Hand()
        self.deck = Deck()
        self.outcomes = ["Natural", "Win", "Lose", "Push"]
        self.outcome = None
        self.standing = False
        
    def hit(self, hand):
        hand.drawCard(self.deck.popCard())
        
    def getHandString(self, hand):
        text = ""
        for card in hand.cards:
            text += "%s " % card.number
        if ( hand is self.dealer
             and len(hand.cards) == 2
             and not self.dealer.hasNatural()
             and not self.standing):
            text = "(Hole) %s" % card.number
        return text.strip()

    def getHandsString(self):
        return ("Your hand: %s." % self.getHandString(self.player) +
                "\nDealer's hand: %s." % self.getHandString(self.dealer))

    def takeTurn(self, action):
        text = "null"
        if action.lower() == "restart":
            self.standing = False
            self.player.discardHand(self.deck)
            self.dealer.discardHand(self.deck)
            self.deck.shuffle()
            self.outcome = None
            self.player.drawCard(self.deck.popCard())
            self.player.drawCard(self.deck.popCard())
            self.dealer.drawCard(self.deck.popCard())
            self.dealer.drawCard(self.deck.popCard())
            text = ("The dealer shuffles the deck and deals you two cards." +
                    "\n%s" % self.getHandsString())
            if self.player.hasNatural() and self.dealer.hasNatural():
                self.outcome = self.outcomes[3]
                text += ("\nPush!")
            elif self.player.hasNatural() and not self.dealer.hasNatural():
                self.outcome = self.outcomes[0]
                text += ("\nNatural!")
            elif not self.player.hasNatural() and self.dealer.hasNatural():
                self.outcome = self.outcomes[2]
                text += ("\nYou lose!")
                        
        elif action.lower() == "hit":
            self.hit(self.player)
            text = ("Toshe: Hit me." +
                    "\n%s" % self.getHandsString())
            if self.player.getValue() > 21:
                self.outcome = self.outcomes[2]
                text += ("\nBust!")
            elif self.player.getValue() == 21:
                return text + "\n" + self.takeTurn("stand")
                        
        elif action.lower() == "stand":
            self.standing = True
            text = "Toshe: Let's see 'em."
            while self.dealer.getValue() < 17:
                self.hit(self.dealer)
            dealerCards = len(self.dealer.cards)
            if dealerCards > 2:
                text += ("\nThe dealer hits %s time%s." % (dealerCards - 2,
                                                           "s" if dealerCards > 3 else ""))
            text += ("\n%s" % self.getHandsString())
            if self.dealer.getValue() > 21 or self.dealer.getValue() < self.player.getValue():
                self.outcome = self.outcomes[1]
                text += ("\nYou win!")
            elif self.dealer.getValue() > self.player.getValue():
                self.outcome = self.outcomes[2]
                text += ("\nYou lose!")
            elif self.dealer.getValue() == self.player.getValue():
                self.outcome = self.outcomes[3]
                text += ("\nPush!")
                
        return text          
