#!usr/bin/env python3

exampleIndex = 0
problemIndex = 0

problemValues = {
    "1" : (10, 100), 
    "2" : (10, 4000000), 
    "3" : (13195, 600851475143), 
    "4" : (2, 3),
    "5" : (10, 20),
    "6" : (10, 100),
    "7" : (6, 10001)
}

def getExampleValue(problemNumber):
    return problemValues[problemNumber](exampleIndex)

def getProblemValue(problemNumber):
    return problemValues[problemNumber](problemIndex)