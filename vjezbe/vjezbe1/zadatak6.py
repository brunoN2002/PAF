import math as math
#r je radijus funkcije, p je x kor. središta, q je y kor. središta, x i y su kordinate tocke.
def tocka_i_kruznica(r,p,q,x,y):
    r2=math.sqrt((x-p)**2+(y-q)**2)
    if r2>r:
        print("tocka se nalazi izvan kružnice")
    if r2<r:
        print("tocka se nalazi unutar kružnice")
    if r2==r:
        print("tocka se nalazi na kruznici")

tocka_i_kruznica(5,0,0,1,1)