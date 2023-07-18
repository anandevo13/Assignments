"""
Q. Python script to sort a list given by user.
"""

# Initialize array
arr = int(input("Enter the elements of the array: "))
temp = 0;

# Displaying elements of original array
print("elements of original array: ")
for i in range(0, len(arr)):
    print(arr[i], end = "")
    

# Sort the array in ascending order
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            
print()

# Displaying elements of the array after sorting
print("elements of array sorted in ascending order: ")
for i in range(0, len(arr)):
    print(arr[i], end = " ")       

    
# Another method

numbers = [1,3,4,2]

# Sorting list of integers in ascending
numbers.sort()
print(numbers)              