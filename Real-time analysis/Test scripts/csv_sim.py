import csv
import pandas as pd
import time

df = pd.read_excel('../Real-time analysis/XLSXs/First_Cycles.xlsx')

# print(df)

fieldnames = ['time', 'Pscl', 'T', 'RH', 'v', 'u', 'Height', 'P', 
              'TD', 'MR', 'DD', 'FF', 'AZ', 'Range', 'Lon', 'Lat',
              'Key', 'UsrKey', 'RadarH']

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
    csv_writer.writeheader()
   

i=0
while True:
    
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
        
        info = {
            'time': df.iloc[i,0],
            'Pscl': df.iloc[i,1],
            'T': df.iloc[i,2],
            'RH': df.iloc[i,3],
            'v': df.iloc[i,4],
            'u': df.iloc[i,5],
            'Height': df.iloc[i,6],
            'P': df.iloc[i,7],
            'TD': df.iloc[i,8],
            'MR': df.iloc[i,9],
            'DD': df.iloc[i,10],
            'FF': df.iloc[i,11],
            'AZ': df.iloc[i,12],
            'Range': df.iloc[i,13],
            'Lon': df.iloc[i,14],
            'Lat': df.iloc[i,15],
            'Key': df.iloc[i,16],
            'UsrKey': df.iloc[i,17],
            'RadarH': df.iloc[i,18]
        }
        
        csv_writer.writerow(info)
        print(df.iloc[i,0], df.iloc[i,6]) # TIME - HEIGHT
        
        i +=1
    time.sleep(1)
