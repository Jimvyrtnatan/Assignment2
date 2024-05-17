import numpy as np

# Define a matrix with two dimensions and one with three dimensions
matrix_2d = np.array([[2, 4], [6, 8]])
matrix_3d = np.array([[[2, 4], [6, 8]], [[8, 6], [4, 2]]])

# Flatten matrix_2d using the flatten method
flat_matrix_2d = matrix_2d.flatten()

print(flat_matrix_2d)