x1=int(input("x kordinate prve tocke: "))
y1=int(input("y kordinate prve tocke: "))
x2=int(input("x kordinate druge tocke: "))
y2=int(input("y kordinate druge tocke: "))
k=(y2-y1)/(x2-x1)
if k+x1-y1<0:
    print("y=", k, "x-", k*x1-y1)
elif k+x1-y1>=0:
    print("y=", k, "x", k*x1-y1)