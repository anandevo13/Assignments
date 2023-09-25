"""
Q. Python script to count the frequency of elements of a tuple
"""

def countX(tup, x):
    count = 0
    for ele in tup:
        if (ele == x):
            count = count + 1
    return count

# Driver count
tup = (10,8,5,2,10,15,10,8,5,8,8,2)
enq = 4
enq1 = 10
enq2 = 8

print(countX(tup, enq))
print(countX(tup, enq1))
print(countX(tup, enq2))        

# Another Approach
# count function is used
def count(tup,en):
    return tup.count(en)

# Driver count
tup = (10,8,5,2,10,15,10,8,5,8,8,2)
enq = 4
enq1 = 10
enq2 = 8

print(count(tup, enq),"times")
print(count(tup, enq1),"times")
print(count(tup, enq2),"times")

# Another Approach
tuple1 = (10,8,5,2,10,15,10,8,5,8,8,2)
x = [i for i in tuple1 if i == 10]
print("the element 10 occurs",len(x),"times")

# Another Approach
tuple1 = (10,8,5,2,10,15,10,8,5,8,8,2)
x = [i for a,i in enumerate(tuple1) if i == 10]
print("the element 10 occurs",len(x),"times")

# Another Approach
tuple1 = (10,8,5,2,10,15,10,8,5,8,8,2)
x = list(filter(lambda i:(i==10), tuple1))
print("the element 10 occurs",len(x),"times")

# Another Approach
from collections import Counter

tuple1 = ("10","8","5","2","10","15","10","8","5","8","8","2")
x = Counter(tuple1)
print("the element 10 occurs",x["10"],"times")

# Another Approach
import operator as op

tuple1 = ("10","8","5","2","10","15","10","8","5","8","8","2")
print(op.countOf(tuple1,"10"))

# Another Approach
from collections import defaultdict

# initialize tuple
test_tup = (4,5,4,5,6,6,5,5,4)
#priniting original tuple
print("The original tuple is: ", str(test_tup))

res = defaultdict(int)
for ele in test_tup:
    # incrementing frequency
    res[ele] += 1
    
#printing result
print("tuple elements frequency is: "+str(dict(res)))    

# Another Approach
from collections import Counter

# initialize tuple
test_tup = (4,5,4,5,6,6,5,5,4)
#priniting original tuple
print("The original tuple is: ", str(test_tup))

#converting result back from defaultdict to dict
res = dict(Counter(test_tup))
#printing result
print("tuple elements frequency is: " + str(res))

# Another Approach
test_tup = (4,5,4,5,6,6,5,5,4)
#priniting original tuple
print("The original tuple is: ", str(test_tup))

res = dict()
x = list(test_tup)
y = []
for i in x:
    if i not in y:
        y.append(i)

for i in y:
    res[i] = x.count(i)

#printing result
print("tuple elements frequency is: " + str(res))