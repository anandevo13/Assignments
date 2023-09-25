"""
Q. Count and display vowels in a string
"""

# Simply using for and comparing it with a string containing all vowels
def check_vow(string, vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)
    
string = "GeeksforGeeks"
vowels = "AEIOUaeiou"
check_vow(string, vowels)

# Another method: Dictionary way
def check_vow(string, vowels):
    # casefold has been used to ignore cases
    string = string.casefold()
    
    # Forms a dictionary with key as a vowel and the value as 0
    count = {}.fromkeys(vowels, 0)
    
    # To count the vowels
    for character in string:
        if character in count:
            count[character] += 1
    return count

vowels = "aeiou"
string = "Geeksforgeeks"
print(check_vow(string,vowels))  

# Another method: Regex way

import re

#Count vowels in a different way using re.findall
def check_vow(string, vowels):
    # using re.findall in string
    str_list = re.findall(f'[{vowels}]', string, re.I) 
    # printing length of string
    print(len(str_list))
    # returning the list of matched element
    return str_list

vowels = 'aeiou'
string = "GeeksforGeeks"
print(check_vow(string,vowels))