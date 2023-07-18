"""
Q. Python script to calculate product of first N odd natural numbers. Value of N is taken from user
"""

n = int(input("enter the value of n: "))

product = 1

for i in range(1, n+1):
    product = product*(2*i-i)
print(product)