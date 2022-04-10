import particle as par

p1=par.Particle()
print(p1.velocity_to_hit_target(70, 0, 0, 0.1, 0.5, 100, 1000, 1698))
print(p1.angle_to_hit_target(200, 0, 0, 0.1, 0.5, 100, 1000, 1698))
#moze se zakljucit da su oba tocna jer jedan za kut od 70 izbacuje brzine u okolini 200 a drugi kada se stavi brzina 200 izbacuje kuteve u okolini 70