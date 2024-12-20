'''
NAME: Nandhakumar KS
DATE: 20-12-2024
Write a program to find the longest string in a list of strings
'''

list=['python','java','c++','c']
longest_string=list[0]
for string in list:
    if len(string)>len(longest_string):
        longest_string = string
print("The longest string is", longest_string)