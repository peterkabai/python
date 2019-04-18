import grids

class Edge():
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __lt__(self, other):
        return self.cost < other.cost

class Node():
    def __init__(self, name, edges=[]):
        self.name = name
        self.distance = sys.maxsize
        edges.sort()
        self.edges = edges
        self.estimate = None
    
    def add(self, edge):
        self.edges.append(edge)
        self.edges.sort()

    def __gt__(self, other):
        return self.estimate + self.distance > other.estimate + other.distance

    def __lt__(self, other):
        return self.estimate + self.distance < other.estimate + other.distance

class Graph():
    def __init__(self):
        self.nodes = {}

    def __getitem__(self, key):
        return self.nodes[key]

    def add(self, node):
        self.nodes[node.name] = node

    def print(self):
        for name, node in self.nodes.items():
            distance = "∞" if node.distance == sys.maxsize else node.distance
            print("Node:", name, "Distance:", distance)
    
    def reset_dist(self):
        for name, node in self.nodes.items():
            node.distance = sys.maxsize

def a_star_grid(graph, start, finish):

    end_row = int(finish.split(" ")[0])
    end_col = int(finish.split(" ")[1])

    # Return right away  if the start is the finish
    if start == finish:
        return [start], 0
    # Create a dictionary of shortest paths
    shortest_paths = {}
    for name, node in graph.nodes.items(): 
        shortest_paths[name] = [name]

    # Set the start node to a distance of zero, and put it in the queue
    graph[start].distance = 0
    queue = [graph[start]]
    finalized = []

    # While the queue is not empty
    while queue:

        # Sort and pop the queue, we want the node with the smallest distance
        queue.sort(reverse=True)
        current = queue.pop()
        
        # Loop through each unfinalized node using the edges of the current
        for edge in current.edges:
            if edge.to not in finalized:

                # Update the distance, if lower than previously
                if graph[edge.to].distance > current.distance + edge.cost:
                    graph[edge.to].distance = current.distance + edge.cost

                    # New for A*
                    name = graph[edge.to].name
                    r = int(name.split(" ")[0])
                    c = int(name.split(" ")[1])
                    graph[edge.to].estimate = abs(end_row-r) + abs(end_col-c)

                    # Store the new shortest path for the node 
                    shortest_paths[edge.to] = list(shortest_paths[current.name])
                    shortest_paths[edge.to].append(edge.to)

                # Add the node to the queue
                queue.append(graph[edge.to])
        
        # Exit the while loop if we are ready to finalize the finish node
        if current.name == finish:
            break

        # Finalize the node 
        finalized.append(current.name)
    path_distance = graph[current.name].distance
    graph.reset_dist()

    # Return a tuple of the path and distance, or a tupple with None if the path was not found
    if len(shortest_paths[finish]) == 1 and path_distance != 0:
        return None, None
    return shortest_paths[finish], path_distance

if __name__ == '__main__':
    # Get the dimention, start, and end
    # Start and end is in the format: row column
    d = int(input())
    start = input()
    end = input()
    
    # Read in the grid of O and X values
    grid = grids.read_grid(d)
    
    # Get pairs of connected points. Use True to allow diagonal moves
    point_pairs = grids.get_pairs(grid, False)
    
    # Greate a graph from the point pairs
    graph = grids.create_from_pairs(point_pairs)
 
    # Run A* on the grid
    a_star_grid(graph, start, end)
    print(a_star_grid(graph, start, end)[1])
