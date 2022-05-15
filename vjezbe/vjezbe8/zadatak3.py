import zadatak1 as zd
import matplotlib.pyplot as plt
import numpy as np

dometC=list()
dometM=list()
Ma=list()
Cd=list()

p1=zd.Particle()

for c in np.arange(0.1, 1, 0.1):
    Cd.append(c)
    p1.set_initial_conditions(10, 30, 0, 0, 0.01, 1, c, 0.05, 0.01)
    dometC.append(p1.rangeRGK())
    p1.reset()

plt.plot(Cd, dometC)
plt.show()

p2=zd.Particle()

for m in np.arange(0.01, 1, 0.1):
    Ma.append(m)
    p2.set_initial_conditions(10, 30, 0, 0, 0.01, 1, 0.1, 0.05, m)
    dometM.append(p2.rangeRGK())
    p2.reset()

plt.plot(Ma, dometM)
plt.show()