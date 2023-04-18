# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:09:56 2021

@author: hola-
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,AutoMinorLocator)

cm2inch = lambda x:x/2.54
fig = plt.figure(constrained_layout=True,figsize=(cm2inch(30),cm2inch(20)))
#fig.subplots_adjust(wspace=0.5, hspace=0., top=0.98)
gs = fig.add_gridspec(3,4)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax4 = fig.add_subplot(gs[0, 3])
ax5 = fig.add_subplot(gs[1, 0])
ax6 = fig.add_subplot(gs[1, 1])
ax7 = fig.add_subplot(gs[1, 2], projection="3d")
ax8 = fig.add_subplot(gs[1, 3], projection="3d")
ax9 = fig.add_subplot(gs[2, 0], projection="polar")
ax10 = fig.add_subplot(gs[2, 1])
ax11 = fig.add_subplot(gs[2, 2])
ax12 = fig.add_subplot(gs[2, 3], projection="3d",computed_zorder=False)

#axins = fig.add_axes([0.15, 0.1, 0.5, 0.3])

#ax2 = fig.add_axes([0.85, 0.4, 0.05, 0.2])
######################(#Filas, #Cols, #Grafica)

x = np.linspace(0,10*np.pi,1200)
x2 = np.linspace(0,10*np.pi,100)
col =  np.abs(np.linspace(-10*np.pi,10*np.pi,100))



y = np.sin(x)
y2 = np.sin(x2+np.random.randn()*0.6)
y3 = np.sin(2*x)
y4 = np.cos(2*x)

#Grafica de sin(x)
#ax1.plot(x,y,c='#994C00',lw=1.0,zorder=2,ls='-')
ax1.scatter(x2,y2,zorder=1, marker='o',
         c = col, s = 50, cmap = 'hot', label='Experimento')
#Grafica de cos(x)
ax1.plot(x,y,color='#00FF00',lw=2.0,zorder=2,ls='-', label='Teoría')
ax1.text(0.001, 0.8, "a)",fontsize=20,color='b', fontname="Comic Sans MS")
ax1.annotate("Texto",xy=(0.01,-1),xytext=(0.001,0.5),
             arrowprops=dict(width=1.0, facecolor='k', edgecolor= 'k', headwidth=5), 
             fontname="Comic Sans MS")

ax1.arrow(0.001,-1,10,0, head_width=0.5, head_length=3.0)
#ax1.set_xscale('log')
ax1.axhline(y=-0.5, xmin= 0, xmax=0.5, ls='--', lw=0.5, alpha=0.5)
ax1.axvline(x=10, ymin=-1.0, ymax=1.0, color='k', ls='--', lw=0.5, alpha=0.5)
ax_twin = ax1.twinx()
ax_twin.plot(x,x**2,color='r',lw=2.0,zorder=2,ls='-', label='Teoría')

axz = zoomed_inset_axes(ax1, zoom=1.2, loc=7)
axz.set_xlim(-0.1,np.pi+0.1)
axz.set_ylim(0,1.1)
axz.plot(x,y,color='#0000FF',lw=2.0,zorder=2,ls='-', label='Teoría')
mark_inset(ax1, axz, 4, 2)
# axins.scatter(x2,y2,zorder=1, marker='o',
        # c = col, s = 50, cmap = 'hot', label='Experimento')

ax1.legend(loc=1,fontsize=8)
mu= 100
sigma = 15
x = mu + sigma*np.random.randn(10000)
ax2.hist(x, edgecolor='r', facecolor='b', rwidth=0.5,
         align = 'right', orientation = 'horizontal')


x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

x_e = np.arange(0.1, 4, 0.01)
y_e = np.exp(-x_e)
#example variable error bar values
yerr = 0.1 + 0.2*np.sqrt(x)
xerr = 0.1 + yerr

# First illustrate basic pyplot interface, using defaults where possible.
ax3.errorbar(x, y, yerr=0.05, color = '#666666', ecolor='b',
            elinewidth=0.5, capsize=3, marker='s', lw = 0.5)
