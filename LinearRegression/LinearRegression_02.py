# -*- coding: utf-8 -*-
"""
Linear Regression

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