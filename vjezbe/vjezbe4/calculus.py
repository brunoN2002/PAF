import matplotlib.pyplot as plt
import math
def der3(func,x,h):
    return((func(x+h)-func(x-h))/(2*h))

def der2(func,x,h):
    return((func(x+h)-func(x))/h)

def der_lista(func,a,b,dx,p):
    if p=="2-step":
        lista_tocki=[a]
        lista_derivacija=[der2(func,a,dx)]
        for i in range(round((b-a)/dx)):
            a+=dx
            lista_tocki.append(a)
            lista_derivacija.append(der2(func,a,dx))
        print(lista_tocki)
        print(lista_derivacija)
    else:
        lista_tocki=[a]
        lista_derivacija=[der3(func,a,dx)]
        for i in range(round((b-a)/dx)):
            a+=dx
            lista_tocki.append(a)
            lista_derivacija.append(der3(func,a,dx))
        print(lista_tocki)
        print(lista_derivacija)
    

def der_plot(func,a,b,dx,p):
    if p=="2-step":
        lista_tocki=[a]
        lista_derivacija=[der2(func,a,dx)]
        for i in range(round((b-a)/dx)):
            a+=dx
            lista_tocki.append(a)
            der2(func,a,dx)
            lista_derivacija.append(der2(func,a,dx))
        plt.plot(lista_tocki, lista_derivacija)
    else:
        lista_tocki=[a]
        lista_derivacija=[der3(func,a,dx)]
        for i in range(round((b-a)/dx)):
            a+=dx
            lista_tocki.append(a)
            der3(func,a,dx)
            lista_derivacija.append(der3(func,a,dx))
        plt.plot(lista_tocki, lista_derivacija)
    
def integral_prav(func,a,b,N):
    dx=(b-a)/N
    lista_tocki=[a]
    lista_integrala_donja=[func(a)*dx]
    lista_integrala_gornja=[func(a+dx)*dx]
    for i in range(N-1):
        a+=dx
        lista_integrala_donja.append(lista_integrala_donja[-1]+(func(a)*dx))
        lista_integrala_gornja.append(lista_integrala_gornja[-1]+(func(a+dx)*dx))
        lista_tocki.append(a)
    plt.scatter(N,lista_integrala_donja[-1])
    plt.scatter(N,lista_integrala_gornja[-1])
    return(lista_integrala_donja[-1], lista_integrala_gornja[-1])

def integral_trap(func,a,b,N):
    dx=(b-a)/N
    lista_tocki=[a]
    lista_integrala=[(func(a)+func(b))*dx/2]
    for i in range(N-1):
        a+=dx
        lista_integrala.append(lista_integrala[-1]+(func(a)*dx))
        lista_tocki.append(a)
    plt.scatter(N, lista_integrala[-1])
    print(lista_integrala)
    return(lista_integrala[-1])

