"""
1. Write a python script to add two numbers(integers) taken from user through keyboard
"""
# Method 1:
num1 = input("first number: ")
num2 = input("second number: ")

# Adding two numbers
sum = int(num1) + int(num2)

# print the sum
print(sum)


# Method 2:
if __name__ == "__main__":
    num1 = 15
    num2 = 12

    # Adding two numbers
    sum_two = lambda num1,num2 : num1 + num2

    # Printing values
    print(sum_two(num1, num2))