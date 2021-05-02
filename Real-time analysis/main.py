# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:20:54 2021
@author: Herck
"""

import pandas as pd

import plot_handler
import methods
import data_line

def main():
    df = pd.read_excel('./XLSXs/First_Cycles.xlsx',
                       names=['time', 'P_in', 'P_out', 'T_in', 'T_out', 'Hum_in',
                              'Hum_out', 'CO2_V1', 'CO2_V2', 'O3_WE', 'O3_AE',
                              'Altitude','flags'],
                     header=0,
                     usecols=[i for i in range(0,13)])
    
# =============================================================================    
#    #SampleCSV1 
#    df = pd.read_excel('./XLSXs/Sample CSV1.xlsx',
#                       names=['time', 'P_in', 'P_out', 'T_in', 'T_out', 'Hum_in',
#                              'Hum_out', 'CO2_V1', 'CO2_V2', 'O3_WE', 'O3_AE',
#                              'Altitude','flags','flowrate','CO2','O3','CoM','SB_temp'],
#                     header=0,
#                     usecols=[i for i in range(0,18)])
# =============================================================================
    
# =============================================================================
#     #Real CSV
#     df = pd.read_csv('./CSVs/data_csv.csv', 
#                      names=['T_in','T_out', 'P_in', 'P_out','Hum_in', 
#                             'Hum_out','Pump_Temp','SB_Temp','Gps_X','Gps_Y','Gps_altitude',
#                             'O3_WE', 'O3_AE', 'CO2_V1', 'CO2_V2','time',
#                             'Altitude','flags'],
#                      header=0,
#                      usecols=[i for i in range(0,13)])
#     
# =============================================================================
    
    df['O3_ppm'] = df.apply(data_line.O3Concentration, axis=1)
    df['CO2_C'] = df.apply(data_line.CO2Concentration, axis=1)
    df['Flowrate'] = methods.flowrate(df.mask(lambda x: x['flags']!=1))
    
# =============================================================================
#     Check names and units
# =============================================================================
    pd.set_option('display.max_rows', None)
    print(df)
    
    flow_plot = plot_handler.flow_rate_plot(df.loc[:,['time','Flowrate']])
    print(flow_plot)
    
    temp_out_plot = plot_handler.temp_press_out_plot(df.loc[:,['T_out','P_out','Altitude']])
    print(temp_out_plot)
    
    humidity_plot = plot_handler.humidity_plot(df.loc[:,['time','Hum_in','Hum_out']])
    print(humidity_plot)
    
    # These need flags
    O3_plot = plot_handler.O3_conc(df.loc[:,['O3_ppm','Altitude']])
    print(O3_plot)
    CO2_plot = plot_handler.CO2_conc(df.loc[:,['CO2_C','Altitude']])
    print(CO2_plot)

    altitude_plot= plot_handler.altitude_time(df.loc[:,['time','Altitude','T_out']])
    print(altitude_plot)
    
    temp_in_plot = plot_handler.temp_press_in_plot(df.loc[:,['T_in','P_in','time']])
    print(temp_in_plot)

if __name__=="__main__":
    main()

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





