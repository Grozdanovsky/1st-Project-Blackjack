import time
from deck import *
from functions import *


c1 = Deck()
c2 = Deck()
c3 = Deck()
c4 = Deck()
c5 = Deck()
main_deck = Deck()
main_deck.set_deck(c1,c2,c3,c4,c5)
player = []
dealer = []

player.append(main_deck.get_card())
player.append(main_deck.get_card())
print_player_cards(player,"Your")
dealer.append(main_deck.get_card())
dealer.append(main_deck.get_card())
print_player_cards([dealer[0]],"Dealers")
blackjack(player)

while True:
    question = input("Do you want another card? ")
    if question.lower() == "yes":
        player.append(main_deck.get_card())
        print_player_cards(player,"Your")
        print_player_cards([dealer[0]],"Dealers")
        if add_sum_cards(player) > 21:
            player = one_or_eleven(player)
            if add_sum_cards(player) > 21:
                break

    elif question.lower() == "no":
        if add_sum_cards(player) > add_sum_cards(dealer):
            add_dealer_cards(player, dealer, main_deck)
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



