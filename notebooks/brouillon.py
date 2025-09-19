import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x)

plt.plot(x, y, label="sin(x)")
plt.title("Courbe sinusoïdale")
plt.xlabel("x (radians)")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

