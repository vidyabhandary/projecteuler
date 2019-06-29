# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:04:02 2019

@author: Vidya

Solution to Project Euler problem 14
https://projecteuler.net/problem=14

Problem Statement :
    
>>>>>>>>>>>  Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is 
thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
    
Result : 

Expected Answer - 837799 with its chain counter = 525

"""

import time

collatz_seq = {1: 1}


def colatz_counter(number):
    ctr = 0
    collatz_number = number

    if collatz_number in collatz_seq.keys():
        ctr += collatz_seq[collatz_number]
        return ctr

    while number >= 1:

        if number in collatz_seq.keys():
            ctr += collatz_seq[number]
            collatz_seq[collatz_number] = ctr
            return ctr

        ctr += 1
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = int((3 * number) + 1)

    collatz_seq[collatz_number] = ctr
    return ctr


if __name__ == '__main__':

    start_time = time.time()

    max_limit = 1000000
    max_collatz_number = 1
    max_counter = 0

    for i in range(1, max_limit):

        counter = colatz_counter(i)

        if counter > max_counter:
            max_counter = counter
            max_collatz_number = i

    total_time = time.time() - start_time
    print(
        f'\nThe number with the longest chain below {max_limit} is {max_collatz_number} with its counter as {max_counter}')
    print('Time taken ', total_time)
