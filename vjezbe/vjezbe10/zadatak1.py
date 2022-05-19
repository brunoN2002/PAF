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
        self.a.append(np.array((0,0,0)))
        self.r.append(r0)
        self.v.append(v0)
        self.E.append(E0)
        self.B.append(B0)

    def reset(self):
        self.__init__()

    def __move(self):
        self.F=self.q*self.E[-1]+self.q*(np.dot(self.v[-1],self.B[-1]))
        self.a.append(self.F/self.m)
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.r.append(self.r[-1]+self.v[-1]*self.dt)
        self.E.append((self.E0))
        self.B.append((self.B0))

    def trajectory(self, t):
        N=int(t/self.dt)
        for i in range(N):
            self.__move()
        fig=plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot(self.r[0],self.r[1],self.r[2])
        plt.show()


p1=ElectricForce()
p1.set_initial_conditions(np.array((0.1,0.1,0.1)),np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),-1,1,0.01)
p1.trajectory(10)