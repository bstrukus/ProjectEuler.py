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

def getLargestPrimeFactorOf(num):
    if isPrime(num):
        return num
        
    maxTestableValue = num // 2
    #print(f'Max testable value of {num} is {maxTestableValue}')
    for i in range(2, maxTestableValue):
        if isPrime(i) and num % i == 0:
            #print(f'Factor found = {i}')
            return getLargestPrimeFactorOf(num // i)
            

# Main code
num = 600851475143

largestPrimeFactor = getLargestPrimeFactorOf(num)
print(f'Largest prime factor of {num} is {largestPrimeFactor}')