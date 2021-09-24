# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:48:25 2021

@author: iliodis
"""
from pandas import Series
# import pandas as pd
import numpy as np

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
        
    return Series(flow_rate, dtype='float64')



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


def O3ConcentrationA(df):
    O3_WE = df.O3_WE_a
    O3_AE = df.O3_AE_a
    T_in = df.T_in
    
    a =  -1*10**(-5)*T_in**3 + 6e-5*T_in**2 + 0.0255*T_in + 1.2683
    WEe = 0.6
    AEe = 0.6
    b = 1 # η σταθερα που συνδεει συγκεντρωση και διορθωμενη μετρηση ρευματος, δεν ξερω ενδεικτικες τιμες, υπολογιζεται στο calibration
    WEc = O3_WE - WEe - a*(O3_AE - AEe)
    
    """Fitting & a=a(T_in)"""
    return b * WEc + 4.5    


def O3ConcentrationB(df):
    O3_WE = df.O3_WE_b
    O3_AE = df.O3_AE_b
    T_in = df.T_in
    
    a =  -1*10**(-5)*T_in**3 + 6e-5*T_in**2 + 0.0255*T_in + 1.2683
    WEe = 0.6
    AEe = 0.6
    b = 1 # η σταθερα που συνδεει συγκεντρωση και διορθωμενη μετρηση ρευματος, δεν ξερω ενδεικτικες τιμες, υπολογιζεται στο calibration
    WEc = O3_WE - WEe - a*(O3_AE - AEe)
    
    """Fitting & a=a(T_in)"""
    return b * WEc + 4.5


def CO2ConcentrationA(df):
    CO2_V1 = df.CO2_V1_a
    CO2_V2 = df.CO2_V2_a
    T_in = df.T_in
    
    a = 2.49
    n = 0.811 # linearization coefficients υπολογιστουν στα tests (me fittings)
    Z = 1.33 
    S = 0.4408   # Zero και Span , θα υπολογιστούν οταν γίνουν τα test (me fittings)
    Tcal = 19.78 # kata protimhsh 20
    apos = 0.000556
    aneg = 0.000438
    bpos = 0.124
    bneg = 0.219
    
    """TOWATCH Fitting Temp"""
    
    NR = CO2_V2/(Z*CO2_V1)
    
    if (T_in>Tcal):
        NRcomp = NR*(1+apos*(T_in-Tcal))
        Scomp = S + bpos*(T_in-Tcal)/Tcal
    else:
        NRcomp = NR*(1+aneg*(T_in-Tcal))
        Scomp = S + bneg*(T_in-Tcal)/Tcal
    
    if (1 - NRcomp > 0):
        result = ((-1/a)*np.log(1-((1-NRcomp)/Scomp))) **(1/n)
    else:
        result = -((1/a)*np.log(1-((-1+NRcomp)/Scomp))) **(1/n)
    return result

def CO2ConcentrationB(df):
    CO2_V1 = df.CO2_V1_b
    CO2_V2 = df.CO2_V2_b
    T_in = df.T_in
    
    a = 2.49
    n = 0.811 # linearization coefficients υπολογιστουν στα tests (me fittings)
    Z = 1.33 
    S = 0.4408   # Zero και Span , θα υπολογιστούν οταν γίνουν τα test (me fittings)
    Tcal = 19.78 # kata protimhsh 20
    apos = 0.000556
    aneg = 0.000438
    bpos = 0.124
    bneg = 0.219
    
    """TOWATCH Fitting Temp"""
    
    NR = CO2_V2/(Z*CO2_V1)
    
    if (T_in>Tcal):
        NRcomp = NR*(1+apos*(T_in-Tcal))
        Scomp = S + bpos*(T_in-Tcal)/Tcal
    else:
        NRcomp = NR*(1+aneg*(T_in-Tcal))
        Scomp = S + bneg*(T_in-Tcal)/Tcal
    
    if (1 - NRcomp > 0):
        result = ((-1/a)*np.log(1-((1-NRcomp)/Scomp))) **(1/n)
    else:
        result = -((1/a)*np.log(1-((1-NRcomp)*(-1/Scomp))))**(1/n)
    return result

""" def CO2Conc(df_asc):
    listA = []
    listB = []

    for i in range(len(df_asc['time'])):
        try:
            mean_temp = df_asc.loc[i-60:i,'T_in'].mean()

            D_V1_a = df_asc.loc[i-60:i,'CO2_V1_a'].max() - df_asc.loc[i-60:i,'CO2_V1_a'].min()
            D_V2_a = df_asc.loc[i-60:i,'CO2_V2_a'].max() - df_asc.loc[i-60:i,'CO2_V2_a'].min()
            
            D_V1_b = df_asc.loc[i-60:i,'CO2_V1_b'].max() - df_asc.loc[i-60:i,'CO2_V1_b'].min()
            D_V2_b = df_asc.loc[i-60:i,'CO2_V2_b'].max() - df_asc.loc[i-60:i,'CO2_V2_b'].min()

            df_new = pd.DataFrame([[mean_temp,D_V1_a,D_V2_a]], columns=['T_in', 'CO2_V1_a', 'CO2_V2_a'])
            listA.append(CO2ConcentrationA(df_new))

            df_new = pd.DataFrame([[mean_temp,D_V1_b,D_V2_b]], columns=['T_in', 'CO2_V1_b', 'CO2_V2_b'])
            listB.append(CO2ConcentrationB(df_new))
        except:
            listA.append(None)
            listB.append(None)


    return Series(listA, dtype='float64'), Series(listB, dtype='float64') """
    