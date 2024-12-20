'''
Name:Nandhakumar KS
DATE:20-12-2024
Write a recursive function to find the sum of all elements in a list.
'''

def sum(list):
    if list==[ ]:
        return 0
    else:
        return list[0]+sum(list[1:])
list=[]
list_size = int(input("Enter the size of list:"))
for i in range (list_size):
    list.append(input())
result = sum(list)
print(result)