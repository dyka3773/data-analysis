# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:12:49 2021

@author: You
"""

import methods

#Dataframe for the altitude plot "df_alt"
import pandas as pd

df = pd.read_excel('./XLSXs/First_Cycles.xlsx',
                       names=['time', 'P_in', 'P_out', 'T_in', 'T_out', 'Hum_in',
                              'Hum_out', 'CO2_V1', 'CO2_V2', 'O3_WE', 'O3_AE',
                              'Altitude','flags'],
                     header=0,
                     usecols=[i for i in range(0,13)])

df['Flowrate'] = methods.flowrate(df.mask(lambda x: x['flags']!=1))
# print(df)

df_alt = pd.DataFrame(columns=("cycle",
              "ymin","ymax","yerrmin","yerrmax",
              "altitude","CO2_1","xerrCO2_1","CO2_2","xerrCO2_2",
              "O3_1","xerrO3_1","O3_2","xerrO3_2"))


j=0
i=0

df_alt.loc[i,"cycle"] = i+1
df_alt.loc[i,"ymin"] = df.loc[0,'Altitude']
            
for k in df['flags']: # TODO: Continue should be somewhere in here
    try:
        if df.loc[j+1, 'flags']-k == 0:
            j+=1
            continue
            
        elif df.loc[j+1, 'flags']-k == 1:
            
            df_alt.loc[i,"cycle"] = i+1
            df_alt.loc[i,"ymin"] = df.loc[j+1,'Altitude']
            j+=1
            
        elif df.loc[j+1, 'flags']-k == -1:
            
            df_alt.loc[i,"ymax"] = df.loc[j,'Altitude']
            i+=1
            j+=1
        
    except:
        df_alt.loc[i,"ymax"] = df.loc[j,'Altitude']
        j+=1
   
# print(df_alt)    

i=0
for row in df_alt['ymin']:             
    # Αν σκοπευουμε να συνεχίσουμε τις μετρήσεις μετα το Ascending Stage του πειράματος θα υπάρχει θέμα εδώ
    
    ymin = df_alt.loc[i,'ymin']
    ymax = df_alt.loc[i,'ymax']
    
    filt = (df['Altitude'] > ymin) & (df['Altitude'] < ymax)
    
    dummy_df = df.loc[filt]
    
    df_alt.loc[i,'altitude'] =(methods.centre_of_mass(dummy_df.reset_index()))
    
    i+=1

df_alt['yerrmin'] = df_alt['altitude'] - df_alt['ymin']
df_alt['yerrmax'] =  df_alt['ymax'] - df_alt['altitude']

# pd.set_option('display.max_columns', None)

print(df_alt)