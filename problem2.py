# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:01:10 2019

@author: Vidya

Solution to Project Euler problem 2
https://projecteuler.net/problem=2

Problem Statement :

>>>>>>>>>>> 
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
>>>>>>>>>>>

Assumptions : 

1. The max value entered is an integer

Result : 
Expected Answer for 4000000 - 4613732

"""

fib_array = {0:0, 1:1}

def fib(n):
    if n not in fib_array:
        fib_array[n] = fib(n-1) + fib(n-2)
    return fib_array[n]

def sum_even_fibonnaci(max):
    sum_even = 0
    x = 0
    
    while True:
        fib_value = fib(x)  
        if (fib_value <= max):
            if (fib_value % 2) == 0:
                sum_even += fib_value
            x += 1
        else:
            break
    print('Sum of even fibonnaci numbers upto {0} is {1}'.format(max, sum_even))

max = int(input('Please enter max value upto which to sum even fibonacci numbers : ').strip())
sum_even_fibonnaci(max)
