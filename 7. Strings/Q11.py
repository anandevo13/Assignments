"""
Q. Python script to count occurrence of a given pattern in a given string.
"""

# Approach 1: Using re.findall() Method

# Python code to demonstrate to count total number of substring in string 
import re
# Initialising string
s = 'ababababa'
 
 
# Count count of substrings using re.findall
res= len(re.findall('(?=(aba))', s))
 
print("Number of substrings", res)

# Another Approach: Using startswith() 

# Python code to demonstrate to count total number of substring in string
# Initialising string
ini_str = "ababababa"
sub_str = 'aba'
 
# Count count of substrings using startswith
res = sum(1 for i in range(len(ini_str))
        if ini_str.startswith("aba", i))
 
# Printing result
print("Number of substrings", res)

# Another Approach: Using count() Method

# Python code to demonstrate to count total number of substring in string
# Initialising string
ini_str = "ababababa"
sub_str = 'aba'
# Count count of substrings using count
def Countofoccurrences(ini_str,sub_str):
 
    # Initialize count and start to 0
    count = 0
    start = 0
 
    # Search through the string till
    # we reach the end of it
    while start < len(ini_str):
 
        # Check if a substring is present from
        # 'start' position till the end
        pos = ini_str.find(sub_str, start)
 
        if pos != -1:
            # If a substring is present, move 'start' to
            # the next position from start of the substring
            start = pos + 1
 
            # Increment the count
            count += 1
        else:
            # If no further substring is present
            break
    # return the value of count
    return count
# Printing result
print("Number of substrings", Countofoccurrences(ini_str,sub_str))

# Another Approach: Using List Comprehension

# Python code to demonstrate to count total number of substring in string
# Initializing string
ini_str = "ababababa"
sub_str = 'aba'
 
# Count count of substrings using list comprehension
res = sum([1 for i in range(len(ini_str)-len(sub_str)+1) if ini_str[i:i+len(sub_str)] == sub_str])
 
# Printing result
print("Number of substrings", res)


# Another Approach: Using sliding window

ini_str = "ababababa"
sub_str = 'aba'
 
count = 0
n = len(ini_str)
m = len(sub_str)
 
for i in range(n - m + 1):
    if ini_str[i:i+m] == sub_str:
        count += 1
 
print("Number of substrings:", count)

# Another Approach

my_string = "GeeksForGeeks"
char_count = my_string.count('e')
print(char_count)

# Another Approach: Python String Count() to Count Occurrences of a given Substring

# Python program to demonstrate the use of count() method without optional parameters
# string in which occurrence will be checked
string = "geeks for geeks"
 
# counts the number of times substring occurs in
# the given string and returns an integer
print(string.count("geeks"))

# Another Approach: Python String Count() to Count Occurrences of Character in Multiple String

# Python program to demonstrate the use of count() method without optional parameters
strings = ["Red", "Green", "orange"]
char_to_count = 'e'
total_count = sum(string.count(char_to_count) for string in strings)
print(total_count)

# Another Approach: Python String count() Method using Regular Expression

import re
 
my_string = "Good Morning and Morning is Great."
substring = "Morning"
substring_count = len(re.findall(substring, my_string))
print(substring_count)

# Another Approach: Python String count() Method using Start and End Parameter

# Python program to demonstrate the use of count() method  using optional parameters
# string in which occurrence will be checked
string = "geeks for geeks"
 
# counts the number of times substring occurs in the given string between index 0 and 5 and returns an integer
print(string.count("geeks", 0, 5))
print(string.count("geeks", 0, 15))

# Returns count of occurrence of "1(0+1)"
def countPattern(s):
    length = len(s)
    oneSeen = False
    # Initialize result
    count = 0
    for i in range(length):
        # check if encountered '1' forms a valid pattern is specified
        if (s[i] == '1' and oneSeen):
            if (s[i-1] == '0'):
                count += 1
        
        # if 1 encountered for first time set oneSeen to 1
        if (s[i] == '1' and oneSeen == 0):
            oneSeen = True
            
        # Check if there is any other character other than '0' or '1'. If so then set oneSeen to 0 to
        # search again for new pattern
        if (s[i] != '0' and s[i] != '1'):
            oneSeen = False
 
    return count            

# Driver code
s = '100001abc101'
print(countPattern(s))
                        