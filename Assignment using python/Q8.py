import numpy as np
from scipy.signal import lfilter
import matplotlib.pyplot as plt

Ycoef = [1, -1, 0.9]
Xcoef = [1]
n = np.linspace(-5, 120, 126)
#Impulse
Xn = np.zeros(len(n))
Xn[0] = 1
hn = lfilter(Xcoef, Ycoef, Xn)
# Unit step
Xb = np.ones(len(n))
fig, axis = plt.subplots(2, 1)
hnb = lfilter(Xcoef, Ycoef, Xb)
print(sum(hn))
axis[0].stem(n, hn,'gold')
axis[0].set_title('h[n] impulse response')
axis[1].stem(n, hnb,'purple')
axis[1].set_title('h[n] unit step')
plt.show()

