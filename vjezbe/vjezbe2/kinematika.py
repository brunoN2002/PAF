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

def horizontalni_hitac(v0, kut, x0, y0, dt):
    v_x=list()
    v_x.append(np.cos(np.radians(kut))*v0)
    v_y=list()
    v_y.append(np.sin(np.radians(kut))*v0)
    x=list()
    x.append(x0)
    y=list()
    y.append(y0)
    a_y=list()
    a_y.append(-9.81)
    a_x=list()
    a_x.append(0)
    t=list()
    t.append(0)
    for i in np.arange(0, 10, dt):
        t.append(t[-1]+dt)
        x.append(x[-1]+v_x[-1]*dt)
        y.append(y[-1]+v_y[-1]*dt)
        v_x.append(v_x[-1]+a_x[-1]*dt)
        v_y.append(v_y[-1]+a_y[-1]*dt)
        a_y.append(-9.81)
        a_x.append(0)
    plt.plot(x, y)
    plt.xlabel("pomak x [m]")
    plt.ylabel("pomak y [m]")
    plt.show()
    plt.plot(t, y)
    plt.xlabel("vrijeme [m/s]")
    plt.ylabel("pomak y [m]")
    plt.show()
    plt.plot(t, x)
    plt.xlabel("vrijeme [m/s]")
    plt.ylabel("pomak x [m]")
    plt.show()