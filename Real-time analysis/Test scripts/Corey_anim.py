# -*- coding: utf-8 -*-
"""
Created on Sun May  2 22:03:13 2021

@author: Herck
"""
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['time']
    y1 = data['Altitude']

    plt.cla()

    plt.plot( y1, x, label='Test')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()