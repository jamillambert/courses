#Password Generator Project
import random

# Removed easily mistaken characters 0, O, I, l
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
symbols = ('!', '#', '$', '%', '&', '(', ')', '*', '+')

print("\nWelcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Solution below

pass_list = [] 
pass_string = ''

for i in range(nr_letters):
    pass_list += random.choice(letters)
for i in range(nr_symbols):
    pass_list += random.choice(symbols)
for i in range(nr_numbers):
    pass_list += random.choice(numbers)

random.shuffle(pass_list)
for char in pass_list:
    pass_string += char
print(f"Your password is: {pass_string}") 