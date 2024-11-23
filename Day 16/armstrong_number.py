"""
Author :Maria
Date:23/11/2024
Version:1.1
This is a python program to check whether if the number is Armstrong number or not.
"""
number=int(input("Enter a number"))
armstrong=number
sum=0
for i in range(number):
    r=number%10
    number=number//10
    sum=sum+r*r*r
if sum==armstrong:
    print("Number is armstrong")
else:
     print("Number is not armstrong")

