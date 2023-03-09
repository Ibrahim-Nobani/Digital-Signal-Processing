import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11)
X = np.exp(-0.1 + 1j*0.3*n)
fig, axs = plt.subplots(4, 1, figsize=(6, 8), sharex=True)
# Mangitude using abs in np
axs[0].stem(n, np.abs(X))
axs[0].set_title('Magnitude')
# Phase using angle in np
axs[1].stem(n, np.angle(X))
axs[1].set_title('Phase')
# Real using real in np
axs[2].stem(n, np.real(X))
axs[2].set_title('Real part')
# Imaginary using imag in numpy
axs[3].stem(n, np.imag(X))
axs[3].set_title('Imaginary part')
plt.show()
