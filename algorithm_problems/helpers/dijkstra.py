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
            distance = "∞" if node.distance == sys.maxsize else node.distance
            print("Node:", name, "Distance:", distance)
    
    def reset_dist(self):
        for name, node in self.nodes.items():
            node.distance = sys.maxsize

def best_first(graph, start, visited=[]):
    visited.append(start)
    print("Visited:", start)
    for edge in graph[start].edges:
        if edge.to not in visited:
            best_first(graph, edge.to, visited)
    return visited

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
    
if __name__ == '__main__':
    # Create a graph and add all nodes, and all edges
    graph = Graph()
    graph.add(Node("A", [Edge("B",3), Edge("D",3), Edge("G",1)]))
    graph.add(Node("B", [Edge("A",3), Edge("C",5)]))
    graph.add(Node("C", [Edge("B",5), Edge("E",6), Edge("F",4), Edge("H",2)]))
    graph.add(Node("D", [Edge("A",3), Edge("F",7)]))
    graph.add(Node("E", [Edge("C",6)]))
    graph.add(Node("F", [Edge("C",4), Edge("D",7), Edge("G",8), Edge("H",1)]))
    graph.add(Node("G", [Edge("A",1), Edge("F",8), Edge("H",4)]))
    graph.add(Node("H", [Edge("C",2), Edge("F",1), Edge("G",4)]))
    graph.add(Node("Z", [Edge("Y",2)]))
    graph.add(Node("Y", [Edge("Z",2)]))

    # Shortest path between start and finish using Dijkstra's meathod
    print(dijkstra_shortest_path(graph, "A", "A"))
    print(dijkstra_shortest_path(graph, "A", "F"))
    print(dijkstra_shortest_path(graph, "A", "H"))
    print(dijkstra_shortest_path(graph, "H", "A"))
    print(dijkstra_shortest_path(graph, "A", "E"))
    print(dijkstra_shortest_path(graph, "A", "Z"))
