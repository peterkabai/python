#! /usr/bin/python3

def merge_interval(arr_in):
    changed = False
    if len(arr_in) <= 1:
        return arr_in
    merged = []
    arr_in.sort(key = lambda i: i[0])
    i = 1
    while i < len(arr_in):
        x1 = arr_in[i-1][0]
        x2 = arr_in[i-1][1]
        y1 = arr_in[i][0]
        y2 = arr_in[i][1]
        if  x2 > y1:
            changed = True
            if x2 > y2:
                merged.append([x1, x2])
            else:
                merged.append([x1, y2])
        else:
            merged.append([x1, x2])   
        i += 1
    
    if changed:
        merged = merge_interval(merged)
    return merged
   
print(merge_interval([[8,13]]))
print(merge_interval([]))
print(merge_interval([[8,13],[1,3],[4,5],[11,17]]))
print(merge_interval([[0,5],[1,4],[3,6]]))
print(merge_interval([[9,12],[8,13]]))
