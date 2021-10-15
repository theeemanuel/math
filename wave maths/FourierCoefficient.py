from scipy.integrate import quad
from scipy.signal import square
import numpy as np
import matplotlib.pyplot as plt

l = np.pi
upto = 11
an = []
bn = []
sum = 0

def f(x):
    return square(x+(np.pi/2))


def integrand(x):
    return (1 / np.pi) * f(x)


def integranda(x):
    return (1 / np.pi) * f(x) * np.cos((np.pi * n * x) / l)


def integrandb(x):
    return (1 / np.pi) * f(x) * np.sin((np.pi * n * x) / l)


a0, err0 = quad(integrand, -l, l)
for n in range(1, upto):
    a, erra = quad(integranda, -l, l)
    an.append(a)
    b, errb = quad(integrandb, -l, l)
    bn.append(b)

x = np.arange(-2*l, 2*l, 0.1)
print("Fourier series expansion of f(x) is given by")
print('f(x) = ', (a0 / 2))
if l == np.pi:
    for n in range(1, upto):
        sum += (an[n-1]*(np.cos(n*x))) + (bn[n-1]*(np.sin(n*x)))
        print(' + (', an[n - 1], ') cos (', n, 'x) + (', bn[n - 1], ') sin (', n, 'x)')
else:
    for n in range(1, upto):
        sum += (an[n-1]*(np.cos((n*np.pi*x)/l))) + (bn[n-1]*(np.sin((n*np.pi*x)/l)))
        print(' + (', an[n - 1], ') cos (', n, 'πx/', l, ') + (', bn[n - 1], ') sin (', n, 'πx/', l, ') + ')
        
plt.plot(x, f(x), 'r')
plt.plot(x, sum, 'g--')
plt.show()
