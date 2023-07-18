"""
Q. Python script to find the greatest number in the list of integers 
"""
"""
# Method 1: Sort the list in ascending order and print the last element in the list

list = [10,20,4,45,99]

# Sorting the list
list.sort()

# printing the last element
print("largest element is: ", list[-1])

"""
# Method 2: Using Max function
list = [10,20,4,45,99]
print("largest element is: ", max(list))

# Method 3

# creating a list
list = []

# asking number of elements to put in list
num = int(input("enter the number of elements in the list: "))

# iterating till num to append elements in list
for i in range(1, num+1):
    ele = int(input("enter elements: "))
    list.append(ele)
    
# print maximum element
print("largest element is: ", max(list))

# Method 4
def myMax(list):
    # Assume first number in the list is largest
    # initially and assign it to variable "max"
    max = list[0]
    
    # Now, traverse through the list and compare each number with "max" value.
    # whichever is largest assign that value to max
    for x in list:
        if x > max:
            max = x
            
    # after complete traversing the list return the "max" value
    return max

# Driver code
list = [10,20,4,45,99]
print("largest element is: ", myMax(list))

# Another method
def maxelement(lst):
    print(max(lst))
    
lst = [20,10,20,4,100]
maxelement(lst) 

# Another method
lst = [20,10,20,4,100]
print(max(lst, key=lambda value:int(value)))

# Another method
from functools import reduce
lst = [20,10,20,4,100]
largest_elem = reduce(max,lst)
print(largest_elem)           
        