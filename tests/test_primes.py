#!/usr/bin/env python3

from .context import primes

defaultPrimeCount = 5

def test_oneIsNotPrime():
    primer = primes.Prime(defaultPrimeCount)
    assert(primer.isPrime(1) == False)

def test_zeroIsNotPrime():
    primer = primes.Prime(defaultPrimeCount)
    assert(primer.isPrime(0) == False)

def test_negativeIsNotPrime():
    primer = primes.Prime(defaultPrimeCount)
    assert(primer.isPrime(-1) == False)

def test_twoIsPrime():
    primer = primes.Prime(defaultPrimeCount)
    assert(primer.isPrime(2) == True)

def test_threeIsPrime():
    primer = primes.Prime(defaultPrimeCount)
    assert(primer.isPrime(3) == True)

def test_pregenerateFirstTenPrimesCorrectly():
    primer = primes.Prime(10)
    generatedPrimes = primer.getPrimes()
    firstTenPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert(generatedPrimes == firstTenPrimes)

def test_tenthPrimeIsTwentyNine():
    primer = primes.Prime(defaultPrimeCount)
    tenthPrime = primer.getNthPrime(10)
    assert(tenthPrime == 29)

def test_generateTenPrimesAfterInitialFive():
    primer = primes.Prime(defaultPrimeCount)
    primer.generatePrimes(10)
    primeCount = len(primer.getPrimes())
    assert(primeCount == 10)