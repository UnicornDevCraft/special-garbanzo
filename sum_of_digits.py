"""This file contains the code for summmarize the digits with no sum() usage"""
from functools import reduce

# My solution to avoid loop
def sum_of_digits(digits):
    """
    Args:
    digits - a list of integers
    Returns:
    result - an integer
    """
    result = reduce(lambda x, y: x + y, digits)
    return result

# Solution with the for loop
def sum_with_for(digits):
    sum_so_far = 0
    for digit in digits:
        sum_so_far += digit
    return sum_so_far


digits = [1, 2, 3, 4, 5, 6]
print(sum_of_digits(digits))
print(sum_with_for(digits))