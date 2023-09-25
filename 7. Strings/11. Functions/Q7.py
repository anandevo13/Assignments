"""
Q. Python function which takes a tuple of int values and returns a dictionary whose each item is a pair 
of int value and its frequency in the tuple.
"""

def countFrequency(my_list):
    # creating a frequency
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
            
            
    for key,value in freq.items():
        print("%d:%d" %(key,value))
        
        
#Driver Function
if __name__ == "__main__":
    my_list = (1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2)
    countFrequency(my_list)

    
    
# Another method
def countFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for items in my_list:
        freq[items] = my_list.count(items)
     
    for key, value in freq.items():
        print("%d:%d" %(key,value))    
                
#Driver Function
if __name__ == "__main__":
    my_list = (1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2)
    countFrequency(my_list)         
    


# Another method
def countFrequency(my_list):
    # Creating an empty dictionary
    count = {}
    for items in my_list:
        count[items] = count.get(items,0) + 1
    return count    
        
#Driver Function
if __name__ == "__main__":
    my_list = (1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2)
    print(countFrequency(my_list))              
