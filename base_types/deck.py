from typing import Type
import random

from .rank import Rank, PokerRank, BlackjackRank
from .suit import Suit
from .card import Card

class Deck:
    def __init__(self, rank: Type[Rank], suit: Type[Suit], alt=''):
        self.cards = []
        self.rank = rank
        self.suit = suit
        if alt == '':
            self.initialize_standard_deck()

    def initialize_standard_deck(self):
        self.cards = [Card(rank, suit) for rank in self.rank for suit in self.suit]

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self) -> Card:
        return self.cards.pop()


POKER_DECK = Deck(PokerRank, Suit)
BLACKJACK_DECK = Deck(BlackjackRank, Suit)
