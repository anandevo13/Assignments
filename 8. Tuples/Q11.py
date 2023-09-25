"""
Q. Write a python script to check whether a tuple is a subset of another tuple or not.
"""

test_tup1 = (10,4,5,6)
test_tup2 = (5,10)

# printing original tuples
print("The original tuple 1: "+ str(test_tup1))
print("The original tuple 2: "+ str(test_tup2))

# check if one tuple is subset of other using is subset()
res = set(test_tup2).issubset(test_tup1)

# printing the result
print("Is second tuple subset of first? :", str(res))


# Another Approach
test_tup1 = (10,4,5,6)
test_tup2 = (5,10)

# printing original tuples
print("The original tuple 1: "+ str(test_tup1))
print("The original tuple 2: "+ str(test_tup2))

# check if one tuple is subset of other using all() + generator expression
res = all(ele in test_tup1 for ele in test_tup2)

# printing the result
print("Is second tuple subset of first? :", str(res))


#Another Approach
test_tup1 = (10,4,5,6)
test_tup2 = (5,10)

x = [j for i in test_tup1 for j in test_tup2]
print(["yes" if x else "no"])


#Another Approach
test_tup1 = (10,4,5,6)
test_tup2 = (5,10)

# printing original tuples
print("The original tuple 1: "+ str(test_tup1))
print("The original tuple 2: "+ str(test_tup2))

#check if one tuple is subset of other
c = 0
res = False
for i in test_tup2:
    if i in test_tup1:
        c += 1
        
if (c == len(test_tup2)):
    res = True
    
# printing result
print ("Is second tuple a subset of first?",str(res))


#Another Approach
test_tup1 = (10,4,5,6)
test_tup2 = (5,10)

x = [j for a,i in enumerate(test_tup1) for j in test_tup2]
print(["yes" if x else "no"])

