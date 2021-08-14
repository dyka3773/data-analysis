import csv
import pandas as pd
import time

df = pd.read_excel('../Real-time analysis/XLSXs/First_Cycles.xlsx')

# print(df)

fieldnames = [
    'time', 
    'P_in', 'P_out',
    'T_in', 'T_out', 
    'Hum_in', 'Hum_out',
    'CO2_V1_a', 'CO2_V2_a',
    'CO2_V1_b', 'CO2_V2_b',
    'O3_WE_a', 'O3_AE_a',
    'O3_WE_b', 'O3_AE_b',
    'Altitude',
    'flags'
    ]

with open('data_csv.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
    csv_writer.writeheader()
   

i=0
while True:
    
    with open('data_csv.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
        
        info = {
            'time': df.iloc[i,0],
            'P_in': df.iloc[i,1],
            'P_out': df.iloc[i,2],
            'T_in': df.iloc[i,3],
            'T_out': df.iloc[i,4],
            'Hum_in': df.iloc[i,5],
            'Hum_out': df.iloc[i,6],
            'CO2_V1_a': df.iloc[i,7],
            'CO2_V2_a': df.iloc[i,8],
            'CO2_V1_b': df.iloc[i,9],
            'CO2_V2_b': df.iloc[i,10],
            'O3_WE_a': df.iloc[i,11],
            'O3_AE_a': df.iloc[i,12],
            'O3_WE_b': df.iloc[i,13],
            'O3_AE_b': df.iloc[i,14],
            'Altitude': df.iloc[i,15],
            'flags': df.iloc[i,16]
        }
        
        csv_writer.writerow(info)
        print(df.iloc[i,0], df.iloc[i,15]) # Time - Altitude
        
        i +=1
    time.sleep(1)
