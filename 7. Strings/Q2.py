"""
Q. Python script to count vowels in a string
"""

def vowel_count(str):
    # initializing count variable to 0
    count = 0
    # creating a set of vowels
    vowel = set("aeiouAEIOU")
    # loop to traverse the alphabet in the given string
    for alphabet in str:
        # if alphabet is present in set vowel
        if alphabet in vowel:
            count = count + 1
        print("No. of vowels: ", count)
        
str = "GeeksforGeeks"
vowel_count(str)         