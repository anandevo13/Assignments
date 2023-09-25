"""
Q. Python function to calculate sum of all even numbers and sum of odd numbers from a given list of int 
values.
"""

def sum(list):
    even_sum = 0
    odd_sum = 0
    
    for sub in list:
        for ele in str(sub):
            if int(ele)%2 == 0:
                even_sum += int(ele)
            else:
                odd_sum += int(ele)
    return(even_sum, odd_sum)

list = [3,4,5,8,9,3,1,9,4,8,3,4,2,3,4,6]
even_sum, odd_sum = sum(list)
print("Odd digit sum: " + str(odd_sum))
print("Even digit sum: " + str(even_sum))            