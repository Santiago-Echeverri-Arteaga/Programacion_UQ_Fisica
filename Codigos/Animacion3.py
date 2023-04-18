# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:05:44 2021

@author: hola-
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation

NUMFRAMES = 200
# create a figure and initialize the data
fig = plt.figure(facecolor='w',figsize=(7,4))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
xs = np.linspace(0,NUMFRAMES/5,10000)
ys = np.sin(xs**2)

ax1.plot(xs, ys, 'r-')
l1, = ax1.plot([0,0],[-1,1],'b-') # line 1 which shows the start point to expand data
l2, = ax1.plot([0,0],[-1,1],'b-') # line 2 which shows the end point to expand data
ax2.plot(xs, ys, 'r-')


def animate(i,l1,l2):
    # update the start/end point, and the data shown in lower subplot
    st,en = i/5-0.5, i/5+0.5
    l1.set_data([st,st],[-1,1])
    l2.set_data([en,en],[-1,1])
    ax2.set_xlim(st,en)
    return fig,

# Animate
ani = mpl.animation.FuncAnimation(fig, animate, fargs=(l1,l2),
                               frames=NUMFRAMES, interval=100, blit=True)
ani.save('Animacion_3.gif', fps=24)