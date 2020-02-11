#!/usr/bin/env python3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

exampleValue = 10
problemValue = 20

mainValue = problemValue

def divisibleByRange(rangeTotal):
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

def main():
    return divisibleByRange(mainValue)

if __name__ == '__main__':
    print(main())