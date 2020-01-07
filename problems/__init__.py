import problems.ex1
import problems.ex2
import problems.ex3
import problems.ex4
import problems.ex5

problemDictionary = [
    problems.ex1.main,
    problems.ex2.main,
    problems.ex3.main,
    problems.ex4.main,
    problems.ex5.main
]

def printAnswer(problemNumber, answerValue):
    print(f'{problemNumber}.) {answerValue}')

def getAnswerFromProblemNumber(problemNumber):
    if problemNumber > len(problemDictionary):
        return 'In progress...'
    else:
        return problemDictionary[problemNumber - 1]()

def run(problemNumber = None):
    if problemNumber == None:
        for i in range(len(problemDictionary)):
            printAnswer(i + 1, getAnswerFromProblemNumber(i + 1))
    else:
        printAnswer(problemNumber, getAnswerFromProblemNumber(problemNumber))
