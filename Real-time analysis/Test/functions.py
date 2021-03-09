# -*- coding: utf-8 -*-
import numpy as np
#from matplotlib

def f(x):
    return np.log(x)

suma=0

for i in range(1000):
    s= np.linspace(0, 100, num=10*i, endpoint=True)
    #print(s)
    
    for j in range(len(s)-1):
        suma += (s[j+1]-s[j]) * (f(( s[j+1]+s[j])/2 ))
        #print(suma)
    """
    for i in range(len(s)-1):
    print(f((s[i+1]+s[i])/2))
    """
    
    print(suma)
    suma=0


