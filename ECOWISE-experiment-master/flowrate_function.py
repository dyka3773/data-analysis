# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:48:25 2021

@author: iliodis
"""


import numpy as np



"""τα αντίστοιχα δεδομένα μέσα και έξω και οι γνωστές ποσότητες"""
pressin=np.array()
pressout=np.array()

tempin=np.array()
tempout=np.array()

vin=2  """lit"""

time=np.array()

"""θεωρώ ότι τα στοιχεία στα arrays έχουν παρθεί ανά dt γνωστό, άρα time[j]=j*dt"""
dt=2   """sec"""



"""η συνάρτηση παροχής"""
def flowrate(pressin,pressout,tempin,tempout,t):
    j=t/dt
    dpin=pressin[j+1]-pressin[j]
    dtin=tempin[j+1]-tempin[j]
    
    pout=(pressout[j+1]+pressout[j])/2
    pin=(pressin[j+1]+pressin[j])/2
    
    tout=(tempout[j+1]+tempout[j])/2
    tin=(tempin[j+1]+tempin[j])/2
    
    flow=(vin/pout)*(tout/tin)*(dpin/dt-(pin/tin)*dtin/dt)
    return flow


