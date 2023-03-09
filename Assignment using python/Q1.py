import numpy as np
import matplotlib.pyplot as plt
n = np.linspace(-5, 5, 11) #Identify Interval
u = np.heaviside(n,1) #The unit sample sequence
x = 2*np.roll(u,2) - np.roll(u,-4) # This does the sequence shift
plt.stem(n, x,'gold')
plt.title("Question 1 Part A",color = 'hotpink')
plt.xlabel('n',color = 'red')
plt.ylabel('X[n]',color = 'red')
plt.show()
#########################
#Part B
n2 = np.linspace(0, 50, 51)
Xn = np.cos(0.04*np.pi*n2)
Ws = np.random.normal(0, 1, 51) #eng.randn(1, 51)
Yn = Xn + 0.2*Ws
plt.stem(n2, Yn,'purple')
plt.title("Question 1 Part B",color = 'hotpink')
plt.xlabel('n')
plt.ylabel('X[n]')
plt.show()

#####################
#Part 3

n = np.linspace(-10, 9, 20)
a = np.array([5,4,3,2,1])
z = np.tile(a,4)
plt.stem(n, z,'hotpink')
plt.title("Question 1 Part C",color = 'silver')
plt.xlabel('n')
plt.ylabel('Z[n]')
plt.show()




