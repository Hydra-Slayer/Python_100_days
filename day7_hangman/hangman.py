import random
from hangman_acsii import stages, logo
from hangman_wordlist import word_list

# selects the word from word list
idx = random.randint(0, len(word_list) - 1) 
word = word_list[idx]
guessed_word = ["_"] * len(word)

#prints logo
print(logo)
print(guessed_word)

# game logic
lives = 6
while lives >= 0:
    guess = input("Guess a letter: ").lower()
    if guess not in word:
            print(stages[lives])
            lives -= 1
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            guessed_word[position] = letter
            print(" ".join(guessed_word))
        
            

        if "_" not in guessed_word:
            print("You win!")
            break
        
# if lives are 0, print you lose
print("You lose!")
print(f"The word was {word}")