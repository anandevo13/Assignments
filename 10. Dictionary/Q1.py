"""
Q. Python script to print dict items(KEY,VALUE), each in one line.
"""

student_score = {
    "John": 10,
    "Ritika": 5,
    "Aadi": 8,
    "Sam":7
}

print(student_score)

# Another Approach:

student_score = {
    "John": 10,
    "Ritika": 5,
    "Aadi": 8,
    "Sam":7
}

# Iterate over key/value pairs in dict and print them
for key,value in student_score.items():
    print(key,':', value)
    
# Another Approach:

student_score = {
    "John": 10,
    "Ritika": 5,
    "Aadi": 8,
    "Sam":7
}

# Iterate over the keys in dictionary, access value & print line by line
for key in student_score:
    print(key,':', student_score[key])   

    
# Another Approach:

student_score = {
    "John": 10,
    "Ritika": 5,
    "Aadi": 8,
    "Sam":7
}

# Iterate over key_value pairs of a dictionary using list comprehension and print them
[print(key,':', value) for key,value in student_score.items()]