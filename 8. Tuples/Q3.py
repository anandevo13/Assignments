"""
Q. Python script to merge two sorted tuples
"""

t1 = (10,20,30,40)
t2 = (5,9,12,18,22,25)
t3 = []
i,j,k = 0,0,0

while i < len(t1) and j < len(t2):
    if t1[i] < t2[j]:
        t3.append(t1[i])
        i += 1
        k += 1
    else:
        t3.append(t2[j])
        j += 1
        k += 1
        
    if i == len(t1):
        while j<len(t2):
            t3.append(t2[j])
            j += 1
            k += 1
    elif j == len(t2):
        while i < len(t1):
            t3.append(t1[i])
            i += 1
            k += 1
            
t3 = tuple(t3)
print("Resulting tuple is: ", t3)
            