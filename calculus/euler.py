# y' = x*y ;  y(1) = 1

import numpy as np
import matplotlib.pyplot as plt

n = 100
h = 0.01
def f(x,y):
    return (x*y)

xi = 1.0
yi = 1.0

x = []
y = []

x.append(xi)
y.append(yi)

for i in range (1, n+1):
    yi = yi + (h * f(xi, yi))
    y.append(yi)
    xi = xi + h
    x.append(xi)

print("  X_n    Y_n    Z_n    error  ")
for i in range (1, n+1):
    print(" {:.2f}".format(x[i]),"  {:.2f}".format(y[i]))

plt.plot(x, y, 'g--', label='Approximated')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.legend(loc='lower right')
plt.show()
