#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:09:56 2019

@author: claire
"""

import numpy as np
import os
import matplotlib.pyplot as plt
import math as m

#os.getcwd() #check current working directory
path = '/home/claire/chiefdom-project'
os.chdir(path)

readStart = 0
readStop = 20000

getMeanPhen = []
getStdPhenAbove = []
getStdPhenBelow = []

    
with open("meanphenotypes.txt", "r") as phenFile:
    for i, line in enumerate(phenFile):
        if i < readStart:
            continue
        elif i < readStop:
            tmpMean = float(line.rstrip().split(',')[0])
            tmpStd = float(line.rstrip().split(',')[1])
            getMeanPhen.append(tmpMean)
            getStdPhenAbove.append(tmpMean + tmpStd)
            getStdPhenBelow.append(tmpMean - tmpStd)
        else:
            break
        
np.nanmean(getMeanPhen)
np.nanmean(getStdPhenAbove)
np.nanmean(getStdPhenBelow)

###########################
# RUN WHOLE BLOCK AT ONCE #
###########################
axes = plt.gca()
#axes.set_xlim([xmin,xmax])
axes.set_ylim([0,1])
plt.plot(getStdPhenAbove, color = '0.90', marker = '.', ls = 'None')
plt.plot(getStdPhenBelow, color = '0.90', marker = '.', ls = 'None')
plt.plot(getMeanPhen, color = 'g', marker = '.', ls = 'None')
###########################

sum(np.isnan(getMeanPhen))/len(getMeanPhen)

getMeanEnv = []
getStdEnvAbove = []
getStdEnvBelow = []

    
with open("meanenvironments.txt", "r") as envFile:
    for i, line in enumerate(envFile):
        if i < readStart:
            continue
        elif i < readStop:
            tmpMean = float(line.rstrip().split(',')[0])
            tmpStd = float(line.rstrip().split(',')[1])
            getMeanEnv.append(tmpMean)
            getStdEnvAbove.append(tmpMean + tmpStd)
            getStdEnvBelow.append(tmpMean - tmpStd)
        else:
            break
        
np.nanmean(getMeanEnv)

###########################
# RUN WHOLE BLOCK AT ONCE #
###########################
axes = plt.gca()
#axes.set_xlim([xmin,xmax])
axes.set_ylim([0,m.ceil(max(getStdEnvAbove))])
plt.plot(getStdEnvAbove, color = '0.90', marker = '.', ls = 'None')
plt.plot(getStdEnvBelow, color = '0.90', marker = '.', ls = 'None')
plt.plot(getMeanEnv,color = 'g', marker = '.', ls = 'None')
###########################

sum(np.isnan(getMeanEnv))/len(getMeanEnv)
len(np.argwhere(getMeanEnv==0))