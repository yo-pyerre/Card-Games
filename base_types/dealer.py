from .deck import Deck
from .player import Player

class Dealer:
    def __init__(self, deck: Deck):
        self.deck = deck

    # Trivial but leaving it in as a reminder to implement "cutting the deck" or sumn like that
    def shuffle(self):
        self.deck.shuffle()

    def deal(self, player: Player):
        player.hand.add_card(self.deck.pop())

