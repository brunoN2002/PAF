import numpy as np
import matplotlib.pyplot as plt
class HarmonicOscilator:
    def __init__(self, k, m, x0, dt):
        self.k=k
        self.m=m
        self.x0=x0
        self.dt=dt
        a=-(k/m)*x0
        self.akceleracija=list()
        self.akceleracija.append(a)
        self.pomak=list()
        self.pomak.append(self.x0)
        self.vrijeme=list()
        self.vrijeme.append(self.dt)
        self.brzina=list()
        self.brzina.append(0)

    def gibanje(self, t):
        for i in np.arange(0, t, self.dt):
            self.brzina.append(self.brzina[-1]+self.akceleracija[-1]*self.dt)
            self.pomak.append(self.pomak[-1]+self.brzina[-1]*self.dt)
            self.akceleracija.append(-(self.k/self.m)*self.pomak[-1])
            self.vrijeme.append(self.vrijeme[-1]+(self.dt))
        plt.plot(self.vrijeme, self.pomak)
        plt.show()
        plt.plot(self.vrijeme, self.brzina)
        plt.show()
        plt.plot(self.vrijeme, self.akceleracija)
        plt.show()

    def period(self):
        if -(self.k/self.m)*self.x0<0:
            while self.brzina[-1]<=0:
                self.brzina.append(self.brzina[-1]+self.akceleracija[-1]*self.dt)
                self.pomak.append(self.pomak[-1]+self.brzina[-1]*self.dt)
                self.akceleracija.append(-(self.k/self.m)*self.pomak[-1])
                self.vrijeme.append(self.vrijeme[-1]+(self.dt))
            print(2*self.vrijeme[-1])
            return(2*self.vrijeme[-1])
        if -(self.k/self.m)*self.x0>0:
            while self.brzina[-1]<=0:
                self.brzina.append(self.brzina[-1]+self.akceleracija[-1]*self.dt)
                self.pomak.append(self.pomak[-1]+self.brzina[-1]*self.dt)
                self.akceleracija.append(-(self.k/self.m)*self.pomak[-1])
                self.vrijeme.append(self.vrijeme[-1]+(self.dt))
            print(2*self.vrijeme[-1])
            return(2*self.vrijeme[-1])

    def reset(self):
        self.akceleracija=list()
        self.pomak=list()
        self.vrijeme=list()
        self.brzina=list()