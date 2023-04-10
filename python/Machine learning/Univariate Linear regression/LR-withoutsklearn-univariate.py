# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:56:33 2022

Objective: To implement linear regression with one variable to predict profits 
for a food truck.To use this data to help you select which city to expand
to next.
@author: arkob
"""



import numpy as np
import pandas as pd
#from sklearn.linear_model import LinearRegression
#from sklearn import datasets, linear_model
#from sklearn.metrics import mean_squared_error, r2_score
#from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



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

theta = pd.DataFrame(np.zeros((X.shape[1])))


########################### Cost function #####################################
def computeCost(X,y,theta):
    
    m = y.size
    
    J = 0
    
    predictions = X.dot(theta)
    sqrErr = sqrErr = (predictions.iloc[:,0]-y)**2
    J = (1/(2*m))*sqrErr.sum()
    
    return J

########################### Cost function #####################################

########################### Gradient descent algorithm (one variable) #####################################

def gradientDescent(X,y,theta,alpha,num_iters):
    
    m = y.size                                                                 # Number of training examples
    n = X.shape[1]                                                             # Number of features
    J_hist = np.zeros(num_iters)
    
    for iteration in range(num_iters):
        predictions = X.dot(theta)
        
        for i in range(n):                                                     # Simultaneous parameter update 
            
            theta.loc[i] = theta.loc[i] - (alpha/m)*X.iloc[:,i].dot((predictions.iloc[:,0]-y))  # Uses vectorized summation
        
        
        J_hist[iteration] = computeCost(X, y, theta)                           # Traking cost function history for every iteration
        
        print('Iteration:',iteration,'; J =', J_hist[iteration])
    
    
    return theta,J_hist

########################### Gradient descent algorithm (one variable) #####################################

############################ Gradient descent settings ########################
num_iters = 1000                                                               # Number of iterations
alpha = 0.01                                                                   # Learning rate
############################ Gradient descent settings ########################

res = gradientDescent(X,y,theta,alpha,num_iters)

################### Gradient descent convergence ##############################
plt.figure('Gradient descent convergence')
plt.plot(res[1])
plt.xlabel('# Iterations')
plt.ylabel('Cost function ')

################### Gradient descent convergence ##############################

################### Plot fitted line ##########################################

plt.figure('LR plot')

ft_line = X.dot(res[0])                                                        # Fitted line

plt.plot(X.iloc[:,1],ft_line,'red')

################### Plot fitted line ##########################################
