# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:10:42 2015

@author: Bruno Godoi Eilliar
"""

import numpy as np
import matplotlib.pyplot as plt
plt.close("all")

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
