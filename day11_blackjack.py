import random

# This is a game of blackjack


deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Function to calculate the score of a hand
def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
       return 0
    if 11 in cards and sum(cards) > 21:
       cards.remove(11)
       cards.append(1)
    return sum(cards)

# Function to compare the scores of the user and the computer
def compare(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "You went over. You lose 😤"
    if user_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# Function to play the game
def play():
    user_cards =[]
    comp_cards =[]
    is_game_over = False
    for _ in range(2):
        user_cards.append(deck[random.randrange(0,13)])
        comp_cards.append(deck[random.randrange(0,13)])
    print(f"your cards: {user_cards}")
    print(f"Opponenets card: {comp_cards[0]}")
    
    while not is_game_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)
        if user_score == 0 or comp_score == 0 or user_score > 21:
           is_game_over = True
        else:
            action = input("Press 'y' to draw or 'n' to pass\n")
            if action == 'y':
                user_cards.append(deck[random.randrange(0,13)])
            else:
               is_game_over = True
    
    while comp_score !=0 and comp_score<17:
       comp_cards.append(deck[random.randrange(0,13)])
       comp_score = calc_score(comp_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))
    
while input("Do you want to play BlackJack?\n") == "y":
   play()

        