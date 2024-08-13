def transposed(matrix:list[list[int]]):
    return [[row[x] for row in matrix] for x in range(len(matrix[0]))]