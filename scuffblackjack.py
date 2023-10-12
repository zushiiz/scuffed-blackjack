import random

def cards():
    c_list = ["jack", "queen", "king"]
    c_value = random.randint(1, 13)
    c = "card"

    if c_value == 11:
        c_value = 10
        new_card = c.replace("card", c_list[0])

    elif c_value == 12:
        c_value = 10
        new_card = c.replace("card", c_list[1])

    elif c_value == 13:
        c_value = 10        
        new_card = c.replace("card", c_list[2])

    else:
        new_card = c_value
    
    return c_value, new_card

def player(play):

    p_point = 0

    while True:

        if play == "stop":
                break

        elif play == "take":
                playerv, playerc = cards()
                p_point += playerv
                print(f"You got {playerc} and you have {p_point} points")

        if p_point > 21:
                print(f"player got more than 21 points dealer wins")
                play_again()

        play = input("take another or stop? (take, stop)")

    return p_point

def dealer():

    d_point = 0

    while d_point <= 17:
        dealerv, dealerc = cards()
        d_point += dealerv
        print(f"the dealer got {dealerc} and has {d_point} points")

        if d_point > 21:
            print(f"dealern got more than 21 points player wins")
            play_again()

    return d_point

def win(psum, dsum):

        if dsum == psum:
            print("its a tie!")

        elif psum < dsum <= 21:
            print(f"the dealer has {dsum} and player has {psum} dealer is the winner")

        elif psum < dsum <= 21:
            print(f"the dealer has {dsum} and player has {psum} player is the winner")

def play_again():
    ask = input("would you like to play again? (yes, no):")
    if ask == "yes":
        blackjack()
    else: 
        print("thank you for playing, have a nice day!")
        exit()

def blackjack():

    play = input("take a card or stop (take, stop):")

    psum = player(play)
    dsum = dealer()
    win(psum, dsum)
    play_again()

blackjack()