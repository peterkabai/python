#! /usr/bin/python3

import fileinput

for line in fileinput.input(["insersionSort.txt"]):
    
    line = line.rstrip("\n")
    print (line)
    