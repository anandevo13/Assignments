"""
Q. Python script to check nature of roots of a given quadratic equation.
"""

print("Equation: ax^2 + bx +c")

a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

d = b**2 - 4*a*c
d1 = d**0.5
if (d<0):
    print("The roots are imaginary")
else:
    r1 = (-b + d1)/2*a
    r2 = (-b - d1)/2*a
    print("The first root: ", round(r1,2))
    print("The second root: ", round(r2,2))