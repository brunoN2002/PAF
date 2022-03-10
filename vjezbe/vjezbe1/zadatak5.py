import matplotlib.pyplot as plt
import numpy as npgit stat
def funkcija_dvije_tocke():
    try:
        x1=float(input("x kordinate prve tocke: "))
        y1=float(input("y kordinate prve tocke: "))
        x2=float(input("x kordinate druge tocke: "))
        y2=float(input("y kordinate druge tocke: "))
        k=(y2-y1)/(x2-x1)
        if k+x1-y1<0:
            print("y=", k, "x  -", abs(k*x1-y1))
        elif k+x1-y1>=0:
            print("y=", k, "x  +", abs(k*x1-y1))
        x = np.linspace(-5,5,100)
        plt.plot(x, k*x+(k*x1-y1))
        z=input("za prikaz krafa upišite p, a za spremanje grafa upišite s: ")
        if z=="p":
            plt.show()
        if z=="s":
            g=input("Upišite naziv pdf datoteke: ")
            plt.savefig(g, formt="pdf")
    except ValueError:
        raise ValueError("kordinate su neispravne, ponovno upišite kordinate") from None

funkcija_dvije_tocke()