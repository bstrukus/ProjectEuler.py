#!usr/bin/env python3

import sys
#import ex1
#from problem import Problem
from problems.problem import BaseProblem

class ImportProblem(BaseProblem):
    pass

def main():
    print(sys.path)
    temp = ImportProblem(1, 100)
    temp.run()

if __name__ == '__main__':
    print("Called directly")
    main()