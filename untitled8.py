import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci

def find_neardata(X,x,y):
    for i in range(x.size):
        if (x[i]<=X):
            x1=x[i]
            x2=x[i+1]
            y1=y[i]
            y2=y[i+1]
    return x1,x2,y1,y2

def ya(X,x,y):
    x1,x2,y1,y2=find_neardata(X,x,y)
    slope=(y2-y1)/(x2-x1)
    distance=(X-x1)
    return y1+slope*distance

def g(x):
    return x*(1-x)*(2-x)
def instant_plot(xL0,xR0,xL,xR,xd,yd):
    plt.plot(xd,yd,color='k')
    plt.axvline(x=xL,color='r')
    plt.axvline(x=xR,color='b')
    plt.axhline(y=0,color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

xd=np.genfromtxt('xc.txt',dtype='float',delimiter=' ')
yd=np.genfromtxt('yc.txt',dtype='float',delimiter=' ')

xL0=-100
xR0=100
xmin=min(xd)
xmax=max(xd)

if (xL0<xmin):
    print("Try again")
tolerance=10**(-6)
xL=xL0
xR=xR0
instant_plot(xL0,xR0,xL,xR,xd,yd)
if (xL>=xmin and xR<=xmax):
    if(ya(xL,xd,yd)*ya(xR,xd,yd)<=0):
        xn=(xL+xR)/2
        if(ya(xL,xd,yd)*ya(xn,xd,yd)<=0):
            xR=xn
        else:
            xL=xn
        while(np.fabs(xL-xR)>=tolerance):
            xn=(xL+xR)/2
            instant_plot(xL0,xR0,xL,xR,xd,yd)
            if(ya(xL,xd,yd)*ya(xn,xd,yd)<=0):
                xR=xn
            else:
                xL=xn
        xr=xL
        print(xr)
else:
    print("Try other xL and xR")