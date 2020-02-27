#!usr/bin/env python3

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exist exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc

from problems.baseProblem import BaseProblem
import itertools


# Values equal to a + b + c
exampleValue = 12
problemValue = 1000

class Ex9(BaseProblem):
    def __init__(self):
        BaseProblem.__init__(self, exampleValue, problemValue)

    def run(self, useExampleValue):
        return self.findPythagoreanTripletForSummation(self.getProblemValue(useExampleValue))

    def findPythagoreanTripletForSummation(self, summation):
        # Create list of all possible
        maxValue = summation - 1 # Need a,b,c candidates to be at least 2 away from summation
        combinations = itertools.combinations(range(1, maxValue), 3)
        for combo in combinations:
            if (sum(combo) == summation):
                a = combo[0]
                b = combo[1]
                c = combo[2]
                if self.checkForPythagoreanTriplet(a, b, c):
                    self.debugLog(f'a = {a}, b = {b}, c = {c}, a+b+c = {a + b + c}')
                    return a * b * c

    def checkForPythagoreanTriplet(self, a, b, c):
        return a**2 + b**2 == c**2