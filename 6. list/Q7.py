"""
Q. Python script to print distinct list elements along with their frequency of occurrence in the list.
"""

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
    
# Driver code
lst = [8,6,8,10,8,20,10,8,8]
x = 8
print('{} has occurred {} times'.format(x,countX(lst, x)))  


# Another method: Count occurrences of an element in a list using count()

def countX(lst, x):
    return lst.count(x)

# Driver code
lst = [8,6,8,10,8,20,10,8,8]
x = 8
print('{} has occurred {} times'.format(x,countX(lst, x))) 


# Another method: Count occurrences of an element in a list using counter()

from collections import Counter          

# declaring the list
lst = [1,1,2,2,3,3,4,4,5,5]

# driver program
x = 3
d = Counter(lst)
print('{} has occurred {} times'.format(x,d[x]))


# Another method: Count occurrences of an element in a list using countof()

import operator as op

# declaring the list
lst = [1,1,2,2,3,3,4,4,5,5]

# driver program
x = 2
print(f"{x} has occurred {op.countOf(lst,x)} times")


# Another method: Count occurrences of an element in a list using dictionary comprehension

lst = ['a','d','d','c','a','b','b','a','c','d','e']

occurrence = {item:lst.count(item) for item in lst}
print(occurrence.get('e'))


# Another method: Count occurrences of an element in a list using panda's library

import pandas as pd

# declaring the list
list = [1,1,2,2,2,3,3,4,4,5,5]
count = pd.Series(list).value_counts()
print("Element count")
print(count)


# Another method: Using list comprehension

list = [1,1,2,2,2,3,3,4,4,5,5]
ele = 1
x = [i for i in list if i == ele]
print("the element", ele, "occurs", len(x), "times")