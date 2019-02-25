#! /usr/bin/python3

import fileinput

line_num = 0
input_list = []

for line in fileinput.input(["input_output/insertion_sort_in_0.txt"]):
    line = line.rstrip("\n")
    if line_num != 0:
        input_list.append(line)
    line_num += 1


def insertion_sort(arr):
    for index in range(1, len(arr)):
        curr = arr[index]
        pos = index
        while pos > 0 and arr[pos-1].split(" ")[2] > curr.split(" ")[2] \
                or (arr[pos-1].split(" ")[2] == curr.split(" ")[2] and arr[pos-1] > curr):
            arr[pos] = arr[pos-1]
            pos = pos - 1
        arr[pos] = curr
        
        for name in arr:
            print(name)
        if index != len(arr)-1:
            print("")

insertion_sort(input_list)
