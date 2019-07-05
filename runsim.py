#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:44:07 2019

@author: claire
"""
import numpy as np
import lifecycle as lc
import warnings
import time
                 
# Initial conditions and parameters  
globalParsDict = {'demes number':1000,
                  'generations number':20000,
                  'initial phenotypes':[0.5],
                  'initial deme size':1} 

localParsDict = {'probability mutation':0.01, 
            'mutation step':[0.005], 
            'density competition':0.1, 
            'basal fertility':2, 
            'cooperation cost':0.05, 
            'cooperation benefit':0.5, 
            'dispersal rate':0.1, 
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
    fileMeanPhenotypes = open("meanphenotypes.txt", "w")
    fileMeanEnvironments = open("meanenvironments.txt", "w")
    with open("parameters.txt","w") as fileParameters:
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

# RUN SINGLE SIMULATION

time_start = time.time()
test = populationDynamics(globalParsDict,localParsDict)
time_elapsed = (time.time() - time_start)