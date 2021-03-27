# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:48:25 2021

@author: iliodis
"""
V_in = 2
dt = 2

#η συνάρτηση παροχής
def flowrate(df):
    j=df['time']/dt
    
    dpin=df.P_in[j+1]-df.P_in[j]
    dtin=df.T_in[j+1]-df.T_in[j]
    
    pout=(df.P_out[j+1]+df.P_out[j])/2
    pin=(df.P_in[j+1]+df.P_in[j])/2
    
    tout=(df.T_out[j+1]+df.T_out[j])/2
    tin=(df.T_in[j+1]+df.T_in[j])/2
    
    flow=(V_in/pout)*(tout/tin)*(dpin/dt-(pin/tin)*dtin/dt)
    return flow


#Ο τρόπος που θα υπολογίζουμε το κέντρο μάζας
#Πρέπει να προηγηθεί το γέμισμα μιας στήλης με τις τιμές της flowrate


#Υπολογισμός m_tot

def centre_of_mass(data, flow): #Το όρισμα θα είναι ένας πίνακας με όλες τις στήλες δεδομένων από μία χρονική στιγμή έως μία άλλη
    
    
    "ΠΡΩΤΑ ΥΠΟΛΟΓΙΖΩ ΤΟ MTOT"
    
    
    #Η στήλη flowrate από το data
    flow_rate = [] 
    
    
    #Fixed σταθερές to be determined
    Mr = 20
    R = 8 
    
    #Έστω ότι ξεκινάει αυτό το κομμάτι της στήλης από t1 ως t2 (χρόνοι)
    time = []    #Πρώτη τιμή t1, τελευταία τιμή t2

    
    #Το αντίστοιχο κομμάτι της πίεσης και θερμοκρασίας ανάμεσα σε t1, t2
    #Πάλι από data
    P_in = []
    T_in = []
    
    #Το αντίστοιχο κομμάτι των υψομέτρων
    altitudes = []
    
    #Η μέση πίεση και θερμοκρασία
    P_mean = sum(P_in)/len(P_in)
    T_mean = sum(T_in)/len(T_in)
    
    suma_m=0
    suma_h=0
    i=0
    for j in flow_rate:
        
        Dt = time[i+1]-time[i]
        
        suma_m+=j*Dt
        
        suma_h+=j*Dt*altitudes[i]
        
        i+=1
        
    mtot = P_mean*Mr/(R*T_mean)*suma_m
    



    "Υπολογισμός κέντρου μάζας (καθ' ύψος)"
    
    
    
    #Το ζητούμενο
    h_cm = P_mean*Mr/(R*T_mean*mtot)*suma_h
    
    
    return h_cm

    
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

