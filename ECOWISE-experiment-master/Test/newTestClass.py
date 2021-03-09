import numpy as np

class Methods:

    #θεωρώ ότι τα στοιχεία στα arrays έχουν παρθεί ανά dt γνωστό, άρα time[j]=j*dt
    dt=2   #sec

    def __init__(self,pressin,pressout,tempin,tempout,t):
        #τα αντίστοιχα δεδομένα μέσα και έξω και οι γνωστές ποσότητες
        self.pressin=np.array()
        self.pressout=np.array()

        self.tempin=np.array()
        self.tempout=np.array()

        self.vin=2  #lit

        self.time=np.array()


    #η συνάρτηση παροχής
    @property               #πλέον έτσι έχουμε access στο flowrate σαν να ήταν μεταβλητή
    def flowrate(self):
        j=self.t/self.dt
        dpin=self.pressin[j+1]-self.pressin[j]
        dtin=self.tempin[j+1]-self.tempin[j]
        
        pout=(self.pressout[j+1]+self.pressout[j])/2
        pin=(self.pressin[j+1]+self.pressin[j])/2
        
        tout=(self.tempout[j+1]+self.tempout[j])/2
        tin=(self.tempin[j+1]+self.tempin[j])/2
        
        flow=(self.vin/pout)*(tout/tin)*(dpin/self.dt-(pin/tin)*dtin/self.dt)
        return flow

