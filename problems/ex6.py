#!/usr/bin/env python3

#The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from problems.baseProblem import BaseProblem

exampleValue = 10
problemValue = 100

class Ex6(BaseProblem):
    def __init__(self):
        BaseProblem.__init__(self, exampleValue, problemValue)

    def sumOfSquaresOfRange(self, rangeLimit):
        operatingRange = range(1, rangeLimit + 1)

        sum = 0
        for i in operatingRange:
            sum += i**2
        return sum

    def squareOfSumOfRange(self, rangeLimit):
        return sum(range(1, rangeLimit + 1))**2

    def squareSumDiff(self, rangeLimit):
        return self.squareOfSumOfRange(rangeLimit) - self.sumOfSquaresOfRange(rangeLimit)

    def run(self, useExampleValue):
        return self.squareSumDiff(self.getProblemValue(useExampleValue))
