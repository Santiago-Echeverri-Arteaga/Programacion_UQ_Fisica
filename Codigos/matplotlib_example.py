import matplotlib.pyplot as plt
import numpy as np
  
  
fig = plt.figure(constrained_layout = True)
gs = fig.add_gridspec(10, 10)
ax = fig.add_subplot(gs[0:5, :])#,projection="3d")
ax2 = fig.add_subplot(gs[5:, :5],projection="polar", facecolor="#666666")
ax3 = fig.add_subplot(gs[5:, 5:9],facecolor = "#0000FF55")


#arriba = fig.add_subplot(2,1,1)
#abajo = fig.add_subplot(2,2,3)
#abajo_2 = fig.add_subplot(4,2,6)

x_hist = np.random.randn(10000)
x = np.linspace(-4,4,1000)
y=314*np.exp(-x**2/2)

x2 = np.linspace(-4,4,10)
y2=314*np.exp(-x2**2/2)

ax.hist(x_hist, bins=100, facecolor="#c76888",edgecolor="#df9e9e",
        orientation="vertical",zorder=1)
ax.plot(x, y, color="black", linewidth=2., linestyle="-.",zorder=2)
ax.scatter(x2, y2, zorder=3, marker="D", edgecolor="k", 
           c=np.random.rand(10), s=20+100*np.random.rand(10), lw=0.5,
            cmap="hsv", alpha=0.6)
plt.show()