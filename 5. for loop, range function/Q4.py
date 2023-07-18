"""
Q. Python script to print a sequence of number with given step size and boundary values. For example boundary 
values are 10 and 30, step is 2 then your output should be 10,12,14,16,18,20,22,24,26,28,30. 
"""

start, end = 10,30

for num in range(10,31,2):
    print(num, end = " ")