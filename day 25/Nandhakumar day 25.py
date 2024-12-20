'''
NAME:Nandhakumar KS
DATE:20-12-2024
recursive function to Count how many times a specific value appears in a list.
'''

list = []
list_size = int(input("Enter the size of list:"))
for i in range (list_size):
    list.append(int(input()))
print(list)
value = int(input("Enter a number in the given list:"))
print(list.count(value))