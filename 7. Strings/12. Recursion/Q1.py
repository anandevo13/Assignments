"""
Q. Write a recursive function to print squares of N natural numbers.
"""

def squares(n):
    l = []
    if n == 1:
        return 1
    else:
        for i in range(1,n+1):
            l.append(i**2)
        print(l)    
        
n = 7
squares(n)        