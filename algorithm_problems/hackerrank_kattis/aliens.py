#! /usr/bin/python3

import fileinput
import sys

def add_to_graph_values(from_node, to_node, graph=None):
    if graph is None:
        graph = {}
    if from_node in graph:
        if to_node not in graph[from_node]:
            if to_node != from_node:
                graph[from_node].append(to_node)
    else:
        graph[from_node] = [to_node]
    if to_node not in graph:
        graph[to_node] = []
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
            if first[c] != second[c]:
                if c > 0:
                    if first[c-1] != second[c-1]:
                        break
                aliens_graph = add_to_graph_values(first[c], second[c], aliens_graph)
                
        except IndexError:
             pass
        c += 1
    i += 1

result = khan_topo(aliens_graph)

print(' '.join(map(str, result)))
