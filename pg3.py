# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:14:01 2019

@author: User
"""

import pandas as pd
import numpy as np
a=["Delhi","Bangalore","Chennai","Mumbai"]
from sklearn.preprocessing import LabelEncoder
lEncoder=LabelEncoder()
b=lEncoder.fit_transform(a)         #all cities are transformed into numeric values
c=["Delhi","Mumbai"]
lEncoder.fit(c)

p=lEncoder.transform(c)
q=lEncoder.inverse_transform([1])
#data=pd.read_csv('50_Startups.csv')
#x=data.iloc[:,0:5].values
#y=data.iloc[:,5].values