ax3.plot(x_e,y_e, color='r')

bar_x = ["Ana","Bob","Charles"]
heigh_x = [52, 20, 87]
heigh2_x = [0, 10, 30]
ax4.barh(bar_x, heigh_x, facecolor='r', edgecolor='b', height=0.5,
       left=[0,10,30])
ax4.barh(bar_x, heigh2_x, facecolor='k', edgecolor='b', height=0.5,
       left=[0,0,0])

ax3.grid(True, 'major', axis='x', lw=2.0)
ax3.xaxis.set_major_locator(MultipleLocator(2))
ax3.xaxis.set_minor_locator(MultipleLocator(0.5))
ax1.set_xticks([-0.01,5*np.pi,10*np.pi])
ax1.set_xticklabels([0,r"$5\pi$",r"$10\pi$"])
ax1.set_xlabel(r'$\mathcal{L}(\rho^\hat{O})$',color='r',fontsize=16)
ax1.set_ylabel(r'$\mathcal{L}(\rho^\hat{O})$',color='b',fontsize=16)



ax5.pie([15,45,25,100],
            colors=['#F54000','#00BB00','#000099','c'],
            labels=['A','B','C', 'D'], explode=[0,0.2,0.04,0.1],
            labeldistance=1.5, shadow=True,
            autopct='%d', pctdistance=1.2)

x = np.linspace(0,10,120)
y = np.linspace(0,10,120)

X,Y = np.meshgrid(x,y)
U = Y**2 - X**2 
V = np.sqrt(1 + X + Y**2)

ax6.streamplot(x,y,U,V, density=1.5, linewidth=0.3,
                   color = X, cmap = 'inferno', arrowsize=0.8,
                   arrowstyle = '->')


t3d = np.linspace(-10,10,2000)
x3d = 10.*np.cos(3*t3d)
y3d = -20.*np.sin(3*t3d)
z3d = 5*t3d
ax7.plot(x3d, y3d, z3d)


theta = np.linspace(-np.pi, np.pi, 1000)

r=1-2*np.cos(theta)

ax9.plot(theta+(r<0)*np.pi,np.abs(r))

x = np.linspace(-2, 2, 100)


X, Y = np.meshgrid(x, x)


z = np.exp(-X**2-Y**2)


ax8.plot_surface(X, Y, z, cmap="jet", rstride=1, cstride=1)
#ax8.plot_wireframe(X, Y, z, cmap="jet", rstride=10, cstride=10)

import matplotlib.image as mpimg

# Read image
img=mpimg.imread('imagen.jpeg')

# Get histogram
ax11.hist(img[:,:,0].ravel(), bins=256, color='r',alpha=0.4)
ax11.hist(img[:,:,1].ravel(), bins=256, color='g',alpha=0.4)
ax11.hist(img[:,:,2].ravel(), bins=256, color='b',alpha=0.4)
ax10.imshow(img,cmap="inferno")

w = np.linspace(0, 20, 120)
lorentz = lambda w0,gamma,A:A*gamma /((w-w0)**2+gamma**2)

from mpl_toolkits.mplot3d import Axes3D
a=0.6
c=["r","g","b","c"]
ax12.add_collection3d(ax12.fill_between(w,lorentz(18,0.8,0.2)+lorentz(8,0.1,0.1),
                                        w*0,alpha=a,color=c[0], zorder=1),4,zdir="y")

ax12.add_collection3d(ax12.fill_between(w,lorentz(6,0.6,0.6),w*0,alpha=a,
                                        color=c[1], zorder=2),3,zdir="y")

ax12.add_collection3d(ax12.fill_between(w,lorentz(4,1.2,0.8),w*0,alpha=a,
                                        color=c[2], zorder=3),2,zdir="y")

ax12.add_collection3d(ax12.fill_between(w,lorentz(2,0.8,1),w*0,alpha=a,
                                        color=c[3], zorder=4),1,zdir="y")

ax12.set_xlim(0,20)
ax12.set_ylim(1,4)
ax12.set_zlim(0,1)

plt.show()
