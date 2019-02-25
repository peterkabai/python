#! /usr/bin/python3

import fileinput

data = []
 
def size():
    print(len(data))
    
def maxLookup():
    print(data[0])
    
def insert(value):
    data.append(int(value))
    length = len(data)
    for index in range(length, -1, -1):
        heapify(data, length, index)
    
def extractMax():
    del data[0]
    length = len(data)
    for index in range(length, -1, -1):
        heapify(data, length, index)
    
def delete(pos):
    del data[int(pos)]
    length = len(data)
    for index in range(length, -1, -1):
        heapify(data, length, index)

def heapify(arr, length, index):
    largest = index
    left = 2 * index + 1 
    right = 2 * index + 2
  
    if left < length and arr[index] < arr[left]: 
        largest = left 
  
    if right < length and arr[largest] < arr[right]: 
        largest = right
  
    if largest != index: 
        arr[index],arr[largest] = arr[largest], arr[index] 
        heapify(arr, length, largest) 
 
line_num = 0

# commands and function for each
switch = {
    "size": size,
    "maxLookup": maxLookup,
    "insert": insert,
    "extractMax": extractMax,
    "delete": delete
}

# read all the lines    
for line in fileinput.input(["input_output/max_binary_heap_in_0.txt"]):
    line = line.rstrip("\n")
    if line_num != 0:
        
        # get the correct function
        function = switch.get(line.split(" ")[0])
        
        # run function, with parameters if needed
        if (len(line.split(" ")) == 2):
            function(line.split(" ")[1])
        else:
            function()
            
    line_num += 1
