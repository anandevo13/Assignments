"""
Q. Python script to find greatest among three numbers
"""

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
num3 = float(input("enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num3) and (num2 >= num1):
    largest = num2
else: 
    largest = num3