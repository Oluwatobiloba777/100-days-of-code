import random
from art import logo

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cardChoice = random.choice(cards)
    return cardChoice

#Hint 2: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculateScore(cards):

#Hint 3: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
#Hint 4: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
#Hint 5: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(userScore, computerScore):
    if userScore > 21 and computerScore > 21:
        return "You went over. You lose"
    if userScore == computerScore:
        return "Draw"
    elif computerScore == 0:
        return "Lose, oppenent has Blackjack"
    elif userScore == 0:
        return "Win with a Blackjack"
    elif userScore > 21:
        return "You went over. You lose"
    elif computerScore > 21:
        return "Opponent went over. You win"
    elif userScore > computerScore:
        return "You win"
    else:
        return "You lose"

def playGame():
    print(logo)
    #Hint 6: Deal the user and computer 2 cards each using deal_card() and append().
    userCards = []
    computerCards = []
    gameOver = False

    for pick in range(2):
        userCards.append(dealCard())
        computerCards.append(dealCard())

    #Hint 7: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not gameOver:

        #Hint 8: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        print(f" Your cards: {userCards}, Current Score: {userScore}")
        print(f" Computer card: {computerCards[0]}")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            gameOver = True
        else:

        #Hint 9: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            userDeal = input("Type 'yes' to get another card, type 'no' to pass: ")
            if userDeal == 'yes':
                userCards.append(dealCard())
            else:
                gameOver = True

    #Hint 10: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computerScore !=0 and computerScore <17:
        computerCards.append(dealCard())
        computerScore = calculateScore(computerCards)
    print(f" Your final hand: {userCards}, Final score: {userScore}")
    print(f" Computer's final hand:{computerCards}, Final score: {computerScore}")
    print(compare(userScore,computerScore))

#Hint 11: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while True:
    choice = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
    if choice == 'yes':
        playGame()
    else:
        print("We hope you had a good game")
        break