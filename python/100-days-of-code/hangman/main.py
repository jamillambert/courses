'''
A text based hangman game.  The user inputs single letters
through the terminal input to try and guess a random word
from the list of words in hangman_words.py

requires
hangman_words.py - list of words provided by 100 days of python course, some non words removed
hangman_art.py - some ASCII art provided by 100 days of python course, the missinging first 
                 stages added

Jamil Lambert 2022
'''

import os, time
from hangman_art import stages, logo
from hangman_words import word_list
import random

# A random word from the list stored in hangman_words.py is chosen
word = random.choice(word_list)
answer = ['_'] * len(word)
lives = len(stages) - 1
previous_choices = ['']
running_text = "Welcome to hangman, choose your first letter (or type 'exit')\n"

while True:
    # Loops until the player chooses to exit the game
    os.system('cls||clear')
    print(logo)
    print(stages[lives])
    print(' '.join(answer) + "\n")
    if '_' not in answer or lives == 0:
        # The game is over and is reset
        if '_' not in answer:
            # There are no more blank letters so the player has won
            print("\nCongradulations you win!\n")
        else:
            # No more lives left so the player has lost
            print("\nSorry you have lost, try again\n")
            print("The word was: " + word +  "\n")
        letter = input("Do you want to play again? (y/n) ")
        if letter == 'y':
            # A new word is chosen and the answer and live variables are reset
            word = random.choice(word_list)
            answer = ['_'] * len(word)
            lives = len(stages) - 1
            previous_choices = ['']
            running_text = "Welcome to hangman, choose your first letter (or type 'exit')\n"
            continue
        else:
            print("\n")
            break
    letter = input(running_text).lower()
    if letter == 'exit':
        break
    elif len(letter) != 1:
        # A single letter was not input
        running_text = 'Already chosen letters: ' + ' '.join(previous_choices)
        running_text += "\n\nInvalid input, enter a single letter (or type 'exit')\n"
    elif letter in previous_choices: 
        # The letter was already chosen, no change to answer or lives
        running_text = 'Already chosen letters: ' + ' '.join(previous_choices)
        running_text += "\n\nYou have already tried {}, try another one (or type 'exit')\n".format(
            letter)
    elif letter in word:
        # The letter chosen is in the word, it is added to the answer array
        previous_choices.append(letter)
        running_text = 'Already chosen letters: ' + ' '.join(previous_choices)
        running_text += "\n\nGood work, {} is in the word, choose the next letter (or type 'exit')\n".format(
            letter)
        for i in range(len(word)):
           if letter == word[i]:
               answer[i] = letter
    else: 
        # The letter is not in the word, 1 life lost
        lives -= 1
        previous_choices.append(letter)
        running_text = 'Already chosen letters: ' + ' '.join(previous_choices)
        running_text += "\n\nSorry, {} is in not in the word, try another one (or type 'exit')\n".format(
            letter)
