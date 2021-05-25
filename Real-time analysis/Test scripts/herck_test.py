# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:51:41 2021

@author: Herck
"""
import pandas as pd
from matplotlib import pyplot as plt
#########################################
plt.style.use('seaborn')
from matplotlib.animation import FuncAnimation
from mpl_toolkits.axes_grid1 import make_axes_locatable

def sensorbox(i):
    df = pd.read_csv('./data.csv', usecols=[3,0,1])
    
    colors = df['T_in']
    
    ax8.cla()
    ax8.scatter(df['time'], df['P_in'], s=30, c=colors, cmap='jet', 
                marker= '.', label = "ECO-WISE 2021")
    ax8.set_title("Sensor box variables")
    ax8.set_xlabel("Time (sec)")
    ax8.set_ylabel("Pressure (mbar)")
    ax8.legend()
    
#     ax9.cla()
#     ax9.set_ylabel("Temperature in (°C)")
#     ax9.yaxis.set_label_position("right")
#     ax9.yaxis.tick_right()
#     ax9.set_aspect(15)
#     ax9.contourf([1], colors, [1], 1, cmap='jet')
    
    
temp_press_in_figure = plt.figure()
ax8 = temp_press_in_figure.add_subplot(111)

div = make_axes_locatable(ax8)
cax = div.append_axes('right', '5%', '5%')

ani = FuncAnimation(temp_press_in_figure, sensorbox, interval=1000)