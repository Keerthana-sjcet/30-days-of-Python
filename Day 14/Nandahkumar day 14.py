'''
NAME:Nandhakumar KS
DATE:2-12-2024
Write a program in python to check if there are multiple maximum elements in a tuple or not,Program to
check if a tuple contains duplicate elements or not,Program to get the index of the least number from a tuple
'''

#program in python to check multiple maximum elements in a tuple
tuple =(1,2,2,3,4,5,5,8,3,6)
if tuple.count(max(tuple)) == 1:
    print("The tuple contains multiple maximum elements.")
else:
    print("The tuple does not contain multiple maximum element.")

#program to check if tuple contains duplicate elements
tuple =(1,2,2,3,4,5,5,8,3,6)
set = set(tuple)
if len(tuple) == len(set) :
    print("Tuple does not contain duplicate elements.")
else:
    print("Tuple contains duplicate elements.")
#program to get the index of the least number from a tuple
tuple =(2,2,3,4,1,5,8,3,6)
print(tuple.index(min(tuple)))