from matplotlib.pyplot import step
import calculus as cal
import math as math
import matplotlib.pyplot as plt
import numpy as np
def f1(x):
    return 3*x**2+2

def f2(x):
    return math.sin(x)

cal.der_lista(f1, 0, 5, 0.1, "moze se bilo sta upisat za 3-step")
cal.der_lista(f2, 0, 5, 0.1, "3-step")

cal.der_plot(f2, 0, 5, 1, "3-step")
cal.der_plot(f2, 0, 5, 0.5, "3-step")
cal.der_plot(f2, 0, 5, 1, "2-step")
cal.der_plot(f2, 0, 5, 0.5, "2-step")
z=np.linspace(0,5,100)
plt.plot(z,np.cos(z))
plt.show()