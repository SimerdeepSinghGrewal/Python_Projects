import os
import random
from hangman_art import *
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(logo)


display = []
for _ in range(word_length):
    display += "_"
guess = 0
while not end_of_game:
    dup = guess
    guess = input("Guess a letter: ").lower()
    clear = lambda: os.system('cls')
    clear()
    if dup == guess:
      print(f"You have already guessed '{guess}' Please enter some other alphabet.")
    else:
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter

      #Check if user is wrong.
      if guess not in chosen_word:
          print(f"Your guessed letter is '{guess}' and it is not present in the answer. You Lose a life")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lost the game.")

      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")

      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")
      print(stages[lives])
print(f'The answer was {chosen_word}.')