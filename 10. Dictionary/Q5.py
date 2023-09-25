"""
Q. Python script to take dictionary from the keyboard and print the sum of values
"""

def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
    
    return final

# Driver function
dict = {'a':100,'b':200,'c':300}
print("Sum:",returnSum(dict))

#Another Approach
def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i
        
    return sum

# Driver function
dict = {'a':100,'b':200,'c':300}
print("Sum:",returnSum(dict))

#Another Approach
def returnSum(dict):
    sum = 0
    for i in dict:
        sum = sum + dict[i]
    return sum

# Driver function
dict = {'a':100,'b':200,'c':300}
print("Sum:",returnSum(dict))

#Another Approach
def returnSum(dict):
    return sum(dict.values())

# Driver function
dict = {'a':100,'b':200,'c':300}
print("Sum:",returnSum(dict))

#Another Approach
import functools

dic = {'a':100,'b':200,'c':300}
sum_dic = functools.reduce(lambda ac,k:ac+dic[k],dic,0)
print("Sum:",sum_dic)
    
        