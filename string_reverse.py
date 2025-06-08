"""This file contains the code to reverse a string exercise"""

# My solution
def string_reverse(string):
    return string[::-1]

# Book solution
def reverse_string(string):
    return "".join(reversed(list(string)))

print(string_reverse("something here is the whole"))
print(reverse_string("something here is the whole"))