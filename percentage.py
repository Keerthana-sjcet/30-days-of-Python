'''
NAME:Nandhakumar KS
DATE:8-11-2024
To write a python program to determine the percentage of marks secured by
the student in a specific subject out of 50.The user should input the subject and marks secured.
'''

Student_name = input("Enter Student Name: ")
Subject_name = input("Enter Subject Name: ")
Marks_obtained = int(input("Enter Marks Obtained: "))
Percentage = (Marks_obtained/50)*100
print("the percentage of marks obtained by",Student_name,"in",Subject_name,"is",Percentage,"%")