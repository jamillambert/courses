def river_sizes(matrix):
    rivers = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
                matrix, new_river = get_river(matrix, row, col)
                rivers.append(new_river)
    print(rivers)         
                
def get_river(matrix, row, col):
    river_len = 1
    if row > 1:
        if matrix[row-1][col] == 1:
            matrix[row-1][col] = 0
            matrix, extra_length = get_river(matrix, row-1, col)
            river_len += extra_length
    if col > 1:
        if matrix[row][col-1] == 1:
            matrix[row][col-1] = 0
            matrix, extra_length = get_river(matrix, row, col-1)
            river_len += extra_length
    if row < len(matrix)-2:
        if matrix[row+1][col] == 1:
            matrix[row+1][col] = 0
            matrix, extra_length = get_river(matrix, row+1, col)
            river_len += extra_length
    if col < len(matrix[0])-2:
        if matrix[row][col+1] == 1:
            matrix[row][col+1] = 0
            matrix, extra_length = get_river(matrix, row, col+1)
            river_len += extra_length
    return matrix, river_len


matrix = [
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]]

river_sizes(matrix)