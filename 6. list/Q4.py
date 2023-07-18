"""
Q. Python script to create a list of first N prime numbers. Value of N is given by user.
"""

num = int(input("enter range: "))

print("prime numbers: ", end = '')

for n in range(1, num):
    for i in range(2,n):
        if (n%i == 0):
            break
        else:
            print(n, end=" ")
            
            