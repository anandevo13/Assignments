"""
Q. Python script to compare two tuples, whether they contain the same elements in any order or not.
"""

t1 = (10,22,33)
t2 = (22,33,10)

print(sorted(t1) == sorted(t2))

# Another Approach

t1 = (10,22,33)
t2 = (22,33,10)

for i in t1:
    if i not in t2:
        print("Not same")
        break
    else:
        print("same")