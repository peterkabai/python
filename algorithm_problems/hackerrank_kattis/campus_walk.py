#! /usr/bin/python3

import fileinput
import sys

from simple_graph import *

line_num = 0
places = []
edge_pairs = []
num_places = None
from_place = None
to_place = None

for line in fileinput.input(["campus_walk_in_2.txt"]):
    
    line = line.rstrip("\n")
    
    if line_num == 0:
        from_place = line

    elif line_num == 1:
        to_place = line

    elif line_num == 2:
        num_places = int(line)
        
    elif line_num <= num_places + 2:
        places.append(line)

    elif line_num > num_places + 3:
        edge_pairs.append(int(line.split(" ")[0]))
        edge_pairs.append(int(line.split(" ")[1]))

    line_num += 1

graph_def = add_edge_pairs(edge_pairs, places, {})
longest = find_longest_path(graph_def, from_place, to_place)

print(len(longest)-1)
