import dijkstra

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

def read_grid(d):
    grid = []
    for r in range(d):
        row = input().split(" ")
        grid.append(row)
    return grid

def get_pairs(grid, diagonal=False):
    d = len(grid)
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

    graph = dijkstra.Graph()

    # Creates a set of from points for the edges
    from_points = []
    for pair in point_pairs:
        from_points.append(str(pair.f))
    from_points = list(set(from_points))

    for point in from_points:
        edges = []
        for pair in point_pairs:
            if point == str(pair.f) and point != str(pair.t):
                edges.append(dijkstra.Edge(str(pair.t),1))
            
        graph.add(dijkstra.Node(str(point), edges))

    return graph
 
if __name__ == '__main__':
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
    print(dijkstra.dijkstra_shortest_path(graph, start, end)[1])
