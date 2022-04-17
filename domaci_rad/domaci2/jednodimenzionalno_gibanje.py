import matplotlib.pyplot as plt
import numpy as np
import math as math

class funkcija_sile:
    def __init__(self):
        self.vrijeme=list()
        self.pomak=list()
        self.brzina=list()
        self.akceleracija=list()
    
    def pocetne_vrijednosti(self, x0, v0, m, dt, F):
        self.F=F
        self.m=m
        self.dt=dt
        self.vrijeme.append(0)
        self.pomak.append(x0)
        self.brzina.append(v0)
        a=(self.F(self.pomak[-1],self.brzina[-1],self.vrijeme[-1]))/self.m
        self.akceleracija.append(a)

    def __move(self):
        self.vrijeme.append(self.vrijeme[-1]+self.dt)
        self.brzina.append(self.brzina[-1]+self.akceleracija[-1]*self.dt)
        self.pomak.append(self.pomak[-1]+self.brzina[-1]*self.dt)
        a=(self.F(self.pomak[-1],self.brzina[-1],self.vrijeme[-1]))/self.m
        self.akceleracija.append(a)

    def graf(self, t, z):
        self.t=t
        while self.vrijeme[-1]<t:
            self.__move()
        if z=="x-t":
            plt.plot(self.vrijeme,self.pomak)
        if z=="v-t":
            plt.plot(self.vrijeme,self.brzina)
        if z=="a-t":
            plt.plot(self.vrijeme,self.akceleracija)

    def reset(self):
        self.__init__()
