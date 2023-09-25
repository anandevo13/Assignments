"""
Q. Python script to reverse a tuple
"""

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

# Driver code
tuples = ('z','a','d','f','g','e','e','k')
print(reverse(tuples))

# Another Approach

# Reversing a list using reversed()
def Reverse(tuples):
	new_tup = ()
	for k in reversed(tuples):
		new_tup = new_tup + (k,)
	print (new_tup)

# Driver Code
tuples = (10, 11, 12, 13, 14, 15)
Reverse(tuples)
        