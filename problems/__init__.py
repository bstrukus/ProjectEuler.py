#!/usr/bin/env python3
import cProfile

from problems.ex1 import Ex1
from problems.ex2 import Ex2
from problems.ex3 import Ex3
import problems.ex4
import problems.ex5
import problems.ex6

import problems.importProblem

#useExampleValues = False
useExampleValues = True

problemDictionary = [
    Ex1(), Ex2(), Ex3()
    #problems.ex4.main,
    #problems.ex5.main,
    #problems.ex6.main
]

def printAnswer(problemNumber, answerValue):
    print(f'{problemNumber}.) {answerValue}')

def getAnswerFromProblemNumber(problemNumber):
    if problemNumber > len(problemDictionary):
        return 'In progress...'
    else:
        return problemDictionary[problemNumber - 1].run(useExampleValues)

def run(problemNumber = None):
    if problemNumber == None or problemNumber == 0:
        for i in range(len(problemDictionary)):
            printAnswer(i + 1, getAnswerFromProblemNumber(i + 1))
    elif problemNumber == -1:
        for i in range(len(problemDictionary)):
            cProfile.run(f'problems.ex{i + 1}.main()')
    else:
        printAnswer(problemNumber, getAnswerFromProblemNumber(problemNumber))