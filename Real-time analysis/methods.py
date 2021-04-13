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
            dtin=df.loc[j+1, 'T_in'] - df.loc[j, 'T_in']
            
            pout=(df.loc[j+1, 'P_out'] + df.loc[j, 'P_out'])/2
            pin=(df.loc[j+1, 'P_in'] + df.loc[j, 'P_in'])/2
            
            tout=(df.loc[j+1, 'T_out'] + df.loc[j, 'T_out'])/2
            tin=(df.loc[j+1, 'T_in'] + df.loc[j, 'T_in'])/2
            
            flow=(V_in/pout)*(tout/tin)*(dpin/dt-(pin/tin)*dtin/dt)
            
            flow_rate.append(flow)
            
            j+=1
        except:
            break
        
    return pd.Series(flow_rate, dtype='float64')


#Ο τρόπος που θα υπολογίζουμε το κέντρο μάζας
#Πρέπει να προηγηθεί το γέμισμα μιας στήλης με τις τιμές της flowrate

def centre_of_mass(df): #Το όρισμα θα είναι ένας πίνακας με όλες τις στήλες δεδομένων από μία χρονική στιγμή έως μία άλλη
    
    # Η στήλη flowrate από το data
    # df['Flowrate']
    
    #Fixed σταθερές to be determined
    Mr = 20
    R = 8 
    
    #Έστω ότι ξεκινάει αυτό το κομμάτι της στήλης από t1 ως t2 (χρόνοι)
    # df['time']    #Πρώτη τιμή t1, τελευταία τιμή t2

    #Το αντίστοιχο κομμάτι της πίεσης και θερμοκρασίας ανάμεσα σε t1, t2
    #Πάλι από data
    # df['P_in']
    # df['T_in']
    
    #Το αντίστοιχο κομμάτι των υψομέτρων
    # df['Altitude']
    
    #Η μέση πίεση και θερμοκρασία
    P_mean = sum(df['P_in'])/len(df['P_in'])
    T_mean = sum(df['T_in'])/len(df['T_in'])
    
    suma_m=0
    suma_h=0
    i=0
    
    for j in df['Flowrate']:
        
        Dt = df.loc[i+1, 'time'] - df.loc[i, 'time']
        
        suma_m += j * Dt
        
        suma_h += j * Dt * df.loc[i, 'Altitude']
        
        i+=1
        
    mtot = P_mean * Mr / (R * T_mean) * suma_m
    
    "Υπολογισμός κέντρου μάζας (καθ' ύψος)"
    
    #Το ζητούμενο
    h_cm = P_mean * Mr / (R * T_mean * mtot) * suma_h
    
    return h_cm
