# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:55:43 2021

@author: Herck
"""
import numpy as np


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
    
    a= 0.652
    n= 0.746 # linearization coefficients υπολογιστουν στα tests (me fittings)
    Z = 1.33 
    S = 0.4408   # Zero και Span , θα υπολογιστούν οταν γίνουν τα test (me fittings)
    Tcal = 19.78 # kata protimhsh 20
    apos = 0.000556
    aneg = 0.000438
    bpos = 0.124
    bneg = 0.219
    
    """TOWATCH Fitting Temp"""
    
    NR = CO2_V1/(Z*CO2_V2)
    
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
    
    a= 0.652
    n= 0.746 # linearization coefficients υπολογιστουν στα tests (me fittings)
    Z = 1.33 
    S = 0.4408   # Zero και Span , θα υπολογιστούν οταν γίνουν τα test (me fittings)
    Tcal = 19.78 # kata protimhsh 20
    apos = 0.000556
    aneg = 0.000438
    bpos = 0.124
    bneg = 0.219
    
    """TOWATCH Fitting Temp"""
    
    NR = CO2_V1/(Z*CO2_V2)
    
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