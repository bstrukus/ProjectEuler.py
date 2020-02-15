#!/usr/bin/env python3
# A palindromic number reads the same both ways. The largest palindrome made from the prodect of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from problems.baseProblem import BaseProblem

exampleValue = 2
problemValue = 3

class Ex4(BaseProblem):
    def __init__(self):
        BaseProblem.__init__(self, exampleValue, problemValue)
    
    def digitsToNum(self, digitCount):
        if digitCount <= 0:
            return 0
        return int(digitCount * '9')

    def findPalindromicNumber(self, digitCount):
        maxVal, minVal = self.digitsToNum(digitCount), self.digitsToNum(digitCount - 1)
        maxPalindrome = 0

        for x in range(maxVal, minVal, -1):
            for y in range(maxVal, minVal, -1):
                product = x * y
                productStr = str(product)
                reverseStr = productStr[::-1]
                if productStr == reverseStr and maxPalindrome < product:
                    maxPalindrome = product

        return maxPalindrome

    def run(self, useExampleValue):
        return self.findPalindromicNumber(self.getProblemValue(useExampleValue))
