"""
Q. Write a recursive function to print all permutation of a given string
"""

# Python program to print all permutations with duplicates allowed 
def toString(list):
    return ''.join(list)

def permute(a,l,r):
    if l == r:
        print (toString(a))
    else:
        for i in range(l,r):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i] = a[i],a[l]
            

# Driver Code
string = "ABC"
n = len(string)
a = list(string)

# Function call
permute(a,0,n)            
            
            