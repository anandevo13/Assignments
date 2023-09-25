"""
Q. Python script to reverse a string
"""

def reverse_slicing(s):
    return s[::-1]

input_str = 'ABCDEF'

if __name__ == "__main__":
    print('Reverse string using slicing= ', reverse_slicing(input_str))
    
# Another method: Revrse using loop

def reverse_for_loop(s):
    s1 = ''
    for c in s:
        # appending chars in reverse order
        s1 = c + s1
    return s1

input_str = 'ABCDEF'
if __name__ == "__main__":
    print('Reverse string using for loop= ', reverse_for_loop(input_str))    
    
# Another method: Using while loop

def reverse_while_loop(s):
    s1 = ''
    length = len(s)-1
    while length >= 0:
        s1 = s1 + s[length]     
        length = length - 1
    return s1

input_str = 'ABCDEF'
if __name__ == "__main__":
    print('Reverse string using while loop= ', reverse_while_loop(input_str))
    
# Another method: using reversed iteration

def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    return s1 

input_str = 'ABCDEF'
if __name__ == "__main__":
    print('Reverse string using reverse iteration= ', reverse_join_reversed_iter(input_str)) 
    
# Another method: using temporary list

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list) 

input_str = 'ABCDEF'
if __name__ == "__main__":
    print('Reverse string using temporary list= ', reverse_list(input_str)) 
    
    
# Another method: using recursion

def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:] + s[0])  
    
s = 'ABCDEF'
if __name__ == "__main__":
    print('Reverse string using reverse recursion= ', reverse_recursion(s))  