import numpy as np
import matplotlib.pyplot as plt

Xn = [1, -0.5, -0.3, -0.1]
Xf = np.fft.fft(Xn, 501)
n = np.linspace(0, np.pi, 501)

fig, axis = plt.subplots(4, 1)
axis[0].plot(n, np.abs(Xf), 'purple')
axis[0].set_title('Magnitude')

axis[1].plot(n, np.real(Xf), 'hotpink')
axis[1].set_title('Real')

axis[2].plot(n, np.angle(Xf), 'gold')
axis[2].set_title('Angle')

axis[3].plot(n, np.imag(Xf), 'brown')
axis[3].set_title('Imaginary')
plt.show()
