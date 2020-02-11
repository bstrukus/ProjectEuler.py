#!/usr/bin/env python3
# A palindromic number reads the same both ways. The largest palindrome made from the prodect of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

exampleValue = 2
problemValue = 3

mainValue = problemValue

def digitsToNum(digitCount):
    if digitCount <= 0:
        return 0
    return int(digitCount * '9')

def findPalindromicNumber(digitCount):
    maxVal, minVal = digitsToNum(digitCount), digitsToNum(digitCount - 1)

    #print(f'Min = {minVal}, max = {maxVal}')

    #products = [0, 0]
    maxPalindrome = 0

    for x in range(maxVal, minVal, -1):
        for y in range(maxVal, minVal, -1):
            product = x * y
            productStr = str(product)
            reverseStr = productStr[::-1]
            if productStr == reverseStr and maxPalindrome < product:
                #products[0] = x
                #products[1] = y
                maxPalindrome = product

    #print(f'4.) {maxPalindrome} from {products[0]} * {products[1]}')
    return maxPalindrome

def main():
    return findPalindromicNumber(mainValue)

if __name__ == '__main__':
    main()