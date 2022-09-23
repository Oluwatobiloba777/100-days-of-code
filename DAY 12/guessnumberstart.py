#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

easyLevel = 10
hardLevel = 5


def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return easyLevel
    else:
        return hardLevel


def userGuess(guess,answer, turn):
    if guess > answer:
        print('Too high.')
        return turn -1
    elif guess < answer:
        print('Too low.')
        return turn -1
    else:
        print(f"You got it! The answer was {answer}")




def startGame():
    print('Welcome to Guess a number game')
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1,100)
    turn = difficulty()
    guess = 0
    gameOver = False
    while not gameOver:
        print(f"You have {turn} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        turn = userGuess(guess,answer,turn)
        if turn ==0:
            print("You are out of guesses, you lose")
            gameOver = True
        elif guess != answer:
            print('Guess again.')

startGame()

