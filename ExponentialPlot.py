import numpy as np
import matplotlib.pyplot as plt
name = input("Apna naam daalein: ")
x = np.arange(-3, 3, 0.002)
y = np.exp(x)
plt.plot(x, y, color="g")
plt.show()
