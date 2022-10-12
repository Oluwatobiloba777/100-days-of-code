from tkinter import *

import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
currentCard = {}
newData = {}

try:
    #the csv file
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    dataFile = pandas.read_csv("data/french_words.csv")
    newData = dataFile.to_dict(orient="records")
else:
    newData = data.to_dict(orient="records")

#function for the card

def card():
    global currentCard, flipTimer
    window.after_cancel(flipTimer)
    currentCard = random.choice(newData)
    canvas.itemconfig(cardTitle, text="French", fill="black")
    canvas.itemconfig(cardWord, text=currentCard["French"], fill="black")
    canvas.itemconfig(cardBackgroundImages, image=cardFront)
    flipTimer = window.after(3000, func=flipCard)


def flipCard():
    canvas.itemconfig(cardTitle, text="English", fill="white")
    canvas.itemconfig(cardWord, text=currentCard["English"], fill="white")
    canvas.itemconfig(cardBackgroundImages, image=cardBack)

def userCard():
    newData.remove(currentCard)

    newdata = pandas.DataFrame(newData)
    newdata.to_csv("data/words_to_learn.csv", index=False)
    card()


#UI
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#this will flip the card
flipTimer = window.after(3000, func=flipCard)

#canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")
#this holds the front image and can be changed in the function for flip card
cardBackgroundImages = canvas.create_image(400, 263, image=cardFront)
cardTitle = canvas.create_text(400, 150,text="", font=("Ariel", 40, "italic"))
cardWord = canvas.create_text(400, 263,text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#button
wrongImage = PhotoImage(file="images/wrong.png")
wrongButton = Button(image=wrongImage, highlightthickness=0, command=card)
wrongButton.grid(row=1, column=0)

rightImage = PhotoImage(file="images/right.png")
rightButton = Button(image=rightImage, highlightthickness=0, command=userCard)
rightButton.grid(row=1, column=1)


card()


window.mainloop()