# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:42:28 2022

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
f=np.sin(np.pi*X)*np.cos(np.pi*Y)
print(f)
extent=[min(x),max(x),min(y),max(y)]
im=plt.imshow(f,extent=extent,cmap=plt.cm.RdBu)