
# i
import numpy as np
from sympy import DiracDelta, sin 
import matplotlib.pyplot as plt

def mister_dirac(t,a):
    DiracDelta(t - a)/a + DiracDelta(t+a)/a


# 
x = np.linspace(-2*np.pi, 2*np.pi, 101)
y = mister_dirac(x, 2)


# Plot the crazyness
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y)
plt.show()


