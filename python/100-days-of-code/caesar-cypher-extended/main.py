'''
A plain text encoder/decoder that takes a single integer as the encoding key
the shift is changed after each letter and spaces and special characters are
used to greatly enhance the security over the simple letter substitution used
in the original caesar cypher

Jamil Lamber 2022
'''

# Added a space to the original list to make breaking the code harder, i.e. word lenghts are also encrypted
# also added some common special characters used in text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', ' ', '_', '!', ',', '.', '?', '$', '&', '#', ';'
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+',
            '=', '@', '%', '^', '*', "'", '"', ':']

text=''

def encrypt_decrypt(text, shift):
    # Takes the text to encode or decode and the key as inputs
    # returns the encoded or decoded text
    encoded = ""
    adv_shift = shift
    for letter in text:
        new_index = alphabet.index(letter) + adv_shift
        while new_index  < 0:
            # Loops back around if the shift pushes off the -ve end
            new_index += len(alphabet)
        while new_index > len(alphabet)-1:
            # Loops back around if the shift pushes off the +ve end
            new_index -= len(alphabet)
        encoded += alphabet[new_index]
        # For each letter the shift is incremented to stop simple breaking of the code
        adv_shift += shift
    return encoded


while True:
    # Loops until the user enters 'x'
    direction = input("\nType 'encode' or 'e' to encrypt, 'decode' or 'd' to decrypt, 'x' to exit:\n")
    if direction == 'x':
        break
    if direction == "encrypt" or direction == 'e':
        text = input("Type your message:\n").lower()
        try:
            shift = int(input("Type the shift number:\n"))
        except:
            print("Invalid shift entered, no encryption done")
            shift = 0
        text = encrypt_decrypt(text, shift)
        print(f"Encoded text is '{text}'")
    elif direction == "decrypt" or direction == 'd':
        # Decoding is simply running the same function in the opposite direction
        # an option is given to reuse the input text and shift to make testing
        # decoding easier
        new_text = input("Type your message or leave blank to decode previous:\n").lower()
        if new_text != '':        
            text = new_text
        try:
            new_shift = int(input("Type the shift number or leave blank to use previous:\n"))
            shift = -new_shift
        except:
            shift = -shift
        text = encrypt_decrypt(text, shift)  
        print(f"Decoded text is '{text}'")
    else:
        print ("invalid option")