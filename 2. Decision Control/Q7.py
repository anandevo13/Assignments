"""
Q. Python srcipt to print a set of three words in dictionary order. Words are given by user.
"""

print("enter the three words: ")
a,b,c = input(), input(), input()

if a < b < c:
    print(a,b,c)
elif a < c < b:
    print(a,c,b)
elif b < c < a:
    print(b,c,a)
elif b < a < c:
    print(b,a,c)
elif c < a < b:
    print(c,a,b)
else:
    print(c,b,a)

# Another method 

print("enter the three words: ")

a,b,c = input(), input(), input()

x = min(a,b,c)
print(x)

if x == a:
    print(min(b,c), max(b,c))
elif x == b:
    print(min(a,c),max(a,c))
else:
    print(min(a,b), max(a,b))
