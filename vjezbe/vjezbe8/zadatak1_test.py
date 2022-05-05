import zadatak1 as zd

p1=zd.Particle()
p1.set_initial_conditions(10, 30, 0, 0, 0.01, 0.1, 0, 0.1, 2)
print(p1.range())
p1.plot_trajectory()