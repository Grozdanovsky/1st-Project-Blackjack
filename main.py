import time
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
print_player_cards([dealer[0]],"Dealers")
blackjack(player)

while True:
    question = input("Do you want another card? ")
    if question.lower() == "yes":
        player.append(c1.get_card())
        print_player_cards(player,"Your")
        print_player_cards([dealer[0]],"Dealers")
        if add_sum_cards(player) > 21:
            player = one_or_eleven(player)
            if add_sum_cards(player) > 21:
                break

    elif question.lower() == "no":
        if add_sum_cards(player) > add_sum_cards(dealer):
            add_dealer_cards(player, dealer, c1)
        if add_sum_cards(player) == add_sum_cards(dealer):
            break
        if add_sum_cards(dealer) > 21:
            dealer = one_or_eleven(dealer)
            if add_sum_cards(dealer) > 21:
                break
        if add_sum_cards(dealer) > add_sum_cards(player) and add_sum_cards(dealer) <= 21:
            break


compare_sums(player, dealer)
time.sleep(10)



