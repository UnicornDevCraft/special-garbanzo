"""This file contains  the function which defines if a word is a palindrome"""
# Using recursion
def is_palindrome(word):
    if len(word) == 1:
        return True
    if word[0] == word[-1]:
        is_palindrome(word[1:-1])
        return True
    else:
        return False

word = "car"
print(is_palindrome(word))

# Using list comprehensions
def is_palindrome_with_for(word):
    check = [True if word[i] == word[-1-i] else False for i in range(round(len(word)/2))]
    return all(check)

print(is_palindrome_with_for(word))
