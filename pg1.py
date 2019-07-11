# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:22:03 2019

@author: User
"""

import numpy as np
import pandas as pd


data=pd.read_csv("headbrain.csv")
x=data.iloc[:,2].values
y=data.iloc[:,3].values

x_mean=np.mean(x)
y_mean=np.mean(y)

def beta_x(x,x_mean):
    bet_xsq=0
    for i in range(0,len(x)):
        bet_xsq+=(x[i]-x_mean)**2
    return bet_xsq

def beta_y(y,y_mean,x_mean):
    bet_num=0
    for j in range(0,len(y)):
        bet_num+=(x[j]-x_mean)*(y[j]-y_mean)
    return bet_num

den=beta_x(x,x_mean)
num=beta_y(y,y_mean,x_mean)
beta1=num/den