#! /usr/bin/python3

import fileinput, math

line_num = 0
input_list = []

for line in fileinput.input(["input_output/quick_sort_in_0.txt"]):
    line = line.rstrip("\n")
    if line_num != 0:
        input_list.append(line)
    line_num += 1
  
def quick_sort(arr, low=0, high=None): 
    
    if high == None:
        high = len(input_list) - 1
    
    if low < high: 
        i = low - 1
        
        # this is where the pivot is set
        # TODO: figure out how to set pivot to give the correct partially sorted lists
        pivot = arr[high]
  
        for j in range(low, high):
            if arr[j].split(" ")[2] < pivot.split(" ")[2] or (pivot.split(" ")[2] == arr[j].split(" ")[2] and pivot > arr[j]):
                i = i + 1 
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
  
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        part = i + 1
  
        quick_sort(arr, low, part - 1) 
        quick_sort(arr, part + 1, high)
        
        for name in arr:
            print(name)
        print("")
        
quick_sort(input_list)
