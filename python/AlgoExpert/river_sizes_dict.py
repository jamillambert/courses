def river_sizes(matrix):
    visited = {}
    rivers = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1 and (row, col) not in visited:
                new_river = follow_river(matrix, row, col, visited)
                rivers.append(new_river)
    return rivers


def follow_river(matrix, row, col, visited):
    river_len = 0
    if (row, col) in visited:
        return river_len
    else:
        visited[(row, col)] = True
        river_len = 1
    if row > 0:
        if matrix[row-1][col] == 1:
            river_len += follow_river(matrix, row-1, col, visited)
    if col > 0:
        if matrix[row][col-1] == 1:
            river_len += follow_river(matrix, row, col-1, visited)
    if row < len(matrix)-1:
        if matrix[row+1][col] == 1:
            river_len += follow_river(matrix, row+1, col, visited)
    if col < len(matrix[row])-1:
        if matrix[row][col+1] == 1:
            river_len += follow_river(matrix, row, col+1, visited)
    return river_len


matrix = [
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]]

print(river_sizes(matrix))
