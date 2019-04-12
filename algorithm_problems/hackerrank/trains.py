#! /usr/bin/python3

import fileinput
import sys

def print_graph(graph):
    keys = graph.keys()
    for key in keys:
        print(key + " = " + str(graph[key]))
        
def add_to_graph(from_node, to_node, all_nodes, graph=None):
    if graph is None:
        graph = {}
    if all_nodes[from_node] in graph:
        graph[all_nodes[from_node]].append(all_nodes[to_node])
    else:
        graph[all_nodes[from_node]] = [all_nodes[to_node]]
    return graph
          
def add_edge_pairs(edges, all_nodes, graph=None):
    if graph is None:
        graph = {}
    i = 0
    while i < len(edges)-1:
        from_node = edges[i]
        to_node = edges[i + 1]
        add_to_graph(from_node, to_node, all_nodes, graph)
        i += 2
    return graph       

def bfs_cluster_util(graph, start=None, visited=None, clusters=None):
    
    # initialize optional vatiables
    if start is None: start = next(iter(graph))
    if clusters is None: clusters = 0
    if visited is None: visited = []
    
    # this keeps track of how many clusters have had BFS done
    clusters += 1
        
    # add the starting point to the queue and
    # the array of visited nodes
    queue = []
    queue.append(start)
    visited.append(start)
    
    # untill the queue of nodes is empty
    while queue:
        
        # remove the first node in the queue
        current = queue.pop(0)
        
        # for all neighbors of the current node 
        for neighbor in graph[current]:
            
            # if we haven't seen it before
            if neighbor not in visited:
                
                # add to the back of the queue 
                # and to the queue of visited nodes
                queue.append(neighbor)
                visited.append(neighbor) 
    
    # check to see if all nodes in the graph have been visited
    for node in graph.keys():
         if node not in visited:
             
             # start bfs at a new unvisited node
             clusters = bfs_cluster_util(graph, node, visited, clusters)
             break
    
    return clusters
    
def count_clusters(graph):
    return bfs_cluster_util(graph) 
    
line_num = 0
places = []
edge_pairs = []
num_places = None

for line in fileinput.input():
    
    line = line.rstrip("\n")
    
    if line_num == 0:
        num_places = int(line)
        
    elif line_num <= num_places:
        places.append(line)

    elif line_num > num_places + 1:
        edge_pairs.append(int(line.split(" ")[0]))
        edge_pairs.append(int(line.split(" ")[1]))

    line_num += 1

graph_def = add_edge_pairs(edge_pairs, places, {})

print(count_clusters(graph_def))
