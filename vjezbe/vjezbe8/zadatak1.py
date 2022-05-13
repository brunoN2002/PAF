from re import X
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
        return (self.x[-1])
    def plot_trajectory(self):
        plt.plot(self.x,self.y)
        return plt.show()

    def __ax2(self, x, v, t):
        return -1*(((self.r*self.C*self.A/2*self.m)*(v)**2)*np.sign(v))

    def __ay2(self, x, v, t):
        return -9.81-(((self.r*self.C*self.A/2*self.m)*(v)**2)*np.sign(v))

    def __moveRGK(self):
        k1vx=self.__ax2(self.x[-1], self.vx[-1], self.vrijeme[-1])*self.dt
        k1x=self.vx[-1]*self.dt
        k2vx=self.__ax2(self.x[-1]+k1x/2, self.vx[-1]+k1vx/2, self.vrijeme[-1]+self.dt/2)*self.dt
        k2x=(self.vx[-1]+k1vx/2)*self.dt
        k3vx=self.__ax2(self.x[-1]+k2x/2, self.vx[-1]+k2vx/2, self.vrijeme[-1]+self.dt/2)*self.dt
        k3x=(self.vx[-1]+k2vx/2)*self.dt
        k4vx=self.__ax2(self.x[-1]+k3x, self.vx[-1]+k3vx, self.vrijeme[-1]+self.dt)*self.dt
        k4x=(self.vx[-1]+k3vx)*self.dt

        k1vy=self.__ay2(self.y[-1], self.vy[-1], self.vrijeme[-1])*self.dt
        k1y=self.vy[-1]*self.dt
        k2vy=self.__ay2(self.y[-1]+k1y/2, self.vy[-1]+k1vy/2, self.vrijeme[-1]+self.dt/2)*self.dt
        k2y=(self.vy[-1]+k1vy/2)*self.dt
        k3vy=self.__ay2(self.y[-1]+k2y/2, self.vy[-1]+k2vy/2, self.vrijeme[-1]+self.dt/2)*self.dt
        k3y=(self.vy[-1]+k2vy/2)*self.dt
        k4vy=self.__ay2(self.y[-1]+k3y, self.vy[-1]+k3vy, self.vrijeme[-1]+self.dt)*self.dt
        k4y=(self.vy[-1]+k3vy)*self.dt

        self.vx.append(self.vx[-1]+(1/6)*(k1vx+2*k2vx+2*k3vx+k4vx))
        self.x.append(self.x[-1]+(1/6)*(k1x+2*k2x+2*k3x+k4x))
        self.vy.append(self.vy[-1]+(1/6)*(k1vy+2*k2vy+2*k3vy+k4vy))
        self.y.append(self.y[-1]+(1/6)*(k1y+2*k2y+2*k3y+k4y))
        self.vrijeme.append(self.vrijeme[-1]+self.dt)

    def rangeRGK(self):
        while self.y[-1]>=0:
            self.__moveRGK()
        return (self.x[-1])

    def plot_trajectoryRGK(self):
        plt.plot(self.x,self.y)
        return plt.show()