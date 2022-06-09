def square_matrix_simple(matrix=[]):
    matrix = matrix
    len_max = len(matrix)
    for l in range (len_max):
        matrix[l]=list(map(lambda x: x**2,matrix[l]))

    return matrix
