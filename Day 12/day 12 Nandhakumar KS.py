'''
NAME:Nandhakumar KS
DATE:21-11-2024
To print a python pattern using numbers.
'''

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(rows,0,-1):
        print(j,end=" ")
    print()

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
