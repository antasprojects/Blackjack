## Card deck

def Blackjack_game():

    import random
    import os
    import time

    clear = lambda: os.system('cls')

    deck = {
        '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5,
        '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
        '10 of Spades': 10, 'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10,
        'Ace of Spades': 11,

        '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5,
        '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
        '10 of Hearts': 10, 'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10,
        'Ace of Hearts': 11,

        '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5,
        '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
        '10 of Diamonds': 10, 'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10,
        'Ace of Diamonds': 11,

        '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5,
        '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
        '10 of Clubs': 10, 'Jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10,
        'Ace of Clubs': 11
    }

    # player first card
    def card_from_deck():
        card_key = random.choice(list(deck.keys()))
        card_val = deck[card_key]
        del deck[card_key]
        return {card_key: card_val}


    def player_draw():
        player_cards.update(card_from_deck())

    def dealer_draw():
        dealer_cards.update(card_from_deck())

    def print_player():
        for card in list(player_cards.keys()):
            print(card)
            time.sleep(1)

    def print_dealer():
        for card in list(dealer_cards.keys()):
            print(card)
            time.sleep(1)


    player_cards = {}
    dealer_cards = {}

    #player first card
    player_draw()

    #dealer first card
    dealer_draw()

    #player second card
    player_draw()

    #dealer second card
    dealer_draw()

    is_winner = False

    print("Dealer has two cards and first of them is:")
    time.sleep(1)
    print(list(dealer_cards.keys())[0])
    time.sleep(1)
    print("Player received two cards:")
    time.sleep(1)
    print_player()

    # player move

    decision = input("You can either stand or hit type your decision! ")

    while decision != "stand":
        if decision == "hit":
            player_draw()
            print_player()
            if sum(list(player_cards.values())) > 21:
                print("\n")
                print("\n")
                print("Dealer cards: ")
                print_dealer()
                print("\n")
                print("Player cards: ")
                print_player()
                print("\n")
                print("The values of your cards exceeded 21! You lost!")
                is_winner = True
                result = "dealer"
                break
        else:
            print("You have to choose hit or stand!")
        decision = input("You can either stand or hit type your decision! ")


    # dealer move
    if is_winner == False:
        dealer_sum = sum(list(dealer_cards.values()))
        while dealer_sum < 17:
            dealer_draw()
            dealer_sum = sum(list(dealer_cards.values()))
        if dealer_sum > 21:
            print("The dealer cards exceed 21, the player won!")
            is_winner == True
            result = "player"



    if is_winner == False:
        print("\n")
        print("Player cards: ")
        print_player()
        print("\n")
        print("Dealer cards: ")
        print_dealer()


        player_sum = sum(list(player_cards.values()))
        if dealer_sum > player_sum:
            print("\n")
            print("Dealer has more points! The dealer wins!")
            result = "dealer"
        elif player_sum > dealer_sum:
            print("\n")
            print("Player has more points! The player wins!")
            result = "player"
        elif dealer_sum == player_sum:
            print("\n")
            print("Player points are the same as dealer, it is a draw!")
            result = "draw"

    return result
