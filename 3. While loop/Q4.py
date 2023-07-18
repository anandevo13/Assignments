"""
Q. Python script to calculate sum of first N odd natural numbers. value of N is taken from user.
"""
n = int(input("enter the number: "))

def oddSum(n):
    sum = 0
    curr = 1
    i = 0
    while i < n:
        sum = sum + curr
        curr = curr + 2
        i = i + 1
    return sum    

print("Sum of first", n,"odd numbers is: ", oddSum(n))