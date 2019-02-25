#! /usr/bin/python3

graph_def = {
    'A': [],
    'B': [],
    'C': ['D'],
    'D': ['B'],
    'E': ['A','B'],
    'F': ['A','C']
}

def print_dict(d):
    keys = d.keys()
    for key in keys:
        print(key + " = " + str(d[key]))

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
          
print(khan_topo_all(graph_def))
