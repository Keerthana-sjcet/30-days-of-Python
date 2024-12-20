'''
NAME:Nandhakumar KS
DATE:20-12-2024
Write a recursive function to find products of digits of a number
'''

def product_of_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) * product_of_digits(n // 10)

number = 1234
result = product_of_digits(number)
print("The product of the digits of", number, "is:", result)
