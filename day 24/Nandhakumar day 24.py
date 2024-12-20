'''
NAME:Nandhakumar KS
DATE:20-12-2024
Write a recursive function to reverse a given string.
'''


def reverse_string(str):
    if len(str) == 0:
        return str
    else:
        return reverse_string(str[1:]) + str[0]


str = "hello python"
print(reverse_string(str))