"""
Q.Python script to calculate length of the string
"""

str = "geeks"
print(len(str))

# Another method: Using for loop

def findlen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter 

str = "geeks"
print(findlen(str)) 

# Another method: Using while loop

def findlen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

str = "geeks"
print(findlen(str)) 

# Another method: Using join and count

def findlen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return((some_random_str).join(str)).count(some_random_str) + 1

str = "geeks"
print(findlen(str))

# Another method: Using reduce methods

import functools

def findlen(string):
    return functools.reduce(lambda x,y:x+1, string,0)

string = 'geeks'
print(findlen(string))    

# Another method: using list comprehension

def findlen(string):
    return sum(1 for i in string);

string = 'geeks'
print(findlen(string))

  