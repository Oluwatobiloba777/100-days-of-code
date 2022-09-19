from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caeser(direction,text,shift):
    cipherText = ""
    if direction == 'decode':
            shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        newPosition = position + shift
        cipherText += alphabet[newPosition]
    print(f"The {direction} result is {cipherText}")



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caeser(text=text,shift=shift,direction=direction)