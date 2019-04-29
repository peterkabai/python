#! /usr/bin/python3

import fileinput

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

def get_all_nodes(graph):
    all_nodes = []
    keys = graph.keys()
    for key in keys:
        all_nodes.append(key)
    return all_nodes
    
def khan_topo_all_util(visited, degrees, stack, graph, nodes, all_topos=None):
    
    if all_topos is None: all_topos = []
    
    got_all = False
    for i in range(len(nodes)):
        if not visited[i] and degrees[i] == 0:
            visited[i] = True
            stack.append(nodes[i])
            
            # decriment the degrees as with normal khans
            for neighbors in graph[nodes[i]]:
                for index, item in enumerate(nodes):
                    if item == neighbors:
                        degrees[index] = degrees[index]-1
            
            # recursive call, runs each time an unvisited node is 0
            all_topos.extend(khan_topo_all_util(visited, degrees, stack, graph, nodes))
            
            # backtracking here
            visited[i] = False
            del stack[-1]
            for neighbors in graph[nodes[i]]:
                for index, item in enumerate(nodes):
                    if item == neighbors:
                        degrees[index] = degrees[index]+1
                
            got_all = True
            
    # adds the new topo to the list of all topos
    if not got_all:
        new_topo = []
        for node in stack:
            new_topo.append(node)
        all_topos.append(new_topo)
        
    return all_topos
    
def khan_topo_all(graph):
    degrees = get_in_degrees(graph)
    nodes = get_all_nodes(graph)
    visited = []
    
    # create an array of false values
    for index in range(len(nodes)):
        visited.append(False)
        
    return khan_topo_all_util(visited, degrees, [], graph, nodes)

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

line_num = 0
places = []
num_cities = None
edge_pairs = []

for line in fileinput.input():
    
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

all_topos = khan_topo_all(graph_def)

list_of_lists = []
for topo in all_topos:
    list_of_lists.append(', '.join(map(str, topo)))
    
list_of_lists.sort()
for l in list_of_lists:
    print(l)
