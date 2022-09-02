from random import *
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# x = np.linspace(0, 1000, 1000)

y = []
for i in range(1000):
    y.append(randint(1, 3))

plt.plot(y)
plt.show()