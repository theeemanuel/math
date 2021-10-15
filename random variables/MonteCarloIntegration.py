import random
import numpy as np
import matplotlib.pyplot as plt

aX = 0
aY = 0
aZ = 0
bX = 2*np.pi
bY = 2*np.pi
bZ = 2*np.pi
N = 10000
n = 1000
integrals = []

def f(x, y, z):
    return (np.exp(np.sin(x*y*z)))

for i in range(n):
    sumf = 0
    for i in range(N):
        xi = random.uniform(aX, bX)
        yi = random.uniform(aY, bY)
        zi = random.uniform(aZ, bZ)
        sumf += f(xi, yi, zi)
    integral = ((bX-aX)*(bY-aY)*(bZ-aZ)*sumf)/N
    integrals.append(integral)

plt.title("Distribution of the integrals")
plt.hist(integrals,bins=40)
plt.xlabel("Integrals")
plt.show()

avgIntegral = sum(integrals)/len(integrals)
print("The value of integration is ",avgIntegral)
