import zadatak1 as zd

p1=zd.BungeeJumping()
p1.set_initial_conditions(100, 50, 100, 0, 80, 0.001)
p1.grafRK(20)

p2=zd.BungeeJumping()
p2.set_initial_conditions(100, 50, 100, 0, 80, 0.001)
p2.graf(20)

p3=zd.BungeeJumping()
p3.set_initial_conditions(100, 50, 100, 1.5, 80, 0.01)
p3.grafRK(100)