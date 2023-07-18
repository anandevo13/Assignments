"""
Q. Write a python script to print squares of numbers from a to b. Values of a and b are given by user.
"""

a = int(input("enter the number: "))
b = int(input("enter the number: "))

def printValues():
    l = []
    for i in range(a, b+1):
        l.append(i**2)
        print(l)

printValues()    