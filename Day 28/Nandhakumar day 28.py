'''
NAME:Nandhakumar KS
DATE:20-12-2024
Write a python program to rotate a list two positions to its right
'''

numbers = [1,2,3,4,5]
positions = 2
rotated_list = numbers[-positions:] + numbers[:-positions]
print("Original list:", numbers)
print("Rotated list:", rotated_list)
