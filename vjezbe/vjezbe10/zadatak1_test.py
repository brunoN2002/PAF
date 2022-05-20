import zadatak1 as zd
import matplotlib.pyplot as plt
import numpy as np

p1=zd.ElectricForce()
p1.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),-1,1,0.01)
p1.plot_trajectory(10)

p2=zd.ElectricForce()
p2.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),1,1,0.01)
p2.plot_trajectory(10)

plt.show()