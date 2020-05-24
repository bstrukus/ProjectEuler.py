#!/usr/bin/env python3
from .context import euler

solveExample = True
solveProblem = False

#EXAMPLE ANSWERS
#1.) 23
#2.) 10
#3.) 29
#4.) 9009
#5.) 2520
#6.) 2640
#7.) 13
#8.) 5832
#9.) 60

#PROBLEM ANSWERS
#1.) 2318
#2.) 4613732
#3.) 6857
#4.) 906609
#5.) 232792560
#6.) 25164150
#7.) 104743
#8.) 23514624000
#9.) 31875000

def test_problem1example():
    problem = euler.problems.Ex1()
    assert problem.run(solveExample) == 23

def test_problem1question():
    problem = euler.problems.Ex1()
    assert problem.run(solveProblem) == 2318

def test_problem2example():
    problem = euler.problems.Ex2()
    assert problem.run(solveExample) == 10

def test_problem2question():
    problem = euler.problems.Ex2()
    assert problem.run(solveProblem) == 4613732

def test_problem3example():
    problem = euler.problems.Ex3()
    assert problem.run(solveExample) == 29

def test_problem3question():
    problem = euler.problems.Ex3()
    assert problem.run(solveProblem) == 6857

def test_problem4example():
    problem = euler.problems.Ex4()
    assert problem.run(solveExample) == 9009

def test_problem4question():
    problem = euler.problems.Ex4()
    assert problem.run(solveProblem) == 906609

def test_problem5example():
    problem = euler.problems.Ex5()
    assert problem.run(solveExample) == 2520

def test_problem5question():
    problem = euler.problems.Ex5()
    assert problem.run(solveProblem) == 232792560

def test_problem6example():
    problem = euler.problems.Ex6()
    assert problem.run(solveExample) == 2640

def test_problem6question():
    problem = euler.problems.Ex6()
    assert problem.run(solveProblem) == 25164150

def test_problem7example():
    problem = euler.problems.Ex7()
    assert problem.run(solveExample) == 13

def test_problem7question():
    problem = euler.problems.Ex7()
    assert problem.run(solveProblem) == 104743

def test_problem8example():
    problem = euler.problems.Ex8()
    assert problem.run(solveExample) == 5832

def test_problem8question():
    problem = euler.problems.Ex8()
    assert problem.run(solveProblem) == 23514624000

def test_problem9example():
    problem = euler.problems.Ex9()
    assert problem.run(solveExample) == 60

def test_problem9question():
    problem = euler.problems.Ex9()
    assert problem.run(solveProblem) == 31875000