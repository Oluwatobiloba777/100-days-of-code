import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if userChoice >= 3 or userChoice < 0: 
    print("An invalid number, you lose!") 
else:
    print(images[userChoice])

    cpu = random.randint(0, 2)
    print("Computer chose:")
    print(images[cpu])


    if userChoice == 0 and cpu == 2:
        print("You win!")
    elif cpu == 0 and userChoice == 2:
        print("You lose")
    elif cpu > userChoice:
        print("You lose")
    elif userChoice > cpu:
        print("You win!")
    elif cpu == userChoice:
        print("It's a draw")