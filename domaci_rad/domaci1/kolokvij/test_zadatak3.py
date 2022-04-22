import ParticleDrop as pd
import matplotlib.pyplot as plt

p1=pd.ParticleDrop()
p1.set_initial_conditions(2000, 200)
p1.izbaceni_objekt(0.01, 2, "x-y")
plt.show()
p1.izbaceni_objekt(0.01, 2, "vy-t")
plt.show()