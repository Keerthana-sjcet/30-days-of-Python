'''
NAME:Nandhakumar KS
DATE:21-11-2024
Python program for day 7.
'''

#1
x = 0
y = 10
while x < 5 and y < 5:
    print(x)
    print(y)
    x += 1
    y -= 1
#2
sum = 0
i = 1
while i <= 10:
    sum += i**2
    i += 1
print(sum)
#3
base = 2
number = 3
result = 1
while number > 0:
    result *= base
    number -= 1
print(result)