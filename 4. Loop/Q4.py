"""
Q. Python script to check whether two given numbers are co-prime or not.
"""

def gcd(p,q):
    # Create the gcd of two positive integers
    while q != 0:
        p,q = q, p%q
    return p

def is_coprime(x,y):
    return gcd(x,y) == 1

print(is_coprime(12,15))