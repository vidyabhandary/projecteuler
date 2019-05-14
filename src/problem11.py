# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:36:54 2019

@author: Vidya

Solution to Project Euler problem 11
https://projecteuler.net/problem=11

Problem Statement :
    
>>>>>>>>>>>  Largest product in a grid

In the 20×20 grid below, four numbers along a diagonal line have been 
marked in red. [Not displaying the grid here]
The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the 
same direction (up, down, left, right, or diagonally) in the 20×20 grid?

>>>>>>>>>>>  

Result : 

Expected Answer - 70600674

Assumptions / Notes : 
    
    1. Reading the grid from a file 'euler11.txt'
    2. To avoid duplication - only the following directions are considered
        a. Right 4 digits
        b. Vertically down
        c. Diagonal Left
        d. Diagonal Right
    For a product the order of the numbers does not matter. 
    From the sample grid - the diagonal product
    26 * 63 * 78 * 14 will be done for the number 26 so we do not have to repeat
    the same for the number 14.

"""

# Read grid from file


def read_grid(filename):

    array = []

    with open(filename, 'r') as file:
        for line in file:
            nums = line.split()
            numbers = [int(n) for n in nums]
            array.append(numbers)

    return array, len(array), len(array[0])


if __name__ == '__main__':

    # Read grid from file
    filename = 'euler11.txt'
    grid, height, width = read_grid(filename)

    # Four numbers are used to get the product computation
    window = 4

    width_range_end = width - window + 1
    height_range_end = height - window + 1

    max_product = 0

    for row in range(height):
        for col in range(width):

            # Right 4 digits
            if col < width_range_end:
                prod = grid[row][col] * grid[row][col + 1] * \
                    grid[row][col + 2] * grid[row][col+3]
                if prod > max_product:
                    max_product = prod

            # Vertically down
            if row < height_range_end:

                prod = grid[row][col] * grid[row+1][col] * \
                    grid[row+2][col] * grid[row+3][col]

                if prod > max_product:
                    max_product = prod

                # Diagonal Right
                if col < width_range_end:

                    prod = grid[row][col] * grid[row+1][col+1] * \
                        grid[row+2][col+2] * grid[row+3][col+3]
                    if prod > max_product:
                        max_product = prod

                # Diagonal Left
                if col >= window - 1:
                    prod = grid[row][col] * grid[row+1][col-1] * \
                        grid[row+2][col-2] * grid[row+3][col-3]
                    if prod > max_product:
                        max_product = prod

    print('Maximum product is ', max_product)
