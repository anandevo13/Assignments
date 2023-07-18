"""
Q. Python script to print all prime numbers between two given numbers.
"""

n = int(input("Enter the lowest range number: "))
a = int(input("Enter the upper range number: "))

print("Prime numbers between", n, "and", a, "are:") 

for num in range(n, a):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)
 
         
                                                