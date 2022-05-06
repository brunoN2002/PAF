import zadatak1 as zd

p1=zd.Particle()
p1.set_initial_conditions(10, 30, 0, 0, 0.01, 100.22, 0.1, 0.05, 0.1)
print(p1.rangeRGK())
p1.plot_trajectoryRGK()