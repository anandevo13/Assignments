"""
Q. Python script to take union of two sets
"""

s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s = s1.union(s2)
print(s)

# Another Approach

s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s = s1|s2
print(s)