import numpy as np
import matplotlib.pyplot as plt

class ElectricForce:
    def __init__(self):
        self.a=list()
        self.r=list()
        self.v=list()
        self.E=list()
        self.B=list()
        self.vrijeme=list()
    
    def set_initial_conditions(self, v0, r0, E0, B0, q, m, dt):
        self.m=m
        self.q=q
        self.dt=dt
        self.v0=v0
        self.r0=r0
        self.E0=E0
        self.B0=B0
        self.vrijeme.append(0)
        self.a.append(np.array((0,0,0)))
        self.r.append(r0)
        self.v.append(v0)
        self.E.append(E0)
        self.B.append(B0)

    def reset(self):
        self.__init__()

    def __move(self):
        self.F=self.q*self.E[-1]+self.q*(np.cross(self.v[-1],self.B[-1]))
        self.a.append(self.F/self.m)
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.r.append(self.r[-1]+self.v[-1]*self.dt)
        self.E.append((self.E0))
        self.B.append((self.B0))

    def plot_trajectory(self,t):
        self.x=list()
        self.y=list()
        self.z=list()
        N=int(t/self.dt)
        for i in range(N):
            self.__move()
        for element in self.r:
            self.x.append(element[0])
            self.y.append(element[1])
            self.z.append(element[2])
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot(self.x,self.y,self.z)

    def __a(self, x, v, t):
        return (self.q*self.E[-1]+self.q*(np.cross(v,self.B[-1])))/self.m


    def __moveRK(self):
        k1vy=self.__a(self.r[-1], self.v[-1], self.vrijeme[-1])*self.dt
        k1y=self.v[-1]*self.dt
        k2vy=self.__a(self.r[-1]+k1y/2, self.v[-1]+k1vy/2, self.vrijeme[-1]+self.dt/2)*self.dt
        k2y=(self.v[-1]+k1vy/2)*self.dt
        k3vy=self.__a(self.r[-1]+k2y/2, self.v[-1]+k2vy/2, self.vrijeme[-1]+self.dt/2)*self.dt
        k3y=(self.v[-1]+k2vy/2)*self.dt
        k4vy=self.__a(self.r[-1]+k3y, self.v[-1]+k3vy, self.vrijeme[-1]+self.dt)*self.dt
        k4y=(self.v[-1]+k3vy)*self.dt

        self.vrijeme.append(self.vrijeme[-1]+self.dt)
        self.v.append(self.v[-1]+(1/6)*(k1vy+2*k2vy+2*k3vy+k4vy))
        self.r.append(self.r[-1]+(1/6)*(k1y+2*k2y+2*k3y+k4y))

    def plot_trajectoryRK(self,t):
        self.x=list()
        self.y=list()
        self.z=list()
        N=int(t/self.dt)
        for i in range(N):
            self.__moveRK()
        for element in self.r:
            self.x.append(element[0])
            self.y.append(element[1])
            self.z.append(element[2])
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot(self.x,self.y,self.z)