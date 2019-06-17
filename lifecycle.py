#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:43:08 2019

@author: claire
"""

#import math
import numpy as np
from functools import reduce

def fertilityFunction(xi,x0,e,params):
    gamma = params[0]
    fb = params[1]
    c = params[2]
    b = params[3]
    
    return max(0,round(fb*(1-c*xi[0]**2+b*x0[0])/(1+gamma*e[0]),3))

def correlation(mutationStep,correlationCoefficient):
    numberTraits = len(mutationStep)
    if numberTraits>1:
        sigmaColumn = np.repeat([mutationStep],len(mutationStep),axis=0)
        sigmaRow = np.repeat(np.transpose([mutationStep]),len(mutationStep),axis=1)
        rhoMatrix = np.repeat([np.repeat(float(correlationCoefficient),len(mutationStep))],len(mutationStep),axis=0)
        np.fill_diagonal(rhoMatrix,1)
        
        corr = reduce(np.multiply,[sigmaColumn, sigmaRow, rhoMatrix])
    
    else:
        corr = np.nan
        
    return corr
    
def mutation(mutationStep,correlationPattern,numberMutants):
    numberTraits = len(mutationStep)
    if numberTraits>1:
        mut = np.random.multivariate_normal(np.repeat(0,numberTraits),correlationPattern,numberMutants)
    
    else:
        mut = np.random.normal(0,mutationStep,numberMutants)
        
    return mut
        
