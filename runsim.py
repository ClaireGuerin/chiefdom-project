#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:44:07 2019

@author: claire
"""
import numpy as np
import lifecycle as lc
                 
# Initial conditions and parameters  
globalParsDict = {'demes number':3,
                  'generations number':1,
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
#    fileMeanPhenotypes = open("meanphenotypes.txt", "a+")
#    fileMeanEnvironments = open("meanenvironments.txt", "a+")
#    fileParameters = open("parameters","a+")
#    print(localParameters,file=fileParameters)
    
    for gen in range(generationsNumber):
#        flattenPhen = []
#        flattenEnv = []
#        for (demePhen,demeEnv) in zip(tmpPop[0],tmpPop[1]): 
#            flattenPhen.append(demePhen)
#            flattenEnv.append(demeEnv)
#        fileMeanPhenotypes.write("{0},{1}\r\n".format(np.mean(flattenPhen),np.std(flattenPhen)))
#        fileMeanEnvironments.write("{0},{1}\r\n".format(np.mean(flattenEnv),np.std(flattenEnv)))
#
        try:
            newTmpPop = lc.lifeCycle(tmpPop,localParameters)
            tmpPop = newTmpPop
        except:
            print("failed at generation {0}".format(gen))
                
#        
#    filesList = [fileMeanPhenotypes,fileMeanEnvironments,fileParameters]
#    for file in filesList: file.close()
        
    return tmpPop
        
test = populationDynamics(globalParsDict,localParsDict)
