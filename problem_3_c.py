
# i
import numpy as np
import matplotlib.pyplot as plt

def phi(x, n):
    if np.abs(x) >= 1./n:
        return 0
    else:
        return n/2.

def f_1(x, a):
    return (x-a)*(x+a)


# 
N = 101
x = np.linspace(-2*np.pi, 2*np.pi, N)
y = np.zeros(N)
f = np.sin(x)
#a = 3
#f = (x-a)*(x+a)
for i in range(N):
    for n in range(1, 100):
        #y[i] += phi(np.sin(x[i]), n)
        y[i] += phi(f[i]), n)/2500.

plt.plot(x,y, x, f,"--")

plt.xlabel('x')
plt.ylabel('$\Phi(f(x))$')
plt.legend(['$\Phi(x)$','$f(x)$'])
plt.show()


