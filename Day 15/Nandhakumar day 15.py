'''
NAME: Nandhakumar KS
DATE: 20-12-2024
Find the second and third number from a list containing Random numbers,
write a program to print first half of a list
'''

#to find the second and third number from a list containing random numbers
list = []
list_size = int(input("Enter a the size of list:"))
for i in range (list_size):
    list.append(int(input()))
print(list[1:3])
#program to print first half of a list
list = []
list_size = int(input("Enter a the size of list:"))
for i in range (list_size):
    list.append(int(input()))
print(list[0:int(len(list)/2)])