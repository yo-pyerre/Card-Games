from .deck import Deck
from .dealer import Dealer

class Game:
    def __init__(self, deck: Deck):
        self.dealer = Dealer(deck)
        self.players = []
        self.state = {}
        self.log = []

