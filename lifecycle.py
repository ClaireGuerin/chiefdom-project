#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:43:08 2019

@author: claire
"""

#import math
import numpy as np
from functools import reduce
#from itertools import repeat
import dictmanip as dm

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
    
def mutation(mutationStep,correlationPattern,numberIndividuals):
    numberTraits = len(mutationStep)
    if numberTraits>1:
        mut = np.random.multivariate_normal(np.repeat(0,numberTraits),correlationPattern,numberIndividuals)
    
    else:
        mut = np.random.normal(0,mutationStep,numberIndividuals)
        
    return mut

def applyMutation(mutationEventBoolean,originalPhenotype,phenotypeDeviation):
    if mutationEventBoolean:
        tmp = originalPhenotype + phenotypeDeviation
        
    else:
        tmp = originalPhenotype
        
    return tmp

def phenotypeBoundaries(unboundedPhenotype,lowBoundary,uppBoundary):
    if unboundedPhenotype < lowBoundary:
        tmp = float(lowBoundary + 10**(-6))
    elif unboundedPhenotype < 1:
        tmp = float(uppBoundary - 10**(-6))
    else:
        tmp = unboundedPhenotype
    return tmp
    
    
        
def lifeCycle(population, parameters):
    
    # EXTRACT VALUES AND PARAMETERS
    
    populationPhenotypes = population[0]
    environmentalStates = population[1]
    probabilityMutation = parameters['probability mutation']
    mutationStep = parameters['mutation step']
    fertilityParameters = dm.extract(parameters,['density competition','basal fertility','cooperation cost','cooperation benefit'])
    dispersalRate = parameters['dispersal rate']
    demeNumber = parameters['demes number']
    mutationCorrelationCoefficient = parameters['mutation correlation coefficient']
    
    #traitsNumber = populationPhenotypes[0].shape[1]
    populationMigrants = np.full(demeNumber,np.nan)
    
    for deme in range(demeNumber): 
        demeSize = environmentalStates[deme]
        demePhenotypes = populationPhenotypes[deme]
        demeEnvironment = environmentalStates[deme]
        demeMeanPhenotypes = np.mean(demePhenotypes,axis=0)
        tmpDemeOffspring = np.full(2,np.nan)
        mutationCorrelationPattern = correlation(mutationStep,mutationCorrelationCoefficient)
        
        # REPRODUCTION
        
        for ind in range(demeSize):
            individualPhenotype = demePhenotypes[ind]
            individualFertility = fertilityFunction(individualPhenotype,demeMeanPhenotypes,demeEnvironment,fertilityParameters)
            numberOffspring = np.random.poisson(10**(-6)+individualFertility)
            tmpDemeOffspring = np.vstack((tmpDemeOffspring,np.repeat([individualPhenotype],numberOffspring,axis=0)))
            
        demeOffspring = np.delete(tmpDemeOffspring,0,axis=0)
        newDemeSize = demeOffspring.shape[0]
        
        # MUTATION
        
        demeMutants = np.random.choice([0,1],newDemeSize,True,[1-probabilityMutation,probabilityMutation]) #true stands for replacement
        #demeNumberMutants = sum(demeMutants)
        demeMutationValues = mutation(mutationStep,mutationCorrelationPattern,newDemeSize)
        
        demeMutateOffspring = np.full(demeOffspring.shape,np.nan)
        
        # MIGRATION
        
        demeMigrants = np.random.choice([0,1],newDemeSize,True,[1-dispersalRate,dispersalRate]) #true stands for replacement
        otherDemes = 
        
        for offspring in range(newDemeSize):
             tmpPhenotype = applyMutation(demeMutants[offspring],demeOffspring[offspring],demeMutationValues[offspring])
             demeMutateOffspring[offspring] = phenotypeBoundaries(tmpPhenotype,0,1)
             
            if demeMigrants     
            
            
        
        
                
        
                
            
            
            