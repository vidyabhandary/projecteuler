# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:04:45 2019

@author: Vidya

Solution to Project Euler problem 6
https://projecteuler.net/problem=6

Problem Statement :

>>>>>>>>>>> Sum square difference

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.

>>>>>>>>>>>

Result : 

Expected Answer - 25164150

"""
import time

# Check the time taken for brute force method
start_time = time.time()

n = 100

# Brute force method

sum_of_squares = 0
square_of_sum = 0

for i in range(n+1):
    square_of_sum += i
    sum_of_squares += (i*i)


square_of_sum *= square_of_sum

diff = square_of_sum - sum_of_squares

# Difference between sum of squares of first 100 natural numbers and
# the square of the sum

print('\nUsing Brute Force method ')
print(f'Sum of the squares of first {n} natural numbers --> {sum_of_squares}')
print(f'Square of the sum of first {n} natural numbers --> {square_of_sum}')
print(
    f'Difference between sum of squares of first {n} natural numbers and the square of the sum is {diff}')
print('-' * 25)

#print("--- %s seconds ---" % (time.time() - start_time))
# Brute force showed 0.0 seconds

# Use list comprehensions

s_squares = sum(i*i for i in range(1, n+1))
sq_sum = sum(i for i in range(1, n+1))

sq_sum *= sq_sum

diff = sq_sum - s_squares

print('\nUsing List Comprehension ')
print(f'Sum of the squares of first {n} natural numbers --> {s_squares}')
print(f'Square of the sum of first {n} natural numbers --> {sq_sum}')
print(
    f'Difference between sum of squares of first {n} natural numbers and the square of the sum is {diff}')

print('-' * 25)

# Use the math formulas
# Sum of natural numbers = n(n+1)/2
# Sum of squares of natural numbers = n(n+1)(2n+1)/6

m_sq_sum = (n * (n + 1)) / 2
m_sq_sum *= m_sq_sum

m_s_squares = (n * (n + 1) * (2 * n + 1)) / 6

diff = m_sq_sum - m_s_squares

print('\nUsing the math formula ')
print(f'Sum of the squares of first {n} natural numbers --> {m_s_squares}')
print(f'Square of the sum of first {n} natural numbers --> {m_sq_sum}')
print(
    f'Difference between sum of squares of first {n} natural numbers and the square of the sum is {diff}')

print("--- %s seconds ---" % (time.time() - start_time))
