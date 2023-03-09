import numpy as np
import matplotlib.pyplot as plt

n1 = np.linspace(-2*np.pi, 2*np.pi, 401)
n2 = np.arange(0, 101)
Xn = np.cos(np.pi*n2/2)
Xf = (1/100)*np.fft.fft(Xn, len(n1))
yn = np.exp(1j*np.pi*n2/4)*Xn
Yf = (1/100)*np.fft.fft(yn, len(n1))

fig, axis = plt.subplots(4, 1,figsize=(10, 10))
axis[0].plot(n1, np.abs(Xf))
axis[0].set_title('Magnitude')

axis[1].plot(n1, (180/np.pi)*np.angle(Xf))
axis[1].set_title('Phase')

axis[2].plot(n1, np.abs(Yf))
axis[2].set_title('Magnitude Spectrum')

axis[3].plot(n1, np.angle(Yf))
axis[3].set_title('Angle Spectrum')
plt.show()
