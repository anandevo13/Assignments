"""
Q. Python function which takes a list of strings as an argument and returns a dictionary whose each item 
is a pair of alphabet(as key) and list of strings begin with that alphabet.
"""

def dictionary(string_input):
    # storing words in the input as a list
    words = string_input.split()
    
    # declaring an input dictionary
    dictionary = {}
    
    for word in words:
        # If key is not present in the dictionary then we will add the key and word to the dictionary
        if (word[0] not in dictionary.keys()):
            # creating a sublist to store words with same key value and adding it to the list
            dictionary[word[0]] = []
            dictionary[word[0]].append(word)
    return dictionary

# Declaring string data
string_input = "Geeks for geeks"
dictionary = dictionary(string_input)
print(dictionary)        