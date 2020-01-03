# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the larges prime factor of the number 600851475143?

def isPrime(num):
    if num <= 1 or num % 2 == 0:
        return False
        
    maxTestableValue = num // 2
    for i in range(2, maxTestableValue):
        if num % i == 0:
            return False
    return True;

def getPrimesLessThan(limit):
    primes = []
    for i in range(1, limit, 2):
        if isPrime(i):
            primes.append(i)
    return primes
    
def getPrimeFactorsOf(num):
    factors = []
    primes = getPrimesLessThan(num)
    for i in primes:
        if num % i == 0:
            factors.append(i)
    
    return factors

num = 600851475143
#num = 13195

largestPrimeFactor = getPrimeFactorsOf(num).pop()
print(f'Largest prime factor of {num} is {largestPrimeFactor}')