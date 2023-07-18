"""
Q. Python script to calculate area of circle, radius is taken from user
"""

r = float(input("Enter the value of r: "))
PI = 3.14
area = PI*(r*r)
print(area)

# Another method

from math import pi

r = float(input("Input the radius of circle: "))
print("The area of the circle with radius" + "" + str(r) + "is:" + str(pi*r**2))

