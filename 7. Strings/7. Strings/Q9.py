"""
Q. Python script to find a pattern in a given string
"""

n = int(input("enter number of cities: "))

city = ()

for i in range(n):
    c = input("enter city: ")
    city += (c,)
    
print(city)

pat = input("enter pattern you want to search for? :")

for c in city:
    if (c.find(pat) != -1):
        print(c) 
        
           