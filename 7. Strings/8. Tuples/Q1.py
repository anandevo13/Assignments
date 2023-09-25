"""
Q. Python script to calculate average of tuple values
"""

test_list = [(1,4,5),(7,8),(2,4,10)]
print("The original list is: " + str(test_list))

# Average of tuple list using loops
sum = 0
for sub in test_list:
    for i in sub:
        sum = sum + i
        
res = sum/len(test_list)
print("The mean of tuple is: " + str(res))        


# Another Approach
# This code doesn't work in VSCode 

from itertools import chain

test_list = [(1, 4, 5), (7, 8), (2, 4, 10)]
print("The original list is : " + str(test_list))

# Average of tuple list using chain() + sum()
temp = list(chain(*test_list))
res = sum(temp) / len(test_list)
print("The mean of tuple list is : " + str(res))

# Another Approach
# This code doesn't work in VSCode

t = (10,20,30,40)
#get average of tuple values
print(sum(t)/len(t))

# Another approach

import statistics

t = (10,20,30,40)
print(statistics.mean(t))

# Another approach

import numpy as np

t = (10,20,30,40)
print(np.mean(t))
