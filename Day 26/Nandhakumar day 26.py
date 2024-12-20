'''
NAME:Nandhakumar KS
DATE:20-12-2024
Sum of even and odd digits of a number 12345678.
'''
list = [1,2,3,4,5,6,7,8]
even_list =[]
odd_list = []
for numbers in list:
    if numbers % 2 ==0:
        even_list.append(numbers)
    else:
        odd_list.append(numbers)
sum_of_even_number = 0
for numbers in even_list:
    sum_of_even_number += numbers
print("The sum of even numbers is",sum_of_even_number)
sum_of_odd_number = 0
for numbers in odd_list:
    sum_of_odd_number += numbers
print("The sum of odd numbers is",sum_of_odd_number)