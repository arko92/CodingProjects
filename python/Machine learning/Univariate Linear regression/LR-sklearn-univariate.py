# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:20:36 2022

@author: arkob
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.linear_model import SGDRegressor
#from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LinearRegression

################ Import data ##################################################
'''
data[0] = population of a city
data[1] = profit of a food truck in that city.
A negative value for profit indicates a loss

'''
data = pd.read_csv('ex1data1.txt', sep=",", header=None)       

################ Import data ##################################################
                 
################ Extract data ##################################################

X = data.iloc[:,0]                                                             # population size in 10,000s (Feature scaled)                         
y = data.iloc[:,1]                                                             # profit in $10,000s (Feature scaled)

m = X.size                                                                     # Number of training examples

################ Extract data ##################################################


################ Initial plotting ##############################################
plt.figure('LR plot')
plt.scatter(X,y)
plt.xlabel('Population size')
plt.ylabel('Profit ($)')
################ Initial plotting ##############################################

X = pd.DataFrame([np.ones(m),X]).T                                             # Adding a column of ones for theta_0

##################### LR algorithm ############################################
reg = LinearRegression(fit_intercept=False)                                    # default Linear regression algorithm 

'''
reg = SGDRegressor(max_iter=3000, tol=1e-5,alpha=0.0001,penalty=None,          # Stochastic gradient descent linear regression algorithm
                   learning_rate='constant',eta0=.0001,
                   verbose=2,shuffle=False,early_stopping=False,
                   validation_fraction=.1,fit_intercept=False,average=False)
'''
reg.fit(X,y)                                                                   # Fitting data to the regression model

theta = reg.coef_                                                              # Theta using iterative approach

#loss = reg.loss_curve_

##################### LR algorithm ############################################

#################### Normal equation ##########################################
theta_normal = pd.DataFrame(np.linalg.inv((X.T).dot(X))).dot((X.T).dot(y))      # Theta using normal equation : Analytical solution
#################### Normal equation ##########################################

################### Plot fitted line ##########################################

plt.figure('LR plot')

ft_line = X.dot(theta)                                                        # Fitted line

plt.plot(X.iloc[:,1],ft_line,'red')

################### Plot fitted line ##########################################

score = reg.score(X,y)