# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:47:02 2019

@author: Vidya

Solution to Project Euler problem 16
https://projecteuler.net/problem=16

Problem Statement :
    
>>>>>>>>>>>  Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

>>>>>>>>>>>  

Result : 
    
Expected Answer - 1366

Notes : 
    
    1. We use python's built in support for big numbers

References :

From the link - 
https://docs.python.org/3/c-api/long.html#integer-objects

All integers are implemented as “long” integer objects of arbitrary size.

And hence there is no need to store the required sum in a special number type 
for big numbers. (Hard limit of memory accessible to python is applicable)
We do the regular power multiplication sum the digits.

"""

import time


def sum_digits(number, exponent):
    exp_result = str(number**exponent)
    sum_result = sum([int(i) for i in exp_result])
    return sum_result


if __name__ == '__main__':

    number = 2
    power = 1000

    start_time = time.time()

    result = sum_digits(number, power)

    end_time = time.time() - start_time

    print('Sum of the digits of the number ', number,
          'to the power ', power, 'is ', result)

    print('Time taken is ', end_time)
