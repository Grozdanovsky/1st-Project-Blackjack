from deck import *
from functions import *


c1 = Deck()

player = []
dealer = []

player.append(c1.get_card())
player.append(c1.get_card())
print_player_cards(player,"Your")
dealer.append(c1.get_card())
dealer.append(c1.get_card())
print("Dealers Cards")
dealer[0].print_card()

while True:
    question = input("Do you want another card? ")
    if question.lower() == "yes":
        player.append(c1.get_card())
        print_player_cards(player,"Your")

        dealer[0].print_card()

        if add_sum_cards(player) > 21:
            print("You Lost!")
            break



    elif question.lower() == "no":
        if add_sum_cards(player) > add_sum_cards(dealer):
            add_dealer_cards(player, dealer, c1)
        compare_sums(player, dealer)
        print_player_cards(player,"Your")
        print_player_cards(dealer,"Dealers")
        break





