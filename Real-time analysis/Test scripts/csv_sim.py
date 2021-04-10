# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:20:07 2021

@author: Herck
"""

import csv
import pandas as pd
import time
import threading

df = pd.read_excel('./Bexus 27 PTU data.xlsx')

# print(df)
def waiting():
    with open('simulation.csv', mode='w') as submission_file:
        submission_file = csv.writer(submission_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        submission_file.writerow(x for x in df)
        
        for _ , row in df.iterrows():
            submission_file.writerow(j for j in row)
            time.sleep(1)
        
    
    # submission_file.close()

timerThread = threading.Thread(target=waiting)
timerThread.daemon = True
timerThread.start()
 
# time.sleep(3)       
# df1 = pd.read_csv('./simulation.csv')
# print(df1)