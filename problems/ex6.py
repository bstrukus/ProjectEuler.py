#!/usr/bin/env python3

#The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

exampleValue = 10
problemValue = 100

mainValue = problemValue

def sumOfSquaresOfRange(rangeLimit):
    operatingRange = range(1, rangeLimit + 1)

    sum = 0
    for i in operatingRange:
        sum += i**2
    return sum

def squareOfSumOfRange(rangeLimit):
    return sum(range(1, rangeLimit + 1))**2

def squareSumDiff(rangeLimit):
    return squareOfSumOfRange(rangeLimit) - sumOfSquaresOfRange(rangeLimit)

def main():
    return squareSumDiff(mainValue)

if __name__ == '__main__':
    print(main())