#!/usr/bin/env python3

class Prime:
    def __init__(self, numberOfPrimesToGenerate):
        self.precalculatedPrimes = [2, 3, 5, 7, 11] # Initialize with first 5 primes
        self.generatePrimes(numberOfPrimesToGenerate)

    def generatePrimes(self, numberOfPrimesToGenerate):
        generatedPrimes = self.precalculatedPrimes 
        
        currentNumber = generatedPrimes[-1] + 1 # Start our search from the end of our known primes
        while len(generatedPrimes) < numberOfPrimesToGenerate:
            if self.isPrime(currentNumber):
                generatedPrimes.append(currentNumber)
            currentNumber += 1
        self.precalculatedPrimes = generatedPrimes

    def getPrimes(self):
        return self.precalculatedPrimes

    def getNthPrime(self, nthValue):
        if nthValue > len(self.precalculatedPrimes):
            self.generatePrimes(nthValue)
        return self.precalculatedPrimes[nthValue - 1]

    def isPrime(self, num):
        if num == 2:
            return True

        if num <= 1 or num % 2 == 0:
            return False

        if num in self.precalculatedPrimes:
            return True
            
        maxTestableValue = num // 2
        for i in range(2, maxTestableValue):
            if num % i == 0:
                return False
        return True