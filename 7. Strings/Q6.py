"""
Q. Python script to count words in a given string
"""

str1 = input("Please enter your own string: ")
total = 1

for i in range(len(str1)):
    if(str1[i] == '' or str1 == '\n' or str1 == '\t'):
        total = total + 1
        
print("Total number of words in this string = ", total)

# Another method

str1 = input("Please enter your own string: ")

total = 1
i = 0

while(i<len(str1)):
    if (str1[i] == '' or str1 == '\n' or str1 == '\t'):
        total = total + 1
    i = i + 1
    
print("Total number of words in this string = ", total)   

# Another method

def count_total_words(str):
    total = 1
    for i in range(len(str1)):
        if (str1[i] == '' or str1 == '\n' or str1 == '\t'):
            total = total + 1
    return total

string = input("Please enter your own string: ")
leng = count_total_words(string)
print("Total number of words in the string = ", leng)
        
