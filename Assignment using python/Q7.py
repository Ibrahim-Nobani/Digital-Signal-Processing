import matplotlib.pyplot as plt
import numpy as np

n = np.arange(-3, 4)
Xn = np.array([3, 11, 7, 0, -1, 4, 2])

n2 = np.random.normal(0, 1, size=len(n))
Yn1 = np.roll(Xn, -2) + n2
Yn2 = np.roll(Xn, -4) + n2
fig,axis = plt.subplots(2,1)
axis[0].stem(n, Yn1,'gold')
axis[0].set_title("Y[n]=X[n-2]-w[n]")
axis[1].stem(n, Yn2)
axis[1].set_title("Y[n]=X[n-4]-w[n]")
plt.show()

corr = np.corrcoef(Xn, Yn1)[0, 1]
corr2 = np.corrcoef(Xn, Yn2)[0, 1]
print(corr)
print(corr2)



