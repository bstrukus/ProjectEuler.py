#!/usr/bin/env python3

# Run all the exercise solutions!
import sys
import euler

def validate_input(inputValue):
    try:
        temp = int(sys.argv[1])
        return temp
    except ValueError:
        print('What was passed is not a number, running all problems.')
        return None

def main():
    if len(sys.argv) == 1:
        euler.run()
    elif len(sys.argv) == 2:
        problemNumber = validate_input(sys.argv[1])
        euler.run(problemNumber)
    else:
        print(f'Not sure what you wanted me to do with these {len(sys.argv)} arguments...')
        print('    Arguments: ', str(sys.argv))

if __name__ == '__main__':
    main()