import jednodimenzionalno_gibanje as gib
import matplotlib.pyplot as plt
k=1
def F(x,v,t):
    return(-k*x)

p1=gib.funkcija_sile()
p1.pocetne_vrijednosti(0, 0, 0.5, 0.01, F)
p1.graf(10, "a-t")
plt.show()

#sve grafove izbacuje kao ravnu crtu iz nepoznatog razloga. nakon puno pokusaja nisam uspio debugirati kod.