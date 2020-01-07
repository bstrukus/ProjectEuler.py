import problems.ex1
import problems.ex2
import problems.ex3
import problems.ex4
import problems.ex5

problemCount = 5

def printAnswer(problemNumber, answerValue):
    print(f'{problemNumber}.) {answerValue}')

def getAnserFromProblemNumber(problemNumber):
    if problemNumber == 1:
        return problems.ex1.main()
    elif problemNumber == 2:
        return problems.ex2.main()
    elif problemNumber == 3:
        return problems.ex3.main()
    elif problemNumber == 4:
        return problems.ex4.main()
    elif problemNumber == 5:
        return problems.ex5.main()
    else:
        return 'In progress...'

def run(problemNumber = None):
    if problemNumber == None:
        for i in range(problemCount):
            printAnswer(i + 1, getAnserFromProblemNumber(i + 1))
    else:
        printAnswer(problemNumber, getAnserFromProblemNumber(problemNumber))
