"""
Q. Python script to calculate sum of all the integers of the list given by user.
"""

total = 0

# creating a list
list = [11,5,17,18,23] 

# iterating each element in list and add them in variable total
for ele in range(0, len(list)):
    total = total + list[ele]
    
# printing total value
print("Sum of all elements in given list:", total)


# Another method
total = 0
ele = 0

# creating a list
list = [11,5,17,18,23]

# iterate each element in list and add them in variable total
while(ele<len(list)):
    total = total + list[ele]
    ele += 1
    
# printing total value
print("Sum of all elements in given list: ", total)    


# Another method: Recursive way

# Creating a list
list = [11,5,17,18,23]

# Creating sum_list function
def sumOflist(list, size):
    if (size == 0):
        return 0
    else:
        return list[size-1] + sumOflist(list, size-1)
    
# Driver Code
total = sumOflist(list,len(list))
print("Sum of all elements in given list: ", total)


# Another method: Using sum() function

# Creating a list
list = [11,5,17,18,23]

# Using sum() function
total = sum(list)

# Printing total value
print("Sum of all elements in given list: ", total)


# Another method: Using add() function of operator module

from operator import *

list1 = [12,15,3,10] 
result = 0 

for i in list1:
    # Adding elements in the list using add function of operator module
    result = add(i, result)
    
# printing the result
print(result)


# Another method: Using enumerate function

list1 = [12,15,3,10]
s = 0
for i, a in enumerate(list1):
    s += a
print(s) 


# Another method: Using list comprehension

list = [12,15,3,10]
s = [i for i in list]
print(sum(s))


# Another method: Using lambda function

list = [12,15,3,10]
print(sum(list(filter(lambda x:(x), list))))      


#  Another method: Using add operator

import operator

list = [12,15,3,10]
s = 0

for i in list:
    s = s + operator.add(0,i)
print(s)    