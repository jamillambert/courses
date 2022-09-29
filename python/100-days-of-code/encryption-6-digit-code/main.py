'''
A plain text encoder/decoder that takes a 6 digit code as the encoding key.
The character shift is changed after each letter using finite field maths 
to greatly enhance the security over the simple letter substitution used 
in the original caesar cypher.

Jamil Lamber 2022
'''

import os

# Added a space to the original list to make breaking the code harder, i.e. word lengths
# are also encrypted, also added some common special characters used in text, 
# and upper case
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', ' ', '_', '!', ',', '.', '?', '$', '&', 
            '#', ';', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            '-', '+', '=', '@', '%', '^', '*', "'", '"', ':']

text=''

primes = [73, 79, 83, 89, 97, 101, 103, 107, 109, 113]  # Prime number used in encoding, the one used is determined by the last digit in the code


def finite_add(x, y, prime):
    return (x + y) % prime


def finite_multiply(x, y, prime):
    return (x * y) % prime


def finite_pow(x, exponent, prime):
    n = exponent % (prime - 1)
    return pow(x, n, prime)


def encrypt_decrypt(text, code, direction):
    # Takes the text to encode or decode and the encryption/decryption code as inputs
    # returns the encoded or decoded text, direction is 1 for encode and -1 for decode
    encoded = ''
    if code == 0:
        print("Invalid code entered, no encryption done")
        return
    # input code is split into digits, from 1 to 10 by adding 1, so there are no 0's
    code1 = int(code / 100000) # First digit in the code, -ve is decode, cannot be 0, enforced on input
    code2 = int(str(abs(code))[1]) + 1       # Second digit
    code3 = int(str(abs(code))[2]) + 1       # Third digit
    code4 = int(str(abs(code))[3]) + 1       # Fourth digit
    code5 = int(str(abs(code))[4]) + 1       # Fifth digit
    prime = primes[int(str(abs(code))[5])]   # Sixth digit used to get the prime at index [sixth digit] 
    
    for letter in text:
        # The letter shift is calculated using all 6 digits of the code
        # the maths is like a finite field
        ax3 = finite_multiply(code1, finite_pow(code4, 3, prime), prime)
        bx2 = finite_multiply(code2, finite_pow(code4, 2, prime), prime)
        cx = finite_multiply(code3, code4, prime)
        cubic = finite_add(finite_add(ax3, bx2, prime), cx, prime)
        shift = direction*cubic  # -ve for decode and +ve for encode

        # Each time a letter is parsed, code1 to code5 are incremented
        code1 = finite_add(code1, code5, prime)
        code2 = finite_add(code2, code5, prime)
        code3 = finite_add(code3, code5, prime)
        code4 = finite_add(code4, code5, prime)
        code5 = finite_add(code5, code5, prime)

        try:
            new_index = alphabet.index(letter) + shift
            while new_index  < 0:
                # Loops back around if the shift pushes off the -ve end
                new_index += len(alphabet)
            while new_index >= len(alphabet):
                # Loops back around if the shift pushes off the +ve end
                new_index -= len(alphabet)
            encoded += alphabet[new_index]
            # For each letter the shift is incremented to stop simple breaking of the code
        except:
            # If a letter entered is not in the encode list it is added
            # unencoded
            encoded += letter
    return encoded


def input_code(text, previous):
    code_text = input(text)
    if code_text == '':
        return previous
    else:
        try:
            code = int(code_text)
            if code < 100000 or code > 999999:
                # A 6 digit code was not entered, or started with a 0
                return 0
            return code
        except:
            return 0


while True:
    # Loops until the user enters 'x'
    choice = input("\nType 'encrypt' or 'e' to encrypt, 'decrypt' or 'd' to decrypt, 'x' to exit:\n")
    os.system('cls||clear')
    if choice == 'x' or choice == 'exit':
        break
    if choice == "encrypt" or choice == 'e':
        text = input("Type the message to encode, or paste text:\n")
        code = input_code("\nEnter a 6 digit code, cannot start with 0:\n", 0)
        text = encrypt_decrypt(text, code, 1)
        print(f"\nEncoded text is '{text}'")
    elif choice == "decrypt" or choice == 'd':
        # Decoding is simply running the same function with a negative code
        # an option is given to reuse the input text and code to make testing
        # decoding easier
        new_text = input(
            "Enter the message to decode, or leave blank to decode previous text:\n")
        if new_text != '':        
            text = new_text
        code = input_code("Enter the 6 digit code or leave blank to use previous:\n", code)
        text = encrypt_decrypt(text, code, -1)  
        print(f"\nDecoded text is '{text}'")
    else:
        print ("\nInvalid option")