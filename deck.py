from card import *
import random

class Deck:
    def __init__(self):
        self.static_list = self.return_list()
        self.shuffle_cards()
        self.playable_list = self.static_list


    def return_list(self):
        list_cards = []

        for item in range(4):
            for item2 in range(1, 14):
                if item == 0:
                    c1 = Card(item2, "Diamonds")
                    list_cards.append(c1)
                elif item == 1:
                    c1 = Card(item2, "Hearts")
                    list_cards.append(c1)
                elif item == 2:
                    c1 = Card(item2, "Spades")
                    list_cards.append(c1)
                elif item == 3:
                    c1 = Card(item2, "Clubs")
                    list_cards.append(c1)

        return list_cards

    def print_cards(self):
        for item in self.playable_list:
            item.print_card()

    def get_card(self):
        card_index = random.randint(1,len(self.playable_list)-1)
        card = self.playable_list.pop(card_index)
        return card

    def shuffle_cards(self):
        random.shuffle(self.static_list)
