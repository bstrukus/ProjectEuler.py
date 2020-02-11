#!/usr/bin/env python3

# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the larges prime factor of the number 600851475143?
from problems.prime import Prime

exampleValue = 13195
problemValue = 600851475143

mainValue = problemValue

primeChecker = Prime(10)

def getLargestPrimeFactorOf(num):
    if primeChecker.isPrime(num):
        return num
        
    maxTestableValue = num // 2
    #print(f'Max testable value of {num} is {maxTestableValue}')
    for i in range(2, maxTestableValue):
        if primeChecker.isPrime(i) and num % i == 0:
            #print(f'Factor found = {i}')
            return getLargestPrimeFactorOf(num // i)
            
def main():
    return getLargestPrimeFactorOf(mainValue)

if __name__ == '__main__':
    print(main())