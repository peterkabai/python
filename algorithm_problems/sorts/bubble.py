#! /usr/bin/python3

# --- Bubble Sort ---
# The larger values "bubble up" towards the end of the array.
# If a value is bigger than the following value, they swap places.
# This repeats over the array, till no swaps are made.
# This means, bubble sort is O(n^2) and space complexity is O(1) 
# Best case time complexity is O(n) if the array is already sorted

def bubble_sort(arr, steps=False, reverse=False):
    swaped = True
    step = 0;
    
    # Terminates when there's a full loop without a swap
    while swaped:
        swaped = False
        for i in range(len(arr)-1):
            
            if not reverse:
                order = arr[i] > arr[i+1] # Regular
            else:
                order = arr[i] < arr[i+1] # Reversed
            
            if order:
                
                # Print the partially sorted array
                if steps:
                    print("Step ", step , ": ", arr, sep="")
                    step += 1
                
                # Swap the two values
                arr[i], arr[i+1] = arr[i+1], arr[i]
                
                # Set the swaped flag to true, to cont. the loop
                swaped = True
    if steps:
        print("Step ", step , ": ", arr, sep="")
    return(arr)
    
# Regular bubble sort
print(bubble_sort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]))

# Printing the intermediate steps
print(bubble_sort([9,1,2,3,4,5,6,7,8], True))

# Reverse bubble sort, with intermediate steps
print(bubble_sort([9,1,2,3,4,5,6,7,8], True, True))
