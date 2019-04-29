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
        for neighbor in graph[current]:
            
            # If we haven't seen it before
            if neighbor[0] not in visited:
                
                # Add to the back of the queue 
                # And to the queue of visited nodes
                queue.append(neighbor[0])
                visited.append(neighbor[0]) 
            else:
                return True
    return False
    
def min_span_tree(edges, directed=True):
    graph = edges_to_dict(edges, directed)
    edges = sorted(edges, key=lambda x: x[1])
    min_tree, output, length = [], [], 0
    v = count_v(edges)
    while len(min_tree) < v-1:
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
  
# Skip the names of the towns
num_towns = int(input())
for i in range(num_towns):
    town = input()

# Read in the roads
roads = []
num_roads = int(input())
for i in range(num_roads):
    line = input().split(", ")
    roads.append([(line[0], line[1]), int(line[2])])

pairs, length = min_span_tree(roads, False)
print(length)
# print(pairs)
