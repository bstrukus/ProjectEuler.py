#!/usr/bin/env python3

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10,001st prime number?

from problems.baseProblem import BaseProblem
from problems.prime import Prime

exampleValue = 6
problemValue = 10001

class Ex7(BaseProblem):
    def __init__(self):
        BaseProblem.__init__(self, exampleValue, problemValue)

    def findNthPrime(self, nthValue):
        primeChecker = Prime(5)
        return primeChecker.getNthPrime(nthValue)

    def run(self, useExampleValue):
        return self.findNthPrime(self.getProblemValue(useExampleValue))
