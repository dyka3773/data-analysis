# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:24:20 2021

@author: Herck
"""
import numpy as np

class data_line:
    
    def __init__(self,df):
        #τα αντίστοιχα δεδομένα μέσα και έξω και οι γνωστές ποσότητες ως DataFrame
        self.df = df
        
# =============================================================================
#       Will this ever Change?
#         
#       self.V_in=2  #litre
# =============================================================================
    
        
    @property
    def CO2Concetration(self):
        
        CO2_V1 = self.df.CO2_V1
        CO2_V2 = self.df.CO2_V2
        T_in = self.df.T_in
        
        a= 1.52
        n= 0.724 # linearization coefficients υπολογιστουν στα tests
        
        # I somehow calculate NRcomp & Scomp
        NRcomp=0
        Scomp=0
          
        Conc= ((-1/a)*np.ln(1-NRcomp/Scomp)) **(1/n)
        return Conc
    
    @property
    def O3Concetration(self):
        
        O3_V1 = self.df.O3_V1
        O3_V2 = self.df.O3_V2
        T_in = self.df.T_in
        
        # Calculating O3
        pass