"""
Q. Python script to count occurrence of a given character in a string
"""

string = input("Please enter your own string: ")
char = input("Please enter your own character: ")

count = 0
for i in range(len(string)):
    if (string[i] == char):
        count = count + 1

print("The total number of times", char, "has occurred = ",count)        

# Another method

i = 0
count = 0
while(i < len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1
    
print("The total number of times", char, "has occurred = ",count)        