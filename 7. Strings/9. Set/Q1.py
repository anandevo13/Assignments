"""
Q. Python script to find common elements between two sets
"""

def common_member(a,b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")
        
a = [1,2,3,4,5]
b = [6,7,8,9,5]
common_member(a,b)        

# Another approach

def common_member(a,b):
    a_set = set(a)
    b_set = set(b)
    #check length
    if len(a_set.intersection(b_set))>0:
        return(a_set.intersection(b_set))
    else:
        print("No common elements")
        
a = [1,2,3,4,5]
b = [6,7,8,9,5]
print(common_member(a,b)) 

# Another approach

def common_member(a,b):
    result = {i for i in a if i in b}
    return result
        
a = [1,2,3,4,5]
b = [6,7,8,9,5]
print(common_member(a,b))
    