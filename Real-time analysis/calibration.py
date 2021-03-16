# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:43:47 2021

@author: Jchar
"""
import pandas as pd
import numpy as np
from numpy import log as ln

def import2_data():
        data = pd.read_csv('./Sample CSV.csv', header=None, usecols=[6,7,],
                           names=['CO2_V1','CO2_V2'])
        
        CO2_V1= data['CO2_V1'].values
        CO2_V1= CO2_V1[1:]
        
        CO2_V2= data['CO2_V2'].values
        CO2_V2= CO2_V2[1:]
        
        data2 = pd.read_csv('./Sample CSV2.csv', header=None, usecols=[0,1],
                                names=['NRcomp','Scomp'])
        NRcomp= data2['NRcomp'].values
        NRcomp= NRcomp[1:]
        
        Scomp= data2['Scomp'].values
        Scomp= Scomp[1:]
        
        return CO2_V1,CO2_V2,NRcomp,Scomp
    
    CO2_V1,CO2_V2,NRcomp,Scomp = import2_data()
    
class Calibration: #Θα εχει μαλλον υπολογισμο NRcomp,Scomp αντι για import, πρεπει πρωτα ομως να γινει temperature compensation 
    
    dt= 2
    a= 1.52
    n= 0.724 # linearization coefficients υπολογιστουν στα tests
    
    def __init__(self,CO2_V1,CO2_V2,NRcomp,Scomp):
        
        self.CO2_V1=np.array(CO2_V1)
        self.CO2_V2=np.array(CO2_V2)
        
        self.NRcomp=np.array(NRcomp)
        self.Scomp=np.array(Scomp)
        

    def CO2Concetration(self, t):
     
       j=t/self.dt #Μέτρηση j αντιστοιχεί στο t/dt βήμα
       
       Conc= ((-1/a)*np.ln(1-NRcomp[j]/Scomp[j])) **(1/n))
       return Conc
      
       

    
    
    