'''
NAME: Nandhakumar KS
DATE: 20-12-2024
1. A program that takes a list of strings as input and returns a new list with all the strings in uppercase.
2. A program that prints all the multiples of a given number.
'''

#program that takes a list of strings as input and returns a new list with all the strings in uppercase
list = []
list_size = int(input("Enter the size of list:"))
for i in range (list_size):
    list.append(input())
print(list)
uppercase_list=[]
for j in list:
    A = j.upper()
    uppercase_list.append(A)
print(uppercase_list)
#program that prints all the multiples of a given number
number = int(input("Enter a number:"))
limit = int(input("Enter a limit:"))
for i in range(1,(limit//number)+1):
    print(number*i)