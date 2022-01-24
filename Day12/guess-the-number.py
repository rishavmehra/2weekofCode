from random import randint
from art import logo

HARD=5
EASY=10
turns=0
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns -1 
    elif guess<answer:
        print("Too low")
        return turns -1 
    else:
        print(f"You got it! The answer was {answer}")

def diff():
    level=input("Choose a difficulty. Type 'easy' or 'hard':")
    if level=="easy":
        return EASY
    if level=="hard":
        return HARD


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer=randint(1,100)
    # print(f"test answer {answer}")
    turns=diff()
    
    guess=0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("Make a guess:"))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You've run out of guess, you lose.")
            return
        elif guess!=answer:
            print("Guess again")

game()