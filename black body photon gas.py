import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Constants set to 1
hbar = 1
kB = 1

# Integrand for internal energy
def integrand(omeg, T):
    return omeg**3 / (np.exp(omeg / T) - 1)

# Temperature range
Ts = np.arange(1.0, 1.9, 0.1)
us = []

for T in Ts:
    u, _ = quad(integrand, 0, np.inf, args=(T,))
    us.append(u)

# Plotting
plt.plot(Ts, us, marker='o',)
plt.xlabel("$Temperature$ $(T)$")
plt.ylabel("$Internal$ $Energy$ $per$ $Volume$ $(u)$")
plt.title("Internal Energy vs Temperature for Photon Gas")

plt.grid(True)
plt.show()

# Print values
for T, u in zip(Ts, us):
    print("T = {:.1f}, u = {:.2f}".format(T,u))

'''
OUTPUT:
T = 1.0, u = 6.49
T = 1.1, u = 9.51
T = 1.2, u = 13.47
T = 1.3, u = 18.55
T = 1.4, u = 24.95
T = 1.5, u = 32.88
T = 1.6, u = 42.56
T = 1.7, u = 54.24
T = 1.8, u = 68.17
'''