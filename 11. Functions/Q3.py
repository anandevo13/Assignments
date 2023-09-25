"""
Q. Python function to print first N prime numbers
"""

def isPrime(n):
    # since 0 and 1 is not prime return false
    if (n == 1 or n == 0):
        return False
    
    # Run a loop from 2 to n-1
    for i in range(2,n):
        if (n%i == 0):
            return False
    return True    

N = 100;
for i in range(1, N+1):
    if(isPrime(i)):
        print(i, end=" ")
        

# Another method:

def isPrime(n):
    if (n == 1 or n == 0):
        return False
    
    for i in range(2,(n//2)+1):
        if (n % i == 0):
            return False
    return True

N = 100;
for i in range(1,N+1):
    if (isPrime(i)):
        print(i, end=" ")      
        
        
# Another method:

def isPrime(n):
    if (n == 1 or n == 0):
        return False
    
    for i in range(2,int(n**(1/2))+1):
        if (n % i == 0):
            return False
    return True

N = 100;
for i in range(1,N+1):
    if (isPrime(i)):
        print(i, end=" ")             
        
        