"""
Q. Python script to create a power set of a given set
"""

#Powerset- Powerset p(s) of a set s is the set of all subsets of s. If s has n elements in it then p(s) 
# will have 2^n elements in it.

from collections import deque

#function to generate a power set of given set 's'
def findPowerSet(S,s,n):
    # if we have considered all elements
    if n == 0:
        print(s)
        return
    # Consider the nth element
    s.append(S[n-1])
    findPowerSet(S,s,n-1)
    #backtrack
    s.pop()
    # or don't consider the nth element
    findPowerSet(S,s,n-1)
    
if __name__ == "__main__":
    S = [1,2,3]
    s = []
    findPowerSet(S,s,len(s))
    

# Another Approach

def findPowerSet(s):
    # 'N' stores the total number of subsets
    N = int(pow(2,len(s)))
    s = list()
    
    # generate each subset one by one
    for i in range(N):
        # check every bit of 'i'
        for j in range(len(s)):
            # if jth bit of i is set, print's[j]'
            if i & (1<<j):
                s.append(s[j])
        print(s)
        s.clear()
        
if __name__ == "__main__":
    s = [1,2,3]                           
    findPowerSet(s)