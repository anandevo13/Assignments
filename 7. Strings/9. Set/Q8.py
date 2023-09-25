"""
Q. Python script to print all possible subsets of r elements each from a given set of N elements
"""

#arr[] --> Input Array
#data[] --> Temporary array to store current combination
#start & end --> Starting & ending indexes in arr[]
#index --> Current index in data
#r --> Size of a combination to be printed

def combinationUtil(arr,n,r,index,data,i):
    # current combination is ready to be printed, print it
    if (index == r):
        for j in range(r):
            print(data[j], end="")
        print("")
        return
    
    # when no more elements are there to put in data[]
    if (i >= n):
        return
    # current is included, put next at next location
    data[index] = arr[i]
    combinationUtil(arr,n,r,index+1, data,i+1)
    
    #current is excluded, replace it with next
    #Note that i+1 is passed, but index is not changed
    combinationUtil(arr,n,r,index,data,i+1)
    
#The main function that prints all combinations of size arr[] of size n. This function mainly uses
#combinationUtil
def printcombination(arr,n,r):
    #A temporary array to store all combination one by one
    data = list(range(r))
    #Print all combination using temporary array 'data[]' 
    combinationUtil(arr,n,r,0,data,0)
    
#Driver code
arr = [10,20,30,40,50]
r = 3
n = len(arr)
printcombination(arr,n,r)

# Another Approach
from functools import reduce

#the data
s = {1,2,3}

#the one liner
ps = lambda s:reduce(lambda P,x:P + [subset | {x} for subset in P],s,[set()])

# Another Approach: Simply pass the set as iterable and the size as arguments in 
# the itertools.combinations() to directly fetch the combination list.
 
# Python Program to Print all subsets of given size of a set
 
import itertools
 
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
 
# Driver Code
s = {1, 2, 3}
n = 2
 
print(findsubsets(s, n))

# Another Approach: We can also use an alternative to the above-discussed method which is 
# mapping set to itertools.combinations() function. 
 
# Python Program to Print all subsets of given size of a set
 
import itertools
from itertools import combinations, chain
 
def findsubsets(s, n):
    return list(map(set, itertools.combinations(s, n)))
     
# Driver Code
s = {1, 2, 3}
n = 2
 
print(findsubsets(s, n))
  
# Another Approach: We are using for loop in itertools.combinations() function and append 
# the combination sets to the list. 
 
# Python Program to print all subsets of given size of a set
 
import itertools
# def findsubsets(s, n):
def findsubsets(s, n):
    return [set(i) for i in itertools.combinations(s, n)]
     
# Driver Code
s = {1, 2, 3, 4}
n = 3
 
print(findsubsets(s, n))

#Another Approach

def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]
 
# wrapper function
def subsets_of_given_size(numbers, n):
    return [x for x in subsets(numbers) if len(x)==n]
 
if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    n = 3
    print(subsets_of_given_size(numbers, n))


           