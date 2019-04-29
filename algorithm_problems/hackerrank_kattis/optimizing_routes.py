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
    all_dist = {}

    for i in range(len(graph.nodes)-1):
        for node in graph.nodes:
            for neighbor in graph[node].edges:
                if graph[node].distance + neighbor.cost < graph[neighbor.to].distance:
                    graph[neighbor.to].distance = graph[node].distance + neighbor.cost

    all_places = list(graph.nodes.keys())
    all_places.sort()
    for name in all_places:
        all_dist[name] = graph[name].distance
    return all_dist

if __name__ == '__main__':

    dictionary = {}
    start = input()
    num_routes = int(input())

    routes = []
    for line in range(num_routes):
        values = input().split(", ")
        routes.append((values[0],values[1]))
    
    dictionary = {}
    num_nodes = int(input())
    for line in range(num_nodes):
        values = input().split(", ")
        if values[0] not in dictionary:
            dictionary[values[0]] = []
        if values[1] not in dictionary:
            dictionary[values[1]] = []
        dictionary[values[0]].append((values[1],values[2]))
    
    graph = Graph()

    for node in dictionary.keys():
        edges = []
        for edge in dictionary[node]:
            edges.append(Edge(edge[0],int(edge[1])))
        graph.add(Node(node, edges))

    all_distances = bellman_ford(graph, "Home")

    routes = sorted(list(routes), key=lambda x: x[0].upper())

    for route in routes:
        current = int(route[1])
        best = all_distances[route[0]]
        if best == current:
            result = "FASTEST"
        elif best < current:
            result = str(current- best)
        else:
            result = "NO PATH"
        print(route[0], result)
