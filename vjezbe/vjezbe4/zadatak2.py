import calculus as cal
import numpy as np
import matplotlib.pyplot as plt
import math as math

def f1(x):
    return np.cos(x)

cal.integral_prav(f1,0,5,200)
cal.integral_prav(f1,0,5,50)
cal.integral_trap(f1,0,5,200)
cal.integral_trap(f1,0,5,50)
z=np.linspace(0,5,100)
plt.plot(z, np.sin(z))
plt.show()