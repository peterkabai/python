import sys

def floyd_warshall(matrix):

    # Do the v^3 Floyd Warshall itterations
    v = len(matrix)
    for i in range(v):
        for j in range(v):
            for k in range(v): 
                if  matrix[j][i] + matrix[i][k] < matrix[j][k]:
                    matrix[j][k] = matrix[j][i] + matrix[i][k]
    return matrix

def make_matrix(routes):

    # Create a list of all places
    names = []
    for route in routes:
        if route[0][0] not in names:
            names.append(route[0][0])
        if route[0][1] not in names:
            names.append(route[0][1])
    names.sort()

    # Create the matrix
    matrix = []
    v = len(names)
    for i in range(v):
        row = []
        for j in range(v):
            if i == j:
                row.append(0)
            else:
                row.append(999)
        matrix.append(row)

    # Add all initial values to the matrix
    for route in routes:
        row = names.index(route[0][0])
        col = names.index(route[0][1])
        dis = route[1]
        matrix[row][col] = dis
        matrix[col][row] = dis

    return names, matrix

def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print("")

def matrix_to_dict(matrix, names):
    starts = {}
    v = len(names)
    for i in range(v):
        start = {}
        for j in range(v):
            start[names[j]] = matrix[i][j]
        starts[names[i]] = start
    return starts

num_people = int(input())
people = []
for i in range(num_people):
    people.append(input())

num_services = int(input())
services = []
for i in range(num_services):
    services.append(input())

num_routes = int(input())
routes = []
for i in range(num_routes):
    values = input().split(", ")
    routes.append(((values[0],values[1]),int(values[2])))

names, matrix= make_matrix(routes)
matrix = floyd_warshall(matrix)
all_dist = matrix_to_dict(matrix, names)

people.sort()
services.sort()
print(" ".join(services))
for person in people:
    distances = []
    for service in services:
        distances.append(str(all_dist[service][person]))
    print(" ".join(distances), person)
