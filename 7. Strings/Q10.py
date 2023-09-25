"""
Q. Python script to remove duplicate characters from a given string
"""

string="geeksforgeeks"
p=""
for char in string:
	if char not in p:
		p=p+char
print(p)
k=list("geeksforgeeks")
