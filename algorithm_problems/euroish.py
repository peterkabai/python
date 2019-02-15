#! /usr/bin/python3

import fileinput

from simple_graph import *

line_num = 0
places = []
num_cities = None
edge_pairs = []

for line in fileinput.input(["euroish_3.txt"]):
    
    line = line.rstrip("\n")
    
    if line_num == 0:
        num_cities = int(line)
        
    elif line_num <= num_cities:
        places.append(line)

    elif line_num > num_cities + 1:
        edge_pairs.append(int(line.split(" ")[0]))
        edge_pairs.append(int(line.split(" ")[1]))

    line_num += 1

graph_def = add_edge_pairs(edge_pairs, places, {})

all_paths = visit_all(graph_def, places)

try:
    print(', '.join(map(str, all_paths[0])))
except IndexError:
    print(all_paths)
