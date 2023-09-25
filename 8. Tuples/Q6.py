"""
Q. Python script to calculate sum of the elements of the tuple.
"""

test_tup = (7,8,9,1,10,7)
print("The original tuple is: " + str(test_tup))

# Tuple elements inversions using list() + sum()
res = sum(list(test_tup))
print("The summation of tuple elements are: " + str(res))

# Another Approach
test_tup = ([7,8],[9,1],[10,7])
print("The original tuple is: " + str(test_tup))

# Tuple elements inversions using map() + list() + sum()
res = sum(list(map(sum, list(test_tup))))
print("The summation of tuple elements are: "+ str(res))

# Another Approach
test_tup = (7,8,9,1,10,7)
print("The original tuple is: " + str(test_tup))
res = 0
for i in test_tup:
    res += i
print("The summation of tuple elements are: " + str(res))    