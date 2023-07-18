"""
Q. Python script to create a list of squares of first N natural numbers. Use for loop to fill list with 
elements. Value of N is taken from user.
"""

N = int(input("enter any number: "))
square = [i**2 for i in range(1,N+1)]
print(square)