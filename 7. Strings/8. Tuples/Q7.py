"""
Q. Python script to create tuples with homogeneous elements from a tuple containing heterogeneous elements
"""

x = (30,4.5,26, 3+4j,'abc', True, 5.6, 2-1j)
t1, t2, t3, t4, t5 = [], [], [], [], []

for e in x:
    if type(e) == int:
        t1.append(e)
    elif type(e) == float:
        t2.append(e)
    elif type(e) == complex:
        t3.append(e)
    elif type(e) == str:
        t4.append(e)
    elif type(e) == bool:
        t5.append(e)
        
        
t1 = tuple(t1)
t2 = tuple(t2)
t3 = tuple(t3)
t4 = tuple(t4)
t5 = tuple(t5)

print(t1,t2,t3,t4,t5, sep='\n')        