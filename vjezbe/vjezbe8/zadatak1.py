from curses import KEY_A1
from xml.sax.handler import DTDHandler
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
    def set_initial_conditions(self, v0, angle, x0, y0, dt, r, C, A, m):
        self.vrijeme.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.ay.append(-9.81)
        self.ax.append(0)
        self.vx.append(np.cos(np.radians(angle))*v0)
        self.vy.append(np.sin(np.radians(angle))*v0)
        self.dt=dt
        self.r=r
        self.C=C
        self.A=A
        self.m=m
    def reset(self):
        self.__init__()
    def __move(self):
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
        self.ax.append(-(self.r*self.C*self.A/2*self.m)*(self.vx[-1])**2)
        self.ay.append(-(9.81-((self.r*self.C*self.A/2*self.m)*(self.vy[-1])**2)))
        self.vrijeme.append(self.vrijeme[-1]+self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def range(self):
        while self.y[-1]>=0:
            self.__move()
            #print(self.y[-1])
        return (self.x[-1])
    def plot_trajectory(self):
        plt.plot(self.x,self.y)
        return plt.show()

    def RGK(self, a):
        k1x=a(self.x[-1], self.vx[-1], self.vrijeme[-1])*self.dt
        k1v=self.vx[-1]
        k2x=
        k2v=
        k3x=
        k3v=
        k4x=
        k4v=