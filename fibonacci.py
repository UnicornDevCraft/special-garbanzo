"""This file contains the function to  calculate the Fibonacci sequence"""
# My approach with for loop
def fibonacci(num):
    sequence = []
    if num <= 1: 
        sequence = [num]
    else:
        for n in range(num):
            if n <= 1:
                num_to_add = n
            else:
                num_to_add = sequence[n-1] + sequence[n-2]
            sequence.append(num_to_add)
    return sequence

# Example approach
def fibonacci_1(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


# Approach recursion
def fibonacci_2(num):
    sequence = []
    if num <= 1:
        return [num]
    if num == 2:
        return [0, 1]
    else:
        sequence = fibonacci_2(num - 1)
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
num = 9
print(fibonacci(num))
print(fibonacci_2(num))