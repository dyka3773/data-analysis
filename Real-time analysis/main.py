# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:20:54 2021
@author: Herck
"""

import pandas as pd

import plot_handler
import methods
from data_line import data_line

def import_data():
    data = pd.read_csv('./Sample CSV.csv', header=None, usecols=[0,1,2,3,4,5,6,7,8,9],
                       names=['P_in','P_out','T_in','T_out','Hum_in'
                              ,'Hum_out','CO2_V','O3_V','Altitude','time'])
    
    P_in= data['P_in'].values
    P_in= P_in[1:]
    
    P_out= data['P_out'].values
    P_out= P_out[1:]
    
    T_in= data['T_in'].values
    T_in= T_in[1:]
    
    T_out= data['T_out'].values
    T_out= T_out[1:]
    
    Hum_in= data['Hum_in'].values
    Hum_in= Hum_in[1:]
    
    Hum_out= data['Hum_out'].values
    Hum_out= Hum_out[1:]
    
    CO2_V= data['CO2_V'].values
    CO2_V= CO2_V[1:]
    
    O3_V= data['O3_V'].values
    O3_V= O3_V[1:]
    
    Altitude= data['Altitude'].values
    Altitude= Altitude[1:]
    
    time= data['time'].values
    time= time[1:]
    
    return P_in, P_out, T_in, T_out, Hum_in, Hum_out, CO2_V, O3_V, Altitude, time



P_in, P_out, T_in, T_out, Hum_in, Hum_out, CO2_V, O3_V, Altitude, time = import_data()

for i in time: #just testing that it works
    print(i)

#inserting data to Methods to get results ready for plots
#NOTE THAT: time isn't inserted as we might need a different or special time for each function
data_to_plot = data_line(P_in, P_out, T_in, T_out, Hum_in, Hum_out, CO2_V, O3_V, Altitude)

#using Methods' methods to get the requested results
flow = methods.flowrate(P_in, T_in, P_out, T_out, time)


#Exemplary plot_handler for Humidity
plot_1 = plot_handler.humidity_plot(Hum_in, Hum_out)

 # ==============================================================================
 # import ./plots
 # 
 # pandas διαχειριση csv
 #
 # εισαγωγη δεδομένων στην methods
 # εξαγωγή δεδομένων για τα plots
 #
 # εισαγει δεδομενα σε plots
 # καλεί plots.py
 # φτυνει plots στο gui
 # ==============================================================================
