# Used to find all paths from a start node
# Works with negative edges

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

def bellman_ford(graph, start):

    graph[start].distance = 0

    for i in range(len(graph.nodes)-1):
        for node in graph.nodes:
            for neighbor in graph[node].edges:
                if graph[node].distance + neighbor.cost < graph[neighbor.to].distance:
                    graph[neighbor.to].distance = graph[node].distance + neighbor.cost
    

    all_places = list(graph.nodes.keys())
    all_places.sort()
    for name in all_places:
        print(name, ": ", graph[name].distance, sep="")

if __name__ == '__main__':

    # Create a graph and add all nodes, and all edges
    graph = Graph()
    graph.add(Node("Bookworks", [Edge("Home",95), Edge("Aquarium",-50)]))
    graph.add(Node("Home", [Edge("Aquarium",150), Edge("Starbucks",12), Edge("Beach",-100)]))
    graph.add(Node("Beach", [Edge("Starbucks",55)]))
    graph.add(Node("Aquarium", [Edge("Bookworks",50)]))
    graph.add(Node("Starbucks", [Edge("Carmel",200)]))
    graph.add(Node("Carmel", [Edge("Home",-100)]))

    # Run Bellman Ford
    bellman_ford(graph, "Home")
