#! /usr/bin/python3

# https://csumb.kattis.com/problems/mjehuric

import fileinput

numbers = []

for line in fileinput.input(["input_output/mjehuric_in_1.txt"]):
    line = line.rstrip("\n")
    numbers = line.split(" ")
    
sorted_numbers = numbers.copy()
sorted_numbers.sort()

while (numbers != sorted_numbers):
    i = 1
    while i < len(numbers):
        if numbers[i] < numbers[i-1]:
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            print(' '.join(map(str, numbers)))
        i += 1
     