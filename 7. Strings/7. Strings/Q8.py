"""
Q. Script to check if a given string is pallindrome or not.
"""

def isPalindrome(s):
    return s == s[::-1]

# Driver code
s = 'malayalam'
ans = isPalindrome(s)
if ans:
    print("yes")
else:
    print("no")
    
    
# Another method:

def isPalindrome(str):

	# Run loop from 0 to len/2
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")
 
 
# Another method
 
def isPalindrome(s):
     
     rev = ''.join(reversed(s))
     if (s == rev):
         return True
     return False
 
# main function
s = "malayalam" 
ans = isPalindrome(s)

if (ans):
    print("yes")
else:
    print("no")
    
    
# Another method

x = "malayalam"

w = ""
for i in x:
    w = i + w 
    
if (x == w):
    print("yes")
else:
    print("no")    
   
   
            