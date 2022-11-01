'''Practice test for the Thompson GIA Test 2: Perceptual speed'''

import random
from os import system

group1 = ('b', 'd', 'g', 'h', 'p', 'q', 'y')
group2 = ('f', 'i', 'j', 'k', 'l', 't')
group3 = ('m', 'n', 'r', 'u', 'v', 'w')
group4 = ('a', 'c', 'e', 'o', 's', 'x', 'z')
score = [0,0]
number_questions = 20

system('cls||clear')
while score[1] < number_questions:
    lower = (random.choice(group1), random.choice(group2),
             random.choice(group3), random.choice(group4))
    
    # Create new lists with the lower case letter instead of using the
    # full lists so there is a higher chance of the letters matching
    second1 = (random.choice(group1).upper(), lower[0].upper())
    second2 = (random.choice(group2).upper(), lower[1].upper())
    second3 = (random.choice(group3).upper(), lower[2].upper())
    second4 = (random.choice(group4).upper(), lower[3].upper())   
    upper = (random.choice(second1), random.choice(second2),
             random.choice(second3), random.choice(second4))

    print(upper)
    print(lower)
    guess = input(f"\n: ")
    matches = 0
    for i in range(0, 4):
        if lower[i] == upper[i].lower():
            matches += 1
    try:
        if int(guess) == matches:
            score[0] += 1
            print("Correct")
        else:
            print(f"Wrong! There are {matches} matches")
    except ValueError:
        print("invalid input")
    score[1] += 1
    input("Press enter for next question")
    system('cls||clear')
print(f"You scored {score[0]} / {score[1]}")