import problems.ex1
import problems.ex2
import problems.ex3
import problems.ex4

def printAnswer(problemNumber, answerValue):
    print(f'{problemNumber}.) {answerValue}')

def run():
    printAnswer(1, problems.ex1.main())
    printAnswer(2, problems.ex2.main())
    printAnswer(3, problems.ex3.main())
    printAnswer(4, problems.ex4.main())