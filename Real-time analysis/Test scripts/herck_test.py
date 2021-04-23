# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:51:41 2021

@author: Herck
"""
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm


def O3_conc(df):
    
    O3_conc_figure, ax5 = plt.subplots()
    
    ax5.grid(linewidth= 0.5, linestyle= '--', color= '#262626', alpha= 0.2)
    plt.rcParams['axes.facecolor'] = '#ccccff'
    ax5.scatter(df['Altitude'], df['O3_ppm'], s=20,marker= '.', 
                  label = "ECO-WISE 2021")
    
    ax5.set_title("O3 concentration")
    ax5.set_xlabel("O3 (ppb)")
    ax5.set_ylabel("Altitude (m)")
    ax5.legend()
    plt.tight_layout()
    
    return O3_conc_figure


def CO2_conc(df):
    
    CO2_conc_figure, ax6 = plt.subplots()
    
    ax6.grid(linewidth= 0.5, linestyle= '--', color= '#262626', alpha= 0.2)
    plt.rcParams['axes.facecolor'] = '#ccccff'
    ax6.scatter(df['Altitude'], df['CO2_C'], s=20, 
                marker= '.', label = "ECO-WISE 2021")
    
    ax6.set_title("CO2 concentration")
    ax6.set_xlabel("CO2 (v/v %)")
    ax6.set_ylabel("Altitude (m)")
    ax6.legend()
    plt.tight_layout()
    
    return CO2_conc_figure


def temp_press_out_plot(df):
    temp_press_out_figure, ax3 = plt.subplots()
    
    plt.style.use('seaborn')
    
    colors=df['T_out']
    
    # ax3.grid(linewidth= 0.5, linestyle= '--', color= '#262626', alpha= 0.2)
    # plt.rcParams['axes.facecolor'] = '#ccccff'
    ax3.scatter(df['P_out'], df['Altitude'], s=20, c=colors, cmap='jet', 
                  label = "ECO-WISE 2021",marker= '.')
    
    cbar = temp_press_out_figure.colorbar(cm.ScalarMappable(cmap= 'jet'),ax = ax3)
    cbar.set_label('Temperature out (°C)')
    
    ax3.set_title("Environmental variables")
    ax3.set_xlabel("Pressure (mbar)")
    ax3.set_ylabel("Altitude (m)")
    ax3.legend()
    plt.tight_layout()
    
    return temp_press_out_figure


def altitude_time(df):
    
    altitude_time_figure, ax7 = plt.subplots()
    
    colors=df['T_out']
    
    ax7.grid(linewidth= 0.5, linestyle= '--', color= '#262626', alpha= 0.2)
    plt.rcParams['axes.facecolor'] = '#ccccff'
    ax7.scatter(df['time'], df['Altitude'], s=20, c=colors, cmap='jet', 
                marker= '.', label = "ECO-WISE 2021")
    
    cbar = altitude_time_figure.colorbar(cm.ScalarMappable(cmap= 'jet'),ax = ax7)
    cbar.set_label('Temperature out (°C)')
    
    ax7.set_title("Balloon altitude (Altitude Over Time)")
    ax7.set_xlabel("Time (min)")
    ax7.set_ylabel("Altitude (m)")
    ax7.legend()
    plt.tight_layout()
    
    return altitude_time_figure



df = pd.read_excel('../XLSXs/Sample CSV1.xlsx', 
                     names=['time', 'P_out',  'T_out',  
                            'Hum_out', 'Altitude','CO2_C','O3_ppm'],
                     header=0,
                     usecols=[0,2,4,6,11,14,15])

print(df)

temp_out_plot = temp_press_out_plot(df.loc[:,['T_out','P_out','Altitude']])
print(temp_out_plot)
altitude_plot= altitude_time(df.loc[:,['time','Altitude','T_out']])
print(altitude_plot)
O3_plot = O3_conc(df.loc[:,['O3_ppm','Altitude']])
print(O3_plot)
CO2_plot = CO2_conc(df.loc[:,['CO2_C','Altitude']])
print(CO2_plot)