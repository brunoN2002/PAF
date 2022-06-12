import numpy as np
import matplotlib.pyplot as plt

class Planets():
    def __init__(self):
        self.lista_r=list()
        self.a=np.array((0,0,0))
        self.v=list()
        self.vrijeme=list()
        self.x=list()
        self.y=list()
        self.z=list()

    def set_initial_conditions(self, m, r, v0):
        self.m=m
        self.v0=v0
        self.r=r
        self.lista_r.append(r)
        self.vrijeme.append(0)
        self.v.append(v0)
        self.x.append(self.r[0])
        self.y.append(self.r[1])
        self.z.append(self.r[2])
        

    def reset(self):
        self.__init__()

def __move(planeti, dt, G=6.67408*10**(-11)):
    for i in planeti:
        i.a=(np.array((0,0,0)))
        for p in planeti:
            if i!=p:
                i.a=i.a+(G*(i.m*p.m)*(p.lista_r[-1]-i.lista_r[-1])/((np.linalg.norm(p.lista_r[-1]-i.lista_r[-1]))**3))/i.m
        i.vrijeme.append(i.vrijeme[-1]+dt)
        i.v.append(i.v[-1]+i.a*dt)
        i.lista_r.append(i.lista_r[-1]+i.v[-1]*dt)
        i.x.append(i.lista_r[-1][0])
        i.y.append(i.lista_r[-1][1])
        i.z.append(i.lista_r[-1][2])
            
                
def plot_trajectory(planeti, t, dt):
    N=int(t/dt)
    for z in range(N):
        __move(planeti, dt)    
    for f in planeti:
        plt.plot(f.x,f.y)

def plot_animate(planeti, t, dt):
    N=int(t/dt)
    for z in range(N):
        __move(planeti, dt)
        for f in planeti:
            plt.plot(f.x,f.y)
        plt.pause(0.0001)
        plt.clf()
