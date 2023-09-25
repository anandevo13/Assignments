"""
Q. Python script to create a dictionary in which each item is a pair of Roll Number(as KEY) and Student 
Name(as VALUE).
"""

#Define the dictionary
dict1 = {}

#Insert data into dictionary
dict1 = {1:[1,"ABC"],
         2:[2,"DEF"],
         3:[3,"XYZ"],
         4:[4,"WUV"],
         }

#print the names of the columns
print("{:<10}{:<10}".format('ROLL','NAME'))

#print each data item
for key,value in dict1.items():
    roll,name = value
    print("{:<10} {:<10}".format(roll,name))
