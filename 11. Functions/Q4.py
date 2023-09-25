"""
Q. Python function to count words in a given array
"""

OUT = 0
IN = 1

def countWords(string):
    state = OUT
    wc = 0
    
    for i in range(len(string)):
        if(string[i] == ' ' or string[i] == '\n' or string[i] == '\t'):
            state = OUT
        elif state == OUT:
            state = IN
            wc += 1
    return wc

string = "One two three \n four \t five"
print("Number of words:" + str(countWords(string)))             


# Another Method:

def countWords(s):
    # Check if the string is null or empty then return zero
    if s.strip() == " ":
        return 0
    
    # Splitting the string
    words = s.split()
    return len(words)

if __name__ == "__main__":
    s = "One two three \n four \t five"
    print("Number of words:", countWords(s))