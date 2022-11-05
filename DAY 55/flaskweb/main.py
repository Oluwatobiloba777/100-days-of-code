from flask import Flask
import random

app = Flask(__name__)

HOME = "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"
HIGH = "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
LOW = "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
RIGHT = "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
randomNumber = random.randint(0, 9)
print(randomNumber)


@app.route('/')
def home():
    return f"<h1>Guess a number between 0 and 9</h1> {HOME}"



@app.route("/<int:guessedNumber>")
def guessNumber(guessedNumber):
    if guessedNumber > randomNumber:
        return f"<h1 style='color: red'>Too high, try again!</h1> {HIGH}"

    elif guessedNumber < randomNumber:
        return f"<h1 style='color: yellow'>Too low, try again!</h1> {LOW}"

    else:
        return f"<h1 style='color: green'>You found me!</h1> {RIGHT}"

