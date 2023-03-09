import matplotlib.pyplot as plt
import numpy as np

x = [3, 11, 7, 0, -1, 4, 2]
h = [2, 3, 0, -5, 2, 1]
y = np.convolve(x, h)
n1 = np.linspace(-3, 3, len(x))
n2 = np.linspace(-1, 4, len(h))
n3 = np.linspace(n1[0] + n2[0], max(n1) + max(n2), len(y))

plt.stem(n3, y, "purple")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.title("Q5")
plt.show()