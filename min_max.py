"""This file contains the function for minimum value in a list"""

def find_minimum(values):
    current_min = float('+inf')
    for value in values:
        if value < current_min:
            current_min = value
    return current_min

def find_maximum(values):
    current_max = float('-inf')
    for value in values:
        if value > current_max:
            current_max = value
    return current_max

values = [1, -3, 2, 0 , 5]
print(find_minimum(values))
print(find_maximum(values))
