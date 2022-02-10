# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:28:43 2022

@author: kimyelim
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
xmin=0
resolution=100
x=np.linspace(xmin,resolution)
print(x)
C=1-sci.erf(x/(4*10000000*0.000001)**0.5)
C2=1-sci.erf(x/(4*10000000*0.0001)**0.5)
C3=1-sci.erf(x/(4*10000000*0.01)**0.5)
C4=1-sci.erf(x/(4*10000000*10)**0.5)
print(C)
fig=plt.figure(dpi=1000)
cm=1/2.54
fig,ax=plt.subplots(figsize=(19*cm,15*cm))
ax.plot(x,C)
ax.plot(x,C2)
ax.plot(x,C3)
ax.plot(x,C4)
fontname={'fontname':'Times New Roman'}
plt.xlabel("x",fontsize=15,**fontname)
plt.ylabel("C",fontsize=15,**fontname)
plt.xticks(np.arange(min(x),max(x),100),fontsize=10,**fontname)
plt.xlim([0,100])
plt.yticks(np.arange(0,1,0.1),fontsize=10,**fontname)
plt.ylim([-0.6,1.1])
plt.legend([r'$C(t=0.000001)=1-erf(x/\sqrt{(4Dt)})$',r'$C2(t=0.0001)=1-erf(x/\sqrt{(4Dt)})$',r'$C3(t=0.01)=1-erf(x/\sqrt{(4Dt)})$',r'$C4(t=10)=1-erf(x/\sqrt{(4Dt)})$'],loc='lower right')
plt.title("density",fontsize=20,**fontname)
fig.savefig('plot_density.png',format='png',bbox_inches='tight',dpi=1000)