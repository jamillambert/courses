import os
from hangman_art import stages, logo
from hangman_words import word_list
import random

word = random.choice(word_list)
answer = ['_'] * len(word)
lives = len(stages)
previous_choices = ['']
running_text = 'Welcome to hangman, choose your first letter (or type exit)\n'

while True:
    os.system('cls||clear')
    print(logo)
    print(stages[lives-1])
    print(' '.join(answer) + "\n")
    if '_' not in answer or lives == 0:
        if '_' not in answer:
            print("\nCongradulations you win!\n")
        else:
            print("\nSorry you have lost, try again\n")
            print("The word was: " + word)
        letter = input("Do you want to play again? (y/n) ")
        if letter == 'y':
            word = random.choice(word_list)
            answer = ['_'] * len(word)
            lives = len(stages)
            previous_choices = ['']
            running_text = 'Welcome to hangman, choose your first letter (or type exit)\n'
            continue
        else:
            break
    print(word)
    letter = input(running_text).lower()
    if letter == 'exit':
        break
    elif len(letter) != 1:
        running_text = 'Already chosen letters: ' + ' '.join(previous_choices)
        running_text += "\n\nInvalid input, enter a single letter (or type exit)\n"
    elif letter in previous_choices:
        running_text = 'Already chosen letters: ' + ' '.join(previous_choices)
        running_text += "\n\nYou have already tried {}, try another one (or type exit)\n".format(
            letter)
    elif letter in word:
        previous_choices.append(letter)
        running_text = 'Already chosen letters: ' + ' '.join(previous_choices)
        running_text += "\n\nGood work, {} is in the word, choose the next letter (or type exit)\n".format(
            letter)
        for i in range(len(word)):
           if letter == word[i]:
               answer[i] = letter
    else:
        lives -= 1
        previous_choices.append(letter)
        running_text = 'Already chosen letters: ' + ' '.join(previous_choices)
        running_text += "\n\nSorry, {} is in not in the word, try another one (or type exit)\n".format(
            letter)
