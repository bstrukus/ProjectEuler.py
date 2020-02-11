#!/usr/bin/env python3

# Base class for all problems

class BaseProblem():
    def __init__(self, exampleVal, problemVal):
        self.exampleValue = exampleVal
        self.problemVal = problemVal

    def run(self):
        print('Working on it!')