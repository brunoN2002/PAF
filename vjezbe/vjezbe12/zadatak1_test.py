import zadatak1 as zd
import matplotlib.pyplot as plt
import numpy as np

zemlja=zd.Planets()
zemlja.set_initial_conditions(5.9742*10**24, np.array((149.6*10**9,0,0)), np.array((0,29.783*10**(3),0)))
sunce=zd.Planets()
sunce.set_initial_conditions(1.989*10**30, np.array((0,0,0)), np.array((0,0,0)))
merkur=zd.Planets()
merkur.set_initial_conditions(0.33*10**24, np.array((57.9*10**9,0,0)), np.array((0,47.4*10**(3),0)))
mars=zd.Planets()
mars.set_initial_conditions(0.642*10**24,np.array((228*10**9,0,0)),np.array((0,24.1*10**(3),0)))
venera=zd.Planets()
venera.set_initial_conditions(4.87*10**24,np.array((108.2*10**9,0,0)),np.array((0,35*10**(3),0)))
lista_planeta=list()
lista_planeta.append(sunce)
lista_planeta.append(zemlja)
lista_planeta.append(merkur)
lista_planeta.append(mars)
lista_planeta.append(venera)
zd.plot_animate(lista_planeta, 31.557*10**6, 10**5)
plt.show()