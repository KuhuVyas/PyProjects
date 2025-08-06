import random
from hangman_words import word_list
from hangman_art import stages, logo
#TODO: Setting the lives, as per the stages in the hangman game 
lives = 6

# TODO: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
