"""
Q. Python script to print first N odd natural numbers in reverse order using range function in for loop.
"""

n = int(input("enter a natural number: "))

for i in range(1, n+1):
   print(2*n-2*i+1, end ='')
    
    
# Another method

for i in range(2*n-1,0,-2):
    print(i, end='')   