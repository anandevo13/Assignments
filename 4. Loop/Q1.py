"""
Q. Python script to print next prime numbers of a given number.
"""

def nxtprime(n):
    while True:
        n += 1
        for i in range(2,n):
            if (n % i == 0):
                break
        else:
            return n
        
n = int(input("enter the number: "))        
print(nxtprime(n))            
    
    