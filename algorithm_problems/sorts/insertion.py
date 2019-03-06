#! /usr/bin/python3

# --- Insersion Sort ---
# Insersion sort takes each value, and compares it to all values to the left of it.
# If the value is larger, it gets inserted, if smaller, it checks the next value to the left.
# This means its time complexity is O(n^2)
# Since the array is changed only by swapping values, its space complexity is O(1)

def insertion_sort(arr, steps=False):
    step = 0
    for i in range(1, len(arr)):
        key = arr[i]
        
        # This is the index of the element one to the left of the current 
        j = i-1
        
        # Compare to all values left of the key element
        while j >= 0 and key < arr[j]:
            
            # Set the element right of the comparison to the one before
            arr[j+1] = arr[j]
            j -= 1
            
        # Insert the key if we reach the left of the array or if the 
        # key is larger than the one directly to the left of it 
        arr[j+1] = key
        
        # Print the partially sorted array
        if steps:
            print("Step ", step , ": ", arr, sep="")
            step += 1
            
    return arr
    
# Do a regular insersion sort
print(insertion_sort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]))

# Printing the intermediate steps
print(insertion_sort([9,8,3,2,5,4,6,7,1], True))
