import numpy as np

# Define a matrix
A = np.array([[2, 4], [6, 8]])

# Calculate the inverse of A using the linalg.inv method
result = np.linalg.inv(A)

print(result)