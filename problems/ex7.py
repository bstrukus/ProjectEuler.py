#!/usr/bin/env python3

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10,001st prime number?

from problems.baseProblem import BaseProblem

exampleValue = 10001
problemValue = 6

class Ex7(BaseProblem):
    def __init__(self):
        BaseProblem.__init__(self, exampleValue, problemValue)
