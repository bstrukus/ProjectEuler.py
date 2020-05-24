#!usr/bin/env python3

class PrimeCache():
    FILENAME = 'prime_cache.txt'
    END_OF_FILE = 'END'
    DEBUG_LOG = False

    def __init__(self):
        self.primeCount = 0
        self.primes = {}

    def __enter__(self):
        self.print('PrimeCache.__enter__')

    def __exit__(self, exc_type, exc_value, traceback):
        self.print('PrimeCache.__exit__')

    def print(self, message):
        if self.DEBUG_LOG:
            print(message)

    def printPrimes(self):
        if self.DEBUG_LOG:
            for index, prime in self.primes.items():
                print(f'{index}:{prime}')

    def addPrime(self, index, prime):
        self.primes[index] = prime

    def getPrimes(self):
        return list(self.primes.values())

    def loadCachedPrimes(self):
        self.print('PrimeCache.loadCachedPrimes')
        with open(self.FILENAME, 'r') as cacheFile:
            cachedPrime = cacheFile.readline()
            while cachedPrime != self.END_OF_FILE:
                parsedPrime = cachedPrime.split(':')
                self.primes[int(parsedPrime[0])] = int(parsedPrime[1].rstrip())
                cachedPrime = cacheFile.readline()
        
        self.printPrimes()
        return self.getPrimes()

    def saveCachedPrimes(self):
        print('PrimeCache.saveCachedPrimes')
        # Overrwrite the whole file for now, want to append in the future
        self.printPrimes()
        with open(self.FILENAME, 'w') as cacheFile:
            for index, prime in self.primes.items():
                cacheFile.write(f'{index}:{prime}\n')
            cacheFile.write(self.END_OF_FILE)

    def count(self):
        return len(self.primes)

if __name__ == '__main__':
    x = PrimeCache()
    x.loadCachedPrimes()
    x.saveCachedPrimes()