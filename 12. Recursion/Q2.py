"""
Q. Write a recursive function to print cubes of first N natural numbers in reverse order.
"""

def cubes(n):
    l = []
    if n == 1:
        return 1
    else:
        for i in range(n,0,-1):
            l.append(pow(i,3))
        print(l)
        
n = 7
cubes(n)            