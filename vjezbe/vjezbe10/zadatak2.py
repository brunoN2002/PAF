import zadatak1 as zd
import matplotlib.pyplot as plt
import numpy as np

electronRK=zd.ElectricForce()
electronRK.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),-1,1,0.01)
electronRK.plot_trajectoryRK(100)

electron=zd.ElectricForce()
electron.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),-1,1,0.01)
electron.plot_trajectory(100)

plt.plot(electron.x,electron.y,electron.z, c="blue")
plt.plot(electronRK.x,electronRK.y,electronRK.z, c="red")
plt.show()