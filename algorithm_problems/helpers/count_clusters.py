#! /usr/bin/python3

def bfs(graph, start):
       
    # add the starting point to the queue and
    # the array of visited nodes
    queue = [start]
    visited = [start]
    
    # untill the queue of nodes is empty
    while queue:
        
        # remove the first node in the queue
        current = queue.pop(0)
        print(current)
        
        # for all neighbors of the current node 
        for neighbor in graph[current]:
            
            # if we haven't seen it before
            if neighbor not in visited:
                
                # add to the back of the queue 
                # and to the queue of visited nodes
                queue.append(neighbor)
                visited.append(neighbor) 
                
def bfs_clusters(graph, start=None, visited=None, clusters=None):
    
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
             clusters = bfs_clusters(graph, node, visited, clusters)
             break
    
    return clusters

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited)
    return visited
        
        
graph = {
    'A': ['B', 'C'],
    'B': ['A','C', 'D'],
    'C': ['D','F','A'],
    'D': ['C','B'],
    'E': ['F'],
    'F': ['C','E'],
    'X': ['Y', 'M'],
    'Y': ['X'],
    'M': ['X'],
    'T': ['S'],
    'S': ['T'],
    'L': []
}
bfs(graph, "A")
print(dfs(graph, "A"))
print(bfs_clusters(graph))