#! /usr/bin/python3

import sys

def add_edge_pairs(edges, all_nodes, graph=None):
    if graph is None:
        graph = {}
    i = 0
    while i < len(edges)-1:
        from_node = edges[i]
        to_node = edges[i + 1]
        add_to_graph(from_node, to_node, all_nodes, graph)
        i += 2
    
    for node in all_nodes:
        if node not in list(graph.keys()):
            graph[node] = []
            
    return graph

def add_to_graph(from_node, to_node, all_nodes, graph=None):
    if graph is None:
        graph = {}
    if all_nodes[from_node] in graph:
        graph[all_nodes[from_node]].append(all_nodes[to_node])
    else:
        graph[all_nodes[from_node]] = [all_nodes[to_node]]
    return graph

def get_in_degrees(graph):
  degrees = []
  
  # create a dictionary of edges to each node
  temp = {}
  for key in graph.keys():
    for value in graph[key]:
      if value not in temp.keys():
        temp[value] = []
      temp[value].append(key)
  
  # count the in edges of each node
  for key in graph.keys():
    if key not in temp.keys():
      degrees.append(0)
    else:
      degrees.append(len(temp[key]))
  
  return(degrees)

def khan_topo(graph):
    ordering = []
  
    # count the in-degree each node
    nodes = graph.keys()
    degrees = get_in_degrees(graph)
    
    # create a queue of nodes with in-degree 0
    queue_of_zero = []
    for index, item in enumerate(nodes):
        if degrees[index] == 0:
            queue_of_zero.append(item)

    # while the queue is not empty
    while len(queue_of_zero) > 0:
        
        # add the first element in the queue to the ordering
        ordering.append(queue_of_zero[0])
        
        # decrement the in-degree of each of the first element’s neighbors.
        for neighbors in graph[queue_of_zero[0]]:
            for index, item in enumerate(nodes):
                if item == neighbors:
                    degrees[index] = degrees[index]-1
                    
                    # add any neighbors that now have in-degree 0 to the queue.
                    if degrees[index] == 0:
                        queue_of_zero.append(item)
        
        # remove the first element from the queue.
        del queue_of_zero[0]
    
    return ordering
  
def khan_topo_cycle(graph):
    return len(get_all_nodes(graph)) != len(khan_topo(graph))
    
def get_all_nodes(graph):
    all_nodes = []
    keys = graph.keys()
    for key in keys:
        all_nodes.append(key)
    return all_nodes
 
places = []
edge_pairs = []

num_places = int(input())

for p in range(num_places):
    places.append(input())
    
num_edges = int(input().split()[1])

for e in range(num_edges):
    edge = input().split()
    edge_pairs.append(int(edge[0]))
    edge_pairs.append(int(edge[1]))
    
graph = add_edge_pairs(edge_pairs, places, {})

if khan_topo_cycle(graph):
    print("Cycle!")
else:
    print("No Cycle!")