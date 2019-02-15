#! /usr/bin/python3

from simple_graph import *

graph_def = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C'],
    'X': ['Y', 'M']
}


print_header("Print Paths:")
print(find_path(graph_def, 'A', 'F'))
print(find_path(graph_def, 'A', 'D'))
print(find_all_paths(graph_def, 'A', 'D'))
print(find_shortest_path(graph_def, 'A', 'D'))
print(find_longest_path(graph_def, 'A', 'D'))

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'V']

graph_def = add_to_graph(0, 7, nodes, graph_def)
graph_def = add_to_graph(5, 7, nodes, graph_def)

print(find_path(graph_def, 'A', 'V'))

print_header("Print Graph:")
print_graph(graph_def)

# adds edge pairs
graph_def = add_edge_pairs([0, 1, 2, 3, 4, 5, 6, 7, 8], nodes, graph_def)

print_header("Print Graph:")
print_graph(graph_def)

visit_all(graph_def, nodes)

print_header("Unique Clusters:")
get_num_clusters(graph_def)


