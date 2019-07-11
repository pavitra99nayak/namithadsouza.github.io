# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:13:48 2019

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('headbrain.csv')
x=data.iloc[:,2].values
y=data.iloc[:,3].values
xmean=np.mean(x)
ymean=np.mean(y)
upper=0
lower=0
for i in range(0,len(x)):                                #for formula refer notes 
    upper=upper+((x[i]-xmean)*(y[i]-ymean))
    lower=lower+((x[i]-xmean)**2)
B1=upper/lower
print(B1)
B0=ymean-(B1*xmean)                #slope m =B1 and coefficient c =B0
print(B0)

x1=data.iloc[:,2:3].values
from sklearn.linear_model import LinearRegression   #it is a class
regressor=LinearRegression()
regressor.fit(x1,y)
m=regressor.coef_
c=regressor.intercept_
print(m)
print(c)

