import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0, np.pi, 501)
Xn = np.exp(1j*n)/(np.exp(1j*n) - 0.5)

fig, axis = plt.subplots(4, 1)
axis[0].plot(n, np.abs(Xn), 'gold')
axis[0].set_title('Absolute')
axis[1].plot(n, np.real(Xn), 'hotpink')
axis[1].set_title('Real')
axis[2].plot(n, np.angle(Xn), 'purple')
axis[2].set_title('Angle')
axis[3].plot(n, np.imag(Xn))
axis[3].set_title('Imaginary')
plt.show()
