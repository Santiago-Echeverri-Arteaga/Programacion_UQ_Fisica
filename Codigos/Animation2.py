import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as an

t = np.linspace(0, 10, 200)
y = np.sin(t)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

line, = ax.plot(t, y)
point, = ax.plot(0, 0, 'o')
ax.set_ylim(-1,1)

def update(i):
    point.set_data([t[i], y[i]])
    return point,


ani = an.FuncAnimation(fig, update, frames=t.size)
ani.save('Animacion_2.gif', fps=30)