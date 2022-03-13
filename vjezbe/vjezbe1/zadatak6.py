import math as math
import matplotlib.pyplot as plt
import numpy as np
#r je radijus funkcije, p je x kor. središta, q je y kor. središta, x i y su kordinate tocke.
def tocka_i_kruznica(r,p,q,x,y,z):
    r2=math.sqrt((x-p)**2+(y-q)**2)
    if r2>r:
        print("tocka se nalazi izvan kružnice")
    if r2<r:
        print("tocka se nalazi unutar kružnice")
    if r2==r:
        print("tocka se nalazi na kruznici")
    d=abs(r-r2)
    circle=plt.Circle((p, q), r, fill=False)
    fig, ax =plt.subplots()
    plt.plot(x, y, marker="o", color="black")
    ax.add_patch(circle)
    if z=="nacrtaj":
        plt.show()
    elif z=="snimi":
        f=input("Upišite ime slike")
        plt.savefig(f)

tocka_i_kruznica(5,0,0,1,1,"snimi")