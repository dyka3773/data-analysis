# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:53:41 2021

@author: Herck
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sensor_box(i):
    df = pd.read_excel('../XLSXs/First_Cycles.xlsx', 
                         names=['time', 'P_in', 'T_in'],
                         usecols=[3,0,1])
    # print(df)
    
    ax8.cla()
    
    colors=df['T_in']
    plot = ax8.scatter(df['time'],df['P_in'], s=20, c=colors, cmap='jet', 
                marker= '.', label = "ECO-WISE 2021")
    temp_press_in_figure.colorbar(plot, ax=ax8,label = 'Temperature in (°C)')
    
    ax8.set_title("Sensor box variables")
    ax8.set_xlabel("Time (sec)")
    ax8.set_ylabel("Pressure (mbar)")
    ax8.legend()
    plt.tight_layout()

temp_press_in_figure, ax8 = plt.subplots()

ani = FuncAnimation(temp_press_in_figure, sensor_box, interval=1000)