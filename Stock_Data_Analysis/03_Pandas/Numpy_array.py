import numpy as np
A = np.array([[1, 2], [3, 4]])
print(A.ndim)
print(A.shape)
print(A.max(), A.mean(), A.min(), A.sum())
print(A[0, 1])
print(A.flatten())
print(A*A)

B = np.array([10, 100])
print(A*B)
print(A.dot(B))