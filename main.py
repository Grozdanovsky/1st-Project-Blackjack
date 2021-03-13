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
        #Printing player cards
        print_player_cards(player,"Your")
        #Printing dealer 1st card
        print_player_cards([dealer[0]],"Dealers")

        if add_sum_cards(player) > 21:
            player = one_or_eleven(player)
            if add_sum_cards(player) > 21:
                print("You Lost!")
                time.sleep(10)
                break



    elif question.lower() == "no":
        if add_sum_cards(player) > add_sum_cards(dealer):
            add_dealer_cards(player, dealer, c1)
        if add_sum_cards(player) == add_sum_cards(dealer):
            print_player_cards(player, "Your")
            print_player_cards(dealer, "Dealers")


            print("You Lost!")
            time.sleep(10)
            break
        if add_sum_cards(dealer) > 21:
            dealer = one_or_eleven(dealer)
            if add_sum_cards(dealer) > 21:
                print_player_cards(dealer,"Dealers")
                print("You Won!")
                time.sleep(10)
                break
        compare_sums(player, dealer)
        #Printing Player cards

        time.sleep(10)
        break




