#! /usr/bin/python3

# https://csumb.kattis.com/problems/lineup

import fileinput

names = []
first_line = True

for line in fileinput.input(["input_output/line_them_up_in_0.txt"]):
    line = line.rstrip("\n")
    if not first_line:
        names.append(line)
    else:
        first_line = False

increasing = names.copy()
increasing.sort()
decreasing = names.copy()
decreasing.sort(reverse=True)

if increasing == names:    
    print("INCREASING")
    
elif decreasing == names:
    print("DECREASING")
    
else:
    print("NEITHER")
 
    

