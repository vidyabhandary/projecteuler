# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:18:57 2019

@author: Vidya

Solution to Project Euler problem 10
https://projecteuler.net/problem=10

Problem Statement :

>>>>>>>>>>>  Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

>>>>>>>>>>>  

Result : 

Expected Answer - 142913828922

Notes - 

Referred to the following links 

1. https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

2. Very fast way to get primes using sieve of erastosthenes, python set 
and python generator

http://rosettacode.org/wiki/Sieve_of_Eratosthenes#Using_set_lookup

3. 
https://codereview.stackexchange.com/questions/132343/project-euler-10-find-the-sum-of-all-the-primes-below-two-million

"""
import time


def erastosthenes(limit):

    # This set will contain the multiples of prime numbers
    multiples = set()

    # Iterate through 2 - 2000000
    for i in range(2, limit + 1):

        # If i has not been eliminated already
        if i not in multiples:

            # Prime number
            yield i

            # Add multiples of the prime in the range to the multiples set
            # Step will be i -> The prime whose multiples we will find
            multiples.update(range(i * i, limit + 1, i))


# Use the division method to get the primes

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

# Use the division method to get the primes and then sum them


def sumPrime(limit):

    if limit <= 1:
        return 0

    if limit == 2:
        return 2

    primeNum = 1
    i = 3
    sumOfPrimes = 2

    while i <= limit:
        primeNum += 2

        if isPrime(primeNum):
            sumOfPrimes += primeNum

        i += 2

    return sumOfPrimes


if __name__ == '__main__':

    limit = 2000000

    start_time = time.time()
    print(sum(erastosthenes(limit)))

    set_approach_time = time.time() - start_time

    # Takes about ~ 0.7 seconds using sets, generators and sieve of erastosthenes
    print('Time taken for the set approach - ', set_approach_time)

    start_time_2 = time.time()

    print(sumPrime(limit))

    trial_division_time = time.time() - start_time_2

    # It takes ~ 17 seconds for the trial division method !!!
    print('Time taken for the division approach  ', trial_division_time)

    # Shows ~ 17 seconds
    print('Time difference between both approaches is ',
          trial_division_time - set_approach_time)
