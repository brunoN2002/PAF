from msilib.schema import SelfReg
import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init__(self):
        self.vrijeme=list()
        self.x=list()
        self.y=list()
        self.ay=list()
        self.ax=list()
        self.vx=list()
        self.vy=list()
    def set_initial_conditions(self, v0, angle, x0, y0, dt):
        self.vrijeme.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.ay.append(-9.81)
        self.ax.append(0)
        self.vx.append(np.cos(np.radians(angle))*v0)
        self.vy.append(np.sin(np.radians(angle))*v0)
        self.dt=dt
    def reset(self):
        self.__init__()
    def __move(self):
        self.vrijeme.append(self.vrijeme[-1]+self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        self.ax.append(0)
        self.ay.append(-9.81)
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
    def range(self):
        while self.y[-1]>=0:
            self.__move()
            #print(self.y[-1])
        return (self.x[-1])
    def plot_trajectory(self):
        plt.plot(self.x,self.y)
        return plt.show()


