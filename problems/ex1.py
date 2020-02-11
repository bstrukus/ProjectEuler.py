#!/usr/bin/env python3

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 100.

from problems.problem import BaseProblem

exampleValue = 10
problemValue = 100

class Ex1(BaseProblem):
    def __init__(self, runWithExampleValue):
        BaseProblem.__init__(self, exampleValue, problemValue)
        
        self.Value = problemValue
        if runWithExampleValue == True:
            self.Value = exampleValue

    def pickySum(self, limit):
        sum = 0
        for i in range(limit):
            if i % 3 == 0 or i % 5 == 0:
                sum += i

        return sum

    def run(self):
        return self.pickySum(self.Value)

def main():
    pickeeSum = Ex1(False)
    return pickeeSum.run()
    #return pickySum(mainValue)

if __name__ == '__main__':
    print(main())
    #myProblem = Ex1(exampleValue, problemValue)
    #myProblem.run()