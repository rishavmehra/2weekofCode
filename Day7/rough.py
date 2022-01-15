import random
import os
from os import system
# import hangman_art
# import hangman_word

from hangman_art import logo
print(logo)
from hangman_word import word_list
chosen_word = random.choice(word_list)
# print(f'Pssst, the solution is {chosen_word}.')
display= []
word_length=range(len(chosen_word))

for letter in word_length:
    display += "_"
# print(display)
end_of_game=False
lives=6
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    system('cls')
    for position in word_length:
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    # print(display)
    if guess not in chosen_word:
        print(f'{guess} it\'s not in the word, You losing the life')
        lives-=1
        if lives ==0:
            end_of_game=True
            print("You Lose!")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You Win!")
    from hangman_art import stages
    print(stages[lives])