from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizBrain: QuizBrain):
        #this is a quiz brain object with quiz brain methods
        self.quiz = quizBrain
        #window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #label
        self.scoreLabel = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.scoreLabel.grid(row=0, column=1)

        #canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125, width=280, text="Testing", font=("Arial",20,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #button
        trueImg = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=trueImg, highlightthickness=0, command=self.trueAnswer)
        self.trueButton.grid(row=2, column=0)

        falseImg = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=falseImg, highlightthickness=0, command=self.falseAnswer)
        self.falseButton.grid(row=2, column=1)

        #the get next question method
        self.getNextQuestion()

        self.window.mainloop()

    #this prints question to the ui
    def getNextQuestion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreLabel.config(text=f"Score: {self.quiz.score}")
            qText = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=qText)
        else:
            #this prints exact score and gives the message of the end of the quiz
            self.canvas.itemconfig(self.text, text=f"You have reached the end of the quiz.\n Your current score is: {self.quiz.score}/{self.quiz.question_number}")
            #this will disable the buttons after quiz has reached the final questions
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")


    def trueAnswer(self):
        answer = self.quiz.check_answer("true")
        self.feedback(answer)

    def falseAnswer(self):
        answer = self.quiz.check_answer("False")
        self.feedback(answer)

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.getNextQuestion)
