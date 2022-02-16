import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
def g(x):
    return x*(1-x)*(2-x)
def instant_plot(xL0,xR0,xL,xR):
    xmin=xL0
    xmax=xR0
    x=np.linspace(xmin,xmax,100)
    y=g(x)
    plt.plot(x,y,color='k')
    plt.axvline(x=xL,color='r')
    plt.axvline(x=xR,color='b')
    plt.axhline(y=0,color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

xL0=0
xR0=2
tolerance=10**(-6)
xL=xL0
xR=xR0
instant_plot(xL0,xR0,xL,xR)
if(g(xL)*g(xR)<=0):
    xn=(xL+xR)/2
    if(g(xL)*g(xn)<=0):
        xR=xn
    else:
        xL=xn
    while(np.fabs(xL-xR)>=tolerance):
        xn=(xL+xR)/2
        instant_plot(xL0,xR0,xL,xR)
        if(g(xL)*g(xn)<=0):
            xR=xn
        else:
            xL=xn
    xr=xL
    print(xr)
else:
    print("Try other xL and xR")

