def add_matrices(matrix1, matrix2):
    # Check if dimensions are the same
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def multiply_matrices(matrix1, matrix2):
    # Check if matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum_product = 0
            for k in range(len(matrix2)):
                sum_product += matrix1[i][k] * matrix2[k][j]
            row.append(sum_product)
        result.append(row)
    
    return result

# Example usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
]

matrix2 = [
    [7, 8, 9],
    [1, 2, 3],
]

# Matrix Addition
sum_result = add_matrices(matrix1, matrix2)
print("Sum of matrices:")
for row in sum_result:
    print(row)

# Matrix Multiplication
matrix3 = [
    [1, 2],
    [3, 4],
    [5, 6],
]

multiplication_result = multiply_matrices(matrix1, matrix3)
print("\nMultiplication of matrices:")
for row in multiplication_result:
    print(row)
