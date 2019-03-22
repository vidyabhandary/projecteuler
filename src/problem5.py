# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:16:56 2019

@author: Vidya

Solution to Project Euler problem 5
https://projecteuler.net/problem=5

Problem Statement :
    
>>>>>>>>>>> Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by 
all of the numbers from 1 to 20?

>>>>>>>>>>>

Result : 
Expected Answer - 232792560

Assumptions / Limitations : 

1. Solution obtained without use of numpy or Math library
2. Using the prime factorization method and not the Euler's LCM, GCD Method

Notes - 
The prime factors for the numbers between 1 and 10,
we get -- 1*2*2*2*3*3*5*7, which happens to be 2520, just as expected.

Prime factors for numbers between 1 and 20,
we get -- 1*2*2*2*2*3*3*5*7*11*13*17*19

"""

# Check if a number is prime


def is_prime(number):

    if number < 2:
        return False

    for i in range(2, number + 1):
        # Can use the math.sqrt function
        if i * i > number:
            break

        if number % i == 0:
            return False

    return True

# Get prime factors of a number - repetition allowed


def get_factors(number):
    factors = []
    mod_number = number

    if number == 0 or number == 1:
        return [number]

    i = 2
    # Use the reducing method to get the prime factors
    while not(mod_number in (0, 1) or i >= number):

        if is_prime(i):
            if mod_number % i == 0:
                factors.append(i)
                mod_number = mod_number // i
                i = 2
            else:
                i += 1
        else:
            i += 1

    if not factors:
        factors.append(number)

    return factors

# Count the multiples of each prime factor


def count_primes(factors):
    prime_count = {}
    for i in factors:
        prime_count[i] = factors.count(i)

    return prime_count


def count_all_factors(num_limit):

    all_factors = []
    max_of_factors = {}

    # Get prime factors for all numbers, count multiples of each prime factor
    # for a number and finally get the aggregate count for each prime factor
    # for all numbers till num_limit
    for i in range(2, num_limit + 1):

        # Get all prime factors of i
        factors = get_factors(i)

        all_factors += factors

        # Get count of the multiples for each prime factor
        count_for_prime = count_primes(factors)

        # If max count for a prime factor is less than the stored max count for
        # the same prime number update the number to reflect the new maximum
        # count - else store the number
        # In essence this count will lead to being able to determine LCM
        for key, value in count_for_prime.items():
            if max_of_factors.get(key):
                if max_of_factors.get(key) < value:
                    max_of_factors[key] = value
            else:
                max_of_factors[key] = value

    return all_factors, max_of_factors

# Based on the count of each prime number upto the number limit -
# retain that prime factor for that many counts - these are the LCM factors


def lcm_factors(all_numbers, max_primes):

    for key, value in max_primes.items():

        # Every prime factor of every number till num_limit
        count_all = all_numbers.count(key)

        # If count of prime factor is not equal to max count for that prime
        # factor
        if count_all != value:
            # Count is greater than max allowed for that prime factor
            if count_all > value:
                for i in range(count_all - value):
                    all_numbers.remove(key)
            # Count is lesser than max allowed for that prime factor
            else:
                for i in range(count_all - value):
                    all_numbers.append(key)

    return all_numbers

# Get the count of the prime factors, create list of these factors and multiply
# to give the LCM or smallest positive number divisible by the range of numbers


def lcm(max_number):
    all_factors, max_of_factors = count_all_factors(max_number)
    lcm_numbers = lcm_factors(all_factors, max_of_factors)

    # Get LCM
    lcm = 1
    for num in lcm_numbers:
        lcm *= num

    return lcm


if __name__ == '__main__':

    num_limit = 20

    # Expected answer - 232792560
    print(f'The smallest positive number that is evenly divisible by numbers from 1 to {num_limit} ', lcm(
        num_limit))
