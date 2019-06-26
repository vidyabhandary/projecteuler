# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:21:51 2019

@author: Vidya

Solution to Project Euler problem 13
https://projecteuler.net/problem=13

Problem Statement :
    
>>>>>>>>>>>  Large sum

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(Each line is a 50 digit number)

<< First few 50 digit numbers only shown here >>
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331

>>>>>>>>>>>  

Result : 
    
Expected Answer - 5537376230

Notes : 
    
    1. Reading the 100 - 50 digit numbers from a file named 'largesum.txt'

References :

From the link - 
https://docs.python.org/3/c-api/long.html#integer-objects

All integers are implemented as “long” integer objects of arbitrary size.

And hence there is no need to store the required sum in a special number type 
for big numbers. (Hard limit of memory accessible to python is applicable)
We do the regular addition and retrieve the first 10 digits.

"""
import time


def read_numbers(filename):
    array_of_nums = []

    with open(filename, 'r') as file:

        # Each line is a 50 digit number
        for line in file:
            num = int(line)
            array_of_nums.append(num)

    return array_of_nums


if __name__ == '__main__':

    filename = 'largesum.txt'
    start_time = time.time()

    large_nums = read_numbers(filename)

    # Retrieve the first 10 digits of the sum of the 100 - 50 digit numbers
    large_sum_10_digits = str(sum(large_nums))[:10]

    total_time = time.time() - start_time

    print(
        f'Frist 10 digits of the sum of 100 50 digit numbers given - {large_sum_10_digits}')
    print('Time taken ', total_time)
