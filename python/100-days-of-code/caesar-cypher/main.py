''' Basic letter substitution "cypher" written for the 100
days of code course.  Extended versions with greatly enhanced
encryption are in separate folders:
caesar-cypher-extended
encryption-6-digit-code
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text=''


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt_decrypt(text, shift):
    encoded = ""
    for letter in text:
        try:
            new_index = alphabet.index(letter) + shift
            while new_index  < 0:
                # Loops back around if the shift pushes off the -ve end
                new_index += len(alphabet)
            while new_index > len(alphabet)-1:
                # Loops back around if the shift pushes off the +ve end
                new_index -= len(alphabet)
            encoded += alphabet[new_index]
        except:
            # If a letter entered is not in the encode list it is added
            # unencoded
            encoded += letter
        
    return encoded


while True:
    direction = input("\nType 'encode' or 'e' to encrypt, 'decode' or 'd' to decrypt, 'x' to exit:\n")
    if direction == 'x':
        break

    if direction == "encrypt" or direction == 'e':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        text = encrypt_decrypt(text, shift)
        print(f"Encoded text is '{text}'")
    elif direction == "decrypt" or direction == 'd':
        new_text = input("Type your message or leave blank to decode previous:\n").lower()
        try:
            new_shift = int(input("Type the shift number or leave blank to use previous:\n"))
            shift = new_shift
        except:
            shift = shift
        if new_text != '':        
            text = new_text
        text = encrypt_decrypt(text, -shift)
        print(f"Decoded text is '{text}'")
    else:
        print ("invalid option")