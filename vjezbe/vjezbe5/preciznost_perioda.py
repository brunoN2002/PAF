import harmonic_oscilator as hrm
import math as math
import matplotlib.pyplot as plt
import numpy as np

dt1=list()
greska=list()
dt=0.01
m=0.5
k=1
x0=10
t=0.01
analiticki_period=2*np.pi*(math.sqrt(m/k))
for i in range(100):
    p1= hrm.HarmonicOscilator(k, m, x0, dt)
    dt=dt+t
    a=abs((((p1.period())-analiticki_period)/analiticki_period)*100)
    dt1.append(dt)
    greska.append(a)
    p1.reset()
plt.plot(dt1,greska)
plt.show()
