import matplotlib.pyplot as plt
import particle as par

p1=par.Particle()
angle1=list()
range1=list()
time1=list()

for angle in range(0, 90, 1):
    p1.set_initial_conditions(100, angle, 0, 0, 0.1)
    angle1.append(angle)
    range1.append(p1.range())
    time1.append(p1.total_time())
    p1.reset()
plt.plot(angle1, range1)
plt.show()
plt.plot(angle1,time1)
plt.show()



