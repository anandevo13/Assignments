"""
Q. Python script to count distinct elements in a list using set
"""

# using sets to count unique values in a list
a_list = [1,2,1,4,1,1,2,3,3,1]

set = set(a_list)
num_values = len(set)
print(num_values)