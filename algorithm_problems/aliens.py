#! /usr/bin/python3

import fileinput
import sys


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
    return paths[shortest_index]


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


def add_to_graph(from_node, to_node, all_nodes, graph=None):
    if graph is None:
        graph = {}
    if all_nodes[from_node] in graph:
        graph[all_nodes[from_node]].append(all_nodes[to_node])
    else:
        graph[all_nodes[from_node]] = [all_nodes[to_node]]

    return graph


def add_to_graph_values(from_node, to_node, graph=None):
    if graph is None:
        graph = {}
    if from_node in graph:
        graph[from_node].append(to_node)
    else:
        graph[from_node] = [to_node]
    return graph


def print_graph(graph):
    keys = graph.keys()
    for key in keys:
        print(key + " = " + str(graph[key]))


def print_header(text):
    print("\n" + text)


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


def visit_all(graph, all_nodes):
    num_nodes = len(all_nodes)
    all_paths = []
    i = 0
    while i < num_nodes:
        j = 0
        while j < num_nodes:
            if i != j:
                all_paths.extend(find_all_paths(graph, all_nodes[i], all_nodes[j]))
            j += 1
        i += 1

    full_paths = []
    for path in all_paths:
        if len(path) == num_nodes:
            full_paths.append(path)

    return full_paths


def get_all_nodes(graph):
    all_nodes = []
    keys = graph.keys()
    for key in keys:
        all_nodes.append(key)
        all_nodes.extend(graph[key])
    return list(set(all_nodes))


line_num = 0
words = []
num_words = None
aliens_graph = {}

for line in fileinput.input():
    
    line = line.rstrip("\n")
    
    if line_num == 0:
        num_words = int(line)
        
    elif line_num <= num_words:
        words.append(line)

    line_num += 1

i = 0
while i < num_words-1:
    first = words[i]
    second = words[i+1]
    c = 0
    for char in words[i]:
        try:
            char_next = words[i+1][c]
            if char not in aliens_graph:
                if char != char_next:
                    aliens_graph = add_to_graph_values(char, char_next, aliens_graph)
            elif char_next not in aliens_graph[char] and char != char_next:
                aliens_graph = add_to_graph_values(char, char_next, aliens_graph)

        except IndexError:
            pass
        c += 1
    i += 1

nodes = get_all_nodes(aliens_graph)
result = visit_all(aliens_graph, nodes)[0]

print(', '.join(map(str, result)))
