import random
from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

plt.plot(x_vals, y_vals)


index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    
    plt.cla()
    plt.plot(x_vals, y_vals)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

# =============================================================================
# def data_gen(t=0):
#     cnt = 0
#     while cnt < 1000:
#         cnt += 1
#         t += 0.1
#         yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
# 
# def init():
#     ax.set_ylim(-1.1, 1.1)
#     ax.set_xlim(0, 10)
#     del xdata[:]
#     del ydata[:]
#     line.set_data(xdata, ydata)
#     return line,
# 
# fig, ax = plt.subplots()
# line, = ax.plot([], [], lw=2)
# ax.grid()
# xdata, ydata = [], []
# 
# 
# def run(data):
#     # update the data
#     t, y = data
#     xdata.append(t)
#     ydata.append(y)
#     xmin, xmax = ax.get_xlim()
# 
#     if t >= xmax:
#         ax.set_xlim(xmin, 2*xmax)
#         ax.figure.canvas.draw()
#     line.set_data(xdata, ydata)
# 
#     return line,
# 
# ani = FuncAnimation(fig, run, data_gen, blit=False, interval=10,
#                           repeat=False, init_func=init)
# plt.show()
# =============================================================================

# print(plt.get_backend())