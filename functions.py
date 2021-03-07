def print_player_cards(player, name):
    print(f"{name} Cards")
    for item in player:
        item.print_card()
    print("=====")



def add_sum_cards(player):
    sum1 = 0
    for item in player:
        if item.get_value() > 10:
            sum1 += 10
        else:
            sum1 += item.get_value()

    return sum1

def compare_sums(player,dealer):
    if (add_sum_cards(player) > add_sum_cards(dealer) and add_sum_cards(player) <= 21) or add_sum_cards(dealer) > 21 :
        print("You WON!")

    elif (add_sum_cards(dealer) >= add_sum_cards(player) and add_sum_cards(dealer) <= 21):
        print("You Lost.")

def add_dealer_cards(player,dealer,c1):
    while add_sum_cards(dealer) <= 21 and add_sum_cards(dealer) <= add_sum_cards(player):
        dealer.append(c1.get_card())



