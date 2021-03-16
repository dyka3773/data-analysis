# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:24:20 2021

@author: Herck
"""
class data_line:
    
    def __init__(self,P_in, P_out, T_in, T_out, Hum_in, Hum_out, CO2_V, O3_V, Altitude,time):
        #τα αντίστοιχα δεδομένα μέσα και έξω και οι γνωστές ποσότητες
        self.P_in=P_in
        self.P_out=P_out
        self.T_in=T_in
        self.T_out=T_out
        self.Hum_in = Hum_in
        self.Hum_out = Hum_out
        self.CO2_V = CO2_V
        self.O3_V = O3_V        
        self.Altitude = Altitude
        self.time=time

# =============================================================================
#       Will this ever Change?
#         
#       self.V_in=2  #litre
# =============================================================================
    
        
    @property
    def CO2Concetration(CO2_V1,CO2_V2,T_in):
      
        # I somehow calculate NRcomp & Scomp     
          
        # Conc= ((-1/a)*np.ln(1-NRcomp/Scomp)) **(1/n))
        # return Conc
        pass
    
    @property
    def O3Concetration(CO2_V1,CO2_V2,T_in):
      
        # Calculating O3
        pass