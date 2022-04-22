import matplotlib.pyplot as plt
import numpy as np
import math as math

class ParticleDrop():
    def __init__(self):
        self.h=list()
        self.vx=list()
        self.vy=list()
        self.x=list()
        self.t=list()
        self.ax=list()
        self.ay=list()

    def reset(self):
        self.__init__()

    def set_initial_conditions(self, h0, vx0):
        self.vx0=vx0
        self.h0=h0
        self.h.append(h0)
        self.vx.append(vx0)
        self.vy.append(0)
        self.x.append(0)
        self.t.append(0)
        self.ax.append(0)
        self.ay.append(-9.81)
        print("objekt je uspiješno stvoren, početna visina objekta je", h0, "m a početna brzina je ", vx0, "m/s")

    def set_new_height(self, h1):
        self.h.clear()
        self.h.append(h1)
        print("objekt je uspiješno promijenjen, početna visina objekta je", h1, "m")

    def change_speed(self, dvx):
        self.vx.clear()
        self.vx.append(self.vx0+dvx)
        print("objekt je uspiješno promijenjen, početna brzina objekta je", self.vx0+dvx, "m/s")

    def __move(self):
        self.t.append(self.t[-1]+self.dt)
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.h.append(self.h[-1]+self.vy[-1]*self.dt)
        self.ax.append(0)
        self.ay.append(-9.81)
        

    def izbaceni_objekt(self, dt, t, z):
        # t je vrijeme nakon kojeg objekt se izbaci iz aviona
        self.dt=dt
        self.x.clear()
        self.x.append(self.vx[-1]*t)
        while self.h[-1]>=0:
            self.__move()
        if z=="x-y":
            plt.plot(self.x,self.h)
        if z=="vy-t":
            plt.plot(self.t,self.vy)

    def vrijeme_pada(self, dt):
        self.dt=dt
        while self.h[-1]>=0:
            self.__move()
        return(self.t[-1])

    #peti nisam stiga, treba ga na isti naacin kao domaci 1, zadatak 1