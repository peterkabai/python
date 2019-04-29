def find_sub_square(size, matrix):
    # Creates a list of top left corners for all 1x1 squares
    corners = []
    for row in range(size):
        for col in range(size):
            value = matrix[row][col]
            if value == '0':
                corners.append((row,col))

    # If there are no initial corners for 1x1 squares then return zero
    # This happens if there are no 0's at all in the matrix
    if len(corners) == 0:
        return 0

    # Here's the iterative dynamic part
    # We knw there's at least one 1x1 square so the sub size is set to 1
    sub_size = 1

    while(True):

        # We define a new list of corners
        next_corners = []
        for corner in corners:
            row = corner[0]
            col = corner[1]
            valid = True

            # For each corner, we check to see if a (sub_size+1)x(sub_size+1) square would be valid
            for shift in range(sub_size+1):
                if row+shift < size and col+shift < size and row+sub_size < size and col+sub_size < size:
                    if matrix[row+shift][col+sub_size] != '0':
                        valid = False
                    elif matrix[row+sub_size][col+shift] != '0':
                        valid = False
                else:
                    valid = False
            if valid:
                next_corners.append(corner)

        # If a (sub_size+1)x(sub_size+1) square would be valid then we continue, otherwise break
        corners = next_corners
        if len(corners) != 0:
            sub_size += 1
        else:
            break

    return(sub_size)

# Read in the input
matrix = []
size = int(input())
for line in range(size):
    matrix.append(input().split(" "))

print(find_sub_square(size, matrix))
