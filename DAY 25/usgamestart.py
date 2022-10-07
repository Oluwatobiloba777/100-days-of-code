import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
allStates = data.state.to_list()
guessedStates = []
while len(guessedStates) < 50:
    answerState = screen.textinput(title=f"{len(guessedStates)}/50 States Correct", prompt="What's another State's name:").title()
    print(answerState)
    #if answer is in 50 states
    if answerState == "Exit":
        #using list comprehension
        missingStates = [state for state in allStates if state not in guessedStates]
        # missingStates = []
        # for state in allStates:
        #     if state not in guessedStates:
        #         missingStates.append(state)
        newData = pd.DataFrame(missingStates)
        newData.to_csv("correction for states.csv")
        break
    if answerState in allStates:
        guessedStates.append(answerState)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateData = data[data.state == answerState]
        t.goto(int(stateData.x), int(stateData.y))
        t.write(answerState)




#screen.exitonclick()
#turtle.mainloop()