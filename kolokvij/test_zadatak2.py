import ParticleDrop as pd

p1=pd.ParticleDrop()
p1.set_initial_conditions(100, 10)
p1.set_new_height(200)
p1.change_speed(10)

p2=pd.ParticleDrop()
p2.set_initial_conditions(50, 7)
p2.set_new_height(100)
p2.change_speed(-3)
print(p2.h)