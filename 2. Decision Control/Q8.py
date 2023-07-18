"""
Q. Python script to accept one complex number from user and display the greater number between real part and 
imaginary part
"""

num1 = float(input("enter the number: "))
num2 = float(input("enter the number: "))

z = complex(num1,num2)

if num1 < num2:
    print(num2)
else:
    print(num1)