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

game_over = False
correct_letters = []

while not game_over:
     # TODO: - Update the code below to tell the user how many lives they have left.
     print(f"****************************{lives}/6 LIVES LEFT****************************")
     guess = input("Guess a letter: ").lower()
     

# TODO: - If the user has entered a letter they've already guessed, print the letter and let them know.
     if guess in correct_letters:
        print(f"You already guessed 😅 {guess}")

     display = ""

     for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

     print("Word to guess: " + display)

     if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed {guess}, that's not in the word. You've lost a life 😒")
        if lives == 0:
          game_over = True

            # TODO: - Update the print statement below to give the user the correct word they were trying to guess.
          print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

     if "_" not in display:
          game_over = True
          print("****************************YOU WIN****************************")
     
     #TODO: - Update the code below to use the stages List from the file hangman_art.py
     print(stages[lives])