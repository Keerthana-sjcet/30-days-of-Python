'''
NAME:Nandhakumar KS
DATE:20-12-2024
Write a program to check if a number is an Armstrong number or not
Write a program to find roots of a quadratic equation .
'''

#program to check if a number is an armstrong or not
number = int(input("Enter a number:"))
armstrong = number
sum = 0
while number>0:
    r = number%10
    number = number//10
    sum = sum+r*r*r
if sum == armstrong:
    print("The given number is armstrong.")
else:
    print("The number is not armstrong.")

#program to find roots of a quadratic equation
import math
a = input("Enter a number:")
b = input("Enter a number:")
c = input("Enter a number:")
d = b*b - 4*a*c
if d ==0:
    root1 = -b/(2*a)
    root2 = root1
    print("Roots are real and equal.")
    print("root 2 and root 1 are",root2 and root1)
elif d>0:
    root1 =(-b+math.sqrt(d)/(2*a))
    root2 =(-b-math.sqrt(d)/(2*a))
    print("roots are unequal and distinct.")
    print("root 1 and root 2 are ",root1 and root2)
else:
    print("roots are complex and imaginary.")