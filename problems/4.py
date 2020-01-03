# A palindromic number reads the same both ways. The largest palindrome made from the prodect of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Check if palindrome
    # Convert int to string
    # Create copy of string, reversed
    # String compare

maxPalindrome = 0
for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        product = str(x * y)
        tcudorp = product[::-1]
        if product == tcudorp:
            maxPalindrome = max(maxPalindrome, x*y)

print(maxPalindrome)