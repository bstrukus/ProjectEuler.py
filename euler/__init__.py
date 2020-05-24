#!/usr/bin/env python3
import cProfile

from .problems import *

useExampleValues = False
#useExampleValues = True

problemDictionary = [
    Ex1(), Ex2(), Ex3(), Ex4(), Ex5(),
    Ex6(), Ex7(), Ex8(), Ex9()
]

def printAnswer(problemNumber, answerValue):
    print(f'{problemNumber}.) {answerValue}')

def getAnswerFromProblemNumber(problemNumber):
    if problemNumber > len(problemDictionary):
        return 'In progress...'
    else:
        return problemDictionary[problemNumber - 1].run(True)

def run(problemNumber = None):
    if problemNumber == None or problemNumber == 0:
        for i in range(len(problemDictionary)):
            printAnswer(i + 1, getAnswerFromProblemNumber(i + 1))
    elif problemNumber == -1:
        for i in range(len(problemDictionary)):
            cProfile.run(f'problems.ex{i + 1}.main()')
    else:
        printAnswer(problemNumber, getAnswerFromProblemNumber(problemNumber))