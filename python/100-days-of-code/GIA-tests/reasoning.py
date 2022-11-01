'''Practice test for the Thompson GIA Test 1: Reasoning'''

import random
from os import system
from re import I

comparator = (('big', 'tall', 'large', 'long'), 
                ('bright', 'light', 'dazzling', 'vivid'),
                ('bright', 'clever', 'smart', 'intelligent'),
                ('happy', 'glad', 'cheerful'),
                ('new', 'recent'),
                ('fast', 'quick', 'speedy')
)
opposites = (('small', 'short', 'small', 'little'),
                ('dark', 'dim', 'dull', 'gloomy'),
                ('dumb', 'dim', 'stupid', 'slow'),
                ('sad', 'unhappy', 'gloomy'),
                ('old', 'ancient'),
                ('slow', 'sluggish')
)
names = ('Adam', 'Alice', 'Al', 'Ali', 'Bob', 'Bill', 'Barb', 'Ben', 'Chris', 'Chloe', 'Dan', 'Doug', 'Deb', 'Ellen')

score = [0,0]
number_questions = 10

def add_er(word):
    '''If word ends in e an r is added, if it ends in y the y is removed and ier added, else er is added'''
    if word[-1] == 'e':
        new_word = word + 'r'
    elif word[-1] == 'y':
        new_word = word[0:-1] + 'ier'
    else:
        new_word = word + 'er'
    return new_word

def phrase_generator(word0, word1, phrase_type):
    '''Return a joining phrase using a random synonym and form
    
    phrase_type 0 means word0 is true, phrase_type 1 means word1 is true
    e.g. phrase_generator(('big', 'large'), ('small', 'short'), 0) 
    could return "is bigger" or "is not as small"
    '''
    phrase = ""
    negate = random.randint(0,1) == 1
    if phrase_type == 0:
        if negate:
            phrase += "not as "
            phrase += random.choice(word1)
        else:
            phrase += add_er(random.choice(word0))
    else:
        if negate:
            phrase += "not as "
            phrase += random.choice(word0)
        else:
            phrase += add_er(random.choice(word1))
    return phrase

system('cls||clear')
while score[1] < number_questions:
    person0 = random.choice(names)
    person1 = random.choice(names)
    ans = ''
    while person1 == person0:
        person1 = random.choice(names)
    index = random.randint(0, len(comparator)-1)
    q_type = random.randint(0,1)
    a_type = random.randint(0,1)
    if a_type == q_type:
        ans = person0
    else:
        ans = person1
    joining_phrase = phrase_generator(comparator[index], opposites[index], q_type)
    if joining_phrase[0:3] == 'not':
        joining_phrase += ' as'
    else:
        joining_phrase += ' than'
    print(f"{person0} is {joining_phrase} {person1}")
    input("\nPress Enter to continue")
    system('cls||clear')
    joining_phrase = phrase_generator(comparator[index], opposites[index], a_type)
    print(f"Who is {joining_phrase}")
    guess = input(': ')

    if guess == ans:
        score[0] += 1
        print("Correct")
    else:
        print(f"Wrong!")
    score[1] += 1
    input("\nPress enter for next question")
    system('cls||clear')
print(f"You scored {score[0]} / {score[1]}")