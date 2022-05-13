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
        return -1*np.sign(v)*self.c*(v)**2

    def __move(self):
        if (self.h-self.l-self.y[-1])<0:
            self.x.append(0)
        else:
            self.x.append(self.h-self.l-self.y[-1])
        self.vrijeme.append(self.vrijeme[-1]+self.dt)
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.a.append(self.g+(self.__Fe(self.x[-1])/self.m)+(self.__Fo(self.v[-1])/self.m))
        self.y.append(self.y[-1]+self.v[-1]*self.dt)

    def graf(self, t):
        for i in range(100000):
            self.__move()
        plt.plot(self.vrijeme,self.y)
        plt.show()

    def __ay2(self, x, v, t):
        return self.g+(self.k*x)+(-1*np.sign(v)*self.c*(v)**2)

    def __moveRK(self):
        if (self.h-self.l-self.y[-1])<0:
            self.x.append(0)
        else:
            self.x.append(self.h-self.l-self.y[-1])

        k1vy=self.__ay2(self.x[-1], self.v[-1], self.vrijeme[-1])*self.dt
        k1y=self.v[-1]*self.dt
        k2vy=self.__ay2(self.x[-1]+k1y/2, self.v[-1]+k1vy/2, self.vrijeme[-1]+self.dt/2)*self.dt
        k2y=(self.v[-1]+k1vy/2)*self.dt
        k3vy=self.__ay2(self.x[-1]+k2y/2, self.v[-1]+k2vy/2, self.vrijeme[-1]+self.dt/2)*self.dt
        k3y=(self.v[-1]+k2vy/2)*self.dt
        k4vy=self.__ay2(self.x[-1]+k3y, self.v[-1]+k3vy, self.vrijeme[-1]+self.dt)*self.dt
        k4y=(self.v[-1]+k3vy)*self.dt

        self.vrijeme.append(self.vrijeme[-1]+self.dt)
        self.v.append(self.v[-1]+(1/6)*(k1vy+2*k2vy+2*k3vy+k4vy))
        self.y.append(self.y[-1]+(1/6)*(k1y+2*k2y+2*k3y+k4y))
        
    def grafRK(self, t):
        N=int(t/self.dt)
        for i in range(N): 
            self.__moveRK()
        #print(self.y)
        #print(self.vrijeme)
        plt.plot(self.vrijeme,self.y)
        plt.show()