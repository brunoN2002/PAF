from msilib.schema import SelfReg
import numpy as np
import matplotlib.pyplot as plt
import math as math
class Particle:
    def __init__(self):
        self.vrijeme=list()
        self.x=list()
        self.y=list()
        self.ay=list()
        self.ax=list()
        self.vx=list()
        self.vy=list()
    def set_initial_conditions(self, v0, angle, x0, y0, dt):
        self.vrijeme.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.ay.append(-9.81)
        self.ax.append(0)
        self.vx.append(np.cos(np.radians(angle))*v0)
        self.vy.append(np.sin(np.radians(angle))*v0)
        self.dt=dt
    def reset(self):
        self.__init__()
    def __move(self):
        self.vrijeme.append(self.vrijeme[-1]+self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        self.ax.append(0)
        self.ay.append(-9.81)
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
    def range(self):
        while self.y[-1]>=0:
            self.__move()
            #print(self.y[-1])
        return (self.x[-1])
    def plot_trajectory(self):
        plt.plot(self.x,self.y)
        return plt.show()
    
    def total_time(self):
        while self.y[-1]>=0:
            self.__move()
        return(self.vrijeme[-1])
    
    def max_speed(self):
        v_ukupna=list()
        while self.y[-1]>=0:
            self.__move()
            v_ukupna.append(math.sqrt((self.vx[-1])**2+(self.vy[-1])**2))
        z=0
        for i in v_ukupna:
            if i>z:
                z=i
        return("maksimalna brzina je", z, "m/s")

    def velocity_to_hit_target(self, angle, x0, y0, dt, dv, r, p, q,):
        v_pogodak=list()
        v0=0
        pogodak=0
        while pogodak==0:
            v0+=dv
            self.set_initial_conditions(v0, angle, x0, y0, dt)
            while self.x[-1]<p:
                self.__move()
            if self.y[-1]>=q-r and self.y[-1]<=q+r:
                pogodak=1
                v_pogodak.append(v0)
            else:
                pogodak=0
            self.reset()
        while pogodak==1:
            v0+=dv
            self.set_initial_conditions(v0, angle, x0, y0, dt)
            while self.x[-1]<p:
                self.__move()
            if self.y[-1]>=q-r and self.y[-1]<=q+r:
                pogodak=1
                v_pogodak.append(v0)
            else:
                pogodak=2
            self.reset()
        return(v_pogodak)

    def angle_to_hit_target(self, v0, x0, y0, dt, dangle, r, p, q,):
        angle_pogodak=list()
        angle=0
        pogodak=0
        while pogodak==0:
            angle+=dangle
            self.set_initial_conditions(v0, angle, x0, y0, dt)
            while self.x[-1]<p:
                self.__move()
            if self.y[-1]>=q-r and self.y[-1]<=q+r:
                pogodak=1
                angle_pogodak.append(angle)
            else:
                pogodak=0
            self.reset()
        while pogodak==1:
            angle+=dangle
            self.set_initial_conditions(v0, angle, x0, y0, dt)
            while self.x[-1]<p:
                self.__move()
            if self.y[-1]>=q-r and self.y[-1]<=q+r:
                pogodak=1
                angle_pogodak.append(angle)
            else:
                pogodak=2
            self.reset()
        return(angle_pogodak)
                    
                    
        







