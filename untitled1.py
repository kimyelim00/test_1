# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:09:55 2022

@author: kimyelim
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
tmin=0
tmax=100
resolution=100000
t=np.linspace(tmin,tmax,resolution)
print(t)
p=0.477*((4*100*t)**0.5)
fig=plt.figure(dpi=1000)
cm=1/2.54
fig,ax=plt.subplots(figsize=(19*cm,15*cm))
ax.plot(t,p)
fontname={'fontname':'Times New Roman'}
plt.xlabel("t",fontsize=15,**fontname)
plt.ylabel("p",fontsize=15,**fontname)
plt.xticks(np.arange(0,10,1),fontsize=10,**fontname)
plt.xlim([0,10])
plt.yticks(np.arange(0,30,2),fontsize=10,**fontname)
plt.ylim([0,30])
plt.legend([r'$p=0.477 \sqrt{4Dt}$'],loc='lower right')
plt.title("density",fontsize=20,**fontname)
fig.savefig('plot_density2.png',format='png',bbox_inches='tight',dpi=1000)