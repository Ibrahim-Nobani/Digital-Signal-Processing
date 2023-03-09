import numpy as np
import matplotlib.pyplot as plt

# The time intervals.
tn1 = np.arange(0, 1, 1/20)
tn2 = np.arange(0, 1, 1/30)
tn3 = np.arange(0, 1, 1/50)
f1,f2=5,15
Gn1 = np.cos(2*np.pi*f1*tn1) + 0.125*np.cos(2*np.pi*f2*tn1)
Gn2 = np.cos(2*np.pi*f1*tn2) + 0.125*np.cos(2*np.pi*f2*tn2)
Gn3 = np.cos(2*np.pi*f1*tn3) + 0.125*np.cos(2*np.pi*f2*tn3)
fig, axis = plt.subplots(3, 1, figsize=(6, 8), sharex=True, sharey=True)
axis[0].stem(tn1, Gn1,'gold')
axis[0].set_title('Fs=20')
axis[1].stem(tn2, Gn2,'purple')
axis[1].set_title('Fs=30')
axis[2].stem(tn3, Gn3)
axis[2].set_title('Fs=50')
plt.show()
