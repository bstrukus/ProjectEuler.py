#!/usr/bin/env python3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from problems.baseProblem import BaseProblem

exampleValue = 10
problemValue = 20

class Ex5(BaseProblem):
    def __init__(self):
        BaseProblem.__init__(self, exampleValue, problemValue)

    def divisibleByRange(self, rangeTotal):
        numberRange = range(rangeTotal, 0, -1)
        divisibleByAll = False
        currentNumber = rangeTotal
        
        while not divisibleByAll:
            divisibleByAll = True   # Assume True until proven otherwise
            for i in numberRange:
                if currentNumber % i > 0:
                    divisibleByAll = False
                    break
            else:
                return currentNumber
            currentNumber += rangeTotal

    def run(self, useExampleValue):
        return self.divisibleByRange(self.getProblemValue(useExampleValue))
