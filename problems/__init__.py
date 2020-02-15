#!/usr/bin/env python3
import cProfile

from problems.ex1 import Ex1
from problems.ex2 import Ex2
from problems.ex3 import Ex3
from problems.ex4 import Ex4
from problems.ex5 import Ex5
from problems.ex6 import Ex6
from problems.ex7 import Ex7

useExampleValues = False
#useExampleValues = True

problemDictionary = [
    Ex1(), Ex2(), Ex3(), Ex4(), Ex5(),
    Ex6(), Ex7()
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