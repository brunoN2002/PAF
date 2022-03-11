import numpy as np
import matplotlib.pyplot as plt
def jednoliko_gibanje(F, m):
    a=F/m
    brzina=list()
    vrijeme=list()
    pomak=list()
    akceleracija=list()
    dt=0.1
    v0=0
    t0=0
    x0=0
    for i in np.arange(0, 10, dt):
        v=v0+a*dt
        v0=v
        t0+=dt
        x=x0+v*dt
        x0=x
        pomak.append(x)
        vrijeme.append(t0)
        brzina.append(v)
        akceleracija.append(a)
    plt.plot(vrijeme, brzina)
    plt.xlabel("vrijeme [s]")
    plt.ylabel("brzina [m/s]")
    plt.show()
    plt.plot(vrijeme, pomak)
    plt.xlabel("vrijeme [s]")
    plt.ylabel("pomak [m]")
    plt.show()
    plt.plot(vrijeme, akceleracija)
    plt.xlabel("vrijeme [s]")
    plt.ylabel("akceleracija [m/s^2]")
    plt.show()


jednoliko_gibanje(9.81, 1)