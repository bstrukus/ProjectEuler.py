#!/usr/bin/env python3

# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the larges prime factor of the number 600851475143?
from problems.prime import Prime
from problems.problem import BaseProblem

exampleValue = 13195
problemValue = 600851475143

useExampleValueInMain = False

class Ex3(BaseProblem):
    def __init__(self):
        BaseProblem.__init__(self, exampleValue, problemValue)
        self.primeChecker = Prime(10)

    def run(self, useExampleValue):
        return self.getLargestPrimeFactorOf(self.getProblemValue(useExampleValue))

    def getLargestPrimeFactorOf(self, num):
        if self.primeChecker.isPrime(num):
            return num
            
        maxTestableValue = num // 2
        #print(f'Max testable value of {num} is {maxTestableValue}')
        for i in range(2, maxTestableValue):
            if self.primeChecker.isPrime(i) and num % i == 0:
                #print(f'Factor found = {i}')
                return self.getLargestPrimeFactorOf(num // i)
            
def main():
    problemSolver = Ex3()
    return problemSolver.run(useExampleValueInMain)

if __name__ == '__main__':
    print(main())