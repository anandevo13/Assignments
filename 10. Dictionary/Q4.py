"""
Q. Write a python script to sort a dict according to VALUE
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
    print("Task3:- \n keys and values sorted in",
          "alphabetical order by the key")
    
    #Note that it will sort in lexicographical order for mathematical way, change it to float
    print(sorted(key_value.items(), key=lambda kv:(kv[1],kv[0])))
    
    
def main():
    # function calling
    dictionary()
    
#main function calling
if __name__ == "__main__":
    main()    
    
    
#Another Approach

from collections import OrderedDict
import numpy as np
 
dict = {'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)
 
keys = list(dict.keys())
values = list(dict.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
 
print(sorted_dict)