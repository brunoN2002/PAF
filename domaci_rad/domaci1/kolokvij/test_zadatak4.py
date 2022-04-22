import ParticleDrop as pd
import math as math
import matplotlib.pyplot as plt
import numpy as np

greska=list()
t1=list()
p1=pd.ParticleDrop()
t=0.001
dt=0.1/100
h=2000
vx=200
analiticko_vrijeme=math.sqrt((2*h)/9.81)
for i in range(100):
    p1.set_initial_conditions(h, vx)
    a=abs((((p1.vrijeme_pada(t))-analiticko_vrijeme)/analiticko_vrijeme)*100)
    t+=dt
    t1.append(t)
    greska.append(a)
    p1.reset()
plt.plot(t1,greska)
plt.show()