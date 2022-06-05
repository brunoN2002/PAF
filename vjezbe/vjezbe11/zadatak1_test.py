import zadatak1 as zd
import matplotlib.pyplot as plt
import numpy as np

zemlja=zd.Planets()
zemlja.set_initial_conditions(5.9742*10**24, np.array((149.6*10**9,0,0)), np.array((0,29.783*10**(3),0)))
sunce=zd.Planets()
sunce.set_initial_conditions(1.989*10**30, np.array((0,0,0)), np.array((0,0,0)))
lista_planeta=list()
lista_planeta.append(sunce)
lista_planeta.append(zemlja)
print(zemlja.r)
print(sunce.r)
print(np.linalg.norm(sunce.r-zemlja.r))
zd.plot_trajectory(lista_planeta, 31.557*10**6, 10**4)
plt.show()