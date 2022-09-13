import numpy as np
import matplotlib.pyplot as plt


dGo = -687.6e3
R = 8.314
T = 298
K = np.exp(-dGo/(R*T))

Q = np.linspace(0.01, 9e120, 10000)

dG = dGo + R*T*np.log(Q)

G = dG.cumsum()

plt.plot(Q, G)

plt.arrow(Q[-1], G[0], dy=dGo, dx=0)

plt.show()
