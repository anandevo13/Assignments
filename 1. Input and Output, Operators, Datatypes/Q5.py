"""
Q. Write a python script to calculate area of triangle lengths of the sides are given by user 
"""

a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))

# Calculate the semi-perimeter
s = (a+b+c)/2

# Calculate the area
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)