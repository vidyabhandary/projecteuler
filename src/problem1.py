# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:07:23 2019

@author: Vidya

Solution to Project Euler problem 1
https://projecteuler.net/problem=1

Problem Statement :
    
>>>>>>>>>>>         
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
>>>>>>>>>>>     

Assumptions : 

1. The max value entered is an integer
    
2. Multiples required of do not change - (In this case 3 & 5)
Else will need variables for 

2a. How many multiples to consider - (In this case - 2 ( 3 & 5 ))
2b. Which multiples ( In this case (3 & 5))
2c. Accordingly the logic for deciding on multiples will change

Result : 
Expected Answer for 1000 - 233168

"""


def sum_multiples(max):
    sum = 0
    for x in range(int(max)):
        if ((x % 3) == 0) or ((x % 5) == 0):
            sum += x

    print('Sum of mutiples of 3 and 5 upto {0} is {1}'.format(max, sum))


max = input('Please enter max value upto which to sum multiples of 3 and 5 : ')
sum_multiples(max)
