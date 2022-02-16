import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
def g(x):
    return sci.erf(x)-0.5
print(g(0))
print(g(0.5))
print(g(1))
xL0=0
xR0=2
tolerance=10**(-6)
xL=xL0
xR=xR0
if(g(xL)*g(xR)<0):
    xn=(xL+xR)/2
    if(g(xL)*g(xn)<0):
        xR=xn
    else:
        xL=xn
    while(np.fabs(xL-xR)>=tolerance):
        xn=(xL+xR)/2
        if(g(xL)*g(xn)<0):
            xR=xn
        else:
            xL=xn
    xr=xL
    print(xr)
else:
    print("Try other xL and xR")