"""
Q. Python script to check whether a number is divisible by 5 or not.
"""

num = int(input("enter a number: "))

if num % 5 == 0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 5")


# Another approach

my_list = [15,20,19,16,18,25,10,75] 

# use anonymous function to filter 
result = list(filter(lambda x:(x%5 == 0), my_list))

# display the result
print("numbers divisible by 5 are:", result)