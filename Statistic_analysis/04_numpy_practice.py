import numpy as np

# np.array
data1 = [0,1,2,3,4,5]
a1 = np.array(data1)
print(a1)
print(type(data1), type(a1))
print(a1.dtype)

b1=a1[1:3]
b1=a1[2:]
b1[2:5]
print(b1)

# Array reshape
Vector = np.arange(10)
Matrix = Vector.reshape(2,5)
Matrix = Vector.reshape(-1,5)
print(Matrix)

# np.arrange
a1=np.arange(start=1, stop=10, step=2)
print(a1)