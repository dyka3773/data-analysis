# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:20:54 2021
@author: Herck
"""

import pandas as pd

import plot_handler
import methods
from data_line import data_line

def main():
    df = pd.read_csv('./Sample CSV.csv', usecols=[0,1,2,3,4,5,6,7,8,9,10])
    
    print(df)
    
    #inserting data to Methods to get results ready for plots
    #NOTE THAT: time isn't inserted as we might need a different or special time for each function
    last_line = data_line(df.tail(1))
    
    #using Methods' methods to get the requested results
    flow = methods.flowrate(df[['P_in', 'T_in', 'P_out', 'T_out', 'time']])
    
    
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
