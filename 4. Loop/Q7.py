"""
Q. Python script to calculate HCF of two numbers
"""

x = int(input("enter a number: "))
y = int(input("enter a number: "))  

def compute_hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
        
    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
        return hcf

print("The H.C.F. is", compute_hcf(x, y))
              