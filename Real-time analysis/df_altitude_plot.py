# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:12:49 2021

@author: You
"""


#Dataframe for the altitude plot "df_alt"
import pandas as pd

df = pd.read_excel('./XLSXs/First_Cycles.xlsx',
                       names=['time', 'P_in', 'P_out', 'T_in', 'T_out', 'Hum_in',
                              'Hum_out', 'CO2_V1', 'CO2_V2', 'O3_WE', 'O3_AE',
                              'Altitude','flags'],
                     header=0,
                     usecols=[i for i in range(0,13)])

df_alt = pd.DataFrame(columns=("cycle",
              "ymin","ymax","yerrmin","yerrmax",
              "altitude","CO2_1","xerrCO2_1","CO2_2","xerrCO2_2",
              "O3_1","xerrO3_1","O3_2","xerrO3_2"))

j=0
i=0
for k in df['flags']:
    
    if df.loc[j+1, 'flags']-k == 1:
        
        df_alt.loc[i,"cycle"] = i+1
        df_alt.loc[i,"ymin"] = df.loc[j,'Altitude']
        
    elif df.loc[j+1, 'flags']-k == -1:
        
        df_alt.loc[i,"ymax"] = df.loc[j,'Altitude']
        i+=1
    
    j+=1
    
#Should we include centre of mass ONLY here???
    
for k in df_alt["ymin"]:
    
    
    df_alt.loc[i-1,"altitude"]