# -*- coding: utf-8 -*-
"""
Linear Regression 01

Author: Bruno Godoi Eilliar
Date: May 19, 2015

"""

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

debug = True
x = np.array([0., 1, 2, 3])
y = np.array([4., 7, 7, 8])
m = float(len(x)) # make sure to work with float number always
alpha = .1
error = .01
# turn on interactive plot mode
plt.figure(1)
plt.ion()

theta0 = 0.
theta1 = 0.


# Compute h_theta
h_theta = theta0 + theta1*x

# Compute Cost Function
a = (h_theta - y)**2
J = (1/(2*m))*np.sum(a)
if debug: print "Cost: ", J

for i in range(1, 200):
    theta0_new = theta0 -alpha*(1/m)*np.sum((h_theta - y))
    theta1_new = theta1 - alpha*(1/m)*np.sum(np.dot((h_theta - y), x))
    if debug:
        print "(Theta0, Theta1): ", theta0_new, theta1_new
    #if (np.abs(theta0-theta0_new) < error) and (np.abs(theta1-theta1_new)< error):
    #    break
    theta0 = np.copy(theta0_new)
    theta1 = np.copy(theta1_new)
    h_theta = theta0 + theta1*x
    
    plt.figure(1)
    plt.clf()
    plt.plot(x, y, 'bo')
    plt.axis([-1, 5, 0, 10])
    plt.plot(x, h_theta, 'r--')
    plt.draw()
    plt.show()
    plt.pause(0.01)
    