import math

def search(value, arr, index = -1):
    
    print(arr)
    
    middle = math.floor(len(arr)/2)

    if index == -1:
        index = middle
        
    if arr[middle] == value:
        return "Found" + str(index)
        
    elif arr[0] == arr[len(arr)-1]:
        return "Not Found"
    
    elif arr[middle] > value:
        index = index - middle
        return search(value, arr[0:middle], index)
        
    elif arr[middle] < value:
        index = index + (len(arr) - middle)
        return search(value, arr[middle:len(arr)], index)
    
    return "Not Found"

print(search(11,[1,2,3,5,9,11,20,24,35,36,37,45,49,50]))
print(search(1,[1,2,3,5,9,11,20,24,35,36,37,45,49,50]))
print(search(49,[1,2,3,5,9,11,20,24,35,36,37,45,49,50]))
print(search(0,[1,2,3,5,9,11,20,24,35,36,37,45,49,50]))