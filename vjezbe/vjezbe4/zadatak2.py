import calculus as cal
import numpy as np
import matplotlib.pyplot as plt
import math as math

def f1(x):
    return x
N=2
cal.integral_trap(f1,0,1,N)
#for N in range(10,200,10):
    #cal.integral_prav(f1,0,10,N)
    #cal.integral_trap(f1,0,10,N)
#y=np.linspace(10,200,10)
#plt.plot(y,0*y+2500)
plt.show()