import numpy as np
import matplotlib.pyplot as plt
a = -20
b = 5
c = 20
t = np.arange(1, 1000, 500)
y =  (a * t**2) + (b* t) + c
plt.plot(t, y)
plt.show()
plt.close()

