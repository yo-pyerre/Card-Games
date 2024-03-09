from enum import Enum, auto

class Suit(Enum):
    DIAMOND = auto()
    HEART = auto()
    SPADE = auto()
    CLUB = auto()

    def __repr__(self):
        return f'{self.name.title()}'
