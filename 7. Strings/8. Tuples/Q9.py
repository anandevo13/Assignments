"""
Q. Python script to compare two tuples, whether they contain the same elements in same order or not
"""

print("Enter elements seperated by comma for first tuple")
t1 = tuple([eval(e) for e in input().split(',')])
print("Enter elements seperated by comma for second tuple")
t2 = tuple([eval(e) for e in input().split(',')])

if t1 == t2:
    print("Yes, tuples are same")
else:
    print('No, tuples are not same')