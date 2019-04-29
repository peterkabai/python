import sys

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
    
    def add(self, edge):
        self.edges.append(edge)
        self.edges.sort()

    def __gt__(self, other):
        return self.distance > other.distance

    def __lt__(self, other):
        return self.distance < other.distance

class Graph():
    def __init__(self):
        self.nodes = {}

    def __getitem__(self, key):
        return self.nodes[key]

    def add(self, node):
        self.nodes[node.name] = node

    def print(self):
        for name, node in self.nodes.items():
            distance = "inf" if node.distance == sys.maxsize else node.distance
            print("Node:", name, "Distance:", distance)
    
    def reset_dist(self):
        for name, node in self.nodes.items():
            node.distance = sys.maxsize

class Point(object):
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __str__(self):
        return str(self.r) + " " + str(self.c)

class Pair(object):
    def __init__(self, f, t):
        self.f = f
        self.t = t

def dijkstra_shortest_path(graph, start, finish):

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
    
def read_grid(d):
    grid = []
    for r in range(d):
        row = input().split(" ")
        grid.append(row)
    return grid

def get_pairs(grid, diagonal=False):
    edges = []
    r = 0
    for row in grid:
        c = 0
        for value in row:
            if value is "O":
                # Check above
                try:
                    if r is not 0 and grid[r-1][c] is not "X":
                        f = Point(r,c)
                        t = Point(r-1,c)
                        edges.append(Pair(f,t))
                except IndexError:
                    pass
                # Check below
                try:
                    if r is not d-1 and grid[r+1][c] is not "X":
                        f = Point(r,c)
                        t = Point(r+1,c)
                        edges.append(Pair(f,t))
                except IndexError:
                    pass
                # Check left
                try:
                    if c is not 0 and grid[r][c-1] is not "X":
                        f = Point(r,c)
                        t = Point(r,c-1)
                        edges.append(Pair(f,t))
                except IndexError:
                    pass
                # Check right
                try:
                    if c is not d-1 and grid[r][c+1] is not "X":
                        f = Point(r,c)
                        t = Point(r,c+1)
                        edges.append(Pair(f,t))
                except IndexError:
                    pass
                # Check diagonals
                if diagonal:
                    # Check top-right
                    try:
                        if c is not d-1 and r is not 0 and grid[r-1][c+1] is not "X":
                            f = Point(r,c)
                            t = Point(r-1,c+1)
                            edges.append(Pair(f,t))
                    except IndexError:
                        pass
                    # Check top-left
                    try:
                        if c is not 0 and r is not 0 and grid[r-1][c-1] is not "X":
                            f = Point(r,c)
                            t = Point(r-1,c-1)
                            edges.append(Pair(f,t))
                    except IndexError:
                        pass
                    # Check bottom-right
                    try:
                        if c is not d-1 and r is not d-1 and grid[r+1][c+1] is not "X":
                            f = Point(r,c)
                            t = Point(r+1,c+1)
                            edges.append(Pair(f,t))
                    except IndexError:
                        pass
                    # Check bottom-left
                    try:
                        if c is not 0 and r is not d-1 and grid[r+1][c-1] is not "X":
                            f = Point(r,c)
                            t = Point(r+1,c-1)
                            edges.append(Pair(f,t))
                    except IndexError:
                        pass
            c += 1
        r += 1
    return edges

def print_pairs(edges):
    for edge in edges:
        print(edge.f, "to", edge.t)

def create_from_pairs(point_pairs):

    graph = Graph()

    # Creates a set of from points for the edges
    from_points = []
    for pair in point_pairs:
        from_points.append(str(pair.f))
    from_points = list(set(from_points))

    for point in from_points:
        edges = []
        for pair in point_pairs:
            if point == str(pair.f) and point != str(pair.t):
                edges.append(Edge(str(pair.t),1))
            
        graph.add(Node(str(point), edges))

    return graph
 
# Get the dimention, start, and end
# Start and end is in the format: row column
d = int(input())
start = input()
end = input()

# Read in the grid of O and X values
grid = read_grid(d)

# Get pairs of connected points. Use True to allow diagonal moves
point_pairs = get_pairs(grid, True)

# Greate a graph from the point pairs
graph = create_from_pairs(point_pairs)

# Print the shortest path length from start to end
print(dijkstra_shortest_path(graph, start, end)[1])
