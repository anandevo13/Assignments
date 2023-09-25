"""
Q. Python script to arrange words in a given string in alphabetical order
"""

def func(s):
    w = s.split(" ")
    for i in range(len(w)):
        # convert all the words into lowercase
        w[i] = w[i].lower()
    s = sorted(w)
    print(''.join(s))
    
s = "the quick brown fox jumps over the lazy dog"
func(s)    

# Another method: Using sort()

def func(s):
    w = s.split(" ")
    for i in range(len(w)):
        w[i] = w[i].lower()
    w.sort()
    # return the sorted words
    return ''.join(w)

s = "the quick brown fox jumps over the lazy dog"
func(s) 
        