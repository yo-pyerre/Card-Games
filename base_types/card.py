from .suit import Suit
from .rank import Rank

class Card:
    def __init__(self, rank: Rank, suit: Suit, hidden: bool = True):
        self.rank = rank
        self.suit = suit
        self.hidden = hidden

    def flip(self):
        self.hidden = False

    # Allow a player to look at their own cards even if they're "Face Down"
    def peek(self):
        return f"{self.rank.__repr__()} of {self.suit.__repr__()}s"

    def __repr__(self):
        if self.hidden:
            return 'Face Down'
        return f"{self.rank.__repr__()} of {self.suit.__repr__()}s"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

