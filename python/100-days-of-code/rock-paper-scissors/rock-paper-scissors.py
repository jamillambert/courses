import os
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

error = "\nInput not recognised\n"
#Write your code below this line 👇

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
    player = input("Choose Rock 'r' Paper 'p' or Scissors 's', or 'x' to exit: ").lower()
    if player == 'x':
        break
    os.system('cls||clear')

    # Print out the text picture from above for the player's choice
    print("Player:" + pictures.get(player, error))

    computer = choices[random.randint(0, 2)] # computer's random choice
    # Print out the text picture from above for the computer's choice        
    print("Computer" + pictures.get(computer, error))

    # Check who wins
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