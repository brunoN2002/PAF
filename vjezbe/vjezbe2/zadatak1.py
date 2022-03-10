import numpy as np
import matplotlib as plt
def jednoliko_gibanje(F, m, v0):
    a=F/m
    brzina=list()
    v=v0
    for dt in np.arange(0, 10, 0.1):
        v=v+a*dt
        brzina.append(v)
    print(brzina)

jednoliko_gibanje(9.81, 1, 0)