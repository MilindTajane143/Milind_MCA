def matrix_sum(matrix1, matrix2):
    # Ensure matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions to compute the sum.")
    
    # Add the corresponding elements of the two matrices
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def matrix_product(matrix1, matrix2):
    # Ensure the number of columns in matrix1 matches the number of rows in matrix2
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in matrix1 must equal the number of rows in matrix2 to compute the product.")
    
    # Compute the product of the matrices
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
               for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    return result

# Example usage
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Compute sum and product
try:
    sum_result = matrix_sum(matrix1, matrix2)
    print("Sum of the matrices:")
    for row in sum_result:
        print(row)
    
    product_result = matrix_product(matrix1, matrix2)
    print("\nProduct of the matrices:")
    for row in product_result:
        print(row)
except ValueError as e:
    print(e)
