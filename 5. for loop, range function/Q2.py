
"""
Q. Python program to print Armstrong number
"""

n = int(input("enter the number: "))
# assigning input value to the s variable
s = n
b = len(str(n))

sum1 = 0

while n != 0:
    r = n % 10
    sum1 = sum1 + (r**b)
    n = n//10
    
if s == sum1:
    print(s, "is armstrong number")
else:
    print(s, "is not armstrong number")    
  
    
# Another method using for loop

num = int(input("Enter a Number:"))
order = len(str(num))
temp = num;
sum = 0
stnum=str(num)
for i in stnum:
    digit =temp%10
    sum += digit **order
    temp = temp//10
if(sum==num):
    print("",num,"is an Armstrong number")
else:
    print("",num,"is not an Armstrong number")    