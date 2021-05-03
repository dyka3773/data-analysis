import csv
import pandas as pd
import time

df = pd.read_excel('../Real-time analysis/XLSXs/First_Cycles.xlsx')

# print(df)

fieldnames = ['time', 'P_in', 'P_out', 'T_in', 'T_out', 'Hum_in', 'Hum_out', 'CO2_V1', 
              'CO2_V2', 'O3_WE', 'O3_AE', 'Altitude', 'flags']

with open('data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
    csv_writer.writeheader()
   

i=0
while True:
    
    with open('data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
        
        info = {
            'time': df.iloc[i,0],
            'P_in': df.iloc[i,1],
            'P_out': df.iloc[i,2],
            'T_in': df.iloc[i,3],
            'T_out': df.iloc[i,4],
            'Hum_in': df.iloc[i,5],
            'Hum_out': df.iloc[i,6],
            'CO2_V1': df.iloc[i,7],
            'CO2_V2': df.iloc[i,8],
            'O3_WE': df.iloc[i,9],
            'O3_AE': df.iloc[i,10],
            'Altitude': df.iloc[i,11],
            'flags': df.iloc[i,12]
        }
        
        csv_writer.writerow(info)
        print(df.iloc[i,0], df.iloc[i,11]) # Time - Altitude
        
        i +=1
    time.sleep(1)
