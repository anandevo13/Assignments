x = 75

def myfunc():
    global x
    x = x+1
    print(x)
    
myfunc()
print(x)