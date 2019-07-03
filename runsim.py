#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:44:07 2019

@author: claire
"""
import numpy as np
import lifecycle as lc
import warnings
                 
# Initial conditions and parameters  
globalParsDict = {'demes number':3,
                  'generations number':10,
                  'initial phenotypes':[0.1],
                  'initial deme size':1} 

localParsDict = {'probability mutation':0.5, 
            'mutation step':[0.2], 
            'density competition':0.1, 
            'basal fertility':2, 
            'cooperation cost':0.05, 
            'cooperation benefit':0.5, 
            'dispersal rate':0.5, 
            'demes number':globalParsDict['demes number'], 
            'mutation correlation coefficient':0} 
  

def populationDynamics(globalParameters,localParameters):
    initDemeSize = globalParameters['initial deme size']
    generationsNumber = globalParameters['generations number']
    phenotypes = globalParameters['initial phenotypes']
    demesNumber = globalParameters['demes number']
    
    initialPhenotypes = [np.repeat([phenotypes],initDemeSize,axis=0)] * demesNumber
    initialEnvironment = []
    for i in initialPhenotypes: initialEnvironment.append([len(i)])
    tmpPop = [initialPhenotypes,initialEnvironment]
    
    # OUTPUT FILES
    fileMeanPhenotypes = open("meanphenotypes.txt", "a+")
    fileMeanEnvironments = open("meanenvironments.txt", "a+")
    fileParameters = open("parameters.txt","a+")
    print(localParameters,file=fileParameters)
    
    for gen in range(generationsNumber):
        demeMeanPhen = []
        demeStdPhen = []
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            for demePhen in tmpPop[0]: 
                demeMeanPhen.append(np.nanmean(demePhen))
                demeStdPhen.append(np.nanstd(demePhen))
            fileMeanPhenotypes.write("{0},{1}\r\n".format(np.mean(demeMeanPhen),np.std(demeStdPhen)))
            fileMeanEnvironments.write("{0},{1}\r\n".format(np.mean(tmpPop[1]),np.std(tmpPop[1])))
#
#        try:
        newTmpPop = lc.lifeCycle(tmpPop,localParameters)
        tmpPop = newTmpPop
#        except:
#            print("failed at generation {0}".format(gen))
                
#        
    filesList = [fileMeanPhenotypes,fileMeanEnvironments,fileParameters]
    for file in filesList: file.close()
        
    return tmpPop
        
test = populationDynamics(globalParsDict,localParsDict)

testpop=[[np.array([[np.nan],[0.1]]), np.array([[np.nan],[0.19187736]]), np.array([[1.00000000e-06],[1.00000000e-01],[9.64776477e-02],[1.43006215e-01]])], [[2], [2], [4]]]