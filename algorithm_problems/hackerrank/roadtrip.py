#! /usr/bin/python3

import fileinput
import sys

from simple_graph import *

line_num = 0
places = []
edge_pairs = []

k = None
from_place = None
num_places = None

for line in fileinput.input(["roadtrip_in_0.txt"]):
    
    line = line.rstrip("\n")
    
    if line_num == 0:
        k = int(line)

    elif line_num == 1:
        from_place = line

    elif line_num == 2:
        num_places = int(line)
        
    elif line_num <= num_places + 2:
        places.append(line)

    elif line_num > num_places + 3:
        edge_pairs.append(int(line.split(" ")[0]))
        edge_pairs.append(int(line.split(" ")[1]))

    line_num += 1

graph_def = add_edge_pairs(edge_pairs, places, {})

print_graph(graph_def)

print(find_all_paths(graph_def, from_place, "la"))

for place in get_k_away(graph_def, from_place, k):
    print(place)
