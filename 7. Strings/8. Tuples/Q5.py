"""
Q. Python script to count elements in the tuple
"""

test_list = [(2,4),(6,7),(5,1),(6,10),(8,7)]
print("The original list: "+ str(test_list))

# tuple list elements count using len() + generator expression
temp = list((int(j) for i in test_list for j in i))
res = len(temp)

# printing the result
print("The tuple list elements count: " + str(res))

# Another Approach
from itertools import chain
test_list = [(2,4),(6,7),(5,1),(6,10),(8,7)]
print("The original list: " + str(test_list))

# tuple list elements count using len() + map() + chain.from_iterable
res = len(list(map(int, chain.from_iterable(test_list))))
print("The tuple list elements count: " + str(res))

# Another Approach
test_list = [(2,4),(6,7),(5,1),(6,10),(8,7)]
x = [j for i in test_list for j in i]
print(len(x))

# Another Approach
test_list = [(2,4),(6,7),(5,1),(6,10),(8,7)]
x = [j for i in enumerate(test_list) for j in i]
print(len(x))