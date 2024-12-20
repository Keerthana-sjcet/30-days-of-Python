'''
NAME : Nandhakumar KS
DATE: 20-12-2024
Program to print fibonacci series
'''

N = int(input("Enter a number:"))
first_term = 0
second_term = 1
print(first_term,second_term,end=" ")
for i in range(2,N):
    next_term = first_term + second_term
    print(next_term,end=" ")
    first_term = second_term
    second_term = next_term