logo = '''
 ________  ___  ___  _______   ________   ________           _________  ___  ___  _______           ________   ___  ___  _____ ______   ________  _______   ________     
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\___   ___\\  \|\  \|\  ___ \         |\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \|___ \  \_\ \  \\\  \ \   __/|        \ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \            \ \  \ \ \   __  \ \  \_|/__       \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \            \ \  \ \ \  \ \  \ \  \_|\ \       \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \            \ \__\ \ \__\ \__\ \_______\       \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|\_________\\_________\            \|__|  \|__|\|__|\|_______|        \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|
                                 \|_________\|_________|                                                                                                                 
                                                                                                                                                                         
                                                                                                                                                                         
'''
import random

answer = int(random.random()*100)

def check_guess(num):
    global answer
    if(num < answer):
        print("Too low!")
        return False
    elif num> answer:
        print("Too high")
        return False
    else:
        print("You guessed the number")
        return True

def set_level():
    level = int(input("Choose difficulty: 1. easy 2. moderate 3. hard:\n"))
    if level == 1:
        lives = 10
        print(f"You have {lives} guesses")
    elif level == 2:
        lives = 7
        print(f"You have {lives} guesses")
    elif level == 3:
        lives = 5
        print(f"You have {lives} guesses")

    else:
        print("Enter valid life")
    return lives

    

def play():
    print(logo)
    print()
    lives = set_level()
    is_correct = False
    while lives>0 and not is_correct:
        guess = int(input("Guess the number from 1 to 100\n"))
        print(f"You have {lives} guesses left!")
        is_correct = check_guess(guess)
        lives-=1
    if lives == 0:
        print("No more lives :(")
play()
    
    
    

