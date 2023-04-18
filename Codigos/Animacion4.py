# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:39:17 2021

@author: hola-
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

NUMFRAMES = 24*3
# create a figure and initialize the data
fig = plt.figure(facecolor='w',figsize=(7,4))



ax1 = fig.add_subplot(1,1,1,projection='3d')
#ax2 = fig.add_subplot(2,1,2,projection='3d')

ax1.set_xlim(-20/5-1,20/5+1)
ax1.set_ylim(-20/5-1,20/5+1)
ax1.set_zlim(-4,4)


def animate(i):
    # update the start/end point, and the data shown in lower subplot
    xs = np.linspace((-4*i/(72)-1),4*i/72+1,120)
    #ys = np.sin(xs**2)

    X, Y = np.meshgrid(xs, xs)

    Z = (X**2)/4 - (Y**2)/6

    ax1.plot_surface(X, Y, Z, cmap='bwr')
    return fig,

# Animate
ani = mpl.animation.FuncAnimation(fig, animate,
                               frames=NUMFRAMES, interval=100, blit=True)
ani.save('Animacion_4.gif', fps=24)