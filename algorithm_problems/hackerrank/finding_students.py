#! /usr/bin/python3

import fileinput

# do binary search here
def find(value, items, low=0, high=None, count=None):
    high = len(items) if high is None else high
    count = 1 if count is None else count + 1
    
    pos = (int) (low + (high - low) / 2)
    if pos == len(items):
        return -1, count - 1
    elif items[pos] == value:
        return pos, count
    elif high == low:
        return -1, count - 1 
    elif items[pos] < value:
        return find(value, items, pos + 1, high, count)
    else:
        assert items[pos] > value
        return find(value, items, low, pos, count)
   
line_num = 0
names = []
num_names = 0
 
for line in fileinput.input():
    
    line = line.rstrip("\n")
     
    if line_num == 0:
        num_names = int(line)
    elif line_num <= num_names:
        names.append(line.split(" ")[0])
    elif line_num > num_names+1:
        index, passes = find(line, names)
        print(str(index) + ": " + str(passes))
    line_num += 1