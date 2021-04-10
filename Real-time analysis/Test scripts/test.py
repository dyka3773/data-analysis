# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:42:51 2021

@author: Herck
"""
import csv
import pandas as pd
import time
import threading


df1 = pd.read_csv('./simulation.csv')
print(df1)