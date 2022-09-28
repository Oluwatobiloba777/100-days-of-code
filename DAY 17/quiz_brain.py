class QuizBrain:

    def __init__(self,list):
        self.questionNumber = 0
        self.questionList = list
        self.score = 0

    def moreQuestions(self):
        return self.questionNumber < len(self.questionList)

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber +=1
        userAnswer = input(f"Question.{self.questionNumber} :{currentQuestion.text} (True/False): ").lower()
        self.checkAnswer(userAnswer,currentQuestion.answer)

    def checkAnswer(self,userAnswer,correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score += 1
            print('You got it right!') 
        
        else:
            print("That's wrong!")
        
        print(f"The correct answer was: {correctAnswer}")
        print(f"Your current score is: {self.score}/{self.questionNumber}")
        print('\n')
