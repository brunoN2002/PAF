import numpy as np
import matplotlib.pyplot as plt
import math as math
def x_y_graf(v0, kut, x0, y0, dt):
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
    while y[-1]>=0:
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

def maksimalna_visina(v0, kut, x0, y0, dt):
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
    while y[-1]>=0:
        t.append(t[-1]+dt)
        x.append(x[-1]+v_x[-1]*dt)
        y.append(y[-1]+v_y[-1]*dt)
        v_x.append(v_x[-1]+a_x[-1]*dt)
        v_y.append(v_y[-1]+a_y[-1]*dt)
        a_y.append(-9.81)
        a_x.append(0)
    b=0
    for i in y:
        if i>b:
            b=i
    print("maksimalna visina je", b, "metara")

def domet(v0, kut, x0, y0, dt):
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
    while y[-1]>=0:
        t.append(t[-1]+dt)
        x.append(x[-1]+v_x[-1]*dt)
        y.append(y[-1]+v_y[-1]*dt)
        v_x.append(v_x[-1]+a_x[-1]*dt)
        v_y.append(v_y[-1]+a_y[-1]*dt)
        a_y.append(-9.81)
        a_x.append(0)
    print("Domet horizontalnog hitca je", x[-1], "metara")

def maksimalna_brzina(v0, kut, x0, y0, dt):
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
    v_ukupna=list()
    v_ukupna.append(v0)
    while y[-1]>=0:
        t.append(t[-1]+dt)
        x.append(x[-1]+v_x[-1]*dt)
        y.append(y[-1]+v_y[-1]*dt)
        v_x.append(v_x[-1]+a_x[-1]*dt)
        v_y.append(v_y[-1]+a_y[-1]*dt)
        a_y.append(-9.81)
        a_x.append(0)
        v_ukupna.append(math.sqrt((v_x[-1])**2+(v_y[-1])**2))
    z=0
    for i in v_ukupna:
        if i>z:
            z=i
    print("maksimalna brzina je", z, "m/s")

maksimalna_brzina(200, 70, 0, 0, 0.01)
