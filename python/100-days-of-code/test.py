# File for testing small sections of code
def river_sizes(matrix):
    rivers = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
                new_river = get_river(matrix, row, col)
                rivers.append(new_river)
    return rivers        
                
def get_river(matrix, row, col):
    river_len = 1
    if row > 0:
        if matrix[row-1][col] == 1:
            matrix[row-1][col] = 0
            river_len += get_river(matrix, row-1, col)
    if col > 0:
        if matrix[row][col-1] == 1:
            matrix[row][col-1] = 0
            river_len += get_river(matrix, row, col-1)
    if row < len(matrix)-1:
        if matrix[row+1][col] == 1:
            matrix[row+1][col] = 0
            river_len += get_river(matrix, row+1, col)
    if col < len(matrix[0])-1:
        if matrix[row][col+1] == 1:
            matrix[row][col+1] = 0
            river_len += get_river(matrix, row, col+1)
    return river_len


matrix = [
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]]

print(river_sizes(matrix))