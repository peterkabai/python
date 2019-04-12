#! /usr/bin/python3

# https://csumb.kattis.com/problems/dyslectionary

import fileinput

category = []

def print_out(category):
    
    longest = 0
    item_num = 0
    for item in category:
        if len(item) > longest:
            longest = len(item)
    
    for item in category:
        category[item_num] = category[item_num][::-1]
        item_num += 1
        
    category.sort()
    
    item_num = 0
    for item in category:
        category[item_num] = category[item_num][::-1]
        item_num += 1
     
    for item in category:
        while(len(item) < longest):
            item = " " + item
        print(item)
        
    return []
    
for line in fileinput.input(["input_output/dyslectionary_in_0.txt"]):
    
    line = line.rstrip("\n")
    if line != "":
        category.append(line)
    else:
        category = print_out(category)
        print("")
        
category = print_out(category)
    
    

