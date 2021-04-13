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
    df = pd.read_csv('./Sample CSV.csv', 
                     names=['time', 'P_in', 'P_out', 'T_in', 'T_out', 'Hum_in', 
                            'Hum_out', 'CO2_V1', 'CO2_V2', 'O3_WE', 'O3_AE',
                            'Altitude'],
                     header=0,
                     usecols=[i for i in range(0,11)])
    
    df['O3_ppm'] = df.apply(data_line.O3Concentration, axis=1)
    df['CO2_%v/v'] = df.apply(data_line.CO2Concentration, axis=1)
    df['Flowrate'] = methods.flowrate(df)
    
# =============================================================================
#     Check names and units
# =============================================================================
    
    print(df)
    
    plot_ex = plot_handler.temp_and_press_plot(df.loc[:,['time','P_out']])
    
    #Exemplary plot_handler for Humidity
    plot_1 = plot_handler.humidity_plot(df['Hum_in'], df['Hum_out'], df['Altitude'])




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
