"""
Q. Python script to print all prime factors of a given number
"""

n = int(input("Please enter any number: "))

for i in range(2, n+1):
    if (n%i == 0):
        isprime = 1
        for j in range(2,(i//2+1)):
            if (i%j == 0):
                isprime = 0
                break
        if(isprime == 1):
            print(" is a prime factor of a given number ", (i,n))  
            
           
# Another method
n = int(input("Please enter any number: "))
i = 1

while(i <= n):
    count = 0
    if (n % i == 0):
        j = 1
        while(j<=1):
            if (i % j == 0):
                count = count + 1
            j = j + 1
            if (count == 2):
                print("%d is a prime factor of a given number %d" %(i,n))  
            i = i + 1      
          
              
    