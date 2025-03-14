import numpy as np

#task1
vector = np.arange(10, 50)
print("Vector:", vector)

#task2
matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n3x3 Matrix:\n", matrix_3x3)

#task3
identity_matrix = np.eye(3)
print("\n3x3 Identity Matrix:\n", identity_matrix)

#task4
random_3x3x3 = np.random.rand(3, 3, 3)
print("\n3x3x3 Random Array:\n", random_3x3x3)

#task5
random_10x10 = np.random.rand(10, 10)
print("\n10x10 Random Array Min:", random_10x10.min(), "Max:", random_10x10.max())

#task6
random_vector = np.random.rand(30)
print("\nMean of Random Vector:", random_vector.mean())

#task7
random_5x5 = np.random.rand(5, 5)
normalized_5x5 = (random_5x5 - random_5x5.min()) / (random_5x5.max() - random_5x5.min())
print("\nNormalized 5x5 Matrix:\n", normalized_5x5)

#task8
matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
product_5x2 = np.dot(matrix_5x3, matrix_3x2)
print("\n5x3 * 3x2 Matrix Product:\n", product_5x2)

#task9
matrix_A = np.random.rand(3, 3)
matrix_B = np.random.rand(3, 3)
dot_product = np.dot(matrix_A, matrix_B)
print("\nDot Product of Two 3x3 Matrices:\n", dot_product)

#task10
matrix_4x4 = np.random.rand(4, 4)
transpose_4x4 = matrix_4x4.T
print("\nTranspose of 4x4 Matrix:\n", transpose_4x4)

#task11
matrix_3x3_det = np.random.rand(3, 3)
determinant = np.linalg.det(matrix_3x3_det)
print("\nDeterminant of 3x3 Matrix:", determinant)

#task12
matrix_A_3x4 = np.random.rand(3, 4)
matrix_B_4x3 = np.random.rand(4, 3)
matrix_product_A_B = np.dot(matrix_A_3x4, matrix_B_4x3)
print("\nMatrix Product (A 3x4 * B 4x3):\n", matrix_product_A_B)

#task13
matrix_3x3 = np.random.rand(3, 3)
vector_3x1 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3, vector_3x1)
print("\nMatrix-Vector Product:\n", matrix_vector_product)

#task14
A = np.random.rand(3, 3)
b = np.random.rand(3, 1)
x = np.linalg.solve(A, b)
print("\nSolution for Ax = b:\n", x)

#task15
matrix_5x5 = np.random.rand(5, 5)
row_sums = matrix_5x5.sum(axis=1)
col_sums = matrix_5x5.sum(axis=0)
print("\nRow-wise sums:", row_sums)
print("Column-wise sums:", col_sums)
