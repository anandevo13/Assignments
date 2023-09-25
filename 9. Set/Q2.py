"""
Q. Python script to create a set of first N prime numbers 
"""

# Python code to implement the approach
import math
 
# Function to generate first n primes
def generatePrime(n):
    X = 0
    i = 2
    flag = False
    while(X < n):
        flag = True
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if (i%j == 0):
                flag = False
                break
        if(flag):
            print(i, end=" ")
            X+=1
        i+=1
    print()
     
# Driver code
 
# Test Case 1
N = 4
 
# Function call
generatePrime(N)
 
# Test Case 2
N = 20
 
# Function call
generatePrime(N)

 


# Another Approach:

def generateprime(N):
    primes = [2]  # Initialize an empty list to store prime numbers and add 2 as the first prime number
    num = 3  # Start checking for prime numbers from 3
    while len(primes) < N:  # Keep searching until we find N prime numbers
        is_prime = True  # Assume the current number is prime until proven otherwise
        for i in range(len(primes)):
            if num % primes[i] == 0:  # If the current number is divisible by any previously found prime numbers
                is_prime = False  # Then it is not a prime number
                break  # Exit the loop since we've already proven it's not prime
        if is_prime:  # If the current number is still prime after checking all previously found prime numbers
            primes.append(num)  # Add it to our list of prime numbers
        num += 2  # Check the next odd number (since even numbers other than 2 are not prime)
 
    for i in range(len(primes)):  # Print the first N prime numbers
        print(primes[i], end=" ")
    print()
 
# Test Case 1
n = 4
generateprime(n)
 
# Test Case 2
n = 1
generateprime(n)


# Another Approach
n = 20
primes = []
i = 2
while len(primes) < n:
    for j in range(2,int(i*0.5)+1):
        if i % j == 0:
            break
    else:
        primes.append(i)
    i += 1    

print(primes)