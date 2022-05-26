import numpy as np
import matplotlib.pyplot as plt
import math as math

class Planets():
    def __init__(self, m, x0, y0, v0):
        self.m=m
        self.vp0=vp0
        self.vo0=vo0
        self.x0=x0
        self.y0=y0
        self.r=[np.array(x0,y0)]
        self.a=[0]
        self.v=[np.array(0,v0)]

class SolarSystem():
    def __init__(self, dt):
        self.planets=list()
        self.G= 6.67408*10^11
        self.dt=dt

    def addPlanet(self, planet):
        self.planets.append(planet)

    def __move(self):
        for i in self.planets:
            for p in self.planets:
                if i.m==i.p:
                    i.a.append(0)
                if i.m!=i.p:
                    i.a.append(self.G*(i.m*p.m)/(abs(p.r[-1]-i.r[-1]))**2)
                    

                    
                

