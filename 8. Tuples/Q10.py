"""
Q. Python script to find the greatest number from a tuple of integer values 
"""

print("Enter number seperated by comma: ")
t1 = tuple([int(e) for e in input().split(',')])
print("Greatest number in the tuple is: ",max(t1))

# Another Approach
t = (25,17,55,63,40)
max_val = t[0]

for i in range(len(t)):
    if t[i]>max_val:
        max_val=t[i]
print("Maximum value is: ",max_val)