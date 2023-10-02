"""
* Name: David Ng
* Date: 1/15/2023
* CSE 160, Winter 2023
* Homework 1
* Description: Homework #1 Assignment
"""

# Uncomment the line below to make the math.sqrt function available
import math

# Problem 1
# This program uses the quadratic formula to solve for roots
# float values for decimal roots
a = float(3)
b = float(-5.86)
c = float(2.5408)
x_1 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)   # plus sign quadratic formula
x_2 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)   # minus sign quadratic formula
print("Problem 1 solution follows:")
print("Root 1:", x_1)   # root 1 answer
print("Root 2:", x_2)   # root 2 answer
print()

# Problem 2
# This program uses a for loop to list all reciprocal from 1 to 10
print("Problem 2 solution follows:")
for i in range(2, 11):  # this for loop executes the ranges 1 to 10
    r = float(1/i)  # changed this to divided 1/i to find decimal
    print('1/' + str(i) + ':', r)
print()

# Problem 3
# This program finds the triangular number of 10
print("Problem 3 solution follows:")

# Provided partially-working solution to problem 3
# `...` are placeholders and should be replaced
n = 10
triangular = 0
for i in range(1, n + 1):  # range of 1 to number + 1
    triangular = int(n * (n + 1)/2)  # the triangular formula by integer
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n * (n + 1) / 2)
print()

# Problem 4
# This program solves the factorial of the number 10
print("Problem 4 solution follows:")
f = 1
n = 10
for i in range(1, n + 1):  # this for loop adds 1 everytime the loop restarts
    f = f * i  # equation for factorial
print(str(n) + "!:", f)  # prints the factorial of 10 with answer "f"
print()
# Problem 5
# This program finds the factorial of numbers one to ten based on num_lines
print("Problem 5 solution follows:")
num_lines = 10
for i in range(num_lines, 0, - 1):  # for loop to countdown from 10 to 1
    f = 1
    for j in range(1, i + 1):  # for loop to find factorials 1 to 10
        f = f * j
    print(str(i) + "!:", f)  # print statement, convert int to str
print()
# Problem 6
# This program finds the value of "e"
print("Problem 6 solution follows:")
num_lines = 10
f = 0
r = 0
e = 1
for i in range(num_lines, 0, - 1):  # for loop to countdown from 10 to 1
    f = 1
    for j in range(1, i + 1):  # for loop to find factorials 1 to 10
        f = f * j
    r = float(1/f)  # reciporcal is equal to the float value of 1/factorial
    e = e + r  # e is then equal to value of e plus the reciprocal
print("e:", e)  # print statement to print final results of "e"
print()
