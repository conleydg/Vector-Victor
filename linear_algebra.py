

class ShapeError(Exception):
    pass

def shape(vector):
    try:
        return len(vector), len(vector[0])
    except:
        return len(vector),

def vector_add(vector_one, vector_two):
    if shape(vector_one) != shape(vector_two):
        raise ShapeError
    return [(a + b) for a, b in zip(vector_one, vector_two)]


def vector_sub(vector_one, vector_two):
    if shape(vector_one) != shape(vector_two):
        raise ShapeError
    return [(a - b) for a, b in zip(vector_one, vector_two)]

def vector_sum(*args):
    length = [len(i) for i in args]
    if max(length) != min(length):
        raise ShapeError
    return [sum(a) for a in zip(*args)]

def dot(vector_one, vector_two):
    if shape(vector_one) != shape(vector_two):
        raise ShapeError
    return sum([(a * b) for a, b in zip(vector_one, vector_two)])


def vector_multiply(vector, scaler):
    return [(a * scaler) for a in vector]

def vector_mean(*args):
    return [sum(a)/len(args) for a in zip(*args)]

def magnitude(vector):
    list_of_squares = [(a**2) for a in vector]
    list_of_sum_of_squares = sum(list_of_squares)
    return list_of_sum_of_squares ** .5

def matrix_row(matrix, index):
    return matrix[index]

def matrix_col(matrix, index):
    return [arg[index] for arg in matrix]

def matrix_add(matrix_one, matrix_two):
     return [vector_add(a, b) for a, b in zip(matrix_one, matrix_two)]

def matrix_sub(matrix_one, matrix_two):
    return [vector_sub(a, b) for a, b in zip(matrix_one, matrix_two)]

def matrix_scalar_multiply(matrix, scaler):
    return [vector_multiply(vector, scaler) for vector in matrix]

def matrix_vector_multiply(matrix, vector_mult):
    return [dot(vector, vector_mult) for vector in matrix]

def matrix_matrix_multiply(matrix_one, matrix_two):
    if len(matrix_two) != len(matrix_one[0]):
        raise ShapeError
    return [matrix_vector_multiply(matrix_one, vector) for vector in matrix_two]
