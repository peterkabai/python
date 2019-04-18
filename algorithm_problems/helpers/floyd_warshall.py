# Used to find all paths from all nodes
# Works with negative edges, but not negative cycles

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

if __name__ == '__main__':
    places = [ 
        (('C', 'R'), 15),
        (('R', 'Q'), 155),
        (('R', 'T'), 15),
        (('C', 'T'), 35),
        (('Q', 'H'), 15),
        (('R', 'J'), 30),
        (('J', 'H'), 115),
        (('R', 'E'), 300),
        (('E', 'H'), 60)
    ]

names, matrix= make_matrix(places)
matrix = floyd_warshall(matrix)
all_dist = matrix_to_dict(matrix, names)

for dist in all_dist.keys():
    print(dist, ":", all_dist[dist])

