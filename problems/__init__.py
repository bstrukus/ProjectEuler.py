#!/usr/bin/env python3
import cProfile

from problems.ex1 import Ex1
import problems.ex2
import problems.ex3
import problems.ex4
import problems.ex5
import problems.ex6

import problems.importProblem

useExampleValues = False

problemDictionary = [
    #problems.ex1.main,
    Ex1(useExampleValues)
    #problems.ex2.main,
    #problems.ex3.main,
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
        return problemDictionary[problemNumber - 1].run()

def run(problemNumber = None):
    if problemNumber == None:
        for i in range(len(problemDictionary)):
            printAnswer(i + 1, getAnswerFromProblemNumber(i + 1))
    elif problemNumber == -1:
        for i in range(len(problemDictionary)):
            cProfile.run(f'problems.ex{i + 1}.main()')
    else:
        printAnswer(problemNumber, getAnswerFromProblemNumber(problemNumber))