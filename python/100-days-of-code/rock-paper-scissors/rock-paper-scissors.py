''' 
A rock paper scissors command line game
The computer's choice is random and a running total is
kept for all games played

Jamil Lambert 2022
'''

import os
import random

# Unicode rock paper and scissors
rock = '👊'
paper = '✋'
scissors = '✌ '
error = "\nInput not recognised\n"

# variables to store the choices and wins
choices = ['r', 'p', 's']
pictures = {
    'r' : rock,
    'p' : paper,
    's' : scissors
}
wins = [0, 0]
os.system('cls||clear')

while True:
    result = 'e' # The result of the game, 'e' is for an error in the input
    player = input(f"Choose {rock} 'r' {paper} 'p' or {scissors}  's', or 'x' to exit: ").lower()
    if player == 'x':
        break
    os.system('cls||clear')

    computer = choices[random.randint(0, 2)] # computer's random choice
    
    # Print out the unicode rock paper scissors for the player and computer
    print("Player " + pictures.get(player, error) +
          " : " + pictures.get(computer, error) + " Computer")

    # Check who wins, all 9 combinations written out for clarity
    if player == 'r':
        if computer == 'r':
            result='d'
        elif computer == 'p':
            result='l'
        elif computer == 's':
            result='w'
    elif player == 'p':
        if computer == 'r':
            result='w'
        elif computer == 'p':
            result='d'
        elif computer == 's':
            result='l'
    elif player == 's':
        if computer == 'r':
            result='l'
        elif computer == 'p':
            result='w'
        elif computer == 's':
            result = 'd'

    # Print out the result, add to the running score and print it too
    if result == 'w':
        print('\033[92m' + "You WIN!!" + '\033[0m')
        wins[0] += 1
    elif result == 'l':
        print('\033[91m' + "Sorry you Loose" + '\033[0m')
        wins[1] += 1
    elif result == 'd':
        print('\033[94m' + "Draw" + '\033[0m')
    elif result == 'e':
        print('\033[91m' +
              "Input not recognised, please enter a single letter, to indicate your choice" + '\033[0m')
    print(f"\nCurrent score is\nYou {wins[0]}:{wins[1]} Computer\n\n")