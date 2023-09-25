"""
Q. Python script to sort a dict according to KEY
"""

def dictionary():
    #Declare hash function
    key_value = {}
    
    #Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    print("key_value", key_value)
    
    #iterkeys() returns an iterator over the dictionary's keys
    for i in sorted(key_value.keys()):
        print(i,end="")
        
def main():
    #function calling
    dictionary()
    
#Main function calling
if __name__ == '__main__':
    main()   
    
# Another Approach

from collections import OrderedDict

dict = {'ravi':'10', 'rajnish':'9', 'sanjeev':'15', 'yash':'2', 'suraj':'32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)     

# Another Approach

def dictionary():
    #Declare hash function
    key_value = {}
    
    #Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    print("key_value", key_value)
    print("Task2:- \n keys and values sorted in",
          "alphabetical order by the key")
    
    #sorted(key_value) returns an iterator over the Dictionary's value
    #sorted in keys
    for i in sorted(key_value):
        print(i,key_value[i],end="")
        
def main():
    #function calling
    dictionary()
    
#main function calling
if __name__ == "__main__":
    main()            