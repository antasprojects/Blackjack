import Blackjack

money = int(input("how much money do you want to cash in? "))



while True:

    if money == 0:
        money = int(input("You run out of money! How much do you want to cash in? "))
    else:

        bet = int(input("your account balance is " + str(money) + " how much do you want to bet? "))

        if bet > money:
            print("You do not have that much money!")
            continue
        else:

            result = Blackjack.Blackjack_game()

            if result == "dealer":
                print("You lost " + str(bet) + "!!!")
                money -= bet
            elif result == "player":
                print("You won " + str(bet) + "!!!" )
                money += bet







