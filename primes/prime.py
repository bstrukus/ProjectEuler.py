#!/usr/bin/env python3

from .primeCache import PrimeCache

class Prime:
    DEBUG_LOG = True

    def __init__(self, numberOfPrimesToGenerate):
        #self.primeCache = PrimeCache()
        self.precalculatedPrimes = [2, 3, 5, 7, 11] #self.primeCache.loadCachedPrimes()
        self.generatePrimes(numberOfPrimesToGenerate)

#    def __enter__(self):
#        self.print('Prime.__enter__')#
#    def __exit__(self, exc_type, exc_value, traceback):
#        self.print('Prime.__exit__')
#        self.syncWithCache()
#        #self.primeCache.saveCachedPrimes()

    def print(self, message):
        if self.DEBUG_LOG:
            print(message)

    def generatePrimes(self, numberOfPrimesToGenerate):
        #self.print(f'Generating {numberOfPrimesToGenerate} primes')

        generatedPrimes = self.precalculatedPrimes 
        
        currentNumber = generatedPrimes[-1] + 1 # Start our search from the end of our known primes
        while len(generatedPrimes) < numberOfPrimesToGenerate:
            if self.isPrime(currentNumber):
                generatedPrimes.append(currentNumber)
            currentNumber += 1
        self.precalculatedPrimes = generatedPrimes

    def syncWithCache(self):
        index = 0
        while index < len(self.precalculatedPrimes):
            #self.primeCache.addPrime(index + 1, self.precalculatedPrimes[index])
            index += 1

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

#if __name__ == '__main__':
#    with Prime(10) as testPrime:
#        print('Test start!')
    
