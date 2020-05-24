#!/usr/bin/env python3

# Base class for all problems

class BaseProblem():
    def __init__(self, problemNumber, getProblemValue):
        self.exampleValue = getProblemValue(problemNumber, True)
        self.problemValue = getProblemValue(problemNumber)
        self.debugging = False

    def getProblemValue(self, useExampleValue):
        if useExampleValue:
            return self.exampleValue
        return self.problemValue

    def run(self, useExampleValue):
        return 'Working on it!'

    def debugLog(self, message):
        if (self.debugging):
            print(message)