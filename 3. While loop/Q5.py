"""
Q. Python script to calculate factorial of a number. Number is taken from user.
"""

num = int(input("enter a number: "))
 
fac = 1
i = 1
 
while i <= num:
    fac = fac * i
    i = i + 1
 
print("factorial of ", num, " is ", fac)


# Another method: Factorial using loop

num = int(input("enter a number: "))
factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("no factorial for negative number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print("The factorial of", num,"is",factorial)    


# Another method: Factorial using recursion

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x*factorial(x-1))

num = int(input("enter a number: "))

#call the factorial function
result = factorial(num)
print(result)

# Another method: lambda

factorial = lambda x:x and x*factorial(x-1) or 1
factorial = lambda a:a*factorial(a-1) if (a>1) else 1

result = factorial(5)
print(result)
