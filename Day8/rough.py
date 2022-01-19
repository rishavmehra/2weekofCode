# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("Hello1")
#   print("Hello1")
#   print("Hello1")
# greet()

# Funtion that allows for input
# def greet_for_name(name):
#     print(f"Hello {name}")
#     print(f"how do you do{name}")
# greet_for_name("Rishu")


#function more than 1 input
# def greet_with(name,location):
#     print(f"hey {name}, how's the weather in {location}")
# # greet_with("rishu","dehra")
# greet_with(location="dehra",name="rishu")

# # Area Calc
# import math
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# def paint_calc(height, width, cover):
#     number_of_cans = (height*width)/cover
#     print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")
# paint_calc(height=test_h, width=test_w, cover=coverage)

#Prime Number Checker
# from random import randrange
# n = int(input("Check this number: "))

# def prime_checker(number):
#     is_prime=True
#     for i in range(2,number-1):
#         if number%i==0:
#             is_prime=False
#     if is_prime:
#         print("It's a prime Number")
#     else:
#         print("It's not a prime Number")

# prime_checker(number=n)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amount):
    cipher=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position + shift_amount
        new_letter = alphabet[new_position]
        cipher += new_letter
    print(f"The encoded text is {cipher}")

def decrypt(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        plain_text += alphabet[new_position]
    print(f" The decoded text is {plain_text} ")

if direction=="encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction=="decode":
    decrypt(cipher_text=text, shift_amount=shift)
