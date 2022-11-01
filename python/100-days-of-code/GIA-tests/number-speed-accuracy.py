'''Practice test for the Thompson GIA Test 3: Number speed & Accuracy'''

import random
from os import system

score = [0,0]
number_questions = 20
max_num = 15

system('cls||clear')
while score[1] < number_questions:
    a = random.randint(1, max_num-5)
    b = random.randint(a+1, max_num-3)
    c = random.randint(b+1, max_num)
    while c - b == b - a:    
        c = random.randint(b+1, max_num)

    numbers = [a, b, c]
    random.shuffle(numbers)
    guess = input(f"\n{numbers}\n: ")
    system('cls||clear')
    if c - b > b - a:
        ans = c
    else:
        ans = a
    try:
        if int(guess) == ans:
            print("Correct")
            score[0] += 1
        else:
            print("Wrong!")
    except ValueError:
        print("Invalid input")
    score[1] += 1
print(f"You scored {score[0]} / {score[1]}")