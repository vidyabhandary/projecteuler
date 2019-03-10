# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:38:03 2019

@author: Vidya

Solution to Project Euler problem 4
https://projecteuler.net/problem=4

Problem Statement :
    
>>>>>>>>>>> 

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

>>>>>>>>>>>

Assumptions  / Limitations : 
    
1. The largest palindrome will be a product between the numbers 900 - 1000


Result : 
Expected Answer - 906609 = 913*993

"""


def isPalindrome(snumber):
    return snumber == snumber[::-1]


max_palindrome_multiple = 0

for x in range(999, 899, -1):
    # To avoid double counting - start at x
    for y in range(x, 899, -1):
        multiple = x * y

        if isPalindrome(str(multiple)):

            if multiple > max_palindrome_multiple:
                x_at_max_palindrome = x
                y_at_max_palindrome = y
                max_palindrome_multiple = multiple

print('Largest Palindrome of product of two 3-digit numbers ',
      max_palindrome_multiple)
print('x ', x_at_max_palindrome)
print('y ', y_at_max_palindrome)
