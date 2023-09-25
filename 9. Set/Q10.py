"""
Q. Two sets represent two identical dices(dice values are from 1 to 6). Write a python script to produce
sample space to get a sum of dice values when rolled is N.
"""

# function to calculate the total number of ways to achieve a given sum with 'n' throws of dice having 
# 'k' faces
def count(n,k,target):
    # if the desired sum is reached with 'n' dices
    if n == 0:
        return 1 if (target == 0) else 0
    # the desired sum can't be reached with current configuration 
    if target < 0 or k*n < target or n > target:
        return 0
    result = 0
    
    # recur for all possible solutions
    for i in range(1,k+1):
        result += count(n-1,k,target-i)
    return result

if __name__ == "__main__":
    n = 4 # n throws
    k = 6 # values 1 to 6
    target = 15 # desired sum
    
print("The total number of ways is", count(n,k,target))        