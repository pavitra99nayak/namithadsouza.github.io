# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:37:30 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:13:48 2019

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('headbrain.csv')
x_train=data.iloc[:,2].values
y_train=data.iloc[:,3].values
x_test=data.iloc[:100,2].values
y_test=data.iloc[:100,3].values
xmean=x_train.mean()
ymean=y_train.mean()
upper=0
lower=0
for i in range(0,len(x)):                                #for formula refer notes 
    upper=upper+((x[i]-xmean)*(y[i]-ymean))
    lower=lower+((x[i]-xmean)**2)
b1=upper/lower
#print(B1)
b0=ymean-(b1*xmean)                #slope m =B1 and coefficient c =B0
#print(B0)

y_pred=b1*x_test+b0
plt.scatter(x_train,y_train,color='red',label='Training')
plt.scatter(x_test,y_pred,color='blue',label='pedicting')
plt.scatter(x_test,y_test,color='green',label='actual/test')
plt.legend()
plt.show()

sst,ssr=0,0
for i in range(len(y_test)):
    sst+=(y_test[i] - y_test.mean())**2
    ssr+=(y_test[i] - y_pred[i].mean())**2
r=1-float(ssr)/float(sst)

print("score of the mark is ",r)

#x1=data.iloc[:,2:3].values
#from sklearn.linear_model import LinearRegression   #it is a class
#regressor=LinearRegression()
#regressor.fit(x1,y)
#m=regressor.coef_
#c=regressor.intercept_
#print(m)
#print(c)

