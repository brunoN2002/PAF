def funkcija_dvije_tocke(x1,y1,x2,y2):
    k=(y2-y1)/(x2-x1)
    if isinstance(x1, float) and isinstance(y1, float) and isinstance(x2, float) and isinstance(y2, float):
        if k+x1-y1<0:
            print("y=", k, "x  -", abs(k*x1-y1))
        elif k+x1-y1>=0:
            print("y=", k, "x  +", abs(k*x1-y1))
    else:
        print("kordinate pogrešno unesene, probajte ponovno")

funkcija_dvije_tocke(1.0,2.0,3.0,4.0)