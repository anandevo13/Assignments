"""
Q. Python script to print indices of all occurrence of a given element in a given list
"""

my_list = [1,2,3,1,5,4]

# find length of the list
list_size = len(my_list)

# declare for loop
for itr in range(list_size):
    # check the condition
    if (my_list[itr] == 1):
        # print the indices
        print(itr)
        
        
# Method 2: Using list comprehension

# initialize a list
my_list = [1,5,3,1,5,4]
item = 5
indices = [i for i in range(len(my_list)) if my_list[i] == item]

# print the indices
print(indices)


# Method 3 
my_list = [1,2,3,1,5,4]
indices = [ind for ind, ele in enumerate(my_list) if ele == 1] 

# print the indices
print(indices)


# Method 4
from itertools import count

# initialize a list
my_list = [1,2,3,1,5,4]

indices = [ind for ind, ele in zip(count(), my_list) if ele == 1]

# print the indices
print(indices)


# Method 5
import numpy

# initialize an array
my_list = numpy.array([1,2,3,1,5,4])
indices = numpy.where(my_list == 1)[0]

# display result
print(indices)       