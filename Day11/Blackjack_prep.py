#day 11 start
import random

cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
values = {
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10,
    'A':11,
}

#gameloop

#deal 1-1 card

player_card_1 = random.choice(cards)
player_card_2 = random.choice(cards)
player_cards = [player_card_1, player_card_2]

dealer_card_1 = random.choice(cards)
dealer_card_2 = random.choice(cards)
dealer_cards = [dealer_card_1, dealer_card_2]

#show first round
print("-----------------------")
print("dealer's cards :")
i = 0
while i < len(dealer_cards) - 1:
    print(dealer_cards[i]+"    hidden card")
    i += 1

print(f"\n\n\n")
print(f"player cards are:")
for card in player_cards:
    print(card)
player_choice = input(" Would you like another card? type 'yes' or 'no': ")
if player_choice == 'no':
    player_score = values[player_card_1] + values[player_card_2]
    print(f"Your score: {player_score}")
    dealer_score = values[dealer_card_1] + values[dealer_card_2]
    print(f"Dealer score at 2 cards is: {dealer_score}")
    while dealer_score<=16:
        dealer_card_new = random.choice(cards)
        print(f"Dealer: {dealer_card_1} + {dealer_card_2} + {dealer_card_new}")
        dealer_score += values[dealer_card_new]
        if dealer_score>21:
            print("dealer futott!!")
            break
        else:
            if dealer_score > player_score:
                print("dealer wins")
            else:
                print("you win")
else:
    player_card_new = random.choice(cards)
    player_cards.insert(player_card_new)
    print(f"player cards are:")
    for card in player_cards:
        print(card)
    pfscore =0
    for card in player_cards:
        pfscore += values[card]
    print(f"player score is {pfscore}")





