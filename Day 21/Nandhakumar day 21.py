'''
NAME: Nandhakumar KS
DATE : 20-12-2024
Write a recursive function to calculate a number raised to a value.
'''

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
print(power(2,3))