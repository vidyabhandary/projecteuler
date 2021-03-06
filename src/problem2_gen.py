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

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.
>>>>>>>>>>>

Assumptions : 

1. The max value entered is an integer

Result : 
Expected Answer for 4000000 - 4613732

############## Timing info

Added code to time summing of even fibonacci numbers using array and
generator

Found that using a generator was faster 

problem2_array.py
Sum of even fibonnaci numbers upto 10 is 10
--- 2.6695196628570557 seconds ---

problem2_array.py
Sum of even fibonnaci numbers upto 4000000 is 4613732
--- 1.6634728908538818 seconds ---

>>>>

problem2_gen.py
Sum of even fibonnaci numbers upto 10 is 10
--- 2.9260706901550293 seconds ---

problem2_gen.py
Sum of even fibonnaci numbers upto 4000000 is 4613732
--- 1.3737201690673828 seconds ---

"""
import time

# Check the time taken for fibonacci using generator
start_time = time.time()


def fibonacci():
    current_num, next_num = 0, 1
    while True:
        current_num, next_num = next_num, current_num + next_num
        yield current_num


def sum_even_fibonnaci_gen(max):
    sum_even = 0
    fib_gen = fibonacci()
    fib_value = fib_gen.__next__()

    while (fib_value <= max):
        if (fib_value % 2) == 0:
            sum_even += fib_value

        fib_value = fib_gen.__next__()
    print('Sum of even fibonnaci numbers upto {0} is {1}'.format(
        max, sum_even))


max = int(input(
    'Please enter max value upto which to sum even fibonacci numbers : ').strip())

sum_even_fibonnaci_gen(max)

print("--- %s seconds ---" % (time.time() - start_time))
