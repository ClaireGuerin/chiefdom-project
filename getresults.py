#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:09:56 2019

@author: claire
"""

import numpy as np
import os
import matplotlib.pyplot as plt

#os.getcwd() #check current working directory
path = '/home/claire/chiefdom-project'
os.chdir(path)

readStart = 0
readStop = 20000

getMeanPhen = []
getStdPhen = []

    
with open("meanphenotypes.txt", "r") as phenFile:
    for i, line in enumerate(phenFile):
        if i < readStart:
            continue
        elif i < readStop:
            getMeanPhen.append(float(line.rstrip().split(',')[0]))
            getStdPhen.append(float(line.rstrip().split(',')[1]))
        else:
            break
        
np.nanmean(getMeanPhen)
np.nanmean(getStdPhen)

plt.plot(getMeanPhen)
plt.plot(getStdPhen)

sum(np.isnan(getMeanPhen))/len(getMeanPhen)
sum(np.isnan(getStdPhen))/len(getStdPhen)

getMeanEnv = []
getStdEnv = []

    
with open("meanenvironments.txt", "r") as envFile:
    for i, line in enumerate(envFile):
        if i < readStart:
            continue
        elif i < readStop:
            getMeanEnv.append(float(line.rstrip().split(',')[0]))
            getStdEnv.append(float(line.rstrip().split(',')[1]))
        else:
            break
        
np.nanmean(getMeanEnv)
np.nanmean(getStdEnv)

plt.plot(getMeanEnv)
plt.plot(getStdEnv)

sum(np.isnan(getMeanEnv))/len(getMeanEnv)
len(np.argwhere(getMeanEnv==0))
sum(np.isnan(getStdEnv))/len(getStdEnv)