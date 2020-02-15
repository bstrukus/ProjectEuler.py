#!/usr/bin/env python3

# Base class for all problems

class BaseProblem():
    def __init__(self, exampleVal, problemVal):
        self.exampleValue = exampleVal
        self.problemValue = problemVal

    def getProblemValue(self, useExampleValue):
        if useExampleValue:
            return self.exampleValue
        return self.problemValue

    def run(self, useExampleValue):
        return 'Working on it!'