import zadatak1 as zd
import matplotlib.pyplot as plt
import numpy as np

def B(t):
    if t<10:
        return np.array((0,0,t/10))
    else:
        return np.array((0,0,1))

def B2(t):
    return np.array((0,0,1))

electron1=zd.ElectricForce()
electron1.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),B2,-1,1,0.01)
electron1.plot_trajectory(30)

electron2=zd.ElectricForce()
electron2.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),B,-1,1,0.01)
electron2.plot_trajectory(30)

electron3=zd.ElectricForce()
electron3.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),B,-1,1,0.01)
electron3.plot_trajectoryRK(30)

positron=zd.ElectricForce()
positron.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),B,1,1,0.01)
positron.plot_trajectoryRK(30)

plt.plot(electron1.x,electron1.y,electron1.z, c="green")
plt.plot(electron2.x,electron2.y,electron2.z, c="red")
plt.plot(electron3.x,electron3.y,electron3.z, c="blue")
plt.plot(positron.x,positron.y,positron.z, c="yellow")

plt.show()