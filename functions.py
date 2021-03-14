from static import special_cards
def print_player_cards(player, name):
    print(f"{name} Cards")

    for item in player:
        card = special_cards.get(item.get_value())

        if card:
            print(card, item.get_suit())
        else:
            item.print_card()
    print("=====")



def add_sum_cards(player):
    sum1 = 0
    for item in player:
        if item.get_value() > 10 and item.get_value() != 11:
            sum1 += 10
        else:
            sum1 += item.get_value()

    return sum1

def compare_sums(player,dealer):
    if (add_sum_cards(dealer) >= add_sum_cards(player) and add_sum_cards(dealer) <= 21) or add_sum_cards(player) > 21:
        print_player_cards(player, "Your")
        print_player_cards(dealer, "Dealers")
        print("You Lost!")


    elif (add_sum_cards(player) > add_sum_cards(dealer) and add_sum_cards(player) <= 21) or add_sum_cards(dealer) > 21 :
        print_player_cards(player, "Your")
        print_player_cards(dealer, "Dealers")
        print("You WON!")

def add_dealer_cards(player,dealer,c1):
    while add_sum_cards(dealer) <= 21 and add_sum_cards(dealer) < add_sum_cards(player):
        dealer.append(c1.get_card())




def one_or_eleven(player):

    for number in range(len(player)):

        if player[number].get_value() == 11:

            player[number].set_value(1)
            break

    return player






def blackjack(player):
    card1 = player[0].get_value()
    card2 = player[1].get_value()
    if (card1 == 1 or card1 == 11) and (card2 > 11 or card2 == 10):
        print("BLACKJACK!!!")
        quit()
    elif (card1 > 11 or card1 == 10) and (card2 == 1 or card2 == 11):
        print("BLACKJACK!!!")
        quit()
    else:
        pass
