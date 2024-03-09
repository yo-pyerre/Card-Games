from .card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def peek(self):
        return [card.peek() for card in self.cards]

    def show(self, index=None):
        if not index:
            for card in self.cards:
                card.flip()
        else:
            self.cards[index].flip()
