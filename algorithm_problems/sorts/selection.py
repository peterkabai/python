#! /usr/bin/python3

# --- Selection Sort ---
# Selection sort takes the smallest element in an array, and swaps it to 
# the end of the sorted sub array in the first section of the array.
# This is done till the sorted array takes up the entire array.
# Selection sort is O(n^2) because it must itterate through 
# the array once for every value in the array.
# The space complexity is O(1) because it jsut swaps the values in the array, 
# and doesn't create any new data structures.

def selection_sort(arr, steps=False, reverse=False):
    step = 0;
    for i in range(len(arr)):
        
        # Gets the min or max of the sub array
        min_or_max = i
        for j in range(i, len(arr)):
            
            # Gets the condition for sorting normally or in reverse
            if not reverse:
                order = arr[min_or_max] > arr[j]
            else:
                order = arr[min_or_max] < arr[j]
                
            # Updates the min or max
            if order:
                min_or_max = j
            
        # Print the partially sorted array
        if steps:
            print("Step ", step , ": ", arr, sep="")
            step += 1
            
        # Does the swap 
        arr[i], arr[min_or_max] = arr[min_or_max], arr[i] 
    return arr


# Do a regular selection sort
print(selection_sort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]))

# Printing the intermediate steps
print(selection_sort([9,1,2,3,4,5,6,7,8], True))

# Reverse selection sort, with intermediate steps
print(selection_sort([9,1,2,3,4,5,6,7,8], True, True))