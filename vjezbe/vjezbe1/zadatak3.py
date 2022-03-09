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
except ValueError:
    raise ValueError("kordinate su neispravne, ponovno upišite kordinate") from None
