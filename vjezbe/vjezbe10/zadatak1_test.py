import zadatak1 as zd
import matplotlib.pyplot as plt
import numpy as np

electron=zd.ElectricForce()
electron.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),-1,1,0.01)
electron.plot_trajectory(10)

positron=zd.ElectricForce()
positron.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),1,1,0.01)
positron.plot_trajectory(10)

plt.show()