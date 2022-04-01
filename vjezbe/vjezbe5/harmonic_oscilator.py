import numpy as np
import matplotlib as plt
class HarmonicOscilator:
    def __init__(self, k, m, x0, dt):
        self.k=k
        self.m=m
        self.x0=x0
        self.dt=dt
        a=-(k/m)*x0
        self.aceleracija=list()
        self.akceleracija.append(a)
        self.pomak=list()
        self.pomak.append(self.x0)
        self.vrijeme=list()
        self.vrijeme.append(self.dt)
        self.brzina=list()
        self.brzina.append(0)
    def gibanje(self):
        for i in np.arange(0, 10, self.dt):
            self.brzina.append(self.brzina[-1]+self.akceleracija[-1]*self.vrijeme[-1])
            self.pomak.append(self.pomak[-1]+self.brzina[-1]*self.vrijeme[-1])
            self.akceleracija.append(-(self.k/self.m)*self.pomak[-1])
            self.vrijeme.append(self.dt)
        plt.plot(self.vrijeme, self.pomak)
        plt.show()