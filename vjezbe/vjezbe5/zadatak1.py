import harmonic_oscilator as hrm
import matplotlib.pyplot as plt

p1= hrm.HarmonicOscilator(1, 0.5, 10, 0.01)
p2= hrm.HarmonicOscilator(1, 0.5, 10, 0.05)
p3= hrm.HarmonicOscilator(1, 0.5, 10, 0.1)

p1.gibanje(5, "x")
p2.gibanje(5, "x")
p3.gibanje(5, "x")
plt.show()

p1.gibanje(5, "v")
p2.gibanje(5, "v")
p3.gibanje(5, "v")
plt.show()

p1.gibanje(5, "a")
p2.gibanje(5, "a")
p3.gibanje(5, "a")
plt.show()