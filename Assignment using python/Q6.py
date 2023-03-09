import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 46) #Interval.
Xn = (np.heaviside(n,1) - np.heaviside(n - 10,1))
hn = (0.9) ** n * np.heaviside(n,1)
Yn = np.convolve(Xn, hn)
fig, axis = plt.subplots(3, 1)
axis[0].stem(n, Xn,"gold")
axis[0].set_title('x(n)')
axis[1].stem(n, hn,"hotpink")
axis[1].set_title('h[n]')
axis[2].stem(n, Yn[:51],"purple")
axis[2].set_title('y(n)')
axis[2].set_xlabel('n')
plt.show()
