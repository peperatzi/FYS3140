
# i
import numpy as np
import matplotlib.pyplot as plt


#f(1) if a <= 1 <= b else 0

def phi(x, n):
    if np.abs(x) >= 1./n:
        return 0
    else:
        return n/2.

# 
N = 101
x = np.linspace(0, 2*np.pi, N)
y = np.zeros(N)
y1 = np.zeros(N)
for i in range(N):
    for t in range(1, 100):
        for n in range(1, t):
            test = np.sin(x[i]-(2./np.pi))
            y[i] = phi(test, n)
            y1[i] = np.sin(x[i])


#y1 = np.sin(x)

# Plot the crazyness
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, 'b', x, y1, 'g')
#plt.plot(x, y, 'b')
plt.show()


