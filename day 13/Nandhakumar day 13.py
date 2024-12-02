'''
NAME:Nandhakumar KS
DATE:31-11-2024
Write a Python program to find the maximum common element between two lists.
'''

list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
list3 = []
for i in list1:
    if i in list2:
        list3.append(i)
print(max(list3))