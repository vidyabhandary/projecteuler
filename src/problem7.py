# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:35:00 2019

@author: Vidya

Solution to Project Euler problem 7
https://projecteuler.net/problem=7

Problem Statement :
    
>>>>>>>>>>>  10001st prime
    
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

>>>>>>>>>>>

Result : 

Expected Answer - 104743

Notes: Memory efficient in that we do not retain the first 10000 primes

"""
import time

# Check the time taken
start_time = time.time()


def isPrime(number):
    if number < 2:
        return False
    elif number == 2:
        return True

    for i in range(2, number + 1):
        if (i * i) > number:
            break

        if number % i == 0:
            return False

    return True


def getNthPrime(limit):

    if limit < 1:
        return 1

    if limit == 1:
        return 2

    primeNum = 1
    numberOfPrimes = 2

    while numberOfPrimes <= limit:
        primeNum += 2

        if isPrime(primeNum):
            numberOfPrimes += 1

    return primeNum


limitNum = 10001
print(f'{limitNum} prime is ', getNthPrime(limitNum))

print("--- %s seconds ---" % (time.time() - start_time))
