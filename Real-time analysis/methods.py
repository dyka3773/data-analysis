# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:48:25 2021

@author: iliodis
"""
import pandas as pd

V_in = 2
dt = 2


#η συνάρτηση παροχής
def flowrate(df):
    flow_rate=[]
    j=0
    
    for k in df['time']:
        try:
            dt = df.loc[j+1, 'time'] - k
            
            dpin=df.loc[j+1, 'P_in'] - df.loc[j, 'P_in']
            
            #dtin=df.loc[j+1, 'T_in'] - df.loc[j, 'T_in']
            
            dtin=0
            pout=(df.loc[j+1, 'P_out'] + df.loc[j, 'P_out'])/2
            pin=(df.loc[j+1, 'P_in'] + df.loc[j, 'P_in'])/2
            
            tout=273+(df.loc[j+1, 'T_out'] + df.loc[j, 'T_out'])/2
            tin=273+(df.loc[j+1, 'T_in'] + df.loc[j, 'T_in'])/2
            
            flow=(V_in/pout)*(tout/tin)*(dpin/dt-(pin/tin)*dtin/dt)*60
            
            flow_rate.append(flow if flow>0 else 0)     # WRONG
            
            j+=1
        except:
            continue
        
    return pd.Series(flow_rate, dtype='float64')



def centre_of_mass(df): #Το όρισμα θα είναι ένας πίνακας με όλες τις στήλες δεδομένων από μία χρονική στιγμή έως μία άλλη
# Only parts of the original dataset needed
    
    #Fixed σταθερές to be determined
    Mr = 20
    R = 8 
    
    #Η μέση πίεση και θερμοκρασία
    P_mean = df['P_in'].mean()
    T_mean = df['T_in'].mean()
    
    
    suma_m=0
    suma_h=0
    i=0
    
    for j in df['Flowrate']:
        try:
            Dt = df.loc[i+1, 'time'] - df.loc[i, 'time']
            
            suma_m += j * Dt
            
            suma_h += j * Dt * df.loc[i, 'Altitude']
            
            i+=1
        except:
            continue
        
    mtot = P_mean * Mr / (R * T_mean) * suma_m
    
    "Υπολογισμός κέντρου μάζας (καθ' ύψος)"
    
    #Το ζητούμενο
    h_cm = (P_mean * Mr / (R * T_mean * mtot)) * suma_h
    
    return h_cm
