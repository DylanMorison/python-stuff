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

    def deal_one(self):
        return self.all_cards.pop()

    def print_cards(self):
        for card in self.all_cards:
            print(card)


new_deck = Deck()
new_deck.shuffle()
print(len(new_deck.all_cards))
mycard = new_deck.deal_one()
print(mycard)
print(len(new_deck.all_cards))