# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:00:21 2019

@author: Vidya

Solution to Project Euler problem 15
https://projecteuler.net/problem=15

Problem Statement :
    
>>>>>>>>>>>  Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Result : 

Expected Answer - 137846528820

Notes :
    The problem can be solved in multiple ways - Some are mentioned below.
    
    1. Using recursion - it will grow exponentially and hence it is not a 
    suitable method.
    
    2. Using Pascal's triangle - Calculate the sum of paths at each node
    which is addition of paths at the previous nodes on top and left.
    https://en.wikipedia.org/wiki/Pascal%27s_triangle
    
    [Pascal's triangle overlaid on a grid gives the number of distinct 
    paths to each square, assuming only rightward and downward movements 
    are considered.]
    
    3. Using the binomial coefficient formula (Combinatorics)
    
  	N-choose-k : (n! / (k! * (n-k)!) - the binomial coefficient formula
	Where:
		n is the total number of moves - for grid of 20 = 20 + 20
		k is the number of down and right moves required (20 each)     

"""
import time
import math

# Recursive method - not recommended
# For a lattice[15, 15] it took 176.7086205482483 = 2 min
# For a lattice[16, 16] it took 692.3842837810516 = 11 min


def recurPath(lattice):
    total_paths = 0

    # Base Case - Reached the end of the path
    if lattice == [0, 0]:
        return 1

    if lattice[1] > 0:
        total_paths += recurPath([lattice[0], lattice[1] - 1])

    if lattice[0] > 0:
        total_paths += recurPath([lattice[0] - 1, lattice[1]])

    return total_paths

# Pascal triangle method


def pascalPath(lattice_size):
    pascal_path = {}

    # Initialize starting points to 1
    for x in range(lattice_size, -1, -1):
        pascal_path[(x, lattice_size)] = 1
        pascal_path[(lattice_size, x)] = 1

    # Now consecutively sum paths from the left node and top node

    start_point = lattice_size - 1
    for j in range(start_point, -1, -1):
        for k in range(start_point, -1, -1):
            pascal_path[(j, k)] = pascal_path[j + 1, k] + pascal_path[j, k + 1]

    return pascal_path[(0, 0)]

# Binomial Coefficient method


def binomialPath(n, k):

    total_paths = math.factorial(
        n) / (math.factorial(k) * math.factorial(n - k))
    return int(total_paths)


if __name__ == '__main__':

    # Using recursive method for a lattice of 15
    lattice = [14, 14]

    start_time = time.time()

    r_paths = recurPath(lattice)
    print('\n--- Calculating total paths using recursion ---')
    print('Total number of paths for a lattice of size ',
          lattice[0], 'is', r_paths)
    print('Total time for recursive method ', time.time() - start_time)

    # Using Pascal triangle method
    start_time = time.time()

    lattice_size = 20
    p_paths = pascalPath(lattice_size)
    print('\n--- Calculating total paths using Pascal triangle method ---')
    print('Total number of paths for a lattice of size ',  'is', p_paths)
    print('Total time for Pascal triangle method ', time.time() - start_time)

    # Binomial coefficient method
    # For grid of 20 - n = 20 + 20 and k = 20
    start_time = time.time()
    b_paths = binomialPath(40, 20)
    print('\n--- Calculating total paths using Binomial coefficient method---')
    print('Total number of paths for a lattice of size ',  'is', b_paths)
    print('Total time for Binomial coefficient method ', time.time() - start_time)
