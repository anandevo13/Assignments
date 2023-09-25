"""
Q. Python function to calculate LCM of two numbers.
"""

def compute_lcm(x,y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y
        
    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm  = greater
            break
        greater += 1
    return lcm
    
num1 = 54
num2 = 24
print("The LCM is", compute_lcm(num1,num2))        