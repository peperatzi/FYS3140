from matplotlib import *
from sympy import *

x = Symbol('x')
y = integrate(x*DiracDelta(x-1), (x, 0, 5.0))   

print x
print y

#print len(x)
#print len(y)

#plot(x, y, "--r", linewidth=2)

