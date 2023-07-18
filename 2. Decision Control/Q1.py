"""
Q. Python script to check whether a given number is even or odd.
"""

num = int(input("enter a number: "))

if (num % 2) == 0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))