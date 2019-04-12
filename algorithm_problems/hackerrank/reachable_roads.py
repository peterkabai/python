#! /usr/bin/python3

# https://csumb.kattis.com/problems/reachableroads


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

def find_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end):
    shortest = sys.maxsize
    shortest_index = -1
    index = 0
    paths = find_all_paths(graph, start, end)
    for path in paths:
        if len(path) < shortest:
            shortest = len(path)
            shortest_index = index
        index += 1
    try:
        return paths[shortest_index]
    except IndexError:
        pass

def find_longest_path(graph, start, end):
    longest = 0
    longest_index = -1
    index = 0
    paths = find_all_paths(graph, start, end)
    for path in paths:
        if len(path) > longest:
            longest = len(path)
            longest_index = index
        index += 1
    return paths[longest_index]
  
  
  
cities = int(input())

for i in range(cities):
    all_nodes = []
    
    ends = int(input())
    roads = int(input())
    endpoints = []
    for r in range(roads):
        line = input().split()
        endpoints.extend(line)
    endpoints.sort()
    needed = 0
    i = 1
    print(endpoints)
    graph = add_edge_pairs(endpoints, ['0','1','2','3','4'])
    
    
    
    print(needed)
        
    


    
# --- Sample 1 ---
# 2
# 5
# 3
# 0 1
# 1 2
# 3 4
# 2
# 1
# 0 1

# 1
# 0