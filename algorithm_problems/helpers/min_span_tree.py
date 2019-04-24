def count_v(edges):
    seen = []
    v = 0
    for edge in edges:
        if edge[0][0] not in seen:
            seen.append(edge[0][0])
            v += 1
        if edge[0][1] not in seen:
            seen.append(edge[0][1])
            v += 1
    return v
  
def edges_to_dict(edges, directed=True):
    graph = {}
    for edge in edges:
        if edge[0][0] not in graph.keys():
            graph[edge[0][0]] = []
        if edge[0][1] not in graph.keys():
            graph[edge[0][1]] = []
        graph[edge[0][0]].append((edge[0][1],edge[1]))
        
        if not directed:
            if edge[0][1] not in graph.keys():
                graph[edge[0][1]] = []
            graph[edge[0][1]].append((edge[0][0],edge[1]))   
            
    return graph

def bfs_cycle_detect(graph, start):
       
    if len(graph) == 0:
        return False

    # Add the starting point to the queue and
    # The array of visited nodes
    queue = [start]
    visited = [start]
    
    # Until the queue of nodes is empty
    while queue:
        
        # Remove the first node in the queue
        current = queue.pop(0)
        
        # For all neighbors of the current node 
        for neighbor in graph[current[0]]:
            
            # If we haven't seen it before
            if neighbor not in visited:
                
                # Add to the back of the queue 
                # And to the queue of visited nodes
                queue.append(neighbor)
                visited.append(neighbor) 
            else: 
                return True
    return False
    
def min_span_tree(edges):
    graph = edges_to_dict(edges)
    edges = sorted(edges, key=lambda x: x[1])
    min_tree, output, length = [], [], 0
    while len(min_tree) <= count_v(edges):
        next_v = edges[0]
        if next_v not in min_tree:
            temp = min_tree[:]
            temp.append(next_v)
            graph = edges_to_dict(temp)
            cycle = bfs_cycle_detect(graph, next_v[0][0])
            if not cycle:
                output.append(edges[0][0])
                length += edges[0][1]
                min_tree = temp[:]
        edges = edges[1:]        
    return output, length
  
# Example 1
edges_1 = [
    [("A", "G"), 1],
    [("B", "A"), 3],
    [("D", "C"), 4],
    [("D", "B"), 6],
    [("E", "B"), 9],
    [("F", "A"), 5],
    [("G", "C"), 14],
    [("G", "D"), 18],
    [("G", "E"), 11],
]

edges_2 = [
    [("H", "G"), 1 ],
    [("I", "C"), 2 ],
    [("6", "F"), 2 ],
    [("A", "B"), 4 ],
    [("C", "F"), 4 ],
    [("8", "G"), 6 ],
    [("C", "D"), 7 ],
    [("H", "I"), 7 ],
    [("A", "H"), 8 ],
    [("B", "C"), 8 ],
    [("D", "E"), 9 ],
    [("F", "E"), 10],
    [("B", "H"), 11],
    [("D", "F"), 14]
]
pairs, length = min_span_tree(edges_1)
print(length, pairs)


