'''
NAME:Nandhakumar KS
DATE:20-12-2024
Write a recursive function to find the nth fibonacci number.
'''

def fibonacci(n):
    first_number = 1
    second_number = 0
    count = 0

    while count < n:
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number

        count += 1

    print(second_number, end=" ")


print(fibonacci(10))