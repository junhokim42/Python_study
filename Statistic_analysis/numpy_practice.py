import numpy as np

# np.array
data1 = [0,1,2,3,4,5]
a1 = np.array(data1)
print(a1)
print(type(data1), type(a1))
print(a1.dtype)

# np.arrange
a1=np.arange(start=1, stop=10, step=2)
print(a1)