# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisibleByRange(rangeTotal):
    numberRange = range(rangeTotal)
    divisibleByAll = False
    currentNumber = rangeTotal
    
    while not divisibleByAll:
        divisibleByAll = True   # Assume True until proven otherwise
        for i in numberRange:
            divisor = i + 1
            if currentNumber % divisor > 0:
                divisibleByAll = False
                break
        else:
            return currentNumber
        currentNumber += rangeTotal

def main():
    return divisibleByRange(20)

if __name__ == '__main__':
    main()