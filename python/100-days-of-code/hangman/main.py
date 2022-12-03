"""
A text based hangman game.  The user inputs single letters
through the terminal input to try and guess a random word
from the list of words in hangman_words.py

requires
hangman_words.py - list of words provided by 100 days of python course, some non words removed
hangman_art.py - some ASCII art provided by 100 days of python course, the missinging first
                 stages added

Jamil Lambert 2022
"""

import os
from hangman_art import stages, logo
from hangman_words import word_list
import random


class GameState:
    """Contains the current state of the game, including the word and guesses so far"""

    def __init__(self):
        self.word = random.choice(word_list)
        self.answer = ['_'] * len(self.word)
        self.lives = len(stages) - 1
        self.previous_choices = []
        self.running_text = "Welcome to hangman, choose your first letter (or type 'exit')\n"

    def game_over(self):
        """Returns True if the game is over"""
        return '_' not in self.answer or self.lives == 0

    def game_won(self):
        """Returns True if the player has won"""
        if '_' not in self.answer:
            # No more blanks in the answer so the player has won
            print("\nCongradulations you win!\n")
            return True
        else:
            # No more lives left so the player has lost
            print("\nSorry you have lost, try again\n")
            print("The word was: " + self.word + "\n")
            return False

    def print_state(self):
        """Prints out the logo and current state of the game"""
        print(logo)
        print(stages[self.lives])  # The hangman drawing that adds a section each time a wrong letter is chosen
        print(' '.join(self.answer) + "\n")

    def input_letter(self):
        """Prompts player to input a letter and return False if they choose to exit"""
        letter = input(self.running_text).lower()
        if letter == 'exit':
            print("\nSorry you have lost, due to being a quitter\n")
            print("The word was: " + self.word + "\n\nBye\n")
            return False
        elif len(letter) != 1:
            # A single letter was not input
            self.running_text = 'Already chosen letters: ' + \
                                ' '.join(self.previous_choices)
            self.running_text += "\n\nInvalid input, enter a single letter (or type 'exit')\n"
            return True
        else:
            self.check_letter(letter)
            return True

    def check_letter(self, letter):
        """Checks if the input letter is valid, and if in the word adds it to the current answer"""
        if letter in self.previous_choices:
            # The letter was already chosen, no change to answer or lives
            self.running_text = 'Already chosen letters: ' + ' '.join(self.previous_choices)
            self.running_text += "\n\nYou have already tried {}, try another one (or type 'exit')\n".format(
                letter)
            return True
        self.previous_choices.append(letter)
        self.running_text = 'Already chosen letters: ' + \
                            ' '.join(self.previous_choices)
        if letter in self.word:
            # The letter chosen is in the word, it is added toe the answer array
            self.running_text += "\n\nGood work, {} is in the word, choose the next letter (or type 'exit')\n".format(
                letter)
            for i in range(len(self.word)):
                if letter == self.word[i]:
                    self.answer[i] = letter
        else:
            # The letter is not in the word, 1 life lost
            self.lives -= 1
            self.running_text += "\n\nSorry, {} is in not in the word, try another one (or type 'exit')\n".format(
                letter)


def main():
    """Creates a new GameState and runs the game until the player chooses to exit"""
    # A random word from the list stored in hangman_words.py is chosen within game
    game = GameState()

    while True:
        # Loops until the player chooses to exit the game
        os.system('cls||clear')
        game.print_state()

        if game.game_over():
            # The game is over
            game.game_won()
            if play_again():
                # A new game with a new word is created
                game = GameState()
                continue
            else:
                print("\n\nThanks for playing, bye\n\n")
                break

        # Display the running text and ask the player to input a letter
        if not game.input_letter():
            # If the player chooses to exit this breaks out of the loop
            break


def play_again():
    """Returns True if the player chooses to play again"""
    letter = input("Do you want to play again? (y/n) ")
    return letter == 'y'


main()
