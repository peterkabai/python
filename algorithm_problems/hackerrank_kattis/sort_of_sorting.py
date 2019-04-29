#! /usr/bin/python3

# https://csumb.kattis.com/problems/sortofsorting

import fileinput

names = []
lines_to_go = 0

def perform_sortish(arr):
    arr.sort(key = lambda i: i[0:2])
    for val in arr:
        print(val)

for line in fileinput.input(["input_output/sort_of_sorting_in_0.txt"]):
    line = line.rstrip("\n")
    
    if lines_to_go == 0:
        if len(names) != 0:
            perform_sortish(names)
            print("")
            names = []
        lines_to_go = int(line)
        
    else:
        names.append(line)
        lines_to_go -= 1
        