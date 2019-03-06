# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:35:36 2019

@author: Vidya

Solution to Project Euler problem 3
https://projecteuler.net/problem=3

Problem Statement :

>>>>>>>>>>> 

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

>>>>>>>>>>>

Assumptions  / Limitations : 

1. The number entered whose largest prime factor is asked for is an integer
2. The integer is a positive integer
3. Returns 1 if the number entered is a prime number

Result : 
Expected Answer for 600851475143 - 6857

"""

def find_largest_prime_factor(number):
    divisor = 2
    largest_divisor = 1
    divisors_of_number = []
    
    while (divisor * divisor) <= number:
        if (number % divisor) == 0:
            divisors_of_number.append(divisor)
            number //= divisor
            largest_divisor = number
        else:
            divisor += 1 if divisor == 2 else 2
    divisors_of_number.append(largest_divisor)            
    return largest_divisor


number = int(input(
    'Please enter number whose largest prime factor is to be found : ').strip())

print(find_largest_prime_factor(number))

