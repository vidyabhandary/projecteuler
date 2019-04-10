# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:26:58 2019

@author: Vidya


Solution to Project Euler problem 9
https://projecteuler.net/problem=9

Problem Statement :
    
>>>>>>>>>>>  Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
    
>>>>>>>>>>>  

Result :
    
Expected Answer - 31875000
    200, 375, 425 whose sum is 1000

"""

import time


def is_pythagorean_triplet(x, y, z):
    return x**2 + y**2 == z**2

# The basic brute force approach


def pythagorean_basic_brute(limit):

    for a in range(1, limit + 1):
        for b in range(a, limit - a + 1):
            c = limit - a - b
            if c < b:
                break
            if is_pythagorean_triplet(a, b, c):
                print('Pythagorean triplet numbers are -- ', a, b, c)
                return a * b * c

# Brute force approach but limiting the number of loops using a < b < c


def pythagorean_brute(limit):

    # Since a < b < c
    a_limit = int(limit / 3)
    b_limit = int(limit / 2)

    for a in range(1, a_limit):
        for b in range(a, b_limit):
            c = limit - a - b
            if c < b:
                break
            if is_pythagorean_triplet(a, b, c):
                print('Pythagorean triplet numbers are -- ', a, b, c)
                return a * b * c


if __name__ == '__main__':

    start_time_basic = time.time()

    limit = 1000
    print('Basic brute force approach ')
    print('Product of the pythagorean triplet numbers is -- ',
          pythagorean_basic_brute(limit))

    end_time_basic = time.time()
    print('Time for basic brute force')
    print(end_time_basic - start_time_basic)

    start_time_brute = time.time()

    limit = 1000
    print('\nReduced brute force approach ')
    print('Product of the pythagorean triplet numbers is -- ',
          pythagorean_brute(limit))

    end_time_brute = time.time()
    print('Time for reduced brute force')
    print(end_time_brute - start_time_brute)

    # Diff in time is 0.01 to 0.002 seconds between basic brute force and
    # reduced brute force for limit of 1000
