import matplotlib.pyplot as plt
import numpy as np
def funkcija_dvije_tocke(x1,y1,x2,y2,z):
    if isinstance(x1, float) and isinstance(y1, float) and isinstance(x2, float) and isinstance(y2, float):
        k=(y2-y1)/(x2-x1)
        if k+x1-y1<0:
            print("y=", k, "x  -", abs(k*x1-y1))
        elif k+x1-y1>=0:
            print("y=", k, "x  +", abs(k*x1-y1))
        x=np.linspace(-5,5,100)
        plt.plot(x, k*x+(k*x1-y1))
        plt.plot(y1,x1, marker='o', markerfacecolor='blue', markersize=10)
        plt.plot(y2,x2, marker='o', markerfacecolor='blue', markersize=10)
        if z=="prikazi":
            plt.show()
        if z=="spremi":
            g=input("Upišite naziv pdf datoteke: ")
            plt.savefig(g, format="pdf")
    else:
        print("kordinate pogrešno unesene, probajte ponovno")


funkcija_dvije_tocke(1.0,2.0,3.0,4.0,"prikazi")