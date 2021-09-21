# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:48:25 2021

@author: iliodis
"""
from pandas import Series
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
    T_in = df.T_in  # σημαντικη για τις τιμες που θα χρησιμοποιηθουν στις σταθερες
    
    # a = 1.3 # correction factor, εξαρταται απο θερμοκρασια μετρησης και σχετιζεται με τις επιφανειες των 2 μετρητων; 
    a = -4e-11*T_in**6 + 6e-9*T_in**5 + 2e-7*T_in**4 - 1e-5*T_in**3 - 2e-6*T_in**2 + 0.0253*T_in + 1.2669
    # Πολυωνυμικό fitting απο το Excel, πιό μεγάλο R^2 απο το εκθετικό (0,9995), προέκυψε απο τον πίνακα με τις τιμές στο SED 
    WEe = 37
    AEe = 25 # μετριουνται σε nanoAmpere , ενδεικτικες τιμες απο τον πινακα για θερμοκρασιες ~20
    b = 1 # η σταθερα που συνδεει συγκεντρωση και διορθωμενη μετρηση ρευματος, δεν ξερω ενδεικτικες τιμες, υπολογιζεται στο calibration
    WEc = O3_WE - WEe - a*(O3_AE - AEe)
    
    """Fitting & a=a(T_in)"""
    return b * WEc      


def O3ConcentrationB(df):
    O3_WE = df.O3_WE_b
    O3_AE = df.O3_AE_b
    T_in = df.T_in  # σημαντικη για τις τιμες που θα χρησιμοποιηθουν στις σταθερες
    
    # a = 1.3 # correction factor, εξαρταται απο θερμοκρασια μετρησης και σχετιζεται με τις επιφανειες των 2 μετρητων; 
    a = -4e-11*T_in**6 + 6e-9*T_in**5 + 2e-7*T_in**4 - 1e-5*T_in**3 - 2e-6*T_in**2 + 0.0253*T_in + 1.2669
    WEe = 37
    AEe = 25 # μετριουνται σε nanoAmpere , ενδεικτικες τιμες απο τον πινακα για θερμοκρασιες ~20
    b = 1 # η σταθερα που συνδεει συγκεντρωση και διορθωμενη μετρηση ρευματος, δεν ξερω ενδεικτικες τιμες, υπολογιζεται στο calibration
    WEc = O3_WE - WEe - a*(O3_AE - AEe)
    
    """Fitting & a=a(T_in)"""
    return b * WEc 


def CO2ConcentrationA(df):
    CO2_V1 = df.CO2_V1_a
    CO2_V2 = df.CO2_V2_a
    T_in = df.T_in
    
    a= 2.49
    n= 0.811 # linearization coefficients υπολογιστουν στα tests (me fittings)
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
    
    a= 2.49
    n= 0.811 # linearization coefficients υπολογιστουν στα tests (me fittings)
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