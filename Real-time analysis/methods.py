# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:48:25 2021

@author: iliodis
"""
V_in = 2
dt = 2

#η συνάρτηση παροχής
def flowrate(P_in, T_in, P_out, T_out, t):
    j=t/dt
    
    dpin=P_in[j+1]-P_in[j]
    dtin=T_in[j+1]-T_in[j]
    
    pout=(P_out[j+1]+P_out[j])/2
    pin=(P_in[j+1]+P_in[j])/2
    
    tout=(T_out[j+1]+T_out[j])/2
    tin=(T_in[j+1]+T_in[j])/2
    
    flow=(V_in/pout)*(tout/tin)*(dpin/dt-(pin/tin)*dtin/dt)
    return flow


#Ο τρόπος που θα υπολογίζουμε το κέντρο μάζας
def Center_of_Mass():
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

