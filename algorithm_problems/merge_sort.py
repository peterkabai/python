#! /usr/bin/python3

import fileinput
from collections import deque

line_num = 0
input_list = []

for line in fileinput.input(["input_output/merge_sort_in_0.txt"]):
    line = line.rstrip("\n")
    if line_num != 0:
        input_list.append(line)
    line_num += 1
  
def mergeSort(arr):

    size = 1
    while size < len(arr) - 1:
        left = 0
        while left < len(arr) - 1:
            mid = left + size - 1

            right = ((2 * size + left - 1, len(arr) - 1)[2 * size + left - 1 > len(arr)-1])

            n1 = mid - left + 1
            n2 = right - mid
            L = [0] * n1
            R = [0] * n2
            for i in range(0, n1):
                L[i] = arr[left + i]
            for i in range(0, n2):
                R[i] = arr[mid + i + 1]


            i, j, k = 0, 0, left
            while i < n1 and j < n2:
                if L[i].split(" ")[2] > R[j].split(" ")[2] or (L[i].split(" ")[2] == R[j].split(" ")[2] and L[i] > R[j]):
                    arr[k] = R[j]
                    j += 1
                else:
                    arr[k] = L[i]
                    i += 1
                k += 1

            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

            for name in arr:
                print(name)
            print("")

            left = left + size * 2

        size = 2 * size
        
mergeSort(input_list)
