'''
NAME:Nandhakumar KS
DATE:21-11-2024
Write a python program to ask the user for radius and find the volume of the sphere.
Write a python program to ask the user for side length and find perimeter of rectangle.
Write a python program to ask the user for any year and check if it is a leap year or not.
'''
import math
radius = int(input ('Enter radius of sphere: '))
volume = math.pi*radius*radius*radius*4/3
print ('The volume of the sphere is: ',volume)
length = int(input('Enter the length of the rectangle: '))
breadth = int(input('Enter the breadth of the rectangle: '))
perimeter = 2*(breadth+length)
print ('The perimeter of the rectangle is: ',perimeter)
year = int(input('Enter the year: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The',year,'is a leap year')