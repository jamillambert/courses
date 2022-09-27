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

#Write your code below this line 👇

choices = ['r', 'p', 's']
wins = [0, 0]
os.system('cls||clear')
while True:
    result = 'e'
    player = input("Choose Rock 'r' Paper 'p' or Scissors 's', or 'x' to exit: ").lower()
    os.system('cls||clear')
    if player ==  'r':
        print(f"You choose: {rock}")
    elif player ==  'p':
        print(f"You choose: {paper}")
    elif player ==  's':
        print(f"You choose: {scissors}")
    elif player ==  'x':
        break
    else:
        result == 'e'
    print('\nComputer chooses:')
    computer = choices[random.randint(0, 2)]
    if computer == 'r':
        print(rock)
    elif computer == 'p':
        print(paper)
    elif computer == 's':
        print(scissors)
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