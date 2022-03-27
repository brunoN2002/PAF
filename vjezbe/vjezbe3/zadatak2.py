import zadatak1 as zd
import math as math
import matplotlib.pyplot as plt
import numpy as np
greska=list()
dt1=list()
p1=zd.Particle()
dt=0.01
p1.set_initial_conditions(10,60,0,0,dt)
t=0.01
analiticki_domet=((10**2)/(9.81))*2*np.sin(np.radians(60))*np.cos(np.radians(60))
for i in range(200):
    p1.set_initial_conditions(10,60,0,0,dt)
    dt=dt+t
    a=abs(((p1.range()-analiticki_domet)/analiticki_domet)*100)
    dt1.append(dt)
    greska.append(a)
    p1.reset()
plt.plot(dt1,greska)
plt.show()

