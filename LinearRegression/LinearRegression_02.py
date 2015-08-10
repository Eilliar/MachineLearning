# -*- coding: utf-8 -*-
"""
Linear Regression
Example 02 - Load data from a txt file

Created on Wed Jul 15 12:53:53 2015

@author: Bruno Godoi Eilliar
"""

import numpy as np
import matplotlib.pyplot as plt

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return np.array(dataMat),np.array(labelMat)

data,y = loadDataSet("ex0.txt")
x = data[:,1]

plt.close("all")
plt.figure(1)
plt.plot(x, y, 'ro')
plt.show()

"""
Fill In with your code bellow
"""
# Create a new figure to plot the data and the hypothesis
plt.figure(2)
plt.ion()

# Define alpha
alpha = 0.1
# Size of data set
m = float(len(x))
# Define Hypothesis
theta0 = 1.
theta1 = 0.
# Compute h_theta
h_theta = theta0 + theta1*x
# Compute the Cost Function
a = (h_theta - y)**2
J = (1/(2*m))*np.sum(a)


for i in range(1, 100):
    #Gradient Descent Algorithm
    theta0_new = theta0 -alpha*(1/m)*np.sum((h_theta - y))
    theta1_new = theta1 - alpha*(1/m)*np.sum(np.dot((h_theta - y), x))
    theta0 = np.copy(theta0_new)
    theta1 = np.copy(theta1_new)
    h_theta = theta0 + theta1*x

    #Show the fitting process
    plt.figure(2)
    plt.clf()
    plt.plot(x, y, 'bo')
    plt.axis([-0.2, 1.2, 2.5, 5])
    plt.plot(x, h_theta, 'r--')
    plt.draw()
    plt.show()
    plt.pause(0.01)