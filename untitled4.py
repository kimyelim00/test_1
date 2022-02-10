# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:43:08 2022

@author: kimyelim
"""

import matplotlib.pyplot as plt
import numpy as np
xmin=-1
xmax=1
resolution=50
x=np.linspace(xmin,xmax,resolution)
ymin=-1
ymax=1
resolution=50
y=np.linspace(ymin,ymax,resolution)
print(x.ndim)
print(y.ndim)
print(x.size)
print(y.size)
X,Y=np.meshgrid(x,y)
f=Y
print(f)
cm=1/2.54
fig=plt.figure(dpi=1000)
fig,ax=plt.subplots(figsize=(19*cm,15*cm))
extent=[min(x),max(x),min(y),max(y)]
im=plt.pcolormesh(X,Y,f,shading='auto',cmap=plt.cm.RdBu)
colorbar=plt.colorbar(im)
ax.set_aspect('equal','box')
ax.set(xlim=(-1,1),ylim=(-0.5,0.5))
plt.xticks(np.arange(-1,1,0.25))
plt.yticks(np.arange(-0.5,0.5,0.25))
colorbar.set_label('colorbar',rotation=270)
cset=plt.contour(X,Y,f,np.arange(-1,1.1,0.2),colors='k')
plt.clabel(cset,inline=True,fontsize=10)
fontname={'fontname':'Times New Roman'}
plt.xlabel("x",fontsize=15,**fontname)
plt.ylabel("y",fontsize=15,**fontname)
plt.title(r'$f=Y$',fontsize=20,**fontname)
fig.savefig('2plot.png',format='png',bbox_inches='tight')