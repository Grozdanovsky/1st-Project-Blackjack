import time
from deck import *
from functions import *
balance = 1000
play = True

while play:

    print(f"Your balance is ${balance}.")
    game = input("Do you want to play? ")
    bet = 0
    if game.lower() == "yes":

        bet = int(input("Place your bet: "))


        if bet > balance:
            print(f"Your bet is bigger than your balance, so your bet now is your remaining balance ${balance}")
            bet = balance

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


        while True:

            multiple = blackjack(player, balance, bet,False)
            if multiple[0] > balance:
                balance = multiple[0]
                print(balance)
                break

            question = input("Do you want another card? ")

            if question.lower() == "yes":
                player.append(main_deck.get_card())

                if add_sum_cards(player) > 21:
                    player = one_or_eleven(player)

                    if add_sum_cards(player) > 21:
                        balance -= bet
                        break
                print_player_cards(player, "Your")
                print_player_cards([dealer[0]], "Dealers")

            elif question.lower() == "no":

                if add_sum_cards(player) > add_sum_cards(dealer) and add_sum_cards(dealer) < 17:
                    add_dealer_cards(player, dealer, main_deck)

                if add_sum_cards(player) == add_sum_cards(dealer) and add_sum_cards(dealer) >= 17:
                    break

                if add_sum_cards(dealer) > 21:
                    dealer = one_or_eleven(dealer)
                    if add_sum_cards(dealer) > 21:
                        break

                if add_sum_cards(dealer) > add_sum_cards(player) and add_sum_cards(dealer) <= 21:
                    break




        new_balance = compare_sums(player, dealer,balance,bet,multiple[1])
        balance = new_balance
        if balance == 0:
            print("You ran out of $$$. BYE")
            time.sleep(5)
            play = False
        time.sleep(5)

    elif game.lower() == "no":
        print(f"Thanks for playing, your balance is ${balance}. BYE")
        time.sleep(5)
        play = False




