import numpy as np
from scipy.signal import lfilter
import matplotlib.pyplot as plt

a = [1]
b = [1, -1]
n1 = np.linspace(0, 21, 22)
###### Part A
Xn_A = 5 * (np.heaviside(n1, 1) - np.heaviside(n1 - 20, 1))
Yn_A = lfilter(b, a, Xn_A)
###### Part B
Xn_B= n1*(np.heaviside(n1, 1)-np.heaviside(n1 - 10, 1))+(20 - n1)*(np.heaviside(n1 - 10, 1)- np.heaviside(n1 - 20, 1))
Yn_B = lfilter(b, a, Xn_B)
###### Part C
n2 = np.arange(0, 100)
Xn_C = np.sin((np.pi * n2) / 25)*(np.heaviside(n2, 1)-np.heaviside(n2 - 100, 1))
Yn_C = lfilter(b, a, Xn_C)

fig, axis = plt.subplots(3, 1)
axis[0].stem(n1, Yn_A,'gold')
axis[0].set_title("A) Rectangular Pulse")
axis[1].stem(n1, Yn_B)
axis[1].set_title("B) Triangular Pulse")
axis[2].stem(n2, Yn_C,'hotpink')
axis[2].set_title("C) Sinusoidal Pulse")
plt.show()
