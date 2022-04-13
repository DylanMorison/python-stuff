from random import shuffle
from Card import suits, ranks, Card


class Deck:
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def print_cards(self):
        for card in self.all_cards:
            print(card)


new_deck = Deck()
new_deck.print_cards()
new_deck.shuffle()
new_deck.print_cards()