# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:48:25 2021

@author: iliodis
"""


import numpy as np

class Methods:

    #θεωρώ ότι τα στοιχεία στα arrays έχουν παρθεί ανά dt γνωστό, άρα time[j]=j*dt
    dt=2   #sec

    def __init__(self,P_in, P_out, T_in, T_out, Hum_in, Hum_out, CO2_V, O3_V, Altitude):
        #τα αντίστοιχα δεδομένα μέσα και έξω και οι γνωστές ποσότητες
        self.P_in=np.array(P_in)
        self.P_out=np.array(P_out)

        self.T_in=np.array(T_in)
        self.T_out=np.array(T_out)
        
        self.Hum_in = np.array(Hum_in)
        self.Hum_out = np.array(Hum_out)
        
        self.CO2_V = np.array(CO2_V)
        self.O3_V = np.array(O3_V)
        
        self.Altitude = np.array(Altitude)

        self.vin=2  #litre


    #η συνάρτηση παροχής
    def flowrate(self, t):
        j=t/self.dt
        
        dpin=self.P_in[j+1]-self.P_in[j]
        dtin=self.T_in[j+1]-self.T_in[j]
        
        pout=(self.P_out[j+1]+self.P_out[j])/2
        pin=(self.P_in[j+1]+self.P_in[j])/2
        
        tout=(self.T_out[j+1]+self.T_out[j])/2
        tin=(self.T_in[j+1]+self.T_in[j])/2
        
        flow=(self.vin/pout)*(tout/tin)*(dpin/self.dt-(pin/tin)*dtin/self.dt)
        return flow
    
    #Συνάρτηση υπολογισμού Συγκέντρωσης Διοξειδίου
    def CO2_Concentration(self,t):
        pass
    
    #Συνάρτηση υπολογισμού Συγκέντρωσης Όζοντος
    def O3_Concentration(self,t):
        pass

    #Ο τρόπος που θα υπολογίζουμε το κέντρο μάζας
    def Center_of_Mass(self):
        #δεν ξέρω τι πρέπει να μπαίνει παραμετρικά γιατι δε ξέρω τι χρειάζεται για να υπολογιστεί αυτό
        pass
    
    
##################### Το παραπάνω είναι η σωστή τεχνική #####################

# =============================================================================
# #τα αντίστοιχα δεδομένα μέσα και έξω και οι γνωστές ποσότητες
# pressin=np.array()
# pressout=np.array()
# 
# tempin=np.array()
# tempout=np.array()
# 
# vin=2  #lit
# 
# time=np.array()
# dt=2   #sec
# 
# 
# 
# #η συνάρτηση παροχής
# def flowrate(pressin,pressout,tempin,tempout,t):
#     j=t/dt
#     dpin=pressin[j+1]-pressin[j]
#     dtin=tempin[j+1]-tempin[j]
#     
#     pout=(pressout[j+1]+pressout[j])/2
#     pin=(pressin[j+1]+pressin[j])/2
#     
#     tout=(tempout[j+1]+tempout[j])/2
#     tin=(tempin[j+1]+tempin[j])/2
#     
#     flow=(vin/pout)*(tout/tin)*(dpin/dt-(pin/tin)*dtin/dt)
#     return flow
# 
# =============================================================================

