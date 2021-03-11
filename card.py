class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def print_card(self):
        print(self.value,self.suit)

    def get_suit(self):
        return self.suit

    def set_value(self,new_value):
        self.value = new_value
