"""
Q. Python script to find cartesian product of two given sets
"""

def findCart(arr1,arr2,n,n1):
    for i in range(0,n):
        for j in range(0,n1):
            print("{", arr1[i], ",", arr2[j] ,"}", end=" ")
            
# Driver code
arr1 =[1,2,3]
arr2 = [4,5,6]
n1 = len(arr1)
n2 = len(arr2)
findCart(arr1,arr2,n1,n2)            