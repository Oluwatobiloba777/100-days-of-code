# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.

import random
from game_data import data
from art import logo,vs


def randomAccount():
    return random.choice(data)

def accountData(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, a {description}, from {country}."


def checkAnswer(guess,firstFollowerCount,secondFollowerCount):
    if firstFollowerCount > secondFollowerCount:
        return guess == 'a'
    else:
        return guess == 'b'

def startGame():
    print(logo)
    score = 0
    firstAccount = randomAccount()
    secondAccount = randomAccount()

    while True:
        firstAccount = secondAccount
        secondAccount = randomAccount()

        while firstAccount == secondAccount:
            secondAccount = randomAccount()

        print(f'A. {accountData(firstAccount)}')
        print(vs)
        print(f'B. {accountData(secondAccount)}')

        guess = input("Who has more followers. 'A' or 'B': ").lower()
        firstFollowerCount = firstAccount['follower_count']
        secondFollowerCount = secondAccount['follower_count']
        result = checkAnswer(guess,firstFollowerCount,secondFollowerCount)


        if result:
            score += 1
            print(f"That's an awesome {score}! You're in the top 10% of players.")
        else:
            print(f"Did we make this too hard for you?... Your final is {score}\n We hope you had a good game")
            break

startGame()
