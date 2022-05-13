import zadatak1 as zd
import matplotlib.pyplot as plt

p1=zd.Particle()
p2=zd.Particle()
p2.set_initial_conditions(10, 30, 0, 0, 0.01, 1, 0.1, 0.05, 0.1)
p1.set_initial_conditions(10, 30, 0, 0, 0.01, 1, 0.1, 0.05, 0.1)
print(p2.range())
print(p1.rangeRGK())
plt.plot(p1.x,p1.y, c="blue")
plt.plot(p2.x,p2.y, c="red")
plt.show()