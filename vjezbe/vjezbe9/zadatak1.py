import numpy as np
import matplotlib.pyplot as plt

class BungeeJumping:
    def __init__(self):
        self.vrijeme=list()
        self.y=list()
        self.a=list()
        self.v=list()
        self.x=list()

    def set_initial_conditions(self, h, l, k, c, m, dt):
        self.h=h
        self.k=k
        self.c=c
        self.m=m
        self.dt=dt
        self.l=l
        self.g=-9.81
        self.vrijeme.append(0)
        self.a.append(0)
        self.v.append(0)
        self.y.append(h)
        self.x.append(0)

    def __Fe(self, x):
        return self.k*x

    def __Fo(self, v):
        return np.sign(v)*self.c*(v)**2

    def __move(self):
        if ((self.h-self.l)-self.y[-1])<0:
            self.x.append(0)
        else:
            self.x.append(self.l-self.y[-1])
        self.vrijeme.append(self.vrijeme[-1]+self.dt)
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.y.append(self.y[-1]+self.v[-1]*self.dt)
        self.a.append((self.g*self.m)/self.m+(self.__Fe(self.x[-1])/self.m)+(self.__Fo(self.v[-1])/self.m))

    def graf(self, t):
        for i in range(10000):
            self.__move()
        plt.plot(self.vrijeme,self.y)
        plt.show()
